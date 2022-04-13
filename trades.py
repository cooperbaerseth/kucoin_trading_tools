BTCUSD = 'XBTUSDTM'
ETHUSDT = 'ETHUSDTM'
DYDXUSDT = 'DYDXUSDTM'

trade = {
    "symbol": 'DYDXUSDTM',
    "side": "long",
    "acct_sz": 139,
    "pct_risk": 0.5,
    "entry_price": 22.974,
    "sl_price": 23.325,
    "take_profits": [[22.638, 50],[22.130, 30]]
}

trade = {
    "symbol": 'DYDXUSDTM',
    "side": 'short',
    "acct_sz": 30,
    "pct_risk": 0.5,
    "entry_price": 23.162,
    "sl_price": 23.356,
    "take_profits": [[22.918, 50],[22.622, 30]]
}
# winner but messed up and auto closed the trade 

trade = {
    "symbol": 'DYDXUSDTM',
    "side": 'long',
    "acct_sz": 30,
    "pct_risk": 0.5,
    "entry_price": 22.479,
    "sl_price": 22.297,
    "take_profits": [[22.716, 50],[22.970, 30]]
}
# winner, but small size for testing

trade = {
    "symbol": 'DOGEUSDTM',
    "side": 'short',
    "acct_sz": 136,
    "pct_risk": 0.5,
    "entry_price": 0.23442,
    "sl_price": 0.23657,
    "take_profits": [[0.23191, 50],[0.22843, 30]]
}
# not started

trade = {
    "symbol": 'ETHUSDTM',
    "side": 'long',
    "acct_sz": 136,
    "pct_risk": 0.5,
    "entry_price": 3348.65,
    "sl_price": 3334.27,
    "take_profits": [[3368.86, 50],[3398.58, 30]]
}
# not started

trade = {
    "symbol": 'ETHUSDTM',
    "side": 'short',
    "acct_sz": 136,
    "pct_risk": 0.2,
    "entry_price": 3389.7,
    "sl_price": 3397.8,
    "take_profits": [[3381.6, 25], [3368.9, 25],[3350.7, 30]]
}
# DONE
# - sweep play
# - stopped out immediately
# - looks like a mid level.. maybe dont play those sweeps
# * could have done margin here because such a small SL???
# * 2 take profits didnt work because num contracts was 3... cant take 25% of 3

trade = {
    "symbol": 'ETHUSDTM',
    "side": 'short',
    "acct_sz": 136,
    "pct_risk": 0.5,
    "entry_price": 3412.9,
    "sl_price": 3427.6,
    "take_profits": [[3381.6, 50],[3367.2, 30]]
}
# TBA... trying to use leverage

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": 136,
    "pct_risk": 0.5,
    "entry_price": 48078,
    "sl_price": 48395,
    "take_profits": [[47764, 50],[47131, 30]]
}
# undocumented
# stopped out immediately

trade = {
    "symbol": 'DOGEUSDTM',
    "side": 'long',
    "acct_sz": 136,
    "pct_risk": 0.3,
    "entry_price": 0.23072,
    "sl_price": 0.22746,
    "take_profits": [[0.23393, 50],[0.23770, 30]]
}
# canceled order.... not confident
# - playing untested level of previous resistance as support
# - stop loss under the level

trade = {
    "symbol": 'DOGEUSDTM',
    "side": 'long',
    "acct_sz": 136,
    "pct_risk": 0.3,
    "entry_price": 0.24039,
    "sl_price": 0.23881,
    "take_profits": [[0.24197, 50],[0.24462, 30]]
}
# - playing untested level of previous resistance as support
# - stop loss under the level
# - hit my entry on TV but not on kucoin
# - came back up to test levels after than and bailed 

trade = {
    "symbol": 'ADAUSDTM',
    "side": 'long',
    "acct_sz": 136,
    "pct_risk": 0.3,
    "entry_price": 2.2226,
    "sl_price": 2.2164,
    "take_profits": [[2.2303, 50],[2.2357, 30]]
}
# trade adjusted for kucoin
# - tried to play untested level after pump
# - stopped out
# - longed a HTF rejection zone... clear mistake
# - lesson is to more strictly take longs in bottom/mid ranges rather than high (on HTF)
# documented

trade = {
    "symbol": 'SOLUSDTM',
    "side": 'long',
    "acct_sz": 136,
    "pct_risk": 0.3,
    "entry_price": 164.689,
    "sl_price": 163.741,
    "take_profits": [[165.749, 50],[167.395, 30]]
}
# playing untested level broken through on pump
# documented

