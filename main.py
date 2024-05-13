from parsing import getClients, getInstruments, getOrders

clients = getClients("datasets/input_clients.csv")
instruments = getInstruments("datasets/input_instruments.csv")
orders = getOrders("datasets/input_orders.csv")


# example of how to get data
print(clients["A"]["currencies"])
print(instruments["SIA"]["lotsize"])
print(orders["A2"]["price"])
