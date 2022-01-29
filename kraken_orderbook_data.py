import json

import csv
from datetime import datetime
import time
import pymysql

import ccxt  # noqa: E402


def get_positive_accounts(balance):
    result = {}
    currencies = list(balance.keys())
    for currency in currencies:
        if balance[currency] and balance[currency] > 0:
            result[currency] = balance[currency]
    return result

#csvfile = open('kraken_orderbook_data.csv', 'a', newline='', encoding='utf-8')

#c = csv.writer(csvfile)
#c.writerow( ['date/time', 'order rank #', 'price (ask)','amount (ask)', 'price (bid)', 'amount (bid)'] )






def kraken_orderbook_function():

    connection = pymysql.connect(host="", user="", passwd="", database="")

    cursor = connection.cursor()
    exchange = ccxt.kraken({
        'apiKey': '',
        'secret': '',
        'enableRateLimit': True,
        'has': {'fetchWithdrawals': True, 'withdraw': True}
    })


    csvfile = open('kraken_orderbook_data.csv', 'a', newline='')  # newline='', encoding='utf-8')
    c = csv.writer(csvfile)

    #get kraken orderflow and format
    kraken_xlm_orderflow_json_unf = exchange.fetch_order_book('XLM/USD')
    kraken_xlm_orderflow_str_unf = json.dumps(kraken_xlm_orderflow_json_unf)

    print(kraken_xlm_orderflow_str_unf)

    #get kraken bid orders
    kraken_xlm_bid_str_unf = (kraken_xlm_orderflow_str_unf.split("asks")[0])

    kraken_xlm_ask_str_unf = (kraken_xlm_orderflow_str_unf.split("asks")[1])
    print(kraken_xlm_ask_str_unf)

    #get first kraken bid order price and amount
    kraken_xlm_bid_1st_unf = (kraken_xlm_bid_str_unf.split(",")[1])
    kraken_xlm_bid_1st = (kraken_xlm_bid_1st_unf.split("[")[2])
    kraken_xlm_bid_amount_1st_unf = (kraken_xlm_bid_str_unf.split(",")[2])
    kraken_xlm_bid_amount_1st = (kraken_xlm_bid_amount_1st_unf.split("]")[0])
    kraken_xlm_bid_amount_1st = kraken_xlm_bid_amount_1st.strip()
    #get second kraken bid order price and amount
    kraken_xlm_bid_2nd_unf = (kraken_xlm_bid_str_unf.split(",")[4])
    kraken_xlm_bid_2nd = (kraken_xlm_bid_2nd_unf.split("[")[1])
    kraken_xlm_bid_amount_2nd_unf = (kraken_xlm_bid_str_unf.split(",")[5])
    kraken_xlm_bid_amount_2nd = (kraken_xlm_bid_amount_2nd_unf.split("]")[0])
    kraken_xlm_bid_amount_2nd  = kraken_xlm_bid_amount_2nd.strip()
    #get third kraken bid order price and amount
    kraken_xlm_bid_3rd_unf = (kraken_xlm_bid_str_unf.split(",")[7])
    kraken_xlm_bid_3rd = (kraken_xlm_bid_3rd_unf.split("[")[1])
    kraken_xlm_bid_amount_3rd_unf = (kraken_xlm_bid_str_unf.split(",")[8])
    kraken_xlm_bid_amount_3rd = (kraken_xlm_bid_amount_3rd_unf.split("]")[0])
    kraken_xlm_bid_amount_3rd = kraken_xlm_bid_amount_3rd.strip()
    ##############################################

    #get first kraken ask order price and amount
    kraken_xlm_ask_1st_unf = (kraken_xlm_ask_str_unf.split(",")[0])
    kraken_xlm_ask_1st = (kraken_xlm_ask_1st_unf.split("[")[2])
    kraken_xlm_ask_amount_1st_unf = (kraken_xlm_ask_str_unf.split(",")[1])
    kraken_xlm_ask_amount_1st = (kraken_xlm_ask_amount_1st_unf.split("]")[0])
    kraken_xlm_ask_amount_1st = kraken_xlm_ask_amount_1st.strip()
    #get second kraken ask order price and amount
    kraken_xlm_ask_2nd_unf = (kraken_xlm_ask_str_unf.split(",")[3])
    kraken_xlm_ask_2nd = (kraken_xlm_ask_2nd_unf.split("[")[1])
    kraken_xlm_ask_amount_2nd_unf = (kraken_xlm_ask_str_unf.split(",")[4])
    kraken_xlm_ask_amount_2nd = (kraken_xlm_ask_amount_2nd_unf.split("]")[0])
    kraken_xlm_ask_amount_2nd = kraken_xlm_ask_amount_2nd.strip()
    #get third kraken ask order price and amount
    kraken_xlm_ask_3rd_unf = (kraken_xlm_ask_str_unf.split(",")[6])
    kraken_xlm_ask_3rd = (kraken_xlm_ask_3rd_unf.split("[")[1])
    kraken_xlm_ask_amount_3rd_unf = (kraken_xlm_ask_str_unf.split(",")[7])
    kraken_xlm_ask_amount_3rd = (kraken_xlm_ask_amount_3rd_unf.split("]")[0])
    kraken_xlm_ask_amount_3rd = kraken_xlm_ask_amount_3rd.strip()
    kraken_ask_bid_data = [datetime.now(), 1, kraken_xlm_ask_1st, kraken_xlm_ask_amount_1st, kraken_xlm_bid_1st, kraken_xlm_bid_amount_1st], [datetime.now(), 2, kraken_xlm_ask_2nd, kraken_xlm_ask_amount_2nd, kraken_xlm_bid_2nd, kraken_xlm_bid_amount_2nd], \
                               [datetime.now(), 3, kraken_xlm_ask_3rd, kraken_xlm_ask_amount_3rd, kraken_xlm_bid_3rd, kraken_xlm_bid_amount_3rd]


    kraken_ask_data = [kraken_xlm_ask_1st, kraken_xlm_ask_amount_1st, kraken_xlm_ask_2nd, kraken_xlm_ask_amount_2nd, kraken_xlm_ask_3rd, kraken_xlm_ask_amount_3rd]

    kraken_bid_data =  [kraken_xlm_bid_1st, kraken_xlm_bid_amount_1st, kraken_xlm_bid_2nd, kraken_xlm_bid_amount_2nd, kraken_xlm_bid_3rd, kraken_xlm_bid_amount_3rd]

    add_kraken_ask_data = ('INSERT INTO `kraken_ask_feed` (`id`, `kraken_ask1`, `kraken_ask_amount1`, `kraken_ask2`, `kraken_ask_amount2`, `kraken_ask3`, `kraken_ask_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{})'.format(
        'NULL', kraken_xlm_ask_1st, kraken_xlm_ask_amount_1st, kraken_xlm_ask_2nd, kraken_xlm_ask_amount_2nd, kraken_xlm_ask_3rd, kraken_xlm_ask_amount_3rd, 'NULL', 'NULL'))
    add_kraken_bid_data = ('INSERT INTO `kraken_bid_feed` (`id`, `kraken_bid1`, `kraken_bid_amount1`, `kraken_bid2`, `kraken_bid_amount2`, `kraken_bid3`, `kraken_bid_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{})'.format(
        'NULL', kraken_xlm_bid_1st, kraken_xlm_bid_amount_1st, kraken_xlm_bid_2nd, kraken_xlm_bid_amount_2nd, kraken_xlm_bid_3rd, kraken_xlm_bid_amount_3rd, 'NULL', 'NULL'))

    cursor.execute(add_kraken_ask_data)
    cursor.execute(add_kraken_bid_data)
    connection.commit()

    connection.close()

    print(kraken_ask_data)
    print(kraken_bid_data)
    for item in kraken_ask_bid_data:
        c.writerow(item)

    csvfile.close()

    time.sleep(1)

    #csvfile.close()

    kraken_ask_feed = open('kraken_ask_feed.text', "w")

    kraken_ask_feed.write(str(kraken_ask_data))

    kraken_ask_feed.close()

    kraken_bid_feed = open('kraken_bid_feed.text', "w")

    kraken_bid_feed.write(str(kraken_bid_data))

    kraken_bid_feed.close()



while True:
    try:
        kraken_orderbook_function()
    except Exception as ex:

        logerros = open('errors.text', "a")

        logerros.write('| kraken error:' + str(datetime.now()) + " " + str(ex))
        logerros.close()

        print(ex)