trade = {
    "symbol": 'ETHUSDTM',
    "side": 'long',
    "acct_sz": 135,
    "pct_risk": 0.5,
    "entry_price": 3486.6,
    "sl_price": 3468.85,
    "take_profits": [[3509.17, 25],[3527.64, 25], [3551.46, 30]]
}
# level swept, changed entry
# canceled... didnt come back and better opportunities

trade = {
    "symbol": 'ETHUSDTM',
    "side": 'short',
    "acct_sz": 135,
    "pct_risk": 0.5,
    "entry_price": 3593.7,
    "sl_price": 3641.2,
    "take_profits": [[3548.0, 50], [3464.42, 30]]
}
# waiting for price to fail before this short
# - price lost level, came back up
# - hit entry and TP1
# - only had 1 lot so TP1 closed trade

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": 135,
    "pct_risk": 0.5,
    "entry_price": 55435,
    "sl_price": 55730,
    "take_profits": [[55031, 50],[54567, 30]]
}
# - playing untested rejection at important level
# - entry hit on kucoin futures with wick
# - TP1 hit immediately
# - accidentally closed position while trying to move stop loss near entry
# - make sure to use market stops for stop loss

trade = {
    "symbol": 'DYDXUSDTM',
    "side": 'long',
    "acct_sz": 136,
    "pct_risk": 1,
    "entry_price": 22.882,
    "sl_price": 22.253,
    "take_profits": [[23.578, 50],[24.542, 30]]
}
# documented 
# - playing untested level after pump that acheived the 1hr move
# - SL a few levels down, near the bottom of the origin
# - decent bounce at entry
# - didn't gain the low, wasn't convinced of reversal
# - bailed early with 1% profit


trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": 135,
    "pct_risk": 0.5,
    "entry_price": 57477,
    "sl_price": 57698,
    "take_profits": [[57070, 50],[56664, 30]]
}
# documented 
# - playing 15min failure and retest
# - TP1 hit, moved SL to entry
# - stopped out at entry

trade = {
    "symbol": 'DOGEUSDTM',
    "side": 'short',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 0.22238,
    "sl_price": 0.22437,
    "take_profits": [[0.22033, 50],[0.21753, 30]]
}
# documented 
# - playing lost and untested levels to short during hard downtrend
# - split short idea over two spots
# - price is at a good place for reversal, so look for hedges
# - stopped out after big pump

trade = {
    "symbol": 'DOGEUSDTM',
    "side": 'short',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 0.22641,
    "sl_price": 0.22903,
    "take_profits": [[0.22280, 50],[0.21770, 30]],
    "PnL": -0.23
}
# documented 
# - playing downtrend untested level lost
# - price neared level and pulled away multiple times but didn't hit entry
# - should have bailed on trade, as the level was probably tested by those moves
# - when price hit level it went straight through

trade = {
    "symbol": 'DOGEUSDTM',
    "side": 'long',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 0.21916,
    "sl_price": 0.21728,
    "take_profits": [[0.22233, 50],[0.22636, 30]],
    "PnL": -0.56
}
# documented
# - hedge for two previous shorts
# - nice place to reverse
# - inverse head and shoulders also playing out
# - TP1 hit, closed early due to BTC bias down

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'long',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 54368,
    "sl_price": 54131,
    "take_profits": [[54819, 50],[55651, 30]],
    "PnL": 1.23,
    "chart_link": "https://www.tradingview.com/x/mkwTYJkk/"
}
# - long sweep play of almost 2 or 3 important levels
# - price came back down to level and bounced beautifully
# - entry hit while sleeping
# - TP1 hit quickly
# - woke up and closed trade, as it was very close to exit
# - MY BEST TRADE SO FAR WITH $1.23 !!!

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 55803,
    "sl_price": 56016,
    "take_profits": [[55433, 50],[54839, 30]],
    "PnL": -0.23,
    "chart_link": "https://www.tradingview.com/x/mkwTYJkk/"
}
# - hedge for long and playing lost level untested
# - price went straight through stop
# - this trade was equivilant to catching a falling knife

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 56090,
    "sl_price": 56328,
    "take_profits": [[55742, 50],[55301, 30]],
    "PnL": -0.35,
    "chart_link": "https://www.tradingview.com/x/RFLlWH7b/"
}
# - stopped out immediately

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 56287,
    "sl_price": 56498,
    "take_profits": [[56044, 50],[55576, 30]],
    "PnL": -0.61,
    "chart_link": "https://www.tradingview.com/x/RFLlWH7b/"
}

