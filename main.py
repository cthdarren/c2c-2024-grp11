from parsing import getClients, getInstruments, getOrders
from validate import currency_check, instrument_check, lot_size_check, validate_all, validate_all_single
from classes import Order, ClientInstrument
from datetime import datetime

clients = getClients("datasets/input_clients.csv")
instruments = getInstruments("datasets/input_instruments.csv")
orders = getOrders("datasets/input_orders.csv")

# examples of how to get data
print(clients["A"].clientId)
print(instruments["SIA"].currency)
print(orders["A2"].price)

position_dict = {}

for instrument in instruments:
    temp = {}
    for client in clients:
        temp[client] = 0
        position_dict[instrument] = temp

exchange_report = "OrderID, RejectionReason\n"
client_report = "ClientID, InstrumentID, NetPosition\n"
instrument_report = "InstrumentID, OpenPrice, ClosePrice, TotalVolume, VWAP, DayHigh, DayLow\n"

result_single = []
for x in orders.values():
    tempres = validate_all_single(x, position_dict, clients, instruments)
    if tempres != True:
        exchange_report += x.orderId + "," + tempres + "\n"

for x in position_dict:
    print(x + ": ", end = "")
    print(position_dict[x])
print(exchange_report)

# test cases
# valid_orders = validate_all(orders, position_dict, clients, instruments)
# print(list(valid_orders.keys()))

assert validate_all_single(Order("Z1", "09:00:00", "A", "SIA", "Buy", "Market", "101"), position_dict, clients, instruments) != True 
assert validate_all_single(Order("Z2", "09:02:00", "A", "SIA", "Buy", "Market", "1000"), position_dict, clients, instruments) == True 
assert validate_all_single(Order("Z3", "09:03:00", "A", "SIA", "Sell", "Market", "101"), position_dict, clients, instruments) != True
assert validate_all_single(Order("Z4", "09:04:00", "B", "SIA", "Sell", "Market", "100"), position_dict, clients, instruments) == True
assert validate_all_single(Order("Z5", "09:05:00", "A", "SIA", "Sell", "Market", "100"), position_dict, clients, instruments) != True
