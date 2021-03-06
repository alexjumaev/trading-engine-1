'''
Project: Trading Engine
Author: Adish Jain
Date: 11/16/2018
'''
import falcon
from database import Database
from get_orders import GetOrders


APP = falcon.API()

db = Database()
get_new_orders = GetOrders(db, APP)

APP.add_route('/orders', get_new_orders)
