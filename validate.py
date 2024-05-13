# 1. take in 3 objects
# 2. validate the csv against each other
# 3. put into 4 priority queues and return 

from position_dictionary import position_dict, initialize_dict

# split poilcy checks into 4 different functions that check 4 different policies
def instrument_check(orders_dict, instruments_dict):

    # takes in orders and instruments CSV
    # checks if the orders instruments field is in the instruments CSV

    res = {
       key : val for key, val in orders_dict.items() 
       if val.instrument in instruments_dict.keys()
    }

    return res

def currency_check(orders_dict, instruments_dict, clients_dict):
    # assuming we take in res from instrument_check as orders_dict
    # takes in orders, clients and instruments CSV
    # Checks if the client's currency is correct for the instrument

    res = {}

    for key, value in orders_dict.items():
        instrument = value.instrument # get instrument field from orders csv
        client = value.client # get client field from orders csv
        instrument_currency = instruments_dict[instrument].currency # get instrument currency
        order_currencies = clients_dict[client].currencies # get list of client currencies
        
        if instrument_currency in order_currencies:
            res[key] = value
         
    return res

def lot_size_check(orders_dict, instruments_dict):
    # takes in orders, and instruments CSV
    # checks if the order's order size is a multiple of the lot size ie modulo = 0

    res = {}
    
    for key, value in orders_dict.items():
        quantity = int(value.quantity)
        instrument = value.instrument
        lot_size = int(instruments_dict[instrument].lotSize)
        if quantity % lot_size == 0:
            res[key] = value

    return res

def position_check(orders_dict, positions_dict, clients_dict):
    # everyone starts with 0
    # only N position check can short sell
    # Y position check must have enough
    # assume we have the positions dictionary
    
    # first check if Y or N. if Y then we check if has enough qty
    # if N then we check qty
    # return all those valid in a dict

    def amount_check(positions_dict, clientId, sell_amount):
        # remember positions dict is a simple dictionary not object of objects
        if positions_dict[clientId] < int(sell_amount):
            return False
        return True

    res = {}

    for key, value in orders_dict.items():
        client = value.client
        sell_amount = value.quantity
        
        if clients_dict[client].positioncheck == "N":
            res[key] = value
        elif clients_dict[client].positioncheck == "Y":
            if value.side == "Sell":
                if amount_check(positions_dict, client, sell_amount):
                    res[key] = value
            else:
                res[key] = value

    return res

# split poilcy checks into 4 different functions that check 4 different policies
def instrument_check_single(order, instruments_dict):

    # takes in order and instruments CSV
    return order.instrument in instruments_dict.keys()

def currency_check_single(order, instruments_dict, clients_dict):
    # assuming we take in res from instrument_check as orders_dict
    # takes in orders, clients and instruments CSV
    # Checks if the client's currency is correct for the instrument

    res = {}

    instrument = order.instrument # get instrument field from orders csv
    client = order.client # get client field from orders csv
    instrument_currency = instruments_dict[instrument].currency # get instrument currency
    client_currencies = clients_dict[client].currencies # get list of client currencies
    
    return instrument_currency in client_currencies
         

def lot_size_check_single(order, instruments_dict):
    # takes in orders, and instruments CSV
    # checks if the order's order size is a multiple of the lot size ie modulo = 0

    res = {}

    quantity = int(order.quantity)
    instrument = order.instrument
    lot_size = int(instruments_dict[instrument].lotSize)

    return quantity % lot_size == 0

def position_check_single(order, positions_dict, clients_dict):
    # everyone starts with 0
    # only N position check can short sell
    # Y position check must have enough
    # assume we have the positions dictionary
    
    # first check if Y or N. if Y then we check if has enough qty
    # if N then we check qty
    # return all those valid in a dict

    def amount_check_single(positions_dict, clientId, sell_amount):
        # remember positions dict is a simple dictionary not object of objects
        if positions_dict[clientId] < int(sell_amount):
            return False
        return True

    client = order.client
    sell_amount = order.quantity
    
    if clients_dict[client].positioncheck == "N":
        return True
    elif clients_dict[client].positioncheck == "Y":
        if order.side == "Sell":
            return amount_check_single(positions_dict, client, sell_amount)
        else:
            return True

    # invalid positioncheck value
    return False


def validate_all(orders_dict, positions_dict, clients_dict, instruments_dict):
    orders_dict = instrument_check(orders_dict, instruments_dict)
    orders_dict = currency_check(orders_dict, instruments_dict, clients_dict)
    orders_dict = lot_size_check(orders_dict, instruments_dict)
    orders_dict = position_check(orders_dict, positions_dict, clients_dict)
    return orders_dict

def validate_all_single(order, positions_dict, clients_dict, instruments_dict):
    if instrument_check_single(order, instruments_dict) == False:
        return "REJECTED - INSTRUMENT NOT FOUND"
    if currency_check_single(order, instruments_dict, clients_dict) == False:
        return "REJECTED - MISMATCH CURRENCY"
    if lot_size_check_single(order,instruments_dict) == False:
        return "REJECTED - INVALID LOT SIZE"
    if position_check_single(order, positions_dict, clients_dict) == False:
        return "REJECTED - POSITION CHECK FAILED"
    return True

