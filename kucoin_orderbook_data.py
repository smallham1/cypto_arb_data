import json

import time

import ccxt  # noqa: E402
from datetime import datetime
import csv
import pymysql
'''csvfile = open('kucoin_orderbook_data.csv', 'w', newline='', encoding='utf-8')
c = csv.writer(csvfile)
c.writerow( ['date/time', 'order rank #', 'price (ask)','amount (ask)', 'price (bid)', 'amount (bid)'] )'''



def kucoin_orderbook_function():
    connection = pymysql.connect(host="", user="", passwd="", database="")

    cursor = connection.cursor()

    exchange1 = ccxt.kucoin({
        'apiKey': '',
        'secret': '',
        "password": '',
        'enableRateLimit': True,
        'has': {'fetchWithdrawals': True, 'withdraw': True}
    })

    csvfile = open('kucoin_orderbook_data.csv', 'a', newline='')
    c = csv.writer(csvfile)

    time.sleep(0.5)
    kucoin_xlm_orderflow_json_unf = exchange1.fetch_order_book('XLM/USDT')
    kucoin_xlm_orderflow_str_unf = json.dumps(kucoin_xlm_orderflow_json_unf)

    #print(kucoin_xlm_orderflow_str_unf)

    kucoin_xlm_bid_str_unf = (kucoin_xlm_orderflow_str_unf.split("asks")[0])

    #get first kucoin bid order price and amount
    kucoin_xlm_bid_1st_unf = (kucoin_xlm_bid_str_unf.split(",")[1])
    kucoin_xlm_bid_1st = (kucoin_xlm_bid_1st_unf.split("[")[2])
    kucoin_xlm_bid_amount_1st_unf = (kucoin_xlm_bid_str_unf.split(",")[2])
    kucoin_xlm_bid_amount_1st = (kucoin_xlm_bid_amount_1st_unf.split("]")[0])
    kucoin_xlm_bid_amount_1st = kucoin_xlm_bid_amount_1st.strip()
    #get second kucoin bid order price and amount
    kucoin_xlm_bid_2nd_unf = (kucoin_xlm_bid_str_unf.split(",")[3])
    kucoin_xlm_bid_2nd = (kucoin_xlm_bid_2nd_unf.split("[")[1])
    kucoin_xlm_bid_amount_2nd_unf = (kucoin_xlm_bid_str_unf.split(",")[4])
    kucoin_xlm_bid_amount_2nd = (kucoin_xlm_bid_amount_2nd_unf.split("]")[0])
    kucoin_xlm_bid_amount_2nd = kucoin_xlm_bid_amount_2nd.strip()
    #get third kucoin bid order price and amount
    kucoin_xlm_bid_3rd_unf = (kucoin_xlm_bid_str_unf.split(",")[5])
    kucoin_xlm_bid_3rd = (kucoin_xlm_bid_3rd_unf.split("[")[1])
    kucoin_xlm_bid_amount_3rd_unf = (kucoin_xlm_bid_str_unf.split(",")[6])
    kucoin_xlm_bid_amount_3rd = (kucoin_xlm_bid_amount_3rd_unf.split("]")[0])
    kucoin_xlm_bid_amount_3rd = kucoin_xlm_bid_amount_3rd.strip()

    kucoin_xlm_ask_str_unf = (kucoin_xlm_orderflow_str_unf.split("asks")[1])

    #get first kucoin bid order price and amount
    kucoin_xlm_ask_1st_unf = (kucoin_xlm_ask_str_unf.split(",")[0])
    kucoin_xlm_ask_1st = (kucoin_xlm_ask_1st_unf.split("[")[2])
    kucoin_xlm_ask_amount_1st_unf = (kucoin_xlm_ask_str_unf.split(",")[1])
    kucoin_xlm_ask_amount_1st = (kucoin_xlm_ask_amount_1st_unf.split("]")[0])
    kucoin_xlm_ask_amount_1st = kucoin_xlm_ask_amount_1st.strip()
    #get second kucoin bid order price and amount
    kucoin_xlm_ask_2nd_unf = (kucoin_xlm_ask_str_unf.split(",")[2])
    kucoin_xlm_ask_2nd = (kucoin_xlm_ask_2nd_unf.split("[")[1])
    kucoin_xlm_ask_amount_2nd_unf = (kucoin_xlm_ask_str_unf.split(",")[3])
    kucoin_xlm_ask_amount_2nd = (kucoin_xlm_ask_amount_2nd_unf.split("]")[0])
    kucoin_xlm_ask_amount_2nd = kucoin_xlm_ask_amount_2nd.strip()

    #get third kucoin bid order price and amount
    kucoin_xlm_ask_3rd_unf = (kucoin_xlm_ask_str_unf.split(",")[4])
    kucoin_xlm_ask_3rd = (kucoin_xlm_ask_3rd_unf.split("[")[1])
    kucoin_xlm_ask_amount_3rd_unf = (kucoin_xlm_ask_str_unf.split(",")[5])
    kucoin_xlm_ask_amount_3rd = (kucoin_xlm_ask_amount_3rd_unf.split("]")[0])
    kucoin_xlm_ask_amount_3rd = kucoin_xlm_ask_amount_3rd.strip()


    kucoin_ask_bid_data = [datetime.now(), 1, kucoin_xlm_ask_1st, kucoin_xlm_ask_amount_1st, kucoin_xlm_bid_1st, kucoin_xlm_bid_amount_1st], [datetime.now(), 2, kucoin_xlm_ask_2nd, kucoin_xlm_ask_amount_2nd, kucoin_xlm_bid_2nd, kucoin_xlm_bid_amount_2nd], \
                               [datetime.now(), 3, kucoin_xlm_ask_3rd, kucoin_xlm_ask_amount_3rd, kucoin_xlm_bid_3rd, kucoin_xlm_bid_amount_3rd]
    #print(kucoin_ask_bid_data)
    kucoin_ask_data = [kucoin_xlm_ask_1st, kucoin_xlm_ask_amount_1st, kucoin_xlm_ask_2nd, kucoin_xlm_ask_amount_2nd,
                       kucoin_xlm_ask_3rd, kucoin_xlm_ask_amount_3rd]
    kucoin_bid_data = [kucoin_xlm_bid_1st, kucoin_xlm_bid_amount_1st, kucoin_xlm_bid_2nd, kucoin_xlm_bid_amount_2nd,
                       kucoin_xlm_bid_3rd, kucoin_xlm_bid_amount_3rd]

    add_kucoin_ask_data = (
        'INSERT INTO `kucoin_ask_feed` (`id`, `kucoin_ask1`, `kucoin_ask_amount1`, `kucoin_ask2`, `kucoin_ask_amount2`, `kucoin_ask3`, `kucoin_ask_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{})'.format(
            'NULL', kucoin_xlm_ask_1st, kucoin_xlm_ask_amount_1st, kucoin_xlm_ask_2nd,
            kucoin_xlm_ask_amount_2nd, kucoin_xlm_ask_3rd,
            kucoin_xlm_ask_amount_3rd, 'NULL', 'NULL'))
    add_kucoin_bid_data = (
        'INSERT INTO `kucoin_bid_feed` (`id`, `kucoin_bid1`, `kucoin_bid_amount1`, `kucoin_bid2`, `kucoin_bid_amount2`, `kucoin_bid3`, `kucoin_bid_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{})'.format(
            'NULL', kucoin_xlm_bid_1st, kucoin_xlm_bid_amount_1st, kucoin_xlm_bid_2nd,
            kucoin_xlm_bid_amount_2nd, kucoin_xlm_bid_3rd,
            kucoin_xlm_bid_amount_3rd, 'NULL', 'NULL'))

    cursor.execute(add_kucoin_ask_data)
    cursor.execute(add_kucoin_bid_data)
    connection.commit()

    connection.close()

    print(kucoin_ask_data)
    print(kucoin_bid_data)



    for item in kucoin_ask_bid_data:

        c.writerow(item)

    csvfile.close()


    kucoin_ask_feed = open('kucoin_ask_feed.text', "w")

    kucoin_ask_feed.write(str(kucoin_ask_data))

    kucoin_ask_feed.close()

    kucoin_bid_feed = open('kucoin_bid_feed.text', "w")

    kucoin_bid_feed.write(str(kucoin_bid_data))

    kucoin_bid_feed.close()









while True:
    try:
        kucoin_orderbook_function()
        time.sleep(1)

    except Exception as ex:

        logerros = open('errors.text', "a")

        logerros.write('| kucoin error:' + str(datetime.now()) + " " + str(ex))
        logerros.close()

        print(ex)
