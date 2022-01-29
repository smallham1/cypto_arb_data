import json


import time
from datetime import datetime
import pymysql
import csv
#root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#sys.path.append(root + '/python')

import ccxt  # noqa: E402


#csvfile = open('mexc_orderbook_data.csv', 'w', newline='', encoding='utf-8')
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
def mexc_orderbook_function():
    #connection = pymysql.connect(host="localhost", user="adminer", passwd="Crypto#123", database="radmin")

    #cursor = connection.cursor()
    exchange = ccxt.mexc({
        'uid': '',
        'apiKey': '',
        'secret': '',
        'enableRateLimit': True,
        'has': {'fetchWithdrawals': True, 'withdraw': True}
    })

    csvfile = open('mexc_orderbook_data.csv', 'a', newline='') # newline='', encoding='utf-8')
    c = csv.writer(csvfile)



    mexc_xlm_orderflow_json_unf = exchange.fetch_order_book('XLM/USDT')
    mexc_xlm_orderflow_str_unf1 = json.dumps(mexc_xlm_orderflow_json_unf)
    mexc_xlm_ask_str_unf = (mexc_xlm_orderflow_str_unf1.split("asks")[1])
    mexc_xlm_bid_str_unf = (mexc_xlm_orderflow_str_unf1.split("asks")[0])

    #get first ask price order
    mexc_xlm_askprice_1st_unf = (mexc_xlm_ask_str_unf.split(",")[0])
    mexc_xlm_askprice_1st = (mexc_xlm_askprice_1st_unf.split("[")[2])

    #get first ask quantity
    mexc_xlm_askprice_1st_quantity_unf = (mexc_xlm_ask_str_unf.split(',')[1])
    mexc_xlm_askprice_1st_quantity = (mexc_xlm_askprice_1st_quantity_unf.split("]")[0])
    mexc_xlm_askprice_1st_quantity = mexc_xlm_askprice_1st_quantity.strip()

    #first ask order value
    mexc_xlm_ask_value_1st = float(mexc_xlm_askprice_1st)*float(mexc_xlm_askprice_1st_quantity)

    #get second ask order price
    mexc_xlm_askprice_2nd_unf = (mexc_xlm_ask_str_unf.split(",")[2])
    mexc_xlm_askprice_2nd = (mexc_xlm_askprice_2nd_unf.split("[")[1])

    #get second ask order quantity
    mexc_xlm_askprice_2nd_quantity_unf = (mexc_xlm_ask_str_unf.split(',')[3])
    mexc_xlm_askprice_2nd_quantity = (mexc_xlm_askprice_2nd_quantity_unf.split("]")[0])

    mexc_xlm_askprice_2nd_quantity = mexc_xlm_askprice_2nd_quantity.strip()
    #get second order value
    mexc_xlm_ask_value_2nd = float(mexc_xlm_askprice_2nd)*float(mexc_xlm_askprice_2nd_quantity)

    #get third order ask price
    mexc_xlm_askprice_3rd_unf = (mexc_xlm_ask_str_unf.split(",")[4])
    mexc_xlm_askprice_3rd = (mexc_xlm_askprice_3rd_unf.split("[")[1])

    #get third ask quanitity
    mexc_xlm_askprice_3rd_quantity_unf = (mexc_xlm_ask_str_unf.split(',')[5])
    mexc_xlm_askprice_3rd_quantity = (mexc_xlm_askprice_3rd_quantity_unf.split("]")[0])

    mexc_xlm_askprice_3rd_quantity = mexc_xlm_askprice_3rd_quantity.strip()

    #get third ask order amount
    mexc_xlm_ask_value_3rd = float(mexc_xlm_askprice_3rd_quantity)*float(mexc_xlm_askprice_3rd)

    ###########################################################################

    #get first bid price order
    mexc_xlm_bidprice_1st_unf = (mexc_xlm_bid_str_unf.split(",")[1])
    mexc_xlm_bidprice_1st = (mexc_xlm_bidprice_1st_unf.split("[")[2])

    #get first bid quantity
    mexc_xlm_bidprice_1st_quantity_unf = (mexc_xlm_bid_str_unf.split(',')[2])
    mexc_xlm_bidprice_1st_quantity = (mexc_xlm_bidprice_1st_quantity_unf.split("]")[0])

    mexc_xlm_bidprice_1st_quantity = mexc_xlm_bidprice_1st_quantity.strip()

    ########################################################33
    mexc_xlm_bidprice_2_unf = (mexc_xlm_bid_str_unf.split(",")[3])
    mexc_xlm_bidprice_2 = (mexc_xlm_bidprice_2_unf.split("[")[1])

    #get first bid quantity
    mexc_xlm_bidprice_2_quantity_unf = (mexc_xlm_bid_str_unf.split(',')[4])
    mexc_xlm_bidprice_2_quantity = (mexc_xlm_bidprice_2_quantity_unf.split("]")[0])

    mexc_xlm_bidprice_2_quantity = mexc_xlm_bidprice_2_quantity.strip()
    ########################################################33
    mexc_xlm_bidprice_3_unf = (mexc_xlm_bid_str_unf.split(",")[5])
    mexc_xlm_bidprice_3 = (mexc_xlm_bidprice_3_unf.split("[")[1])

    #get first bid quantity
    mexc_xlm_bidprice_3_quantity_unf = (mexc_xlm_bid_str_unf.split(',')[6])
    mexc_xlm_bidprice_3_quantity = (mexc_xlm_bidprice_3_quantity_unf.split("]")[0])

    mexc_xlm_bidprice_3_quantity = mexc_xlm_bidprice_3_quantity .strip()

    mexc_ask_bid_data = [datetime.now(), 1, mexc_xlm_askprice_1st, mexc_xlm_askprice_1st_quantity, mexc_xlm_bidprice_1st, mexc_xlm_bidprice_1st_quantity], [datetime.now(), 2, mexc_xlm_askprice_2nd, mexc_xlm_askprice_2nd_quantity, mexc_xlm_bidprice_2, mexc_xlm_bidprice_2_quantity], \
                               [datetime.now(), 3, mexc_xlm_askprice_3rd, mexc_xlm_askprice_3rd_quantity, mexc_xlm_bidprice_3, mexc_xlm_bidprice_3_quantity]



    mexc_ask_data = [mexc_xlm_askprice_1st, mexc_xlm_askprice_1st_quantity, mexc_xlm_askprice_2nd, mexc_xlm_askprice_2nd_quantity, mexc_xlm_askprice_3rd, mexc_xlm_askprice_3rd_quantity]

    mexc_bid_data = [mexc_xlm_bidprice_1st, mexc_xlm_bidprice_1st_quantity, mexc_xlm_bidprice_2, mexc_xlm_bidprice_2_quantity, mexc_xlm_bidprice_3, mexc_xlm_bidprice_3_quantity]
    #print('raw orderbook')
    #print(mexc_xlm_orderflow_str_unf1)
    #print('compiled data')
    #print(mexc_ask_bid_data)
    #print('ask/bid')

    add_mexc_ask_data = (
        "INSERT INTO `mexc_ask_feed` (`id`, `mexc_ask1`, `mexc_ask_amount1`, `mexc_ask2`, `mexc_ask_amount2`, `mexc_ask3`, `mexc_ask_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{});".format(
            'NULL', mexc_xlm_askprice_1st, mexc_xlm_askprice_1st_quantity, mexc_xlm_askprice_2nd, mexc_xlm_askprice_2nd_quantity, mexc_xlm_askprice_3rd,
            mexc_xlm_askprice_3rd_quantity, 'current_timestamp()', 'NULL'))
    add_mexc_bid_data = (
        "INSERT INTO `mexc_bid_feed` (`id`, `mexc_bid1`, `mexc_bid_amount1`, `mexc_bid2`, `mexc_bid_amount2`, `mexc_bid3`, `mexc_bid_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{});".format(
            'NULL', mexc_xlm_bidprice_1st, mexc_xlm_bidprice_1st_quantity, mexc_xlm_bidprice_2, mexc_xlm_bidprice_2_quantity, mexc_xlm_bidprice_3,
            mexc_xlm_bidprice_3_quantity, 'current_timestamp()	', 'NULL'))
    #new_order = ("INSERT INTO `mexc_bid_feed` (`id`, `mexc_bid1`, `mexc_bid_amount1`, `mexc_bid2`, `mexc_bid_amount2`, `mexc_bid3`, `mexc_bid_amount3`, `created_at`, `updated_at`) VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, current_timestamp(), NULL);".format('NULL', mexc_xlm_bidprice_1st, mexc_xlm_bidprice_1st_quantity, mexc_xlm_bidprice_2, mexc_xlm_bidprice_2_quantity, mexc_xlm_bidprice_3, 'NULL', 'NULL'))

    #cursor.execute(add_mexc_ask_data)
    #cursor.execute(add_mexc_bid_data)
    #connection.commit()

    #connection.close()
    print(mexc_ask_data)
    print(mexc_bid_data)
    #print('XXXXXXX')
    #print(mexc_ask_bid_data)


    for item in mexc_ask_bid_data:

        c.writerow(item)

    csvfile.close()

    mexc_ask_feed = open('mexc_ask_feed.text', "w")

    mexc_ask_feed.write(str(mexc_ask_data))

    mexc_ask_feed.close()

    mexc_bid_feed = open('mexc_bid_feed.text', "w")

    mexc_bid_feed.write(str(mexc_bid_data))

    mexc_bid_feed.close()