# - two trades spread over 1% risk
# - playing hard dump from support level as new resistance
# - picking two different levels to spread risk
# - stopped out... pumped very hard through range

trade = {
    "symbol": 'ETHUSDTM',
    "side": 'long',
    "acct_sz": 136,
    "pct_risk": 0.5,
    "entry_price": 3638,
    "sl_price": 3614,
    "take_profits": [[3712.20, 50],[3740.55, 30]],
    "PnL": 1.73,
    "chart_link": "https://www.tradingview.com/x/GmOTJan7/"
}
# hit and finished, not documented
# playing untested level after pump, SL underzone
# perfect action, hit the entry and bounced past TP1 and 2 in 1 hour

trade = {
    "symbol": 'MATICUSDTM',
    "side": 'long',
    "acct_sz": 136,
    "pct_risk": 0.7,
    "entry_price": 1.279,
    "sl_price": 1.232,
    "take_profits": [[1.393, 50],[1.504, 30]]
}
# submitted, not hit
# playing untested level after pump, SL underzone
# had alert set for this zone earlier

trade = {
    "symbol": 'ADAUSDTM',
    "side": 'long',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 2.12142,
    "sl_price": 2.06477,
    "take_profits": [[2.22459, 50],[2.31272, 30]],
    "PnL": 0.63,
    "chart_link": "https://www.tradingview.com/x/5MMsrNvE/"
}
# playing higher low on 4hr chart, betting for higher high
# - first profit target hit, pulled out early right before pump to nearly second PT

trade = {
    "symbol": 'BTTUSDTM',
    "side": 'long',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 0.003255,
    "sl_price": 0.003097,
    "take_profits": [[0.003517, 50],[0.003819, 30]]
}
# playing higher low on 4hr chart, don't even need higher high for good R
# TP1 at 2R
# blasted through SL on BTC dump

trade = {
    "symbol": 'BTTUSDTM',
    "side": 'short',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 0.003826,
    "sl_price": 0.003867,
    "take_profits": [[0.003746, 50],[0.003703, 30]]
}
# playing important failure level that was failed to gain, basically an origin sweep
# tight SL, TP1 at 2R

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'long',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 64110,
    "sl_price": 63508,
    "take_profits": [[65382, 50],[66082, 30]]
}
# playing untested level after pump

trade = {
    "symbol": 'SOLUSDTM',
    "side": 'long',
    "acct_sz": 139,
    "pct_risk": 0.5,
    "entry_price": 187,
    "sl_price": 181,
    "take_profits": [[200, 50],[213, 30]],
    "PnL": 1.25,
    "chart_link": "https://www.tradingview.com/x/lqoKWtBt/"
}
# playing nice untested level for S/R flip
# hit and won!

trade = {
    "symbol": 'SOLUSDTM',
    "side": 'short',
    "acct_sz": 139,
    "pct_risk": 1,
    "entry_price": 211,
    "sl_price": 216,
    "take_profits": [[204, 50],[193, 30]],
    "PnL": 2.49,
    "chart_link": "https://www.tradingview.com/x/lqoKWtBt/"
}
# playing sweep of ATH
# not submitted yet, waiting for confirmation of sweep ... sweep confirmed, moved SL up a little due to new 4hr high
# entry hit
# hit entry almost exactly then moved away nicely to TP1 and beyond
# moved stop loss to entry since we have lost key levels

trade = {
    "symbol": 'ETHUSDTM',
    "side": 'short',
    "acct_sz": 139,
    "pct_risk": 1,
    "entry_price": 4126,
    "sl_price": 4181,
    "take_profits": [[4013, 50],[3897, 30]],
    "PnL": -1.15,
    "chart_link": "https://www.tradingview.com/x/y8tHiAWj/"
}
# playing untested failure that lost 4hr swing.. waiting to see what PA looks like as it approaches entry
# hit and stopped out

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'long',
    "acct_sz": 141,
    "pct_risk": 1,
    "entry_price": 60453,
    "sl_price": 59469,
    "take_profits": [[62471, 50],[64644, 30]],
    "PnL": -1.79,
    "chart_link": "https://www.tradingview.com/x/xdOVNcug/"
}
# playing mostly untested 4hr level after pump out of down trend
# almost hit TP then dumped

trade = {
    "symbol": 'ICPUSDTM',
    "side": 'long',
    "acct_sz": 141,
    "pct_risk": 1,
    "entry_price": 44.6,
    "sl_price": 42,
    "take_profits": [[49.8, 50],[56.4, 30]],
    "PnL": -1.47,
    "chart_link": "https://www.tradingview.com/x/9j13huYF/"
}
# playing untested 4rh level after pump.. nice level for support
# blasted through stop on BTC dump

