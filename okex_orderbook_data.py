import json

import time
from datetime import datetime

import csv
#root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#sys.path.append(root + '/python')
import logging
import ccxt  # noqa: E402
import pymysql

#csvfile = open('okex_orderbook_data.csv', 'w', newline='', encoding='utf-8')
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
def okex_orderbook_function():
    connection = pymysql.connect(host="", user="", passwd="", database="")

    cursor = connection.cursor()
    exchange = ccxt.okex({
        'uid': '',
        'apiKey': '',
        'secret': '',
        'enableRateLimit': True,
        'has': {'fetchWithdrawals': True, 'withdraw': True}
    })

    csvfile = open('okex_orderbook_data.csv', 'a', newline='') # newline='', encoding='utf-8')
    c = csv.writer(csvfile)

    okex_xlm_orderflow_json_unf = exchange.fetch_order_book('XLM/USDT')
    okex_xlm_orderflow_str_unf1 = json.dumps(okex_xlm_orderflow_json_unf)
    okex_xlm_ask_str_unf = (okex_xlm_orderflow_str_unf1.split("asks")[1])
    okex_xlm_bid_str_unf = (okex_xlm_orderflow_str_unf1.split("asks")[0])

    #get first ask price order
    okex_xlm_askprice_1st_unf = (okex_xlm_ask_str_unf.split(",")[0])
    okex_xlm_askprice_1st = (okex_xlm_askprice_1st_unf.split("[")[2])

    #get first ask quantity
    okex_xlm_askprice_1st_quantity_unf = (okex_xlm_ask_str_unf.split(',')[1])
    okex_xlm_askprice_1st_quantity = (okex_xlm_askprice_1st_quantity_unf.split("]")[0])
    okex_xlm_askprice_1st_quantity = okex_xlm_askprice_1st_quantity.strip()
    #first ask order value
    okex_xlm_ask_value_1st = float(okex_xlm_askprice_1st)*float(okex_xlm_askprice_1st_quantity)

    #get second ask order price
    okex_xlm_askprice_2nd_unf = (okex_xlm_ask_str_unf.split(",")[2])
    okex_xlm_askprice_2nd = (okex_xlm_askprice_2nd_unf.split("[")[1])

    #get second ask order quantity
    okex_xlm_askprice_2nd_quantity_unf = (okex_xlm_ask_str_unf.split(',')[3])
    okex_xlm_askprice_2nd_quantity = (okex_xlm_askprice_2nd_quantity_unf.split("]")[0])
    okex_xlm_askprice_2nd_quantity = okex_xlm_askprice_2nd_quantity.strip()
    #get second order value
    okex_xlm_ask_value_2nd = float(okex_xlm_askprice_2nd)*float(okex_xlm_askprice_2nd_quantity)

    #get third order ask price
    okex_xlm_askprice_3rd_unf = (okex_xlm_ask_str_unf.split(",")[4])
    okex_xlm_askprice_3rd = (okex_xlm_askprice_3rd_unf.split("[")[1])

    #get third ask quanitity
    okex_xlm_askprice_3rd_quantity_unf = (okex_xlm_ask_str_unf.split(',')[5])
    okex_xlm_askprice_3rd_quantity = (okex_xlm_askprice_3rd_quantity_unf.split("]")[0])
    okex_xlm_askprice_3rd_quantity = okex_xlm_askprice_3rd_quantity.strip()
    #get third ask order amount
    okex_xlm_ask_value_3rd = float(okex_xlm_askprice_3rd_quantity)*float(okex_xlm_askprice_3rd)

    ###########################################################################

    #get first bid price order
    okex_xlm_bidprice_1st_unf = (okex_xlm_bid_str_unf.split(",")[1])
    okex_xlm_bidprice_1st = (okex_xlm_bidprice_1st_unf.split("[")[2])

    #get first bid quantity
    okex_xlm_bidprice_1st_quantity_unf = (okex_xlm_bid_str_unf.split(',')[2])
    okex_xlm_bidprice_1st_quantity = (okex_xlm_bidprice_1st_quantity_unf.split("]")[0])
    okex_xlm_bidprice_1st_quantity = okex_xlm_bidprice_1st_quantity.strip()

    ########################################################33
    okex_xlm_bidprice_2_unf = (okex_xlm_bid_str_unf.split(",")[3])
    okex_xlm_bidprice_2 = (okex_xlm_bidprice_2_unf.split("[")[1])

    #get first bid quantity
    okex_xlm_bidprice_2_quantity_unf = (okex_xlm_bid_str_unf.split(',')[4])
    okex_xlm_bidprice_2_quantity = (okex_xlm_bidprice_2_quantity_unf.split("]")[0])
    okex_xlm_bidprice_2_quantity = okex_xlm_bidprice_2_quantity.strip()

    ########################################################33
    okex_xlm_bidprice_3_unf = (okex_xlm_bid_str_unf.split(",")[5])
    okex_xlm_bidprice_3 = (okex_xlm_bidprice_3_unf.split("[")[1])

    #get first bid quantity
    okex_xlm_bidprice_3_quantity_unf = (okex_xlm_bid_str_unf.split(',')[6])
    okex_xlm_bidprice_3_quantity = (okex_xlm_bidprice_3_quantity_unf.split("]")[0])
    okex_xlm_bidprice_3_quantity = okex_xlm_bidprice_3_quantity.strip()

    okex_ask_bid_data = [datetime.now(), 1, okex_xlm_askprice_1st, okex_xlm_askprice_1st_quantity, okex_xlm_bidprice_1st,okex_xlm_bidprice_1st_quantity], [datetime.now(), 2, okex_xlm_askprice_2nd, okex_xlm_askprice_2nd_quantity, okex_xlm_bidprice_2, okex_xlm_bidprice_2_quantity], \
                               [datetime.now(), 3, okex_xlm_askprice_3rd, okex_xlm_askprice_3rd_quantity, okex_xlm_bidprice_3, okex_xlm_bidprice_3_quantity]



    okex_ask_data = [okex_xlm_askprice_1st, okex_xlm_askprice_1st_quantity, okex_xlm_askprice_2nd, okex_xlm_askprice_2nd_quantity, okex_xlm_askprice_3rd, okex_xlm_askprice_3rd_quantity]

    okex_bid_data = [okex_xlm_bidprice_1st, okex_xlm_bidprice_1st_quantity, okex_xlm_bidprice_2, okex_xlm_bidprice_2_quantity, okex_xlm_bidprice_3, okex_xlm_bidprice_3_quantity]
    #print('raw orderbook')
    #print(okex_xlm_orderflow_str_unf1)
    #print('compiled data')
    #print(okex_ask_bid_data)
    #print('ask/bid')

    add_okex_ask_data = (
        "INSERT INTO `okex_ask_feed` (`id`, `okex_ask1`, `okex_ask_amount1`, `okex_ask2`, `okex_ask_amount2`, `okex_ask3`, `okex_ask_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{});".format(
            'NULL', okex_xlm_askprice_1st, okex_xlm_askprice_1st_quantity, okex_xlm_askprice_2nd,
            okex_xlm_askprice_2nd_quantity, okex_xlm_askprice_3rd,
            okex_xlm_askprice_3rd_quantity, 'current_timestamp()', 'NULL'))
    add_okex_bid_data = (
        "INSERT INTO `okex_bid_feed` (`id`, `okex_bid1`, `okex_bid_amount1`, `okex_bid2`, `okex_bid_amount2`, `okex_bid3`, `okex_bid_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{});".format(
            'NULL', okex_xlm_bidprice_1st, okex_xlm_bidprice_1st_quantity, okex_xlm_bidprice_2,
            okex_xlm_bidprice_2_quantity, okex_xlm_bidprice_3,
            okex_xlm_bidprice_3_quantity, 'current_timestamp()', 'NULL'))
    new_bid_data = (
        "INSERT INTO `okex_bid_feed` (`id`, `okex_bid1`, `okex_bid_amount1`, `okex_bid2`, `okex_bid_amount2`, `okex_bid3`, `okex_bid_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{});".format(
            'NULL', '1', '1', '1', '1', '1', '1', 'current_timestamp()', '1'))

    print('inserting')
    cursor.execute(add_okex_ask_data)
    cursor.execute(add_okex_bid_data)
    cursor.execute()
    connection.commit(new_bid_data)
    time.sleep(1)

    print('inserted')

    connection.close()
    print(okex_ask_data)
    print(okex_bid_data)
    #print('XXXXXXX')
    #print(okex_ask_bid_data)


    for item in okex_ask_bid_data:

        c.writerow(item)

    csvfile.close()

    okex_ask_feed = open('okex_ask_feed.text', "w")

    okex_ask_feed.write(str(okex_ask_data))

    okex_ask_feed.close()

    okex_bid_feed = open('okex_bid_feed.text', "w")

    okex_bid_feed.write(str(okex_bid_data))

    okex_bid_feed.close()




while True:
    try:
        okex_orderbook_function()


        time.sleep(1)

    except Exception as ex:
        logerros = open('errors.text', "a")
        logerros.write('| okex error:' + str(datetime.now()) + " " + str(ex))
        logerros.close()
        print(ex)


    '''print(okex_xlm_orderflow_str_unf1)
    print('######################################')
    print(okex_xlm_bid_str_unf)
    print('okex ask price:', okex_xlm_askprice_1st)
    print('okex quantity:', okex_xlm_askprice_1st_quantity)
    print('okex ask price:', okex_xlm_askprice_2nd)
    print('okex quantity:', okex_xlm_askprice_2nd_quantity)
    print('okex ask price', okex_xlm_askprice_3rd)
    print('okex quantity:', okex_xlm_askprice_3rd_quantity)'''
    '''print(okex_xlm_bidprice_1st)
    print(okex_xlm_bidprice_1st_quantity)
    print(okex_xlm_bidprice_2)
    print(okex_xlm_bidprice_2_quantity)
    print(okex_xlm_bidprice_3)
    print(okex_xlm_bidprice_3_quantity)'''
