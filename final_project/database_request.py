import mysql.connector as mysql


@staticmethod
def check_changing_user_name():
    litecart = mysql.connect(host='127.0.0.1',
                             user='root',
                             passwd='',
                             database='litecart')
    try:
        cursor = litecart.cursor()
        query = 'SELECT firstname, lastname FROM lc_customers WHERE id=1'
        cursor.execute(query)
        full_name_list = cursor.fetchall()
        full_name = full_name_list[0][0] + ' ' + full_name_list[0][1]
        assert full_name == 'Abraham Warner', 'Error. Full name isn\'t change!'
    finally:
        litecart.close()

@staticmethod
def check_order_at_db():
    litecart = mysql.connect(host='127.0.0.1',
                             user='root',
                             passwd='',
                             database='litecart')
    try:
        cursor = litecart.cursor()
        query = "SELECT * FROM `lc_orders`"
        cursor.execute(query)
        assert len(query) > 0, 'Error. Your order doesn\'t confirm!'
    finally:
        litecart.close()