trade = {
    "symbol": 'CRVUSDTM',
    "side": 'long',
    "acct_sz": 141,
    "pct_risk": 1,
    "entry_price": 3.624,
    "sl_price": 3.417,
    "take_profits": [[4.035, 50],[4.715, 30]]
}
# playing midpoint of untested HTF zone after major pump... zone corresponds with previous major resistance


trade = {
    "symbol": 'CRVUSDTM',
    "side": 'short',
    "acct_sz": 138,
    "pct_risk": 0.5,
    "entry_price": 5.077,
    "sl_price": 5.202,
    "take_profits": [[4.823, 50],[4.663, 30]],
    "PnL": -0.82,
    "chart_link": "https://www.tradingview.com/x/HF0Lni8m/"
}
# untested failure of ATH level
# - if this gets stopped... the lesson is "wait for a level to lose before entering", this trade was a knife catch
# - stopped out

trade = {
    "symbol": 'CRVUSDTM',
    "side": 'long',
    "acct_sz": 138,
    "pct_risk": 0.5,
    "entry_price": 4.516,
    "sl_price": 4.462,
    "take_profits": [[4.631, 50],[4.682, 30]]
}

trade = {
    "symbol": 'CRVUSDTM',
    "side": 'long',
    "acct_sz": 138,
    "pct_risk": 0.5,
    "entry_price": 4.48,
    "sl_price": 4.393,
    "take_profits": [[4.666, 50],[4.779, 30]]
}
# untested level after pump over important level to gain for reversal
# splitting risk over two levels

trade = {
    "symbol": 'SHIBUSDTM',
    "side": 'short',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 0.00008491,
    "sl_price": 0.00008631,
    "take_profits": [[0.00008197, 50],[0.00007639, 30]],
}

trade = {
    "symbol": 'SHIBUSDTM',
    "side": 'short',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 0.00008616,
    "sl_price": 0.00008815,
    "take_profits": [[0.000082, 50],[0.00007639, 30]],
}
# shorting ATH level previously lost on HTF
# spreading risk over two levels

trade = {
    "symbol": 'SHIBUSDTM',
    "side": 'short',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 0.0000748,
    "sl_price": 0.00007777,
    "take_profits": [[0.00006886, 50],[0.00006735, 30]],
    "PnL": 0.81,
    "chart_link": "https://www.tradingview.com/x/wwssbQWQ/"
}
trade = {
    "symbol": 'SHIBUSDTM',
    "side": 'short',
    "acct_sz": 137,
    "pct_risk": 0.5,
    "entry_price": 0.00007617,
    "sl_price": 0.0000791,
    "take_profits": [[0.00007029, 50],[0.00006735, 30]],
    "PnL": 0.81,
    "chart_link": "https://www.tradingview.com/x/wwssbQWQ/"
}
# spreading short of lost 15m/1hr level over two trades
# lowest short hit
# TP1 hit
# achieved levels, canceled both shorts

trade = {
    "symbol": 'SHIBUSDTM',
    "side": 'long',
    "acct_sz": 138,
    "pct_risk": 0.5,
    "entry_price": 0.00007214,
    "sl_price": 0.00006992,
    "take_profits": [[0.00007656, 50],[0.00008188, 30]],
    "PnL": -1.64,
    "chart_link": "https://www.tradingview.com/x/YvV7VtHy/"
}

trade = {
    "symbol": 'SHIBUSDTM',
    "side": 'long',
    "acct_sz": 138,
    "pct_risk": 0.5,
    "entry_price": 0.00006872,
    "sl_price": 0.00006542,
    "take_profits": [[0.00007532, 50],[0.00007866, 30]],
    "PnL": -1.64,
    "chart_link": "https://www.tradingview.com/x/YvV7VtHy/"
}
# SHIB gaining levels, looks like reversal of retracement
# playing longs as we're gaining
# split entry over two levels
# hit first PT but ultimately fell through both trade's stops

trade = {
    "symbol": 'MANAUSDTM',
    "side": 'short',
    "acct_sz": 138,
    "pct_risk": 0.5,
    "entry_price": 1.419,
    "sl_price": 1.492,
    "take_profits": [[1.276, 50],[1.181, 30]],
    "PnL": -0.61,
    "chart_link": "https://www.tradingview.com/x/I0SLzx74/"
}
# playing sweep of origins near ATH
# only entrying if 4hr sweep is confirmed
# had a sweep of the same area again and then dumped to first PT

