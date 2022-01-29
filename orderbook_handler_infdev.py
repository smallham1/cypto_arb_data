import time
import numpy as np
from datetime import datetime
import csv
import requests

np.set_printoptions(suppress=True)
np.set_printoptions(sign=' ')
np.set_printoptions(formatter={'float': '{: 0.6f}'.format})

url = "http://72.76.64.74/api/v1/order/create"

payload = {'email': 'admin@test.com',
           'password': '1234'}
files = [

]
headers = {
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI1IiwianRpIjoiODM0ZTgwNDJmYzc5ZmI5MWRkNWM5MTk5NTMyMTg3MThmNmU3NDYxYTMyN2U2ZGMwMTlhNDViOWVjNzJmMmE1MDMyYTAyNGUzZjM3MGI2OGIiLCJpYXQiOjE2Mzc0NjkyMTUsIm5iZiI6MTYzNzQ2OTIxNSwiZXhwIjoxNjY5MDA1MjE1LCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.NMsDlzkohrrRJpe1qzJlPbmo1PNmw1mRbwZnFE2bbFzOQyugmbGdef_U9CPqzdEWbu65TUUXZLP6qWpqUNQcK3misoEJNbD4FHdT-_unf1yKMfbOkVRPVILdZHfdGtSVFt2tifJnEHMCC25CvbIGQzyKbVKhcGEdkX6hfvkm_gNK03uKcEFKYs40k4hYLZpSwwKGEyD-Q_hOWpQOFjZTOeCkXf6-Il-6xe-_tWyK2OD3n7JJCb8hcKC0MNZkNHeqKWq2wRuwpKHRqrZw6VrQfddE5q7IPzB9fLqw-0Bn44Mp7lUBaAZY58hrjmhBXnHqYx0EXsG66chIcAyse03VpJDA8z5OIS27AYVRIG4iAZNr16zIdVz36T_hwkd_1TVF7jEp8r6o-b1iJNWB4qGstxnqdco7TA1H-vCFo_m-X7tW4BvNPYK1MqIom8vFT4zeKx0nsngAri5I6WD5XWVKUDvrWkdF0bMI2dspLRHY8mN4xoLqy6el9OSgPOtfDUbSpnA_MZjorv0NEG1nAqEJZ7GAW5i2Tz5fGO2aCtirJztni7JbF9AJAHbfdnH0rCss86VmaUeX_31yeyZGs-qpFf1MgIDDjvrG3KRGnlLgAuw0ZZSkQt2Y_cbifOGx0Y-xxdKZQqN8oNRTWiXjNLBxDNXW-egA6bN-lWAEUvDeW3M'
}

def orderbook_handler():


    time.sleep(1)
    mexc_ask_feed =  open('mexc_ask_feed.text')
    mexc_ask_flow = mexc_ask_feed.readlines()

    mexc_ask_flow = str(mexc_ask_flow)
    mexc_ask_flow = mexc_ask_flow[3:]
    mexc_ask_flow = mexc_ask_flow[:-3]
    mexc_ask_flow = mexc_ask_flow.replace("'", "")
    mexc_ask_flow = mexc_ask_flow.replace(" ", "")
    mexc_ask_flow = mexc_ask_flow.split(",")

    mexc_bid_feed = open('mexc_bid_feed.text')
    mexc_bid_flow = mexc_bid_feed.readlines()

    mexc_bid_flow = str(mexc_bid_flow)
    mexc_bid_flow = mexc_bid_flow[3:]
    mexc_bid_flow = mexc_bid_flow[:-3]
    mexc_bid_flow = mexc_bid_flow.replace("'", "")
    mexc_bid_flow = mexc_bid_flow.replace(" ", "")
    mexc_bid_flow = mexc_bid_flow.split(",")

#######################################################
    okex_ask_feed =  open('okex_ask_feed.text')
    okex_ask_flow = okex_ask_feed.readlines()

    okex_ask_flow = str(okex_ask_flow)
    okex_ask_flow = okex_ask_flow[3:]
    okex_ask_flow = okex_ask_flow[:-3]
    okex_ask_flow = okex_ask_flow.replace("'", "")
    okex_ask_flow = okex_ask_flow.replace(" ", "")
    okex_ask_flow = okex_ask_flow.split(",")

    okex_bid_feed = open('okex_bid_feed.text')
    okex_bid_flow = okex_bid_feed.readlines()

    okex_bid_flow = str(okex_bid_flow)
    okex_bid_flow = okex_bid_flow[3:]
    okex_bid_flow = okex_bid_flow[:-3]
    okex_bid_flow = okex_bid_flow.replace("'", "")
    okex_bid_flow = okex_bid_flow.replace(" ", "")
    okex_bid_flow = okex_bid_flow.split(",")

####################################################
    huobi_ask_feed = open('huobi_ask_feed.text')
    huobi_ask_flow = huobi_ask_feed.readlines()

    huobi_ask_flow = str(huobi_ask_flow)
    huobi_ask_flow = huobi_ask_flow[3:]
    huobi_ask_flow = huobi_ask_flow[:-3]
    huobi_ask_flow = huobi_ask_flow.replace("'", "")
    huobi_ask_flow = huobi_ask_flow.replace(" ", "")
    huobi_ask_flow = huobi_ask_flow.split(",")

    huobi_bid_feed = open('huobi_bid_feed.text')
    huobi_bid_flow = huobi_bid_feed.readlines()

    huobi_bid_flow = str(huobi_bid_flow)
    huobi_bid_flow = huobi_bid_flow[3:]
    huobi_bid_flow = huobi_bid_flow[:-3]
    huobi_bid_flow = huobi_bid_flow.replace("'", "")
    huobi_bid_flow = huobi_bid_flow.replace(" ", "")
    huobi_bid_flow = huobi_bid_flow.split(",")

