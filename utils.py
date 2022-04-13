import pdb
import pickle
from kucoin_futures.client import Market
from kucoin_futures.client import Trade
from kucoin_futures.client import User

client_market = Market(url='https://api-futures.kucoin.com')
client_market = Market()
key = ''
secret = ''
passphrase = ''
client_trade = Trade(key=key, secret=secret, passphrase=passphrase, is_sandbox=False)
client_user = User(key=key, secret=secret, passphrase=passphrase, is_sandbox=False)

cur_trades_dir = "cur_trades.pkl"

def get_question(pos_cost, acct_sz, avail_bal, pos_sz, num_contracts, sl_pct):
    trade_cost = "\033[92m(" + str(round(pos_cost, 2)) + "/" + str(round(avail_bal, 2)) + ")\033[0m"
    trade_worth = "\033[92m$" + str(round(pos_sz,2)) + "(" + str(num_contracts + 1) + " CONTRACTS)\033[0m."
    max_loss = "Max loss is \033[91m $" + str(round(pos_sz * sl_pct, 2)) + "\033[0m"
    trade_risk = "Trade risk is \033[91m" + str(round(((pos_sz * sl_pct)/acct_sz)*100, 2)) + "%\033[0m"
    question = ("Trade costs " + trade_cost + " available balance and will be worth " + trade_worth + "\n" + max_loss + "\n" + trade_risk + "\nTake trade?")
    return question

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

def get_leverage_level(position_size,  avail_bal, maint_margin, stop_loss_pct):
    # calculate optimal leverage:
    # 1. Available balance > cost of trade
    # 2. Max amount lost in trade is less than max amount loss tolorated (cost*main_mgn)
    lev_lvl = 1 # default value
    buffer_pct = 0.01
    leverage_levels = [1, 2, 3, 4, 5]
    for lvl in leverage_levels[::-1]:
        pos_cost = position_size * (1/lvl)
        # if (pos_cost > avail_bal) or (position_size * stop_loss_pct >= pos_cost * maint_margin):
        if (pos_cost + (pos_cost * buffer_pct) > avail_bal) or (pos_cost - (pos_cost * stop_loss_pct) <= position_size * maint_margin):
            continue
        else:
            lev_lvl = lvl
            return lev_lvl, pos_cost

    return 0, 0    # return 0 as leverage level if not enough funds with this amount of contracts
    abort_trade_and_quit("from get_leverage_level: NOT ENOUGH FUNDS AVAILABLE")
    

def get_position_size_and_leverage_level(trade, entry_price, contract_mult, maint_margin, sl_pct):
    if trade['acct_sz'] == '':
        acct_sz = client_user.get_account_overview(currency='USDT')['accountEquity']
    else:
        acct_sz = trade['acct_sz']

    pos_sz = (acct_sz * trade['pct_risk'] * 0.01) / sl_pct
    
    total_pos_contracts = int(pos_sz / (entry_price * contract_mult))
    if total_pos_contracts < 1:
        abort_trade_and_quit("get_position_size_and_leverage_level: POSITION TOO SMALL FOR A SINGLE CONTRACT")

    # find maximum number of contracts able to trade with
    avail_bal = client_user.get_account_overview(currency='USDT')['availableBalance']
    for num_contracts in range(total_pos_contracts)[::-1]:
        # reset desired position size after determining number of contracts (for leverage calculation)
        pos_sz = (num_contracts + 1) * (entry_price * contract_mult)
        leverage_lvl, pos_cost = get_leverage_level(pos_sz, avail_bal, maint_margin, sl_pct)
        print(pos_cost)
        if leverage_lvl != 0:
            question = get_question(pos_cost, acct_sz, avail_bal, pos_sz, num_contracts, sl_pct)
            if yes_or_no(question):
                return (num_contracts + 1), pos_sz, leverage_lvl

    # if avail_bal < pos_sz
    abort_trade_and_quit("get_position_size_and_leverage_level: TRADE REJECTED")

def check_total_risk(trade, cur_trades, cur_stop_orders, max_concurrent_acct_risk_pct):
    cur_risk_pct = 0.0
    for order in cur_stop_orders['items']:
        for t in cur_trades:
            if t['stop_id'] == order['id']:
                cur_risk_pct += t['pct_risk']
    print("Current Total Risk Pre-trade: " + str(cur_risk_pct) + "% of account")
    print("Current Total Risk Pre-trade: " + str(cur_risk_pct + trade['pct_risk']) + "% of account")

    if cur_risk_pct + trade['pct_risk'] >= max_concurrent_acct_risk_pct:
        abort_trade_and_quit("TRADE WOULD EXCEED MAX RISK")

def abort_trade_and_quit(message):
    print("!!!!!!!!!!!! TRADE ABORTED !!!!!!!!!!!!!")
    print("!!!!!!! " + message + " !!!!!!!")
    exit()

def delete_inactive_trades(cur_stop_orders, cur_trades, trade):
    # delete old inactive trades
    cur_order_ids = []
    for order in cur_stop_orders['items']:
        cur_order_ids.append(order['id'])
    temp = cur_trades.copy()
    delete_idx = []
    for i, t in enumerate(temp):
        if t['stop_id'] not in cur_order_ids:
            delete_idx.append(i)
    cur_trades_buffer = []
    for i in range(len(cur_trades)):
        if i not in delete_idx:     # leave out indices of delete_idx, keep all others
            cur_trades_buffer.append(cur_trades[i])

    # save current trade
    cur_trades.append(trade)
    pickle.dump(cur_trades, open(cur_trades_dir, "wb"))