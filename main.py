from parsing import getClients, getInstruments, getOrders
from classes import Client

clients = getClients("datasets/input_clients.csv")
instruments = getInstruments("datasets/input_instruments.csv")
orders = getOrders("datasets/input_orders.csv")


print(clients["A"].clientId)
print(instruments["SIA"].currency)
print(orders["A2"].price)
# example of how to get data
