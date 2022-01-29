import json
import time
from datetime import datetime
import csv
#root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#sys.path.append(root + '/python')

import ccxt  # noqa: E402


#csvfile = open('cex_orderbook_data.csv', 'w', newline='', encoding='utf-8')
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
def cex_orderbook_function():
    exchange = ccxt.cex({
        'uid': '',
        'apiKey': '',
        'secret': '',
        'enableRateLimit': True,
        'has': {'fetchWithdrawals': True, 'withdraw': True}
    })

    csvfile = open('cex_orderbook_data.csv', 'a', newline='') # newline='', encoding='utf-8')
    c = csv.writer(csvfile)

    cex_xlm_orderflow_json_unf = exchange.fetch_order_book('XLM/USD')
    cex_xlm_orderflow_str_unf1 = json.dumps(cex_xlm_orderflow_json_unf)
    cex_xlm_ask_str_unf = (cex_xlm_orderflow_str_unf1.split("asks")[1])
    cex_xlm_bid_str_unf = (cex_xlm_orderflow_str_unf1.split("asks")[0])

    #get first ask price order
    cex_xlm_askprice_1st_unf = (cex_xlm_ask_str_unf.split(",")[0])
    cex_xlm_askprice_1st = (cex_xlm_askprice_1st_unf.split("[")[2])

    #get first ask quantity
    cex_xlm_askprice_1st_quantity_unf = (cex_xlm_ask_str_unf.split(',')[1])
    cex_xlm_askprice_1st_quantity = (cex_xlm_askprice_1st_quantity_unf.split("]")[0])
    cex_xlm_askprice_1st_quantity = cex_xlm_askprice_1st_quantity.strip()
    #first ask order value
    cex_xlm_ask_value_1st = float(cex_xlm_askprice_1st)*float(cex_xlm_askprice_1st_quantity)

    #get second ask order price
    cex_xlm_askprice_2nd_unf = (cex_xlm_ask_str_unf.split(",")[2])
    cex_xlm_askprice_2nd = (cex_xlm_askprice_2nd_unf.split("[")[1])

    #get second ask order quantity
    cex_xlm_askprice_2nd_quantity_unf = (cex_xlm_ask_str_unf.split(',')[3])
    cex_xlm_askprice_2nd_quantity = (cex_xlm_askprice_2nd_quantity_unf.split("]")[0])
    cex_xlm_askprice_2nd_quantity = cex_xlm_askprice_2nd_quantity.strip()
    #get second order value
    cex_xlm_ask_value_2nd = float(cex_xlm_askprice_2nd)*float(cex_xlm_askprice_2nd_quantity)

    #get third order ask price
    cex_xlm_askprice_3rd_unf = (cex_xlm_ask_str_unf.split(",")[4])
    cex_xlm_askprice_3rd = (cex_xlm_askprice_3rd_unf.split("[")[1])

    #get third ask quanitity
    cex_xlm_askprice_3rd_quantity_unf = (cex_xlm_ask_str_unf.split(',')[5])
    cex_xlm_askprice_3rd_quantity = (cex_xlm_askprice_3rd_quantity_unf.split("]")[0])
    cex_xlm_askprice_3rd_quantity = cex_xlm_askprice_3rd_quantity.strip()
    #get third ask order amount
    cex_xlm_ask_value_3rd = float(cex_xlm_askprice_3rd_quantity)*float(cex_xlm_askprice_3rd)

    ###########################################################################

    #get first bid price order
    cex_xlm_bidprice_1st_unf = (cex_xlm_bid_str_unf.split(",")[1])
    cex_xlm_bidprice_1st = (cex_xlm_bidprice_1st_unf.split("[")[2])

    #get first bid quantity
    cex_xlm_bidprice_1st_quantity_unf = (cex_xlm_bid_str_unf.split(',')[2])
    cex_xlm_bidprice_1st_quantity = (cex_xlm_bidprice_1st_quantity_unf.split("]")[0])
    cex_xlm_bidprice_1st_quantity = cex_xlm_bidprice_1st_quantity.strip()

    ########################################################33
    cex_xlm_bidprice_2_unf = (cex_xlm_bid_str_unf.split(",")[3])
    cex_xlm_bidprice_2 = (cex_xlm_bidprice_2_unf.split("[")[1])

    #get first bid quantity
    cex_xlm_bidprice_2_quantity_unf = (cex_xlm_bid_str_unf.split(',')[4])
    cex_xlm_bidprice_2_quantity = (cex_xlm_bidprice_2_quantity_unf.split("]")[0])
    cex_xlm_bidprice_2_quantity = cex_xlm_bidprice_2_quantity.strip()

    ########################################################33
    cex_xlm_bidprice_3_unf = (cex_xlm_bid_str_unf.split(",")[5])
    cex_xlm_bidprice_3 = (cex_xlm_bidprice_3_unf.split("[")[1])

    #get first bid quantity
    cex_xlm_bidprice_3_quantity_unf = (cex_xlm_bid_str_unf.split(',')[6])
    cex_xlm_bidprice_3_quantity = (cex_xlm_bidprice_3_quantity_unf.split("]")[0])
    cex_xlm_bidprice_3_quantity = cex_xlm_bidprice_3_quantity.strip()

    cex_ask_bid_data = [datetime.now(), 1, cex_xlm_askprice_1st, cex_xlm_askprice_1st_quantity, cex_xlm_bidprice_1st,cex_xlm_bidprice_1st_quantity], [datetime.now(), 2, cex_xlm_askprice_2nd, cex_xlm_askprice_2nd_quantity, cex_xlm_bidprice_2, cex_xlm_bidprice_2_quantity], \
                               [datetime.now(), 3, cex_xlm_askprice_3rd, cex_xlm_askprice_3rd_quantity, cex_xlm_bidprice_3, cex_xlm_bidprice_3_quantity]



    cex_ask_data = [cex_xlm_askprice_1st, cex_xlm_askprice_1st_quantity, cex_xlm_askprice_2nd, cex_xlm_askprice_2nd_quantity, cex_xlm_askprice_3rd, cex_xlm_askprice_3rd_quantity]

    cex_bid_data = [cex_xlm_bidprice_1st, cex_xlm_bidprice_1st_quantity, cex_xlm_bidprice_2, cex_xlm_bidprice_2_quantity, cex_xlm_bidprice_3, cex_xlm_bidprice_3_quantity]

    print(cex_ask_data)
    print(cex_bid_data)
    #print('XXXXXXX')
    #print(cex_ask_bid_data)


    for item in cex_ask_bid_data:

        c.writerow(item)

    csvfile.close()

    csvfile.close()

    cex_ask_feed = open('cex_ask_feed.text', "w")

    cex_ask_feed.write(str(cex_ask_data))

    cex_ask_feed.close()

    cex_bid_feed = open('cex_bid_feed.text', "w")

    cex_bid_feed.write(str(cex_bid_data))

    cex_bid_feed.close()




while True:
    try:
        cex_orderbook_function()




        time.sleep(1)


    except Exception as ex:

        logerros = open('errors.text', "a")

        logerros.write('| cex error:' + str(datetime.now()) + " " + str(ex))
        logerros.close()

        print(ex)


    '''print(cex_xlm_orderflow_str_unf1)
    print('######################################')
    print(cex_xlm_bid_str_unf)
    print('CEX ask price:', cex_xlm_askprice_1st)
    print('CEX quantity:', cex_xlm_askprice_1st_quantity)
    print('CEX ask price:', cex_xlm_askprice_2nd)
    print('CEX quantity:', cex_xlm_askprice_2nd_quantity)
    print('CEX ask price', cex_xlm_askprice_3rd)
    print('CEX quantity:', cex_xlm_askprice_3rd_quantity)'''
    '''print(cex_xlm_bidprice_1st)
    print(cex_xlm_bidprice_1st_quantity)
    print(cex_xlm_bidprice_2)
    print(cex_xlm_bidprice_2_quantity)
    print(cex_xlm_bidprice_3)
    print(cex_xlm_bidprice_3_quantity)'''