trade = {
    "symbol": 'CRVUSDTM',
    "side": 'long',
    "acct_sz": 138,
    "pct_risk": 0.5,
    "entry_price": 4.65,
    "sl_price": 4.393,
    "take_profits": [[4.750, 50],[4.828, 30]],
    "PnL": -0.51,
    "chart_link": "https://www.tradingview.com/x/XrxMU5Kf/"
}
trade = {
    "symbol": 'CRVUSDTM',
    "side": 'long',
    "acct_sz": 138,
    "pct_risk": 0.5,
    "entry_price": 4.682,
    "sl_price": 4.625,
    "take_profits": [[4.797, 50],[4.878, 30]],
    "PnL": -0.51,
    "chart_link": "https://www.tradingview.com/x/XrxMU5Kf/"
}
# playing start of potential reversal... spliting risk over two trades
# stopped outand then pumped way past PT2 for both entries....
# played too high of levels

trade = {
    "symbol": 'MANAUSDTM',
    "side": 'long',
    "acct_sz": 131,
    "pct_risk": 0.5,
    "entry_price": 2.799,
    "sl_price": 2.667,
    "take_profits": [[3.078, 50],[3.326, 30]],
    "PnL": -0.54,
    "chart link": "https://www.tradingview.com/x/skLECDyE/"
}
# playing retest of failure of ATH.. SL below origin move and fib level
# small reaction and went through SL

trade = {
    "symbol": 'MATICUSDTM',
    "side": 'short',
    "acct_sz": 131,
    "pct_risk": 0.5,
    "entry_price": 1.9099,
    "sl_price": 1.9318,
    "take_profits": [[1.8693, 50],[1.8388, 30]],
    "PnL": -0.49,
    "chart_link": "https://www.tradingview.com/x/95fo1iJc/"
}
# trying to play retest of retest after important level of support lost
# blasted straight through SL

trade = {
    "symbol": 'BATUSDTM',
    "side": 'long',
    "acct_sz": 135,
    "pct_risk": 0.5,
    "entry_price": 1.2567,
    "sl_price": 1.3516,
    "take_profits": [[1.21, 50],[1.43, 30]],
    "PnL": 0.14,
    "chart_link": "https://www.tradingview.com/x/z2weYiOs/"
}
# played untested level after pump
# noticed that we're having resistance at a previous important level and looked like downtrend continuation so bailed early

trade = {
    "symbol": 'MANAUSDTM',
    "side": 'long',
    "acct_sz": 132,
    "pct_risk": 0.5,
    "entry_price": 2.72,
    "sl_price": 2.682,
    "take_profits": [[2.796, 50],[2.841, 30]],
    "PnL": 1.75,
    "chart_link": "https://www.tradingview.com/x/bXZvpXTR/"
}

trade = {
    "symbol": 'DOGEUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "sl_price": 0.28243,
    "PnL": .22,
    "chart_link": "https://www.tradingview.com/x/UBO08Qf4/" 
}
trade = {
    "symbol": 'DOGEUSDTM',
    "side": 'short',
    "take_profits": [[0.27981, 50], [0.27881, 30]]
}
# market smash doge short trade... lost level and dump.. took retest

trade = {
    "symbol": 'MANAUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.5,
    "sl_price": 2.818,
    "PnL": -0.88,
    "chart_link": "https://www.tradingview.com/x/87kKFc7i/"
}
trade = {
    "symbol": 'MANAUSDTM',
    "side": 'long',
    "take_profits": [[2.881, 50], [2.911, 30]]
}

trade = {
    "symbol": 'MANAUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.5,
    "sl_price": 3.087,
    "PnL": 0.97,
    "chart_link": "https://www.tradingview.com/x/X7bj58gO/"
}
trade = {
    "symbol": 'MANAUSDTM',
    "side": 'long',
    "take_profits": [[3.19, 50], [3.221, 30]]
}

trade = {
    "symbol": 'SOLUSDTM',
    "side": 'long',
    "acct_sz": 132,
    "pct_risk": 0.5,
    "entry_price": 202.991,
    "sl_price": 202.3,
    "take_profits": [[204.353, 50],[205.207, 30]],
    "PnL": 0.35,
    "chart_image": "https://www.tradingview.com/x/KZOO1w54/"
}
# played gained level after sweep of origin
# hit first PT1 and started dumping... after a retrace up I bailed early with confluence on BTC resistance

