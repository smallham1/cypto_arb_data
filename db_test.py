import pymysql
import pymysql


connection = pymysql.connect(host="localhost",user="adminer",passwd="Crypto#123",database="radmin")
cursor = connection.cursor()

add_bithumb_orderbook_data = ("INSERT INTO `bithumb_ask_feed` (`id`, `bithumb_ask1`, `bithumb_ask_amount1`, `bithumb_ask2`, `bithumb_ask_amount2`, `bithumb_ask3`, `bithumb_ask_amount3`, `created_at`, `updated_at`) VALUES (NULL, '', NULL, NULL, '', '', '', NULL, NULL);")
               #"(id, datetime, order_rank, price_ask, amount_ask, price_bid, amount_bid) "
new_bid_data = ("SELECT MAX(id)")

cursor.execute(new_bid_data)
connection.commit()

connection.close()
print(add_bithumb_orderbook_data)
print(connection)
print(cursor)
print('####')




add_bithumb_ask_data = ('INSERT INTO `bithumb_ask_feed` (`id`, `bithumb_ask1`, `bithumb_ask_amount1`, `bithumb_ask2`, `bithumb_ask_amount2`, `bithumb_ask3`, `bithumb_ask_amount3`, `created_at`, `updated_at`) VALUES ({},{},{},{},{},{},{},{},{})'.format('NULL', bithumb_ask1, bithumb_ask_amount1, bithumb_ask2, bithumb_ask_amount2, bithumb_ask3, bithumb_ask_amount3, 'NULL', 'NULL'))




'''url = "http://72.76.64.74/api/v1/order/create"

payload = {'email': 'admin@test.com',
           'password': '1234'}
files = [

]
headers = {
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI1IiwianRpIjoiODM0ZTgwNDJmYzc5ZmI5MWRkNWM5MTk5NTMyMTg3MThmNmU3NDYxYTMyN2U2ZGMwMTlhNDViOWVjNzJmMmE1MDMyYTAyNGUzZjM3MGI2OGIiLCJpYXQiOjE2Mzc0NjkyMTUsIm5iZiI6MTYzNzQ2OTIxNSwiZXhwIjoxNjY5MDA1MjE1LCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.NMsDlzkohrrRJpe1qzJlPbmo1PNmw1mRbwZnFE2bbFzOQyugmbGdef_U9CPqzdEWbu65TUUXZLP6qWpqUNQcK3misoEJNbD4FHdT-_unf1yKMfbOkVRPVILdZHfdGtSVFt2tifJnEHMCC25CvbIGQzyKbVKhcGEdkX6hfvkm_gNK03uKcEFKYs40k4hYLZpSwwKGEyD-Q_hOWpQOFjZTOeCkXf6-Il-6xe-_tWyK2OD3n7JJCb8hcKC0MNZkNHeqKWq2wRuwpKHRqrZw6VrQfddE5q7IPzB9fLqw-0Bn44Mp7lUBaAZY58hrjmhBXnHqYx0EXsG66chIcAyse03VpJDA8z5OIS27AYVRIG4iAZNr16zIdVz36T_hwkd_1TVF7jEp8r6o-b1iJNWB4qGstxnqdco7TA1H-vCFo_m-X7tW4BvNPYK1MqIom8vFT4zeKx0nsngAri5I6WD5XWVKUDvrWkdF0bMI2dspLRHY8mN4xoLqy6el9OSgPOtfDUbSpnA_MZjorv0NEG1nAqEJZ7GAW5i2Tz5fGO2aCtirJztni7JbF9AJAHbfdnH0rCss86VmaUeX_31yeyZGs-qpFf1MgIDDjvrG3KRGnlLgAuw0ZZSkQt2Y_cbifOGx0Y-xxdKZQqN8oNRTWiXjNLBxDNXW-egA6bN-lWAEUvDeW3M'
}
payload = {
    'low_ask': '1',
    'low_ask_avg_price_first_two_orders': '2',
    'low_ask_avg_price_first_three_orders': '3'
}
response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)'''
