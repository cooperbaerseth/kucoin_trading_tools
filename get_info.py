import pdb
from kucoin_futures.client import Market

#  MarketData
client = Market(url='https://api-futures.kucoin.com')
# client = Market()

ret = client.get_contracts_list()

for i in ret:
    print(i)
# pdb.set_trace()