trade = {
    "symbol": 'ETHUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "sl_price": 4319.02,
    "PnL": 0.24,
    "chart_image": "https://www.tradingview.com/x/Xiil6Zjw/"
}
trade = {
    "symbol": 'ETHUSDTM',
    "side": 'short',
    "take_profits": [[4300.9, 50], [4294.2, 30]]
}
# played retest of key support lost
# something wrong with market smash entry though... the position size should have been much higher

trade = {
    "symbol": 'ENJUSDTM',
    "side": 'long',
    "acct_sz": 130,
    "pct_risk": 0.5,
    "entry_price": 2.989,
    "sl_price": 2.959,
    "take_profits": [[3.049, 50], [3.082, 30]],
    "PnL": -0.80,
    "chart_image": "https://www.tradingview.com/x/kS71CULd/"
}
# thought it was a reversal but it was a retest of previously lost important level...

trade = {
    "symbol": 'ENJUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "sl_price": 2.969
}
trade = {
    "symbol": 'ENJUSDTM',
    "side": 'short',
    "take_profits": [[2.888, 50], [2.86, 30]]
}
# retest of lost important level... see 15min/1hr
# PT1 took a little early

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'long',
    "acct_sz": 127,
    "pct_risk": 1,
    "entry_price": 61864,
    "sl_price": 61368,
    "take_profits": [[62846, 50], [63688, 30]],
    "PnL": (2.33-2.12),
    "chart_link": "https://www.tradingview.com/x/llTer4bu/"
}
# good place to hold for higher low
# stopped out, but dump was so abrupt I knew it was a sweep and re-entered at same entry
# PT1 hit soon, and took all profits near PT2

trade = {
    "symbol": 'SOLUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 241.241,
    "sl_price": 242.848,
    "take_profits": [[237.604, 50]],
    'PnL': 0.34,
    "char_image": "https://www.tradingview.com/x/nOgNEV65/"
}
# waited for resistance after hard pump
# saw a sweep so submitted a resting order hear top

trade = {
    "symbol": 'SOLUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 238.8,
    "sl_price": 237.826,
    "take_profits": [[240.774, 50]],
    "PnL": 0.56,
    "chart_image": "https://www.tradingview.com/x/A79Y9c3B/"
}
# playing higher low after hard pump

trade = {
    "symbol": 'SHIBUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 0.0000529,
    "sl_price": 0.00005472,
    "take_profits": [[0.00004943, 50]],
    "PnL": 0.59,
    "chart_image": "tradingview.com/x/FxscqRGn/"
}
# looked for lost levels after dump

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 60780,
    "sl_price": 60914,
    "take_profits": [[60527, 50]],
    "PnL": -0.89,
    "chart_link": "https://www.tradingview.com/x/4c59KZ0j/"
}
# playing retest of level lost after dump..

trade = {
    "symbol": 'ADAUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 2.23711,
    "sl_price": 2.22098,
    "take_profits": [[2.26738, 50]],
    "PnL": 1.15,
    "chart_image": "https://www.tradingview.com/x/zTSV2TwR/"
}
# played 15 min origin sweep
# - bug with moving stop loss caused to sell all position early in profit

trade = {
    "symbol": 'MANAUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 2.966,
    "sl_price": 2.852,
    "take_profits": [[3.183, 50]],
    "PnL": 1.04,
    "chart_link": "https://www.tradingview.com/x/48wSf95m/"
}

trade = {
    "symbol": 'ADAUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.7,
    "entry_price": 2.09487,
    "sl_price": 2.07361,
    "take_profits": [[2.1374, 50]],
    "PnL": -0.71,
    "chart_link": "https://www.tradingview.com/x/ciFUgP0J/"
}

trade = {
    "symbol": 'SHIBUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 0.00005637,
    "sl_price": 0.00005476,
    "take_profits": [[0.00005476, 50]],
    "PnL": 0.38,
    "chart_link": "https://www.tradingview.com/x/5eQfiArr/"
}
trade = {
    "symbol": 'SHIBUSDTM',
    "side": 'short',
    "take_profits": [[0.00005302, 25]]
}

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.7,
    "entry_price": 66438,
    "sl_price": 66185,
    "take_profits": [[66941, 50]],
    "PnL": -1.05,
    "chart_link": "https://www.tradingview.com/x/smyY6Ytn/"
}
# # sweep play
# # lost

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 60115,
    "sl_price": 59905,
    "take_profits": [[60546, 50]],
    "PnL": -1.22,
    "chart_link": "https://www.tradingview.com/x/NwSsHxSM/"
}

