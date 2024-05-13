from parsing import getClients, getInstruments, getOrders
from validate import currency_check, instrument_check, lot_size_check, validate_all

clients = getClients("datasets/input_clients.csv")
instruments = getInstruments("datasets/input_instruments.csv")
orders = getOrders("datasets/input_orders.csv")

# examples of how to get data
print(clients["A"].clientId)
print(instruments["SIA"].currency)
print(orders["A2"].price)

position_dict = {}

for client in clients:
    position_dict[client] = 0


# test cases
valid_orders = validate_all(orders, position_dict, clients, instruments)
print(list(valid_orders.keys()))

assert list(valid_orders.keys()) == ['A1', 'B1', 'C1', 'E1', 'A2', 'B3', 'C3', 'B4', 'E2', 'B5', 'C4', 'B6', 'A3', 'E3']
