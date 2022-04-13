import pdb
import pickle
import os
from utils import get_leverage_level, check_total_risk, abort_trade_and_quit, delete_inactive_trades
from utils import client_market, key, secret, passphrase, client_trade, client_user, cur_trades_dir

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'long',
    "take_profits": [[41716, 50], [42554, 25]]
}

# trade = {
#     "symbol": 'CROUSDTM',
#     "side": 'long',
#     "take_profits": [[0.67232, 25], [0.67741, 25], [0.68289, 10]]
# }


# trade = {
#     "symbol": 'XBTUSDTM',
#     "side": 'long',
#     "take_profits": [[49161, 50]]
# }


# determine sides of trade and stops
if trade['side'] == 'long':
    trade_side = 'buy'
    stop_side = 'sell'
else:
    stop_side = 'buy'
    trade_side = 'sell'

# create take profits
order_id_tp = []
total_pos_contracts = abs(client_trade.get_position_details(trade['symbol'])['currentQty'])
contracts_left = total_pos_contracts
for tp in trade['take_profits']:
    tp_contracts = int(total_pos_contracts*tp[1]*0.01)

    # verify that we're reducing by at least one contract, and make sure we have enough contracts left to reduce
    if tp_contracts < 1:
        tp_contracts += 1
    if tp_contracts > contracts_left:
        tp_contracts = contracts_left
    if contracts_left == 0:
        continue
    tp_id = client_trade.create_limit_order(
        price=str(tp[0]), 
        size=str(tp_contracts), 
        symbol=trade['symbol'], 
        side=stop_side, 
        lever='1', 
        reduceOnly=True)
    # pdb.set_trace()
    contracts_left -= tp_contracts
    order_id_tp.append(tp_id)

    print("====== Take Profit ======")
    print("Num Contracts: " + str(tp_contracts))