trade = {
    "symbol": 'MANAUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "sl_price": 3.30301,
    "PnL": .38,
    "chart_link": "https://www.tradingview.com/x/PoMM1NRA/"
}

trade = {
    "symbol": 'SANDUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 4.33507,
    "sl_price": 4.39044,
    "take_profits": [[4.23103, 50]],
    "PnL": -0.66,
    "chart_link": "https://www.tradingview.com/x/fkV3yiNE/"
}

trade = {
    "symbol": 'MANAUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 3.62,
    "sl_price": 3.716,
    "take_profits": [[3.451, 50]],
    "PnL": -0.59,
    "chart_link": "https://www.tradingview.com/x/oTI9JX6p/"
}

trade = {
    "symbol": 'BNBUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "sl_price": 589.97,
    "PnL": -0.77,
    "chart_link": "https://www.tradingview.com/x/WS91uDRm/"
}

trade = {
    "symbol": 'SANDUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 7.61929,
    "sl_price": 7.69482,
    "take_profits": [[7.47045,50]],
    "PnL": -0.69,
    "chart_link": "https://www.tradingview.com/x/wVYGrfsw/"
}

trade = {
    "symbol": 'SHIBUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 0.00003854,
    "sl_price": 0.00003821,
    "take_profits": [[0.00003942,50]],
    "PnL": -0.46,
    "chart_link": "https://www.tradingview.com/x/9Ej2uTOc/"
}

trade = {
    "symbol": 'SANDUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 7.74199,
    "sl_price": 7.81921,
    "take_profits": [[7.57077,50]],
    "PnL": 2.69,
    "chart_link": "https://www.tradingview.com/x/CwqGOJlP/"
}

trade = {
    "symbol": 'GALAUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 0.70852,
    "sl_price": 0.72167,
    "take_profits": [[0.68186,50]],
    "PnL": -0.66,
    "chart_link": "https://www.tradingview.com/x/Eob1on6I/"
}

trade = {
    "symbol": 'GALAUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 0.74024,
    "sl_price": 0.764,
    "take_profits": [[0.69597,50]],
    "PnL": -0.56,
    "chart_link": "https://www.tradingview.com/x/WiyMe5wC/"
}

trade = {
    "symbol": 'GALAUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 0.76535,
    "sl_price": 0.78414,
    "take_profits": [[0.73195,50]],
    "PnL": 0.58,
    "chart_link": "https://www.tradingview.com/x/hAIWOFxj/"
}

trade = {
    "symbol": 'AVAXUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 129.3,
    "sl_price": 130.54,
    "take_profits": [[127.02,50]],
    "PnL": 1.69,
    "chart_link": "https://www.tradingview.com/x/upWTilyt/"
}

trade = {
    "symbol": 'ETHUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 4080.5,
    "sl_price": 4097.5,
    "take_profits": [[4047.5,50]],
    "PnL": 0.37,
    "chart_link": "https://www.tradingview.com/x/fckR4ylm/"
}

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "take_profits": [[54353, 50]],
    "PnL": -1.07,
    "chart_link": "https://www.tradingview.com/x/HCp2f5DI/"
}

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 54251,
    "sl_price": 54187,
    "take_profits": [[54377, 33]],
    "PnL": -2.77,
    "chart_link": "https://www.tradingview.com/x/YiPeOfhH/"
}

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "sl_price": 54365,
    "PnL": 0.13,
    "chart_link": "https://www.tradingview.com/x/7cmoVpyQ/"
}

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 54274,
    "sl_price": 54391,
    "take_profits": [[54048, 100]],
    "PnL": -0.49,
    "chart_link": "https://www.tradingview.com/x/ufHlXOjA/"
}

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 54553,
    "sl_price": 54689,
    "take_profits": [[54281, 33]],
    "PnL": -0.19,
    "chart_link": "https://www.tradingview.com/x/ZtceQsar/"
}

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 58756,
    "sl_price": 58933,
    "take_profits": [[58414, 50], [58061, 50]],
    "PnL": 1.52,
    "chart_link": "https://www.tradingview.com/x/usZUliQu/"
}

trade = {
    "symbol": 'ETHUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 4452.5,
    "sl_price": 4462.50,
    "take_profits": [[4435, 50]],
    "PnL": -0.59,
    "chart_link": "https://www.tradingview.com/x/yAycqEa1/"
}

