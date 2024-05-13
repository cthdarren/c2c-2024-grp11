from parsing import getClients, getInstruments, getOrders
from validate import currency_check, instrument_check, lot_size_check, validate_all, validate_all_single
from classes import Order

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

exchange_report = "OrderID, RejectionReason\n"
# test cases
result_single = []
for x in orders.values():
    tempres = validate_all_single(x, position_dict, clients, instruments)
    if tempres != True:
        exchange_report += x.orderId + "," + tempres + "\n"

print(exchange_report)
valid_orders = validate_all(orders, position_dict, clients, instruments)
print(list(valid_orders.keys()))

assert validate_all_single(Order("Z1", "09:00:00", "A", "SIA", "Buy", "Market", "101"), position_dict, clients, instruments) == False
assert validate_all_single(Order("Z2", "09:02:00", "A", "SIA", "Buy", "Market", "1000"), position_dict, clients, instruments) == True 
assert validate_all_single(Order("Z3", "09:03:00", "A", "SIA", "Sell", "Market", "101"), position_dict, clients, instruments) == False
assert validate_all_single(Order("Z4", "09:04:00", "B", "SIA", "Sell", "Market", "100"), position_dict, clients, instruments) == True
assert validate_all_single(Order("Z5", "09:05:00", "A", "SIA", "Sell", "Market", "100"), position_dict, clients, instruments) == False
