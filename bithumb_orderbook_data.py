from json import loads as load_json
import json
from datetime import datetime as DateTime
from base64 import b64encode, b64decode
from hmac import digest
import requests
import csv
import time
from datetime import datetime
import pymysql


#csvfile = open('bithumb_orderbook_data.csv', 'a', newline='', encoding='utf-8')

#c = csv.writer(str(bithumb_orderbook_data.csv))
#c.writerow( ['date/time', 'order rank #', 'price (ask)','amount (ask)', 'price (bid)', 'amount (bid)'] )

api_key = 'de9235bce0b7674b73a393586d1bef20'
secret_code = 'b7d3c3a1aa922180a9a43f72942d70d0224a82e55843ee7530166a1d3da0436f'

URL_WITHDRAW = 'https://global-openapi.bithumb.pro/openapi/v1/withdraw'
URL = 'https://global-openapi.bithumb.pro/openapi/v1/spot/'
DEPTH_URL = 'https://global-openapi.bithumb.pro/market/data/orderBook?symbol='
CONFIG_URL = 'https://global-openapi.bithumb.pro/market/data/config'


class BithumbGlobalError(RuntimeError):
    def __init__(self, code, msg):
        super().__init__('[%s] %s' % (code, msg))


SIDE_MAP = {
    'ask': 'sell',
    'bid': 'buy',
    'sell': 'sell',
    's': 'sell',
    'buy': 'buy',
    'a': 'sell',
    'b': 'buy',
}


def direction(direction):
    return SIDE_MAP[direction.lower()]


def depth(data):
    data = data['info']
    asks = [(float(row[0]), float(row[1])) for row in data['s']]
    bids = [(float(row[0]), float(row[1])) for row in data['b']]

    return {'asks': asks, 'bids': bids}


def all_pairs(data):
    return data['info']['spotConfig']


class Secret:
    def __init__(self, api_key, secret_code):
        self.__api_key = api_key
        self.__secret_code = secret_code.encode()

    def sign(self, data):
        data = list(data.items())
        data.sort()
        msg = '&'.join(['%s=%s' % (k, v) for k, v in data])
        return digest(self.__secret_code, msg.encode('utf-8'), 'sha256').hex()

    @property
    def api_key(self):
        return self.__api_key