####################################################
    gateio_ask_feed = open('gateio_ask_feed.text')
    gateio_ask_flow = gateio_ask_feed.readlines()

    gateio_ask_flow = str(gateio_ask_flow)
    gateio_ask_flow = gateio_ask_flow[3:]
    gateio_ask_flow = gateio_ask_flow[:-3]
    gateio_ask_flow = gateio_ask_flow.replace("'", "")
    gateio_ask_flow = gateio_ask_flow.replace(" ", "")
    gateio_ask_flow = gateio_ask_flow.split(",")

    gateio_bid_feed = open('gateio_bid_feed.text')
    gateio_bid_flow = gateio_bid_feed.readlines()

    gateio_bid_flow = str(gateio_bid_flow)
    gateio_bid_flow = gateio_bid_flow[3:]
    gateio_bid_flow = gateio_bid_flow[:-3]
    gateio_bid_flow = gateio_bid_flow.replace("'", "")
    gateio_bid_flow = gateio_bid_flow.replace(" ", "")
    gateio_bid_flow = gateio_bid_flow.split(",")


######################################################
    kucoin_ask_feed = open('kucoin_ask_feed.text')
    kucoin_ask_flow = kucoin_ask_feed.readlines()

    kucoin_ask_flow = str(kucoin_ask_flow)
    kucoin_ask_flow = kucoin_ask_flow[3:]
    kucoin_ask_flow = kucoin_ask_flow[:-3]
    kucoin_ask_flow = kucoin_ask_flow.replace("'", "")
    kucoin_ask_flow = kucoin_ask_flow.replace(" ", "")
    kucoin_ask_flow = kucoin_ask_flow.split(",")


    kucoin_bid_feed = open('kucoin_bid_feed.text')
    kucoin_bid_flow = kucoin_bid_feed.readlines()

    kucoin_bid_flow = str(kucoin_bid_flow)
    kucoin_bid_flow = kucoin_bid_flow[3:]
    kucoin_bid_flow = kucoin_bid_flow[:-3]
    kucoin_bid_flow = kucoin_bid_flow.replace("'", "")
    kucoin_bid_flow = kucoin_bid_flow.replace(" ", "")
    kucoin_bid_flow = kucoin_bid_flow.split(",")

######################################################
    zb_ask_feed = open('zb_ask_feed.text')
    zb_ask_flow = zb_ask_feed.readlines()

    zb_ask_flow = str(zb_ask_flow)
    zb_ask_flow = zb_ask_flow[3:]
    zb_ask_flow = zb_ask_flow[:-3]
    zb_ask_flow = zb_ask_flow.replace("'", "")
    zb_ask_flow = zb_ask_flow.replace(" ", "")
    zb_ask_flow = zb_ask_flow.split(",")

    zb_bid_feed = open('zb_bid_feed.text')
    zb_bid_flow = zb_bid_feed.readlines()

    zb_bid_flow = str(zb_bid_flow)
    zb_bid_flow = zb_bid_flow[3:]
    zb_bid_flow = zb_bid_flow[:-3]
    zb_bid_flow = zb_bid_flow.replace("'", "")
    zb_bid_flow = zb_bid_flow.replace(" ", "")
    zb_bid_flow = zb_bid_flow.split(",")

######################################################
    bithumb_ask_feed = open('bithumb_ask_feed.text')
    bithumb_ask_flow = bithumb_ask_feed.readlines()

    bithumb_ask_flow = str(bithumb_ask_flow)
    bithumb_ask_flow = bithumb_ask_flow[3:]
    bithumb_ask_flow = bithumb_ask_flow[:-3]
    bithumb_ask_flow = bithumb_ask_flow.replace("'", "")
    bithumb_ask_flow = bithumb_ask_flow.replace(" ", "")
    bithumb_ask_flow = bithumb_ask_flow.split(",")

    bithumb_bid_feed = open('bithumb_bid_feed.text')
    bithumb_bid_flow = bithumb_bid_feed.readlines()

    bithumb_bid_flow = str(bithumb_bid_flow)
    bithumb_bid_flow = bithumb_bid_flow[3:]
    bithumb_bid_flow = bithumb_bid_flow[:-3]
    bithumb_bid_flow = bithumb_bid_flow.replace("'", "")
    bithumb_bid_flow = bithumb_bid_flow.replace(" ", "")
    bithumb_bid_flow = bithumb_bid_flow.split(",")

#####################################################
    kraken_ask_feed = open('kraken_ask_feed.text')
    kraken_ask_flow = kraken_ask_feed.readlines()

    kraken_ask_flow = str(kraken_ask_flow)
    kraken_ask_flow = kraken_ask_flow[3:]
    kraken_ask_flow = kraken_ask_flow[:-3]
    kraken_ask_flow = kraken_ask_flow.replace("'", "")
    kraken_ask_flow = kraken_ask_flow.replace(" ", "")
    kraken_ask_flow = kraken_ask_flow.split(",")

    kraken_bid_feed = open('kraken_bid_feed.text')
    kraken_bid_flow = kraken_bid_feed.readlines()

    kraken_bid_flow = str(kraken_bid_flow)
    kraken_bid_flow = kraken_bid_flow[3:]
    kraken_bid_flow = kraken_bid_flow[:-3]
    kraken_bid_flow = kraken_bid_flow.replace("'", "")
    kraken_bid_flow = kraken_bid_flow.replace(" ", "")
    kraken_bid_flow = kraken_bid_flow.split(",")