while True:
    try:
        mexc_orderbook_function()

        #mexc_price_feed = open('mexc_price_feed.text', "w")

        #mexc_price_feed.write(str(mexc_ask_data) + str(mexc_bid_data))

        #mexc_price_feed.close()


        time.sleep(1)


    except Exception as ex:

        logerros = open('errors.text', "a")

        logerros.write('| mexc error:' + str(datetime.now()) + " " + str(ex))

        logerros.close()

        print(ex)


    '''print(mexc_xlm_orderflow_str_unf1)
    print('######################################')
    print(mexc_xlm_bid_str_unf)
    print('mexc ask price:', mexc_xlm_askprice_1st)
    print('mexc quantity:', mexc_xlm_askprice_1st_quantity)
    print('mexc ask price:', mexc_xlm_askprice_2nd)
    print('mexc quantity:', mexc_xlm_askprice_2nd_quantity)
    print('mexc ask price', mexc_xlm_askprice_3rd)
    print('mexc quantity:', mexc_xlm_askprice_3rd_quantity)'''
    '''print(mexc_xlm_bidprice_1st)
    print(mexc_xlm_bidprice_1st_quantity)
    print(mexc_xlm_bidprice_2)
    print(mexc_xlm_bidprice_2_quantity)
    print(mexc_xlm_bidprice_3)
    print(mexc_xlm_bidprice_3_quantity)'''

