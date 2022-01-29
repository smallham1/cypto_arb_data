import json
import pymysql
import time
from datetime import datetime

import csv
#root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#sys.path.append(root + '/python')

import ccxt  # noqa: E402


#csvfile = open('huobi_orderbook_data.csv', 'w', newline='', encoding='utf-8')
#c = csv.writer(csvfile)
#c.writerow( ['date/time', 'order rank #', 'price (ask)','amount (ask)', 'price (bid)', 'amount (bid)'] )


def get_positive_accounts(balance):
    result = {}
    currencies = list(balance.keys())
    for currency in currencies:
        if balance[currency] and balance[currency] > 0:
            result[currency] = balance[currency]
    return result

    #define exchange


x = 0
def huobi_orderbook_function():
    connection = pymysql.connect(host="localhost", user="adminer", passwd="Crypto#123", database="radmin")

    cursor = connection.cursor()
    exchange = ccxt.huobi({
        'uid': '',
        'apiKey': '',
        'secret': '',
        'enableRateLimit': True,
        'has': {'fetchWithdrawals': True, 'withdraw': True}
    })

    csvfile = open('huobiglobal_orderbook_data.csv', 'a', newline='') # newline='', encoding='utf-8')
    c = csv.writer(csvfile)

    huobi_xlm_orderflow_json_unf = exchange.fetch_order_book('XLM/USDT')
    huobi_xlm_orderflow_str_unf1 = json.dumps(huobi_xlm_orderflow_json_unf)
    huobi_xlm_ask_str_unf = (huobi_xlm_orderflow_str_unf1.split("asks")[1])
    huobi_xlm_bid_str_unf = (huobi_xlm_orderflow_str_unf1.split("asks")[0])

    #get first ask price order
    huobi_xlm_askprice_1st_unf = (huobi_xlm_ask_str_unf.split(",")[0])
    huobi_xlm_askprice_1st = (huobi_xlm_askprice_1st_unf.split("[")[2])

    #get first ask quantity
    huobi_xlm_askprice_1st_quantity_unf = (huobi_xlm_ask_str_unf.split(',')[1])
    huobi_xlm_askprice_1st_quantity = (huobi_xlm_askprice_1st_quantity_unf.split("]")[0])
    huobi_xlm_askprice_1st_quantity = huobi_xlm_askprice_1st_quantity.strip()
    #first ask order value
    huobi_xlm_ask_value_1st = float(huobi_xlm_askprice_1st)*float(huobi_xlm_askprice_1st_quantity)

    #get second ask order price
    huobi_xlm_askprice_2nd_unf = (huobi_xlm_ask_str_unf.split(",")[2])
    huobi_xlm_askprice_2nd = (huobi_xlm_askprice_2nd_unf.split("[")[1])

    #get second ask order quantity
    huobi_xlm_askprice_2nd_quantity_unf = (huobi_xlm_ask_str_unf.split(',')[3])
    huobi_xlm_askprice_2nd_quantity = (huobi_xlm_askprice_2nd_quantity_unf.split("]")[0])
    huobi_xlm_askprice_2nd_quantity = huobi_xlm_askprice_2nd_quantity.strip()
    #get second order value
    huobi_xlm_ask_value_2nd = float(huobi_xlm_askprice_2nd)*float(huobi_xlm_askprice_2nd_quantity)

    #get third order ask price
    huobi_xlm_askprice_3rd_unf = (huobi_xlm_ask_str_unf.split(",")[4])
    huobi_xlm_askprice_3rd = (huobi_xlm_askprice_3rd_unf.split("[")[1])

    #get third ask quanitity
    huobi_xlm_askprice_3rd_quantity_unf = (huobi_xlm_ask_str_unf.split(',')[5])
    huobi_xlm_askprice_3rd_quantity = (huobi_xlm_askprice_3rd_quantity_unf.split("]")[0])
    huobi_xlm_askprice_3rd_quantity = huobi_xlm_askprice_3rd_quantity.strip()
    #get third ask order amount
    huobi_xlm_ask_value_3rd = float(huobi_xlm_askprice_3rd_quantity)*float(huobi_xlm_askprice_3rd)

    ###########################################################################

    #get first bid price order
    huobi_xlm_bidprice_1st_unf = (huobi_xlm_bid_str_unf.split(",")[1])
    huobi_xlm_bidprice_1st = (huobi_xlm_bidprice_1st_unf.split("[")[2])

    #get first bid quantity
    huobi_xlm_bidprice_1st_quantity_unf = (huobi_xlm_bid_str_unf.split(',')[2])
    huobi_xlm_bidprice_1st_quantity = (huobi_xlm_bidprice_1st_quantity_unf.split("]")[0])
    huobi_xlm_bidprice_1st_quantity = huobi_xlm_bidprice_1st_quantity.strip()

    ########################################################33
    huobi_xlm_bidprice_2_unf = (huobi_xlm_bid_str_unf.split(",")[3])
    huobi_xlm_bidprice_2 = (huobi_xlm_bidprice_2_unf.split("[")[1])

    #get first bid quantity
    huobi_xlm_bidprice_2_quantity_unf = (huobi_xlm_bid_str_unf.split(',')[4])
    huobi_xlm_bidprice_2_quantity = (huobi_xlm_bidprice_2_quantity_unf.split("]")[0])
    huobi_xlm_bidprice_2_quantity = huobi_xlm_bidprice_2_quantity.strip()

    ########################################################33
    huobi_xlm_bidprice_3_unf = (huobi_xlm_bid_str_unf.split(",")[5])
    huobi_xlm_bidprice_3 = (huobi_xlm_bidprice_3_unf.split("[")[1])

    #get first bid quantity
    huobi_xlm_bidprice_3_quantity_unf = (huobi_xlm_bid_str_unf.split(',')[6])
    huobi_xlm_bidprice_3_quantity = (huobi_xlm_bidprice_3_quantity_unf.split("]")[0])
    huobi_xlm_bidprice_3_quantity = huobi_xlm_bidprice_3_quantity.strip()

    huobi_ask_bid_data = [datetime.now(), 1, huobi_xlm_askprice_1st, huobi_xlm_askprice_1st_quantity, huobi_xlm_bidprice_1st,huobi_xlm_bidprice_1st_quantity], [datetime.now(), 2, huobi_xlm_askprice_2nd, huobi_xlm_askprice_2nd_quantity, huobi_xlm_bidprice_2, huobi_xlm_bidprice_2_quantity], \
                               [datetime.now(), 3, huobi_xlm_askprice_3rd, huobi_xlm_askprice_3rd_quantity, huobi_xlm_bidprice_3, huobi_xlm_bidprice_3_quantity]



    huobi_ask_data = [huobi_xlm_askprice_1st, huobi_xlm_askprice_1st_quantity, huobi_xlm_askprice_2nd, huobi_xlm_askprice_2nd_quantity, huobi_xlm_askprice_3rd, huobi_xlm_askprice_3rd_quantity]

    huobi_bid_data = [huobi_xlm_bidprice_1st, huobi_xlm_bidprice_1st_quantity, huobi_xlm_bidprice_2, huobi_xlm_bidprice_2_quantity, huobi_xlm_bidprice_3, huobi_xlm_bidprice_3_quantity]
    #print('raw orderbook')
    #print(huobi_xlm_orderflow_str_unf1)
    #print('compiled data')
    #print(huobi_ask_bid_data)
    #print('ask/bid')

    add_huobi_ask_data = (
        'INSERT INTO `huobi_ask_feed` (`id`, `huobi_ask1`, `huobi_ask_amount1`, `huobi_ask2`, `huobi_ask_amount2`, `huobi_ask3`, `huobi_ask_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{})'.format(
            'NULL', huobi_xlm_askprice_1st, huobi_xlm_askprice_1st_quantity, huobi_xlm_askprice_2nd,
            huobi_xlm_askprice_2nd_quantity, huobi_xlm_askprice_3rd,
            huobi_xlm_askprice_3rd_quantity, 'NULL', 'NULL'))
    add_huobi_bid_data = (
        'INSERT INTO `huobi_bid_feed` (`id`, `huobi_bid1`, `huobi_bid_amount1`, `huobi_bid2`, `huobi_bid_amount2`, `huobi_bid3`, `huobi_bid_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{})'.format(
            'NULL', huobi_xlm_bidprice_1st, huobi_xlm_bidprice_1st_quantity, huobi_xlm_bidprice_2,
            huobi_xlm_bidprice_2_quantity, huobi_xlm_bidprice_3,
            huobi_xlm_bidprice_3_quantity, 'NULL', 'NULL'))

    cursor.execute(add_huobi_ask_data)
    cursor.execute(add_huobi_bid_data)
    connection.commit()

    connection.close()
    print(huobi_ask_data)
    print(huobi_bid_data)
    #print('XXXXXXX')
    #print(huobi_ask_bid_data)


    for item in huobi_ask_bid_data:

        c.writerow(item)

    csvfile.close()

    huobi_ask_feed = open('huobi_ask_feed.text', "w")

    huobi_ask_feed.write(str(huobi_ask_data))

    huobi_ask_feed.close()

    huobi_bid_feed = open('huobi_bid_feed.text', "w")

    huobi_bid_feed.write(str(huobi_bid_data))

    huobi_bid_feed.close()



while True:
    try:
        huobi_orderbook_function()


        time.sleep(1)


    except Exception as ex:

        logerros = open('errors.text', "a")

        logerros.write('| huobi error:' + str(datetime.now()) + " " + str(ex))

        logerros.close()

        print(ex)


    '''print(huobi_xlm_orderflow_str_unf1)
    print('######################################')
    print(huobi_xlm_bid_str_unf)
    print('huobi ask price:', huobi_xlm_askprice_1st)
    print('huobi quantity:', huobi_xlm_askprice_1st_quantity)
    print('huobi ask price:', huobi_xlm_askprice_2nd)
    print('huobi quantity:', huobi_xlm_askprice_2nd_quantity)
    print('huobi ask price', huobi_xlm_askprice_3rd)
    print('huobi quantity:', huobi_xlm_askprice_3rd_quantity)'''
    '''print(huobi_xlm_bidprice_1st)
    print(huobi_xlm_bidprice_1st_quantity)
    print(huobi_xlm_bidprice_2)
    print(huobi_xlm_bidprice_2_quantity)
    print(huobi_xlm_bidprice_3)
    print(huobi_xlm_bidprice_3_quantity)'''