########################################################
    cex_ask_feed = open('cex_ask_feed.text')
    cex_ask_flow = cex_ask_feed.readlines()

    cex_ask_flow = str(cex_ask_flow)
    cex_ask_flow = cex_ask_flow[3:]
    cex_ask_flow = cex_ask_flow[:-3]
    cex_ask_flow = cex_ask_flow.replace("'", "")
    cex_ask_flow = cex_ask_flow.replace(" ", "")
    cex_ask_flow = cex_ask_flow.split(",")

    cex_bid_feed = open('cex_bid_feed.text')
    cex_bid_flow = cex_bid_feed.readlines()

    cex_bid_flow = str(cex_bid_flow)
    cex_bid_flow = cex_bid_flow[3:]
    cex_bid_flow = cex_bid_flow[:-3]
    cex_bid_flow = cex_bid_flow.replace("'", "")
    cex_bid_flow = cex_bid_flow.replace(" ", "")
    cex_bid_flow = cex_bid_flow.split(",")

##############################################

    mexc_bid_array_unf = np.array(mexc_bid_flow)
    mexc_ask_array_unf = np.array(mexc_ask_flow)
    mexc_bid_array_str = np.reshape(mexc_bid_array_unf, (6,))
    mexc_ask_array_str = np.reshape(mexc_ask_array_unf, (6,))
    mexc_bid_array = mexc_bid_array_str.astype(np.float)
    mexc_ask_array = mexc_ask_array_str.astype(np.float)
############################################################

    okex_bid_array_unf = np.array(okex_bid_flow)
    okex_ask_array_unf = np.array(okex_ask_flow)
    okex_bid_array_str = np.reshape(okex_bid_array_unf, (6,))
    okex_ask_array_str = np.reshape(okex_ask_array_unf, (6,))
    okex_bid_array = okex_bid_array_str.astype(np.float)
    okex_ask_array = okex_ask_array_str.astype(np.float)

##############################################################
    huobi_bid_array_unf = np.array(huobi_bid_flow)
    huobi_ask_array_unf = np.array(huobi_ask_flow)
    huobi_bid_array_str = np.reshape(huobi_bid_array_unf, (6,))
    huobi_ask_array_str = np.reshape(huobi_ask_array_unf, (6,))
    huobi_bid_array = huobi_bid_array_str.astype(np.float)
    huobi_ask_array = huobi_ask_array_str.astype(np.float)

##############################################################

    gateio_bid_array_unf = np.array(gateio_bid_flow)
    gateio_ask_array_unf = np.array(gateio_ask_flow)
    gateio_bid_array_str = np.reshape(gateio_bid_array_unf, (6,))
    gateio_ask_array_str = np.reshape(gateio_ask_array_unf, (6,))
    gateio_bid_array = gateio_bid_array_str.astype(np.float)
    gateio_ask_array = gateio_ask_array_str.astype(np.float)

#################################################################

    kucoin_bid_array_unf = np.array(kucoin_bid_flow)
    kucoin_ask_array_unf = np.array(kucoin_ask_flow)
    kucoin_bid_array_str = np.reshape(kucoin_bid_array_unf, (6,))
    kucoin_ask_array_str = np.reshape(kucoin_ask_array_unf, (6,))
    kucoin_bid_array = kucoin_bid_array_str.astype(np.float)
    kucoin_ask_array = kucoin_ask_array_str.astype(np.float)

##################################################################

    zb_bid_array_unf = np.array(zb_bid_flow)
    zb_ask_array_unf = np.array(zb_ask_flow)
    zb_bid_array_str = np.reshape(zb_bid_array_unf, (6,))
    zb_ask_array_str = np.reshape(zb_ask_array_unf, (6,))
    zb_bid_array = zb_bid_array_str.astype(np.float)
    zb_ask_array = zb_ask_array_str.astype(np.float)

######################################################################

    bithumb_bid_array_unf = np.array(bithumb_bid_flow)
    bithumb_ask_array_unf = np.array(bithumb_ask_flow)
    bithumb_bid_array_str = np.reshape(bithumb_bid_array_unf, (6,))
    bithumb_ask_array_str = np.reshape(bithumb_ask_array_unf, (6,))
    bithumb_bid_array = bithumb_bid_array_str.astype(np.float)
    bithumb_ask_array = bithumb_ask_array_str.astype(np.float)

######################################################################

    kraken_bid_array_unf = np.array(kraken_bid_flow)
    kraken_ask_array_unf = np.array(kraken_ask_flow)
    kraken_bid_array_str = np.reshape(kraken_bid_array_unf, (6,))
    kraken_ask_array_str = np.reshape(kraken_ask_array_unf, (6,))
    kraken_bid_array = kraken_bid_array_str.astype(np.float)
    kraken_ask_array = kraken_ask_array_str.astype(np.float)

######################################################################

    cex_bid_array_unf = np.array(cex_bid_flow)
    cex_ask_array_unf = np.array(cex_ask_flow)
    cex_bid_array_str = np.reshape(cex_bid_array_unf, (6,))
    cex_ask_array_str = np.reshape(cex_ask_array_unf, (6,))
    cex_bid_array = cex_bid_array_str.astype(np.float)
    cex_ask_array = cex_ask_array_str.astype(np.float)

