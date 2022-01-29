import pymysql
import pymysql


connection = pymysql.connect(host="localhost",user="#####",passwd="#####",database="#####")
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




