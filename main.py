from parsing import getClients, getInstruments, getOrders
from validate import currency_check, instrument_check, lot_size_check, validate_all, validate_all_single
from classes import Order, ClientInstrument, Book
from datetime import datetime

clients = getClients("datasets/input_clients.csv")
instruments = getInstruments("datasets/input_instruments.csv")
orders = getOrders("datasets/input_orders.csv")

# examples of how to get data
print(clients["A"].clientId)
print(instruments["SIA"].currency)
print(orders["A2"].price)

position_dict = {}
instrument_books = {}

for instrument in instruments:
    instrument_books[instrument] = Book(instruments, orders, clients, "SIA")
    temp = {}
    for client in clients:
        temp[client] = 0
        position_dict[instrument] = temp

exchange_report = "OrderID, RejectionReason\n"
client_report = "ClientID, InstrumentID, NetPosition\n"
instrument_report = "InstrumentID, OpenPrice, ClosePrice, TotalVolume, VWAP, DayHigh, DayLow\n"


result_single = []

cont_trading = False

for curr_order in orders.values():
    tempres = validate_all_single(curr_order, position_dict, clients, instruments)
    if tempres != True:
        exchange_report += curr_order.orderId + "," + tempres + "\n"
    else:
        instrument_books[curr_order.instrument].insert_order(curr_order)
        
        # Open auction
        if datetime.strptime(curr_order.time,'%H:%M:%S') >= datetime.strptime('9:00:00','%H:%M:%S') and datetime.strptime(curr_order.time,'%H:%M:%S') < datetime.strptime('9:30:00','%H:%M:%S'):
            siaBook.insert_order(curr_order)  
        
        # Continuous trading
        elif datetime.strptime(curr_order.time,'%H:%M:%S') < datetime.strptime('16:00:00','%H:%M:%S'):
            # Execute this for the first order in the continuous trading session
            if cont_trading == False: 
                siaBook.execute_auction()
                cont_trading = True
            siaBook.insert_order(curr_order)
            siaBook.execute_cont()
            
        # Close auction
        elif datetime.strptime(curr_order.time,'%H:%M:%S') < datetime.strptime('16:10:00','%H:%M:%S'):
            siaBook.insert_order(curr_order)
        siaBook.execute_auction()

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