class BithumbGlobalRestAPI:
    def __init__(self, api_key, secret_code):
        if api_key and secret_code:
            self.__secret = Secret(api_key, secret_code)
        else:
            self.__secret = None
        self.__session = session = requests.session()
        session.headers.update({'content-Type': 'application/json'})

    @property
    def session(self):
        return self.__session

    def post(self, action, parms):
        ts = str(int(DateTime.now().timestamp() * 1000))
        data = {
            'apiKey': self.__secret.api_key,
            'bizCode': action,
            'msgNo': ts,
            'timestamp': ts,
        }
        data.update(parms)

        data['signature'] = self.__secret.sign(data)

        response = self.session.post(url=URL + action, json=data, timeout=15)
        response = load_json(response.text)

        if response['code'] != '0':
            raise BithumbGlobalError(response['code'], response['msg'])
        return response['data']

    def withdraw(self, cointype, address, volume, mark='AUTO', memo=None):
        parms = {
            'coinType': cointype,
            'address': address,
            'quantity': volume,
            'mark': mark
        }
        action = 'withdraw'
        if memo:
            parms['extendParam'] = memo
        ts = str(int(DateTime.now().timestamp() * 1000))
        data = {
            'apiKey': self.__secret.api_key,
            'bizCode': action,
            'msgNo': ts,
            'timestamp': ts,
        }
        data.update(parms)

        data['signature'] = self.__secret.sign(data)

        response = self.session.post(url=URL_WITHDRAW, json=data, timeout=15)
        response = load_json(response.text)

        if response['code'] != '0':
            raise BithumbGlobalError(response['code'], response['msg'])
        return response['data']

    def all_pairs(self):
        response = self.__session.get(CONFIG_URL)
        data = load_json(response.text)
        return all_pairs(data)

    def place_order(self, symbol, side, price, amount):
        symbol = symbol.replace('/', '-')
        parms = {
            'symbol': symbol,
            'type': 'market',
            'side': direction(side),
            'price': '%.8f' % -1,
            'quantity': '%.8f' % amount
        }
        return self.post('placeOrder', parms)['orderId']

    def cancel_order(self, symbol, order_id):
        parms = {
            'symbol': symbol.replace('/', '-'),
            'orderID': order_id,
        }
        result = self.post('cancelOrder', parms)
        return result

    def balance(self, coin=None):
        parms = {
            'assetType': 'spot'
        }
        if coin:
            parms['coinType'] = coin
        result = self.post('assetList', parms)
        return result

    def orders(self, side=None, queryRange='thisweek', coinType=None, marketType=None, status=None, page=1, count=10):
        parms = {
            'page': str(page),
            'count': str(count)
        }
        parms['queryRange'] = queryRange
        if side:
            assert side in ('buy', 'sell')
            parms['side'] = side
        if coinType:
            parms['coinType'] = coinType
        if marketType:
            parms['marketType'] = marketType
        if status:
            assert status in ('traded', 'trading')
            parms['status'] = status
        return self.post('orderList', parms)

    def order_detail(self, order_id, page=1, count=10):
        parms = {
            'orderId': order_id,
            'page': str(page),
            'count': str(count)
        }
        return self.post('strikeOrderListApi', parms)

    def market(self, coin=None, market=None):
        parms = {}
        if coin:
            parms['fcoinId'] = coin
        if market:
            parms['fmarketId'] = market
        return self.post('MARKET_SPOT', parms)

    def depth(self, symbol, count):
        url = DEPTH_URL + symbol.replace('/', '-')
        data = load_json(self.__session.get(url, timeout=5).text)
        return depth(data)

    def query_order(self, symbol, order_id):
        symbol = symbol.replace('/', '-')
        order = self.post('singleOrder', {'symbol': symbol, 'orderId': order_id})
        return order

    def openning_orders(self, symbol, id_only=True):
        result = []
        page = 1
        while True:
            parms = {
                'count': 50,
                'page': page,
                'symbol': symbol.replace('/', '-'),
            }
            orders = self.post('openOrders', parms)
            result += orders['list']
            if int(orders['num']) <= page * 50:
                break
            else:
                page += 1
        if id_only:
            result = [row['orderId'] for row in result]
        return result

