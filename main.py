from parsing import getClients, getInstruments, getOrders
from validate import currency_check, instrument_check

clients = getClients("datasets/input_clients.csv")
instruments = getInstruments("datasets/input_instruments.csv")
orders = getOrders("datasets/input_orders.csv")


# example of how to get data
# print(clients["A"]["currencies"])
# print(instruments["SIA"]["lotsize"])
# print(orders["A2"]["price"])

# example of check instrument validation
# print(instrument_check(orders, instruments))

# example of check currency validation
print(currency_check(orders, instruments, clients))
