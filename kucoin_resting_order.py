import pdb
import pickle
import os
from utils import get_leverage_level, check_total_risk, abort_trade_and_quit, delete_inactive_trades, get_position_size_and_leverage_level
from utils import client_market, key, secret, passphrase, client_trade, client_user, cur_trades_dir

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 46300,
    "sl_price": 46190,
    "take_profits": [[46533, 50]]
}



# current trades pickle
if os.path.exists(cur_trades_dir):
    cur_trades = pickle.load(open( cur_trades_dir, "rb" ))
else:
    cur_trades = []

# max concurrent account risk limits the ammount of loss to the account possible in any group of concurrent trades
max_concurrent_acct_risk_pct = 10

# check current total risk
cur_stop_orders = client_trade.get_open_stop_order()
check_total_risk(trade, cur_trades, cur_stop_orders, max_concurrent_acct_risk_pct)

# determine position size
contract_info = client_market.get_contracts_list()

# get symbol's contract multiplier
for c in contract_info:
    if c['symbol'] == trade['symbol']:
        contract_mult = c['multiplier']
        maint_margin = c['maintainMargin']

# get percent change in stop loss
sl_pct = abs(trade['entry_price'] - trade['sl_price']) / trade['entry_price']

# get position size and leverage based on trade parameters
total_pos_contracts, pos_sz, leverage_lvl = get_position_size_and_leverage_level(trade, trade['entry_price'], contract_mult, maint_margin, sl_pct)

# determine sides of trade and stops
if trade['side'] == 'long':
    trade_side = 'buy'
    stop_side = 'sell'
    stop_dir = 'down'
else:
    stop_side = 'buy'
    stop_dir = 'up'
    trade_side = 'sell'

# create entry as limit order
order_id_entry = client_trade.create_limit_order(
    symbol=trade['symbol'], 
    side=trade_side, 
    lever=str(leverage_lvl), 
    size=str(total_pos_contracts), 
    price=str(trade['entry_price']))

print("\n\033[93m====== Entry ======\033[0m")
print("Symbol: " + str(trade['symbol']))
print("Side: " + str(trade['side']))
print("Entry: " + str(trade['entry_price']))
print("Pos Size: " + str(pos_sz))
print("Total Pos Contracts: " + str(total_pos_contracts))
print("Leverage: " + str(leverage_lvl))

# create stop loss as stop limit order
order_id_sl = client_trade.create_market_order(
    stop=stop_dir, 
    stopPriceType='TP', 
    stopPrice=str(trade['sl_price']),  
    size=str(total_pos_contracts), 
    symbol=trade['symbol'], 
    side=stop_side, 
    lever='1', 
    reduceOnly=True)
trade['stop_id'] = order_id_sl['orderId']

# create take profits
# pdb.set_trace()
order_id_tp = []
contracts_left = total_pos_contracts
for tp in trade['take_profits']:
    tp_contracts = int(total_pos_contracts*tp[1]*0.01)
    # pdb.set_trace()

    # verify that we're reducing by at least one contract, and make sure we have enough contracts left to reduce
    if tp_contracts < 1:
        tp_contracts += 1
    if tp_contracts > contracts_left:
        tp_contracts = contracts_left
    if contracts_left == 0:
        continue
    tp_id = client_trade.create_limit_order(
        stop=stop_dir, 
        stopPriceType='TP', 
        stopPrice=str(trade['entry_price']), 
        price=str(tp[0]), 
        size=str(tp_contracts), 
        symbol=trade['symbol'], 
        side=stop_side, 
        lever='1', 
        reduceOnly=True)
    contracts_left -= tp_contracts
    order_id_tp.append(tp_id)

    print("\n\033[93m====== Take Profit ======\033[0m")
    print("Num Contracts: " + str(tp_contracts))

# delete old inactive trades
delete_inactive_trades(cur_stop_orders, cur_trades, trade)