#####################################################################
    mexc_ask_depth1 = mexc_ask_array[1]
    mexc_ask_depth2 = mexc_ask_array[3]
    mexc_ask_depth3 = mexc_ask_array[5]
    mexc_ask_depth_sum = mexc_ask_depth1 + mexc_ask_depth2 + mexc_ask_depth3

    mexc_ask_price1 = mexc_ask_array[0]
    mexc_ask_price2 = mexc_ask_array[2]
    mexc_ask_price3 = mexc_ask_array[4]

    okex_ask_depth1 = okex_ask_array[1]
    okex_ask_depth2 = okex_ask_array[3]
    okex_ask_depth3 = okex_ask_array[5]
    okex_ask_depth_sum = okex_ask_depth1 + okex_ask_depth2 + okex_ask_depth3

    okex_ask_price1 = okex_ask_array[0]
    okex_ask_price2 = okex_ask_array[2]
    okex_ask_price3 = okex_ask_array[4]

    huobi_ask_depth1 = huobi_ask_array[1]
    huobi_ask_depth2 = huobi_ask_array[3]
    huobi_ask_depth3 = huobi_ask_array[5]
    huobi_ask_depth_sum = huobi_ask_depth1 + huobi_ask_depth2 + huobi_ask_depth3

    huobi_ask_price1 = huobi_ask_array[0]
    huobi_ask_price2 = huobi_ask_array[2]
    huobi_ask_price3 = huobi_ask_array[4]

    gateio_ask_depth1 = gateio_ask_array[1]
    gateio_ask_depth2 = gateio_ask_array[3]
    gateio_ask_depth3 = gateio_ask_array[5]
    gateio_ask_depth_sum = gateio_ask_depth1 + gateio_ask_depth2 + gateio_ask_depth3

    gateio_ask_price1 = gateio_ask_array[0]
    gateio_ask_price2 = gateio_ask_array[2]
    gateio_ask_price3 = gateio_ask_array[4]

    kucoin_ask_depth1 = kucoin_ask_array[1]
    kucoin_ask_depth2 = kucoin_ask_array[3]
    kucoin_ask_depth3 = kucoin_ask_array[5]
    kucoin_ask_depth_sum = kucoin_ask_depth1 + kucoin_ask_depth2 + kucoin_ask_depth3

    kucoin_ask_price1 = kucoin_ask_array[0]
    kucoin_ask_price2 = kucoin_ask_array[2]
    kucoin_ask_price3 = kucoin_ask_array[4]

    zb_ask_depth1 = zb_ask_array[1]
    zb_ask_depth2 = zb_ask_array[3]
    zb_ask_depth3 = zb_ask_array[5]
    zb_ask_depth_sum = zb_ask_depth1 + zb_ask_depth2 + zb_ask_depth3

    zb_ask_price1 = zb_ask_array[0]
    zb_ask_price2 = zb_ask_array[2]
    zb_ask_price3 = zb_ask_array[4]

    bithumb_ask_depth1 = bithumb_ask_array[1]
    bithumb_ask_depth2 = bithumb_ask_array[3]
    bithumb_ask_depth3 = bithumb_ask_array[5]
    bithumb_ask_depth_sum = bithumb_ask_depth1 + bithumb_ask_depth2 + bithumb_ask_depth3

    bithumb_ask_price1 = bithumb_ask_array[0]
    bithumb_ask_price2 = bithumb_ask_array[2]
    bithumb_ask_price3 = bithumb_ask_array[4]

    kraken_ask_depth1 = kraken_ask_array[1]
    kraken_ask_depth2 = kraken_ask_array[3]
    kraken_ask_depth3 = kraken_ask_array[5]
    kraken_ask_depth_sum = kraken_ask_depth1 + kraken_ask_depth2 + kraken_ask_depth3

    kraken_ask_price1 = kraken_ask_array[0]
    kraken_ask_price2 = kraken_ask_array[2]
    kraken_ask_price3 = kraken_ask_array[4]

    cex_ask_depth1 = cex_ask_array[1]
    cex_ask_depth2 = cex_ask_array[3]
    cex_ask_depth3 = cex_ask_array[5]
    cex_ask_depth_sum = cex_ask_depth1 + cex_ask_depth2 + cex_ask_depth3

    cex_ask_price1 = cex_ask_array[0]
    cex_ask_price2 = cex_ask_array[2]
    cex_ask_price3 = cex_ask_array[4]