def bithumb_orderbook_funtion():
    connection = pymysql.connect(host="localhost", user="adminer", passwd="Crypto#123", database="radmin")

    cursor = connection.cursor()


    time.sleep(2)
    a = BithumbGlobalRestAPI(api_key, secret_code)
    #print(a.all_pairs())
    bithumb_xlm_orderflow = a.depth(symbol = 'XLM/USDT', count='1')

    #bithumb parse the asks
    bithumb_ask1  = bithumb_xlm_orderflow['asks'][0][0]
    bithumb_ask_amount1  = bithumb_xlm_orderflow['asks'][0][1]
    bithumb_ask2  = bithumb_xlm_orderflow['asks'][1][0]
    bithumb_ask_amount2  = bithumb_xlm_orderflow['asks'][1][1]
    bithumb_ask3  = bithumb_xlm_orderflow['asks'][2][0]
    bithumb_ask_amount3  = bithumb_xlm_orderflow['asks'][2][1]
    bithumb_ask4  = bithumb_xlm_orderflow['asks'][3][0]
    bithumb_ask_amount4  = bithumb_xlm_orderflow['asks'][3][1]
    bithumb_ask5  = bithumb_xlm_orderflow['asks'][4][0]
    bithumb_ask_amount5  = bithumb_xlm_orderflow['asks'][4][1]
    bithumb_ask6  = bithumb_xlm_orderflow['asks'][5][0]
    bithumb_ask_amount6  = bithumb_xlm_orderflow['asks'][5][1]
    bithumb_ask7  = bithumb_xlm_orderflow['asks'][6][0]
    bithumb_ask_amount7  = bithumb_xlm_orderflow['asks'][6][1]

    #bithumb parse the bids
    bithumb_bid1  = bithumb_xlm_orderflow['bids'][0][0]
    bithumb_bid_amount1  = bithumb_xlm_orderflow['bids'][0][1]
    bithumb_bid2  = bithumb_xlm_orderflow['bids'][1][0]
    bithumb_bid_amount2  = bithumb_xlm_orderflow['bids'][1][1]
    bithumb_bid3  = bithumb_xlm_orderflow['bids'][2][0]
    bithumb_bid_amount3  = bithumb_xlm_orderflow['bids'][2][1]
    bithumb_bid4  = bithumb_xlm_orderflow['bids'][3][0]
    bithumb_bid_amount4  = bithumb_xlm_orderflow['bids'][3][1]
    bithumb_bid5  = bithumb_xlm_orderflow['bids'][4][0]
    bithumb_bid_amount5  = bithumb_xlm_orderflow['bids'][4][1]
    bithumb_bid6  = bithumb_xlm_orderflow['bids'][5][0]
    bithumb_bid_amount6  = bithumb_xlm_orderflow['bids'][5][1]
    bithumb_bid7  = bithumb_xlm_orderflow['bids'][6][0]
    bithumb_bid_amount7  = bithumb_xlm_orderflow['bids'][6][1]

    bithumb_ask_bid_data = [datetime.now(), 1, bithumb_ask1, bithumb_ask_amount1, bithumb_bid1, bithumb_bid_amount1], [datetime.now(), 2, bithumb_ask2, bithumb_ask_amount2, bithumb_bid2, bithumb_bid_amount2], \
                           [datetime.now(), 3, bithumb_ask3, bithumb_ask_amount3, bithumb_bid3, bithumb_bid_amount3], [datetime.now(), 4, bithumb_ask4, bithumb_ask_amount4, bithumb_bid4, bithumb_bid_amount4], \
                           [datetime.now(), 5, bithumb_ask5, bithumb_ask_amount5, bithumb_bid5, bithumb_bid_amount5], [datetime.now(),6, bithumb_ask6, bithumb_ask_amount6, bithumb_bid6, bithumb_bid_amount6], \
                           [datetime.now(), 7, bithumb_ask7, bithumb_ask_amount7, bithumb_bid7, bithumb_bid_amount7]


    bithumb_ask_data = [bithumb_ask1, bithumb_ask_amount1, bithumb_ask2, bithumb_ask_amount2, bithumb_ask3, bithumb_ask_amount3]
    bithumb_bid_data = [bithumb_bid1, bithumb_bid_amount1, bithumb_bid2, bithumb_bid_amount2, bithumb_bid3, bithumb_bid_amount3]
    print(bithumb_ask_data)
    print(bithumb_bid_data)

    add_bithumb_ask_data = ('INSERT INTO `bithumb_ask_feed` (`id`, `bithumb_ask1`, `bithumb_ask_amount1`, `bithumb_ask2`, `bithumb_ask_amount2`, `bithumb_ask3`, `bithumb_ask_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{})'.format('NULL', bithumb_ask1, bithumb_ask_amount1, bithumb_ask2, bithumb_ask_amount2, bithumb_ask3, bithumb_ask_amount3, 'NULL', 'NULL'))
    add_bithumb_bid_data = ('INSERT INTO `bithumb_bid_feed` (`id`, `bithumb_bid1`, `bithumb_bid_amount1`, `bithumb_bid2`, `bithumb_bid_amount2`, `bithumb_bid3`, `bithumb_bid_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{})'.format('NULL', bithumb_bid1, bithumb_bid_amount1, bithumb_bid2, bithumb_bid_amount2, bithumb_bid3, bithumb_bid_amount3, 'NULL', 'NULL'))

    cursor.execute(add_bithumb_ask_data)
    cursor.execute(add_bithumb_bid_data)
    connection.commit()

    connection.close()
    '''bithumb_ask2_data = [2, bithumb_ask2, bithumb_ask_amount2]
    bithumb_ask3_data = [3, bithumb_ask3, bithumb_ask_amount3]
    bithumb_ask4_data = [4, bithumb_ask4, bithumb_ask_amount4]
    bithumb_ask5_data = [5, bithumb_ask5, bithumb_ask_amount5]
    bithumb_ask6_data = [6, bithumb_ask6, bithumb_ask_amount6]
    bithumb_ask7_data = [7, bithumb_ask7, bithumb_ask_amount7]'''

    #print asks
    '''print(bithumb_xlm_orderflow)

    print('asks')
    print(bithumb_ask1)
    print(bithumb_ask_amount1)
    print(bithumb_ask2)
    print(bithumb_ask_amount2)
    print(bithumb_ask3)
    print(bithumb_ask_amount3)
    print(bithumb_ask4)
    print(bithumb_ask_amount4)
    print(bithumb_ask5)
    print(bithumb_ask_amount5)
    print(bithumb_ask6)
    print(bithumb_ask_amount6)
    print(bithumb_ask7)
    print(bithumb_ask_amount7)

    #print(bithumb_ask_bid_data)

    print(bithumb_ask1_data)
    print(bithumb_ask2_data)
    print(bithumb_ask3_data)
    print(bithumb_ask4_data)
    print(bithumb_ask5_data)
    print(bithumb_ask6_data)
    print(bithumb_ask7_data)'''


    #bithumb bids
    #print(bithumb_xlm_orderflow)
    '''print('bids')
    print(bithumb_bid1)
    print(bithumb_bid_amount1)
    print(bithumb_bid2)
    print(bithumb_bid_amount2)
    print(bithumb_bid3)
    print(bithumb_bid_amount3)
    print(bithumb_bid4)
    print(bithumb_bid_amount4)
    print(bithumb_bid5)
    print(bithumb_bid_amount5)
    print(bithumb_bid6)
    print(bithumb_bid_amount6)
    print(bithumb_bid7)
    print(bithumb_bid_amount7)'''



    bithumb_ask_feed = open('bithumb_ask_feed.text', "w")

    bithumb_ask_feed.write(str(bithumb_ask_data))

    bithumb_ask_feed.close()

    bithumb_bid_feed = open('bithumb_bid_feed.text', "w")

    bithumb_bid_feed.write(str(bithumb_bid_data))

    bithumb_bid_feed.close()


    the_list = bithumb_ask_bid_data
    csvfile = open('bithumb_orderbook_data.csv', 'a', newline='')  # newline='', encoding='utf-8')

    c = csv.writer(csvfile)
    print(bithumb_ask_bid_data)

    for item in bithumb_ask_bid_data:

        c.writerow(item)

    csvfile.close()

while True:

    try:
        bithumb_orderbook_funtion()

        time.sleep(1)


    except Exception as ex:

        logerros = open('errors.text', "a")

        logerros.write('| bithumb error:' + str(datetime.now()) + " " + str(ex))

        logerros.close()

        print(ex)

#bithumb get balance
#bithumb_usdt_balance_json_unf = a.balance('USDT')
#bithumb_usdt_balance_str = json.dumps(bithumb_usdt_balance_json_unf)
#bithumb_usdt_balance = (bithumb_usdt_balance_str.split('"')[13])
#print(bithumb_usdt_balance)

#bithumb order
#bithumb_test_order = a.place_order(symbol='XLM-USDT', side='sell', price='price', amount= float(bithumb_xlm_balance))
#print(bithumb_xlm_balance)

#bithumb_usdt_withdraw = a.withdraw(cointype='USDT-TRC20', address='TTSJ719BGnR24gMsvLbTHv93r6Nj5DpBSo', volume=bithumb_usdt_balance)
#print(bithumb_usdt_withdraw)
#place_order('placeOrder', 'XLM-KRW', side = 'sell', price = -1, amount = 450)['111']
