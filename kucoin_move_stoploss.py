import pdb
import pickle
import os
from kucoin_futures.client import Market
from kucoin_futures.client import Trade
from kucoin_futures.client import User
from utils import get_leverage_level, check_total_risk, abort_trade_and_quit
from utils import client_market, key, secret, passphrase, client_trade, client_user, cur_trades_dir

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "num_contracts": 3,
    "sl_price": 48198,
    "limit": ''
}

# determine sides of trade and stops
if trade['limit'] == '':
    if trade['side'] == 'long':
        stop_side = 'sell'
        stop_dir = 'down'
    else:
        stop_side = 'buy'
        stop_dir = 'up'
else:
    if trade['side'] == 'long':
        stop_side = 'sell'
        stop_dir = 'up'
    else:
        stop_side = 'buy'
        stop_dir = 'down'

# create stop loss as stop order
if trade['limit'] == '':
    order_id_sl = client_trade.create_market_order(
        stop=stop_dir, 
        stopPriceType='TP', 
        stopPrice=str(trade['sl_price']),  
        size=str(trade['num_contracts']), 
        symbol=trade['symbol'], 
        side=stop_side,
        lever='1',
        reduceOnly=True)
else:
    order_id_sl = client_trade.create_limit_order(
        stop=stop_dir, 
        stopPriceType='TP', 
        stopPrice=str(trade['limit']), 
        price=str(trade['sl_price']), 
        size=str(trade['num_contracts']), 
        symbol=trade['symbol'], 
        side=stop_side, 
        lever='1', 
        reduceOnly=True)