########################################################################
    mexc_bid_depth1 = mexc_bid_array[1]
    mexc_bid_depth2 = mexc_bid_array[3]
    mexc_bid_depth3 = mexc_bid_array[5]
    mexc_bid_depth_sum = mexc_bid_depth1 + mexc_bid_depth2 + mexc_bid_depth3

    mexc_bid_price1 = mexc_bid_array[0]
    mexc_bid_price2 = mexc_bid_array[2]
    mexc_bid_price3 = mexc_bid_array[4]

    okex_bid_depth1 = okex_bid_array[1]
    okex_bid_depth2 = okex_bid_array[3]
    okex_bid_depth3 = okex_bid_array[5]
    okex_bid_depth_sum = okex_bid_depth1 + okex_bid_depth2 + okex_bid_depth3

    okex_bid_price1 = okex_bid_array[0]
    okex_bid_price2 = okex_bid_array[2]
    okex_bid_price3 = okex_bid_array[4]

    huobi_bid_depth1 = huobi_bid_array[1]
    huobi_bid_depth2 = huobi_bid_array[3]
    huobi_bid_depth3 = huobi_bid_array[5]
    huobi_bid_depth_sum = huobi_bid_depth1 + huobi_bid_depth2 + huobi_bid_depth3

    huobi_bid_price1 = huobi_bid_array[0]
    huobi_bid_price2 = huobi_bid_array[2]
    huobi_bid_price3 = huobi_bid_array[4]

    gateio_bid_depth1 = gateio_bid_array[1]
    gateio_bid_depth2 = gateio_bid_array[3]
    gateio_bid_depth3 = gateio_bid_array[5]
    gateio_bid_depth_sum = gateio_bid_depth1 + gateio_bid_depth2 + gateio_bid_depth3

    gateio_bid_price1 = gateio_bid_array[0]
    gateio_bid_price2 = gateio_bid_array[2]
    gateio_bid_price3 = gateio_bid_array[4]

    kucoin_bid_depth1 = kucoin_bid_array[1]
    kucoin_bid_depth2 = kucoin_bid_array[3]
    kucoin_bid_depth3 = kucoin_bid_array[5]
    kucoin_bid_depth_sum = kucoin_bid_depth1 + kucoin_bid_depth2 + kucoin_bid_depth3

    kucoin_bid_price1 = kucoin_bid_array[0]
    kucoin_bid_price2 = kucoin_bid_array[2]
    kucoin_bid_price3 = kucoin_bid_array[4]

    zb_bid_depth1 = zb_bid_array[1]
    zb_bid_depth2 = zb_bid_array[3]
    zb_bid_depth3 = zb_bid_array[5]
    zb_bid_depth_sum = zb_bid_depth1 + zb_bid_depth2 + zb_bid_depth3

    zb_bid_price1 = zb_bid_array[0]
    zb_bid_price2 = zb_bid_array[2]
    zb_bid_price3 = zb_bid_array[4]

    bithumb_bid_depth1 = bithumb_bid_array[1]
    bithumb_bid_depth2 = bithumb_bid_array[3]
    bithumb_bid_depth3 = bithumb_bid_array[5]
    bithumb_bid_depth_sum = bithumb_bid_depth1 + bithumb_bid_depth2 + bithumb_bid_depth3

    bithumb_bid_price1 = bithumb_bid_array[0]
    bithumb_bid_price2 = bithumb_bid_array[2]
    bithumb_bid_price3 = bithumb_bid_array[4]

    kraken_bid_depth1 = kraken_bid_array[1]
    kraken_bid_depth2 = kraken_bid_array[3]
    kraken_bid_depth3 = kraken_bid_array[5]
    kraken_bid_depth_sum = kraken_bid_depth1 + kraken_bid_depth2 + kraken_bid_depth3

    kraken_bid_price1 = kraken_bid_array[0]
    kraken_bid_price2 = kraken_bid_array[2]
    kraken_bid_price3 = kraken_bid_array[4]

    cex_bid_depth1 = cex_bid_array[1]
    cex_bid_depth2 = cex_bid_array[3]
    cex_bid_depth3 = cex_bid_array[5]
    cex_bid_depth_sum = cex_bid_depth1 + cex_bid_depth2 + cex_bid_depth3

    cex_bid_price1 = cex_bid_array[0]
    cex_bid_price2 = cex_bid_array[2]
    cex_bid_price3 = cex_bid_array[4]

