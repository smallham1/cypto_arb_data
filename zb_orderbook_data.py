import json

import time
from datetime import datetime
import pymysql
import csv
#root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#sys.path.append(root + '/python')

import ccxt  # noqa: E402


#csvfile = open('zb_orderbook_data.csv', 'w', newline='', encoding='utf-8')
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
def zb_orderbook_function():
    connection = pymysql.connect(host="", user="", passwd="", database="")

    cursor = connection.cursor()
    URL = "https://api.zb.work/data"

    exchange = ccxt.zb({
        'uid': '',
        'apiKey': '',
        'secret': '',
        'url': 'https://api.zb.work/data',
        'enableRateLimit': True,
        'has': {'fetchWithdrawals': True, 'withdraw': True}
    })

    csvfile = open('zb_orderbook_data.csv', 'a', newline='') # newline='', encoding='utf-8')
    c = csv.writer(csvfile)

    zb_xlm_orderflow_json_unf = exchange.fetch_order_book('XLM/USDT')
    zb_xlm_orderflow_str_unf1 = json.dumps(zb_xlm_orderflow_json_unf)
    zb_xlm_ask_str_unf = (zb_xlm_orderflow_str_unf1.split("asks")[1])
    zb_xlm_bid_str_unf = (zb_xlm_orderflow_str_unf1.split("asks")[0])

    #get first ask price order
    zb_xlm_askprice_1st_unf = (zb_xlm_ask_str_unf.split(",")[0])
    zb_xlm_askprice_1st = (zb_xlm_askprice_1st_unf.split("[")[2])

    #get first ask quantity
    zb_xlm_askprice_1st_quantity_unf = (zb_xlm_ask_str_unf.split(',')[1])
    zb_xlm_askprice_1st_quantity = (zb_xlm_askprice_1st_quantity_unf.split("]")[0])
    zb_xlm_askprice_1st_quantity = zb_xlm_askprice_1st_quantity.strip()
    #first ask order value
    zb_xlm_ask_value_1st = float(zb_xlm_askprice_1st)*float(zb_xlm_askprice_1st_quantity)

    #get second ask order price
    zb_xlm_askprice_2nd_unf = (zb_xlm_ask_str_unf.split(",")[2])
    zb_xlm_askprice_2nd = (zb_xlm_askprice_2nd_unf.split("[")[1])

    #get second ask order quantity
    zb_xlm_askprice_2nd_quantity_unf = (zb_xlm_ask_str_unf.split(',')[3])
    zb_xlm_askprice_2nd_quantity = (zb_xlm_askprice_2nd_quantity_unf.split("]")[0])
    zb_xlm_askprice_2nd_quantity = zb_xlm_askprice_2nd_quantity.strip()
    #get second order value
    zb_xlm_ask_value_2nd = float(zb_xlm_askprice_2nd)*float(zb_xlm_askprice_2nd_quantity)

    #get third order ask price
    zb_xlm_askprice_3rd_unf = (zb_xlm_ask_str_unf.split(",")[4])
    zb_xlm_askprice_3rd = (zb_xlm_askprice_3rd_unf.split("[")[1])

    #get third ask quanitity
    zb_xlm_askprice_3rd_quantity_unf = (zb_xlm_ask_str_unf.split(',')[5])
    zb_xlm_askprice_3rd_quantity = (zb_xlm_askprice_3rd_quantity_unf.split("]")[0])
    zb_xlm_askprice_3rd_quantity = zb_xlm_askprice_3rd_quantity.strip()
    #get third ask order amount
    zb_xlm_ask_value_3rd = float(zb_xlm_askprice_3rd_quantity)*float(zb_xlm_askprice_3rd)

    ###########################################################################

    #get first bid price order
    zb_xlm_bidprice_1st_unf = (zb_xlm_bid_str_unf.split(",")[1])
    zb_xlm_bidprice_1st = (zb_xlm_bidprice_1st_unf.split("[")[2])

    #get first bid quantity
    zb_xlm_bidprice_1st_quantity_unf = (zb_xlm_bid_str_unf.split(',')[2])
    zb_xlm_bidprice_1st_quantity = (zb_xlm_bidprice_1st_quantity_unf.split("]")[0])
    zb_xlm_bidprice_1st_quantity = zb_xlm_bidprice_1st_quantity.strip()

    ########################################################33
    zb_xlm_bidprice_2_unf = (zb_xlm_bid_str_unf.split(",")[3])
    zb_xlm_bidprice_2 = (zb_xlm_bidprice_2_unf.split("[")[1])

    #get first bid quantity
    zb_xlm_bidprice_2_quantity_unf = (zb_xlm_bid_str_unf.split(',')[4])
    zb_xlm_bidprice_2_quantity = (zb_xlm_bidprice_2_quantity_unf.split("]")[0])
    zb_xlm_bidprice_2_quantity = zb_xlm_bidprice_2_quantity.strip()

    ########################################################33
    zb_xlm_bidprice_3_unf = (zb_xlm_bid_str_unf.split(",")[5])
    zb_xlm_bidprice_3 = (zb_xlm_bidprice_3_unf.split("[")[1])

    #get first bid quantity
    zb_xlm_bidprice_3_quantity_unf = (zb_xlm_bid_str_unf.split(',')[6])
    zb_xlm_bidprice_3_quantity = (zb_xlm_bidprice_3_quantity_unf.split("]")[0])
    zb_xlm_bidprice_3_quantity = zb_xlm_bidprice_3_quantity.strip()

    zb_ask_bid_data = [datetime.now(), 1, zb_xlm_askprice_1st, zb_xlm_askprice_1st_quantity, zb_xlm_bidprice_1st,zb_xlm_bidprice_1st_quantity], [datetime.now(), 2, zb_xlm_askprice_2nd, zb_xlm_askprice_2nd_quantity, zb_xlm_bidprice_2, zb_xlm_bidprice_2_quantity], \
                               [datetime.now(), 3, zb_xlm_askprice_3rd, zb_xlm_askprice_3rd_quantity, zb_xlm_bidprice_3, zb_xlm_bidprice_3_quantity]



    zb_ask_data = [zb_xlm_askprice_1st, zb_xlm_askprice_1st_quantity, zb_xlm_askprice_2nd, zb_xlm_askprice_2nd_quantity, zb_xlm_askprice_3rd, zb_xlm_askprice_3rd_quantity]

    zb_bid_data = [zb_xlm_bidprice_1st, zb_xlm_bidprice_1st_quantity, zb_xlm_bidprice_2, zb_xlm_bidprice_2_quantity, zb_xlm_bidprice_3, zb_xlm_bidprice_3_quantity]

    add_zb_ask_data = (
        'INSERT INTO `zb_ask_feed` (`id`, `zb_ask1`, `zb_ask_amount1`, `zb_ask2`, `zb_ask_amount2`, `zb_ask3`, `zb_ask_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{})'.format(
            'NULL', zb_xlm_askprice_1st, zb_xlm_askprice_1st_quantity, zb_xlm_askprice_2nd,
            zb_xlm_askprice_2nd_quantity, zb_xlm_askprice_3rd,
            zb_xlm_askprice_3rd_quantity, 'NULL', 'NULL'))
    add_zb_bid_data = (
        'INSERT INTO `zb_bid_feed` (`id`, `zb_bid1`, `zb_bid_amount1`, `zb_bid2`, `zb_bid_amount2`, `zb_bid3`, `zb_bid_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{})'.format(
            'NULL', zb_xlm_bidprice_1st, zb_xlm_bidprice_1st_quantity, zb_xlm_bidprice_2,
            zb_xlm_bidprice_2_quantity, zb_xlm_bidprice_3,
            zb_xlm_bidprice_3_quantity, 'NULL', 'NULL'))

    cursor.execute(add_zb_ask_data)
    cursor.execute(add_zb_bid_data)
    connection.commit()

    connection.close()
    print('raw orderbook')
    print(zb_xlm_orderflow_str_unf1)
    print('compiled data')
    print(zb_ask_bid_data)
    print('ask/bid')
    print(zb_ask_data)
    print(zb_bid_data)
    #print('XXXXXXX')
    #print(zb_ask_bid_data)


    for item in zb_ask_bid_data:

        c.writerow(item)

    csvfile.close()

    zb_ask_feed = open('zb_ask_feed.text', "w")

    zb_ask_feed.write(str(zb_ask_data))

    zb_ask_feed.close()

    zb_bid_feed = open('zb_bid_feed.text', "w")

    zb_bid_feed.write(str(zb_bid_data))

    zb_bid_feed.close()




while True:
    try:
        zb_orderbook_function()


        time.sleep(1)


    except Exception as ex:

        logerros = open('errors.text', "a")

        logerros.write('| zb error:' + str(datetime.now()) + " " + str(ex))

        logerros.close()

        print(ex)


    '''print(zb_xlm_orderflow_str_unf1)
    print('######################################')
    print(zb_xlm_bid_str_unf)
    print('zb ask price:', zb_xlm_askprice_1st)
    print('zb quantity:', zb_xlm_askprice_1st_quantity)
    print('zb ask price:', zb_xlm_askprice_2nd)
    print('zb quantity:', zb_xlm_askprice_2nd_quantity)
    print('zb ask price', zb_xlm_askprice_3rd)
    print('zb quantity:', zb_xlm_askprice_3rd_quantity)'''
    '''print(zb_xlm_bidprice_1st)
    print(zb_xlm_bidprice_1st_quantity)
    print(zb_xlm_bidprice_2)
    print(zb_xlm_bidprice_2_quantity)
    print(zb_xlm_bidprice_3)
    print(zb_xlm_bidprice_3_quantity)'''
