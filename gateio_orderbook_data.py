import json

import time
from datetime import datetime
import pymysql
import csv
#root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#sys.path.append(root + '/python')

import ccxt  # noqa: E402


#csvfile = open('gateio_orderbook_data.csv', 'w', newline='', encoding='utf-8')
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
def gateio_orderbook_function():
    connection = pymysql.connect(host="", user="", passwd="", database="")

    cursor = connection.cursor()
    exchange = ccxt.gateio({
        'uid': '',
        'apiKey': '',
        'secret': '',
        'enableRateLimit': True,
        'has': {'fetchWithdrawals': True, 'withdraw': True}
    })

    csvfile = open('gateio_orderbook_data.csv', 'a', newline='') # newline='', encoding='utf-8')
    c = csv.writer(csvfile)

    gateio_xlm_orderflow_json_unf = exchange.fetch_order_book('XLM/USDT')
    gateio_xlm_orderflow_str_unf1 = json.dumps(gateio_xlm_orderflow_json_unf)
    gateio_xlm_ask_str_unf = (gateio_xlm_orderflow_str_unf1.split("asks")[1])
    gateio_xlm_bid_str_unf = (gateio_xlm_orderflow_str_unf1.split("asks")[0])

    #get first ask price order
    gateio_xlm_askprice_1st_unf = (gateio_xlm_ask_str_unf.split(",")[0])
    gateio_xlm_askprice_1st = (gateio_xlm_askprice_1st_unf.split("[")[2])

    #get first ask quantity
    gateio_xlm_askprice_1st_quantity_unf = (gateio_xlm_ask_str_unf.split(',')[1])
    gateio_xlm_askprice_1st_quantity = (gateio_xlm_askprice_1st_quantity_unf.split("]")[0])
    gateio_xlm_askprice_1st_quantity = gateio_xlm_askprice_1st_quantity.strip()
    #first ask order value
    gateio_xlm_ask_value_1st = float(gateio_xlm_askprice_1st)*float(gateio_xlm_askprice_1st_quantity)

    #get second ask order price
    gateio_xlm_askprice_2nd_unf = (gateio_xlm_ask_str_unf.split(",")[2])
    gateio_xlm_askprice_2nd = (gateio_xlm_askprice_2nd_unf.split("[")[1])

    #get second ask order quantity
    gateio_xlm_askprice_2nd_quantity_unf = (gateio_xlm_ask_str_unf.split(',')[3])
    gateio_xlm_askprice_2nd_quantity = (gateio_xlm_askprice_2nd_quantity_unf.split("]")[0])
    gateio_xlm_askprice_2nd_quantity = gateio_xlm_askprice_2nd_quantity.strip()
    #get second order value
    gateio_xlm_ask_value_2nd = float(gateio_xlm_askprice_2nd)*float(gateio_xlm_askprice_2nd_quantity)

    #get third order ask price
    gateio_xlm_askprice_3rd_unf = (gateio_xlm_ask_str_unf.split(",")[4])
    gateio_xlm_askprice_3rd = (gateio_xlm_askprice_3rd_unf.split("[")[1])

    #get third ask quanitity
    gateio_xlm_askprice_3rd_quantity_unf = (gateio_xlm_ask_str_unf.split(',')[5])
    gateio_xlm_askprice_3rd_quantity = (gateio_xlm_askprice_3rd_quantity_unf.split("]")[0])
    gateio_xlm_askprice_3rd_quantity = gateio_xlm_askprice_3rd_quantity.strip()
    #get third ask order amount
    gateio_xlm_ask_value_3rd = float(gateio_xlm_askprice_3rd_quantity)*float(gateio_xlm_askprice_3rd)

    ###########################################################################

    #get first bid price order
    gateio_xlm_bidprice_1st_unf = (gateio_xlm_bid_str_unf.split(",")[1])
    gateio_xlm_bidprice_1st = (gateio_xlm_bidprice_1st_unf.split("[")[2])

    #get first bid quantity
    gateio_xlm_bidprice_1st_quantity_unf = (gateio_xlm_bid_str_unf.split(',')[2])
    gateio_xlm_bidprice_1st_quantity = (gateio_xlm_bidprice_1st_quantity_unf.split("]")[0])
    gateio_xlm_bidprice_1st_quantity = gateio_xlm_bidprice_1st_quantity.strip()

    ########################################################33
    gateio_xlm_bidprice_2_unf = (gateio_xlm_bid_str_unf.split(",")[3])
    gateio_xlm_bidprice_2 = (gateio_xlm_bidprice_2_unf.split("[")[1])

    #get first bid quantity
    gateio_xlm_bidprice_2_quantity_unf = (gateio_xlm_bid_str_unf.split(',')[4])
    gateio_xlm_bidprice_2_quantity = (gateio_xlm_bidprice_2_quantity_unf.split("]")[0])
    gateio_xlm_bidprice_2_quantity = gateio_xlm_bidprice_2_quantity.strip()

    ########################################################33
    gateio_xlm_bidprice_3_unf = (gateio_xlm_bid_str_unf.split(",")[5])
    gateio_xlm_bidprice_3 = (gateio_xlm_bidprice_3_unf.split("[")[1])

    #get first bid quantity
    gateio_xlm_bidprice_3_quantity_unf = (gateio_xlm_bid_str_unf.split(',')[6])
    gateio_xlm_bidprice_3_quantity = (gateio_xlm_bidprice_3_quantity_unf.split("]")[0])
    gateio_xlm_bidprice_3_quantity = gateio_xlm_bidprice_3_quantity.strip()

    gateio_ask_bid_data = [datetime.now(), 1, gateio_xlm_askprice_1st, gateio_xlm_askprice_1st_quantity, gateio_xlm_bidprice_1st,gateio_xlm_bidprice_1st_quantity], [datetime.now(), 2, gateio_xlm_askprice_2nd, gateio_xlm_askprice_2nd_quantity, gateio_xlm_bidprice_2, gateio_xlm_bidprice_2_quantity], \
                               [datetime.now(), 3, gateio_xlm_askprice_3rd, gateio_xlm_askprice_3rd_quantity, gateio_xlm_bidprice_3, gateio_xlm_bidprice_3_quantity]



    gateio_ask_data = [gateio_xlm_askprice_1st, gateio_xlm_askprice_1st_quantity, gateio_xlm_askprice_2nd, gateio_xlm_askprice_2nd_quantity, gateio_xlm_askprice_3rd, gateio_xlm_askprice_3rd_quantity]

    gateio_bid_data = [gateio_xlm_bidprice_1st, gateio_xlm_bidprice_1st_quantity, gateio_xlm_bidprice_2, gateio_xlm_bidprice_2_quantity, gateio_xlm_bidprice_3, gateio_xlm_bidprice_3_quantity]
    #print('raw orderbook')
    #print(gateio_xlm_orderflow_str_unf1)
    #print('compiled data')
    #print(gateio_ask_bid_data)
    #print('ask/bid')
    add_gateio_ask_data = (
        "INSERT INTO `gateio_ask_feed` (`id`, `gateio_ask1`, `gateio_ask_amount1`, `gateio_ask2`, `gateio_ask_amount2`, `gateio_ask3`, `gateio_ask_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{});".format(
            'NULL', gateio_xlm_askprice_1st, gateio_xlm_askprice_1st_quantity, gateio_xlm_askprice_2nd,
            gateio_xlm_askprice_2nd_quantity, gateio_xlm_askprice_3rd,
            gateio_xlm_askprice_3rd_quantity, 'NULL', 'NULL'))
    add_gateio_bid_data = (
        "INSERT INTO `gateio_bid_feed` (`id`, `gateio_bid1`, `gateio_bid_amount1`, `gateio_bid2`, `gateio_bid_amount2`, `gateio_bid3`, `gateio_bid_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{});".format(
            'NULL', gateio_xlm_bidprice_1st, gateio_xlm_bidprice_1st_quantity, gateio_xlm_bidprice_2,
            gateio_xlm_bidprice_2_quantity, gateio_xlm_bidprice_3,
            gateio_xlm_bidprice_3_quantity, 'NULL', 'NULL'))
    new_order = ("INSERT INTO `gateio_ask_feed` (`id`, `gateio_ask1`, `gateio_ask_amount1`, `gateio_ask2`, `gateio_ask_amount2`, `gateio_ask13`, `gateio_ask_amount3`, `created_at`, `updated_at`) VALUES (NULL, NULL, NULL, NULL, NULL, NULL, NULL, current_timestamp(), NULL);".format('NULL', '1', '1', '1', '1', '1', '1', 'NULL', 'NULL'))
    cursor.execute(add_gateio_ask_data)
    cursor.execute(add_gateio_bid_data)
    connection.commit()

    connection.close()
    print(gateio_ask_data)
    print(gateio_bid_data)
    #print('XXXXXXX')
    #print(gateio_ask_bid_data)


    for item in gateio_ask_bid_data:

        c.writerow(item)

    csvfile.close()

    gateio_ask_feed = open('gateio_ask_feed.text', "w")

    gateio_ask_feed.write(str(gateio_ask_data))

    gateio_ask_feed.close()

    gateio_bid_feed = open('gateio_bid_feed.text', "w")

    gateio_bid_feed.write(str(gateio_bid_data))

    gateio_bid_feed.close()





while True:
    try:
        gateio_orderbook_function()


        time.sleep(1)

    except Exception as ex:

        logerros = open('errors.text', "a")

        logerros.write('| gateio error:' + str(datetime.now()) + " " + str(ex))
        logerros.close()

        print(ex)


    '''print(gateio_xlm_orderflow_str_unf1)
    print('######################################')
    print(gateio_xlm_bid_str_unf)
    print('gateio ask price:', gateio_xlm_askprice_1st)
    print('gateio quantity:', gateio_xlm_askprice_1st_quantity)
    print('gateio ask price:', gateio_xlm_askprice_2nd)
    print('gateio quantity:', gateio_xlm_askprice_2nd_quantity)
    print('gateio ask price', gateio_xlm_askprice_3rd)
    print('gateio quantity:', gateio_xlm_askprice_3rd_quantity)'''
    '''print(gateio_xlm_bidprice_1st)
    print(gateio_xlm_bidprice_1st_quantity)
    print(gateio_xlm_bidprice_2)
    print(gateio_xlm_bidprice_2_quantity)
    print(gateio_xlm_bidprice_3)
    print(gateio_xlm_bidprice_3_quantity)'''