#####################################################################
    ask_array = np.stack(
        [mexc_ask_array, okex_ask_array, huobi_ask_array, gateio_ask_array, kucoin_ask_array, zb_ask_array, bithumb_ask_array, kraken_ask_array, cex_ask_array])
    bid_array = np.stack(
        [mexc_bid_array, okex_bid_array, huobi_bid_array, gateio_bid_array, kucoin_bid_array, zb_bid_array, bithumb_bid_array, kraken_bid_array, cex_bid_array])

    #find lowest ask in array and coords
    low_ask = np.min(ask_array, axis = 0)
    low_ask_raw_val = low_ask[0]
    low_ask_coords = np.where(ask_array == low_ask_raw_val)
    low_ask = low_ask[0]

    #find lowest bid in array and coords
    high_bid = np.max(bid_array, axis = 0)
    high_bid_raw_val = high_bid[0]
    high_bid_coords = np.where(bid_array == high_bid_raw_val)
    high_bid = high_bid[0]


    #assign coords of low price to  exchage
    if low_ask_coords[0] == [0]:
        low_ask_ex = "mexc"
        low_ask_depth = mexc_ask_depth_sum
        low_ask_price1 = mexc_ask_price1
        low_ask_price2 = mexc_ask_price2
        low_ask_price3 = mexc_ask_price3
        low_ask_depth1 = mexc_ask_depth1
        low_ask_depth2 = mexc_ask_depth2
        low_ask_depth3 = mexc_ask_depth3

    if low_ask_coords[0] == [1]:
        low_ask_ex = "okex"
        low_ask_depth = okex_ask_depth_sum
        low_ask_depth = okex_ask_depth_sum
        low_ask_price1 = okex_ask_price1
        low_ask_price2 = okex_ask_price2
        low_ask_price3 = okex_ask_price3
        low_ask_depth1 = okex_ask_depth1
        low_ask_depth2 = okex_ask_depth2
        low_ask_depth3 = okex_ask_depth3

    if low_ask_coords[0] == [2]:
        low_ask_ex = "huobi"
        low_ask_depth = huobi_ask_depth_sum
        low_ask_depth = huobi_ask_depth_sum
        low_ask_price1 = huobi_ask_price1
        low_ask_price2 = huobi_ask_price2
        low_ask_price3 = huobi_ask_price3
        low_ask_depth1 = huobi_ask_depth1
        low_ask_depth2 = huobi_ask_depth2
        low_ask_depth3 = huobi_ask_depth3

    if low_ask_coords[0] == [3]:
        low_ask_ex = "gateio"
        low_ask_depth = gateio_ask_depth_sum
        low_ask_depth = gateio_ask_depth_sum
        low_ask_price1 = gateio_ask_price1
        low_ask_price2 = gateio_ask_price2
        low_ask_price3 = gateio_ask_price3
        low_ask_depth1 = gateio_ask_depth1
        low_ask_depth2 = gateio_ask_depth2
        low_ask_depth3 = gateio_ask_depth3

    if low_ask_coords[0] == [4]:
        low_ask_ex = "kucoin"
        low_ask_depth = kucoin_ask_depth_sum
        low_ask_depth = kucoin_ask_depth_sum
        low_ask_price1 = kucoin_ask_price1
        low_ask_price2 = kucoin_ask_price2
        low_ask_price3 = kucoin_ask_price3
        low_ask_depth1 = kucoin_ask_depth1
        low_ask_depth2 = kucoin_ask_depth2
        low_ask_depth3 = kucoin_ask_depth3

    if low_ask_coords[0] == [5]:
        low_ask_ex = "zb"
        low_ask_depth = zb_ask_depth_sum
        low_ask_depth = zb_ask_depth_sum
        low_ask_price1 = zb_ask_price1
        low_ask_price2 = zb_ask_price2
        low_ask_price3 = zb_ask_price3
        low_ask_depth1 = zb_ask_depth1
        low_ask_depth2 = zb_ask_depth2
        low_ask_depth3 = zb_ask_depth3

    if low_ask_coords[0] == [6]:
        low_ask_ex = "bithumb"
        low_ask_depth = bithumb_ask_depth_sum
        low_ask_depth = bithumb_ask_depth_sum
        low_ask_price1 = bithumb_ask_price1
        low_ask_price2 = bithumb_ask_price2
        low_ask_price3 = bithumb_ask_price3
        low_ask_depth1 = bithumb_ask_depth1
        low_ask_depth2 = bithumb_ask_depth2
        low_ask_depth3 = bithumb_ask_depth3

    if low_ask_coords[0] == [7]:
        low_ask_ex = "kraken"
        low_ask_depth = kraken_ask_depth_sum
        low_ask_depth = kraken_ask_depth_sum
        low_ask_price1 = kraken_ask_price1
        low_ask_price2 = kraken_ask_price2
        low_ask_price3 = kraken_ask_price3
        low_ask_depth1 = kraken_ask_depth1
        low_ask_depth2 = kraken_ask_depth2
        low_ask_depth3 = kraken_ask_depth3

    if low_ask_coords[0] == [8]:
        low_ask_ex = "cex"
        low_ask_depth = cex_ask_depth_sum
        low_ask_depth = cex_ask_depth_sum
        low_ask_price1 = cex_ask_price1
        low_ask_price2 = cex_ask_price2
        low_ask_price3 = cex_ask_price3
        low_ask_depth1 = cex_ask_depth1
        low_ask_depth2 = cex_ask_depth2
        low_ask_depth3 = cex_ask_depth3

        #assign bid coords to exchange
    if high_bid_coords[0] == [0]:
        high_bid_ex = "mexc"
        high_bid_depth = mexc_bid_depth_sum
        high_bid_price1 = mexc_bid_price1
        high_bid_price2 = mexc_bid_price2
        high_bid_price3 = mexc_bid_price3
        high_bid_depth1 = mexc_bid_depth1
        high_bid_depth2 = mexc_bid_depth2
        high_bid_depth3 = mexc_bid_depth3

    if high_bid_coords[0] == [1]:
        high_bid_ex = "okex"
        high_bid_depth = okex_bid_depth_sum
        high_bid_depth = okex_bid_depth_sum
        high_bid_depth = okex_bid_depth_sum
        high_bid_price1 = okex_bid_price1
        high_bid_price2 = okex_bid_price2
        high_bid_price3 = okex_bid_price3
        high_bid_depth1 = okex_bid_depth1
        high_bid_depth2 = okex_bid_depth2
        high_bid_depth3 = okex_bid_depth3

    if high_bid_coords[0] == [2]:
        high_bid_ex = 'huobi'
        high_bid_depth = huobi_bid_depth_sum
        high_bid_depth = huobi_bid_depth_sum
        high_bid_price1 = huobi_bid_price1
        high_bid_price2 = huobi_bid_price2
        high_bid_price3 = huobi_bid_price3
        high_bid_depth1 = huobi_bid_depth1
        high_bid_depth2 = huobi_bid_depth2
        high_bid_depth3 = huobi_bid_depth3

    if high_bid_coords[0] == [3]:
        high_bid_ex = 'gatio'
        high_bid_depth = gateio_bid_depth_sum
        high_bid_price1 = gateio_bid_price1
        high_bid_price2 = gateio_bid_price2
        high_bid_price3 = gateio_bid_price3
        high_bid_depth1 = gateio_bid_depth1
        high_bid_depth2 = gateio_bid_depth2
        high_bid_depth3 = gateio_bid_depth3

    if high_bid_coords[0] == [4]:
        high_bid_ex = 'kucoin'
        high_bid_depth = kucoin_bid_depth_sum
        high_bid_price1 = kucoin_bid_price1
        high_bid_price2 = kucoin_bid_price2
        high_bid_price3 = kucoin_bid_price3
        high_bid_depth1 = kucoin_bid_depth1
        high_bid_depth2 = kucoin_bid_depth2
        high_bid_depth3 = kucoin_bid_depth3

    if high_bid_coords[0] == [5]:
        high_bid_ex = 'zb'
        high_bid_depth = zb_bid_depth_sum
        high_bid_price1 = zb_bid_price1
        high_bid_price2 = zb_bid_price2
        high_bid_price3 = zb_bid_price3
        high_bid_depth1 = zb_bid_depth1
        high_bid_depth2 = zb_bid_depth2
        high_bid_depth3 = zb_bid_depth3

    if high_bid_coords[0] == [6]:
        high_bid_ex = 'bithumb'
        high_bid_depth = bithumb_bid_depth_sum
        high_bid_price1 = bithumb_bid_price1
        high_bid_price2 = bithumb_bid_price2
        high_bid_price3 = bithumb_bid_price3
        high_bid_depth1 = bithumb_bid_depth1
        high_bid_depth2 = bithumb_bid_depth2
        high_bid_depth3 = bithumb_bid_depth3

    if high_bid_coords[0] == [7]:
        high_bid_ex = 'kraken'
        high_bid_depth = kraken_bid_depth_sum
        high_bid_price1 = kraken_bid_price1
        high_bid_price2 = kraken_bid_price2
        high_bid_price3 = kraken_bid_price3
        high_bid_depth1 = kraken_bid_depth1
        high_bid_depth2 = kraken_bid_depth2
        high_bid_depth3 = kraken_bid_depth3

    if high_bid_coords[0] == [8]:
        high_bid_ex = 'cex'
        high_bid_depth = cex_bid_depth_sum
        high_bid_price1 = cex_bid_price1
        high_bid_price2 = cex_bid_price2
        high_bid_price3 = cex_bid_price3
        high_bid_depth1 = cex_bid_depth1
        high_bid_depth2 = cex_bid_depth2
        high_bid_depth3 = cex_bid_depth3

    '''print('ask array:')
    print(ask_array)
    print('lowest ask:')
    print(low_ask)
    print(low_ask_ex)

    print('high array:')
    print(bid_array)
    print('highest bid:')
    print(high_bid)
    print(high_bid_ex)'''

    net_arbitrage = high_bid - low_ask

    #for item in low_ask, low_ask_ex, high_bid, high_bid_ex, ask_array, bid_array:

    #Avg price for all three orders in orderbook
    low_ask_avg_price_all_top = (low_ask_price1*low_ask_depth1) + (low_ask_price2*low_ask_depth2) + (low_ask_price3*low_ask_depth3)
    low_ask_depth_sum_all = float(low_ask_depth1) + float(low_ask_depth2) + float(low_ask_depth3)
    low_ask_avg_price_all = low_ask_avg_price_all_top/low_ask_depth_sum_all
    #print('avg price ask all', low_ask_avg_price_all)

    high_bid_avg_price_all_top = (high_bid_price1 * high_bid_depth1) + (high_bid_price2 * high_bid_depth2) + (high_bid_price3 * high_bid_depth3)
    high_bid_depth_sum_all = float(high_bid_depth1) + float(high_bid_depth2) + float(high_bid_depth3)
    high_bid_avg_price_all = high_bid_avg_price_all_top / high_bid_depth_sum_all
    #print('avg price bid all', high_bid_avg_price_all)

    #average price for top two orders

    low_ask_avg_price_2_top = (low_ask_price1*low_ask_depth1) + (low_ask_price2*low_ask_depth2)
    low_ask_depth_sum_2_all = float(low_ask_depth1) + float(low_ask_depth2)
    low_ask_avg_price_2_all = low_ask_avg_price_2_top/low_ask_depth_sum_2_all
    #print('avg price ask top 2', low_ask_avg_price_2_all)

    high_bid_avg_price_2_top = (high_bid_price1 * high_bid_depth1) + (high_bid_price2 * high_bid_depth2)
    high_bid_depth_sum_2_all = float(high_bid_depth1) + float(high_bid_depth2)
    high_bid_avg_price_2_all = high_bid_avg_price_2_top / high_bid_depth_sum_2_all
    #print('avg price bid top 2', high_bid_avg_price_2_all)

    #average price for first order
    low_ask_avg_price_1_all = low_ask_price1
    high_bid_avg_price_1_all = high_bid_price1

    low_ask2_sum = low_ask_depth1 + low_ask_depth2
    low_ask3_sum = low_ask_depth1 + low_ask_depth2 + low_ask_depth3


    first_order_arbitrage = net_arbitrage
    second_order_arbitrage = high_bid_avg_price_2_all - low_ask_avg_price_2_all
    third_order_arbitrage = high_bid_avg_price_all - low_ask_avg_price_all


    print("net arb:", f'{net_arbitrage:.20f}')

    print("2nd order net arb:", f'{second_order_arbitrage:.20f}')

    print("3rd order net arb:", f'{third_order_arbitrage:.20f}')
    print('low ask:', low_ask_ex)
    print('high bid:', high_bid_ex)

    ask_array_str_unf = str(ask_array)
    ask_array_str = ask_array_str_unf.replace("\n", "\t")

    bid_array_str_unf = str(bid_array)
    bid_array_str = bid_array_str_unf.replace("\n", "\t")

    csvfile = open('orderbook_handler_data_all.csv', 'a', newline='')  # newline='', encoding='utf-8')

    c = csv.writer(csvfile)

    c.writerow([str(datetime.now()), low_ask_avg_price_1_all, low_ask_avg_price_2_all, low_ask_avg_price_all, low_ask_ex, low_ask_depth1, (low_ask_depth1*low_ask_avg_price_1_all), low_ask2_sum, (low_ask2_sum *low_ask_avg_price_2_all), low_ask3_sum, (low_ask3_sum*low_ask_avg_price_all),
                high_bid_avg_price_1_all, high_bid_avg_price_2_all, high_bid_avg_price_all, high_bid_ex, high_bid_depth1, (high_bid_depth1*high_bid), high_bid_depth_sum_2_all, (high_bid_depth_sum_2_all*high_bid_avg_price_2_all), high_bid_depth_sum_all, (high_bid_depth_sum_all*high_bid_avg_price_all),
                first_order_arbitrage, second_order_arbitrage, third_order_arbitrage, ask_array_str, bid_array_str])

    csvfile.close()

    if float(net_arbitrage) >= 0.001:

        payload = {
            "time": str(datetime.now()),
            "low_ask": low_ask_avg_price_1_all,
            "low_ask_avg_price_first_two_orders": low_ask_avg_price_2_all,
            "low_ask_avg_price_first_three_orders": low_ask_avg_price_all,
            "low_ask_exchange": low_ask_ex,
            "low_ask_depth_first_order_xlm": low_ask_depth1,
            "low_ask_depth_first_order_usd": (low_ask_depth1*low_ask_avg_price_1_all),
            "low_ask_depth_first_two_xlm": low_ask2_sum,
            "low_ask_depth_first_two_usd": (low_ask2_sum *low_ask_avg_price_2_all),
            "low_ask_depth_all_three_xlm": low_ask3_sum,
            "low_ask_depth_all_three_usd": (low_ask3_sum*low_ask_avg_price_all),
            "high_bid": high_bid_avg_price_1_all,
            "high_bid_avg_price_first_three_orders": high_bid_avg_price_2_all,
            "high_bid_avg_price_first_two_orders": high_bid_avg_price_all,
            "high_bid_exchange": high_bid_ex,
            "high_bid_depth_first_order_xlm": high_bid_depth1,
            "high_bid_depth_first_order_usd": (high_bid_depth1*high_bid),
            "high_bid_depth_two_orders_xlm": high_bid_depth_sum_2_all,
            "high_bid_depth_two_orders_usd": (high_bid_depth_sum_2_all*high_bid_avg_price_2_all),
            "high_bid_depth_three_orders_xlm": high_bid_depth_sum_all,
            "high_bid_depth_three_orders_usd": (high_bid_depth_sum_all*high_bid_avg_price_all),
            "first_order_arbitrage": first_order_arbitrage,
            "second_order_arbitrage": second_order_arbitrage,
            "third_order_arbitrage": third_order_arbitrage,
            "ask_array": ask_array_str,
            "bid_array": bid_array_str
        }

        print(payload)
        csvfile1 = open('orderbook_handler_data_arb_only.csv', 'a', newline='')
        c = csv.writer(csvfile1)
        c.writerow([str(datetime.now()), low_ask_avg_price_1_all, low_ask_avg_price_2_all, low_ask_avg_price_all, low_ask_ex, low_ask_depth1, (low_ask_depth1*low_ask_avg_price_1_all), low_ask2_sum, (low_ask2_sum *low_ask_avg_price_2_all), low_ask3_sum, (low_ask3_sum*low_ask_avg_price_all), high_bid_avg_price_1_all, high_bid_avg_price_2_all, high_bid_avg_price_all, high_bid_ex, high_bid_depth1, (high_bid_depth1*high_bid), high_bid_depth_sum_2_all, (high_bid_depth_sum_2_all*high_bid_avg_price_2_all), high_bid_depth_sum_all, (high_bid_depth_sum_all*high_bid_avg_price_all),first_order_arbitrage, second_order_arbitrage, third_order_arbitrage, ask_array_str, bid_array_str])


        csvfile1.close()

        best_order_arb = open('best_order_arb.text', "w")

        best_order_arb.write(str(low_ask_ex))
        best_order_arb.write('|')
        best_order_arb.write(str(low_ask_price1))
        best_order_arb.write('|')
        best_order_arb.write(str(low_ask_price2))
        best_order_arb.write('|')
        best_order_arb.write(str(low_ask_price3))
        best_order_arb.write('|')
        best_order_arb.write(str(low_ask_depth1))
        best_order_arb.write('|')
        best_order_arb.write(str(low_ask_depth2))
        best_order_arb.write('|')
        best_order_arb.write(str(low_ask_depth3))
        best_order_arb.write('|')
        best_order_arb.write(str(high_bid_ex))
        best_order_arb.write('|')
        best_order_arb.write(str(high_bid_price1))
        best_order_arb.write('|')
        best_order_arb.write(str(high_bid_price2))
        best_order_arb.write('|')
        best_order_arb.write(str(high_bid_price3))
        best_order_arb.write('|')
        best_order_arb.write(str(high_bid_depth1))
        best_order_arb.write('|')
        best_order_arb.write(str(high_bid_depth2))
        best_order_arb.write('|')
        best_order_arb.write(str(high_bid_depth3))
        best_order_arb.write('|')
        best_order_arb.write('|')
        best_order_arb.write('bid array')
        best_order_arb.write('| \n')
        best_order_arb.write(str(bid_array))
        best_order_arb.write('| \n')
        best_order_arb.write('ask array')
        best_order_arb.write('|\n')
        best_order_arb.write(str(ask_array))
        best_order_arb.close()


while True:
    try:
        orderbook_handler()
        time.sleep(1)

    except Exception as ex:

        logerros = open('orderbook_handler_errors.text', "a", newline='')

        logerros.write('| orderbook hanlder error:' + str(datetime.now()) + " " + str(ex))
        logerros.close()

        print(ex)