trade = {
    "symbol": 'LUNAUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 1,
    "entry_price": 55.776,
    "sl_price": 56.129,
    "take_profits": [[55.085, 50]],
    "PnL": -1.80,
    "chart_link": "https://www.tradingview.com/x/GoHNATgW/"
}
# should have bailed when seeing long bias against BTC.. 
# e.g. seeing LUNA go up proportionally or more with BTC, but not as much down with BTC

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "sl_price": 58372,
    "PnL": -0.97,
    "chart_link": "https://www.tradingview.com/x/Vu7RZu2a/"
}

trade = {
    "symbol": 'LUNAUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 1,
    "entry_price": 56.721,
    "sl_price": 57.073,
    "take_profits": [[56.013, 50]],
    "PnL": -1.20,
    "chart_link": "https://www.tradingview.com/x/2wrSmRmy/"
}

trade = {
    "symbol": 'SHIBUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 1,
    "entry_price": 0.00004586,
    "sl_price": 0.0000456,
    "take_profits": [[0.0000464, 50]],
    "PnL": -1.28,
    "chart_link": "https://www.tradingview.com/x/alvnCUMU/"
}

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.7,
    "entry_price": 56559,
    "sl_price": 56321,
    "take_profits": [[57011, 50]],
    "PnL": -.90,
    "chart_link": "https://www.tradingview.com/x/VBSIvmhi/"
}

trade = {
    "symbol": 'SANDUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 6.7079,
    "sl_price": 6.78725,
    "take_profits": [[6.55231, 50]],
    "PnL": -0.54,
    "chart_link": "https://www.tradingview.com/x/b8JXkSdy/"
}

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "sl_price": 56777,
    "PnL": 0.60,
    "chart_link": "https://www.tradingview.com/x/ZsolPJsx/"
}

trade = {
    "symbol": 'SANDUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 6.35475,
    "sl_price": 6.17532,
    "take_profits": [[6.7459, 50]],
    "PnL": 1.40,
    "chart_link": "https://www.tradingview.com/x/IG9uc1CR/"
}

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.7,
    "entry_price": 56326,
    "sl_price": 56074,
    "take_profits": [[56801, 50]],
    "PnL": 1.06,
    "chart_link": "https://www.tradingview.com/x/KGrFzCdV/"
}

trade = {
    "symbol": 'GALAUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.5,
    "sl_price": 0.54170,
    "PnL": 0.71,
    "chart_link": "https://www.tradingview.com/x/Y01Y3pA8/"
}

trade = {
    "symbol": 'SHIBUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 0.000041,
    "sl_price": 0.00004086,
    "take_profits": [[0.00004128, 50], [0.00004147, 25], [0.00004188, 25]],
    "PnL": 2.84,
    "chart_link": "https://www.tradingview.com/x/DWuqKbta/"
}

trade = {
    "symbol": 'AVAXUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.7,
    "entry_price": 91.03,
    "sl_price": 93.24,
    "take_profits": [[86.88, 40], [84.67, 40]],
    "PnL": -.70,
    "chart_link": "https://www.tradingview.com/x/nCPjEkNd/"
}

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 48228,
    "sl_price": 48392,
    "take_profits": [[47924, 50]],
    "PnL": 0.78,
    "chart_link": "https://www.tradingview.com/x/ZeeKyD1z/"
}

trade = {
    "symbol": 'AVAXUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "entry_price": 86.69,
    "sl_price": 87.33,
    "take_profits": [[85.57, 50]],
    "PnL": -0.12,
    "chart_link": "https://www.tradingview.com/x/PhBSkWLN/"
}

trade = {
    "symbol": 'ETHUSDTM',
    "side": 'long',
    "acct_sz": '',
    "pct_risk": 1,
    "sl_price": 3982.32,
    "PnL": -1.25,
    "chart_link": "https://www.tradingview.com/x/zLNbS10Z/"
}

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.9,
    "entry_price": 49088,
    "sl_price": 49403,
    "take_profits": [[48482, 50]],
    "PnL": -1.07,
    "chart_link": ["https://www.tradingview.com/x/0hT575F9/", "https://www.tradingview.com/x/ocPoLfWc/"]
}

trade = {
    "symbol": 'MATICUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.9,
    "entry_price": 2.1837,
    "sl_price": 2.2115,
    "take_profits": [[2.1386, 50]],
    "PnL": 0.58,
    "chart_link": ["https://www.tradingview.com/x/xNvMbf8Y/", "https://www.tradingview.com/x/jsoEIDJp/"]
}

trade = {
    "symbol": 'XBTUSDTM',
    "side": 'short',
    "acct_sz": '',
    "pct_risk": 0.5,
    "sl_price": 51170,
    "PnL": 1.56,
    "chart_link": "https://www.tradingview.com/x/GFNpvJBg/"
}