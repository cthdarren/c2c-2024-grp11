# 1. take in 3 objects
# 2. validate the csv against each other
# 3. put into 4 priority queues and return 

# split poilcy checks into 4 different functions that check 4 different policies
def instrument_check(orders_dict, instruments_dict):

    # takes in orders and instruments CSV
    # checks if the orders instruments field is in the instruments CSV

    res = {key : val for key, val in orders_dict.items() 
           if val["instrument"] in instruments_dict.keys()}

    return res

def currency_check(orders_dict, instruments_dict, clients_dict):
    # assuming we take in res from instrument_check as orders_dict
    # takes in orders, clients and instruments CSV
    # Checks if the client's currency is correct for the instrument

    res = {}

    for key, value in orders_dict.items():
        instrument = value["instrument"] # get instrument field from orders csv
        client = value["clientId"] # get client field from orders csv
        instrument_currency = instruments_dict[instrument]["currency"] # get instrument currency
        order_currencies = clients_dict[client]["currencies"] # get list of client currencies
        
        if instrument_currency in order_currencies:
            res[key] = value
         
    return res

def lot_size_check():
    # takes in orders, and instruments CSV
    # checks if the order's order size is a multiple of the lot size ie modulo = 0
    pass

def position_check():
    # everyone starts with 0
    # only N position check can short sell
    # Y position check must have enough
    # assume we have the positions dictionary
    pass