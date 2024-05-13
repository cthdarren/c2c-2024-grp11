from parsing import getClients, getInstruments, getOrders
from classes import Client
from validate import currency_check, instrument_check, lot_size_check
from position_dictionary import position_dict

clients = getClients("datasets/input_clients.csv")
instruments = getInstruments("datasets/input_instruments.csv")
orders = getOrders("datasets/input_orders.csv")


print(clients["A"].clientId)
print(instruments["SIA"].currency)
print(orders["A2"].price)
# example of how to get data
# print(clients["A"]["currencies"])
# print(instruments["SIA"]["lotsize"])
# print(orders["A2"]["price"])

# example of check instrument validation
# print(instrument_check(orders, instruments))

# example of check currency validation
# print(currency_check(orders, instruments, clients))

# example of check lot size validation
# print(lot_size_check(orders, instruments))

# example of check position validation
# print(position_check(orders, position_dict, clients))

# example 
valid_orders = validate_all(orders, position_dict, clients, instruments)
print(valid_orders)