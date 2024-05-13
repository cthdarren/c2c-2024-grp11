# do validation on each new trade (darren's update)

# then carry out trades

### trading algorithm ###

# we should add all orders to the book first
# then check the book for matching order prices

# if no matches, move on to the next line to add

# if match, fulfil order
# -> assuming its a buy order @ 32.2
# -> first reduce the sell orders from the lowest price up to the matched price
# -> clear all from the lowest sell order in the book first 
# -> you are left with either remainder in the sell or remainder in the buy
### we are not considering market order at this stage (cell 10 in the workbook)

# (cell 11)
# 1. add it to the book (market, sell, 100)
# 2. we know that there are no matching prices right now, so we can start considering the highest buy price / or lowest sell price conversely
# 3. so we sell 100 or the highest bid price in the book
# 4. and we keep selling at decreasing prices as long as it clears
# 5. we update the final book according to the remainder

# (cell 12)
# add at the same price / just add another row bruh

from classes import Book
from validate import validate_all_single

def add_order(new_order, positions_dict, clients_dict, instruments_dict):
    # validate order function if pass then 
    # add row to the book
    validate_all_single(new_order, positions_dict, clients_dict, instruments_dict)
    Book.insert_order(new_order)

def time_check(new_order):
    if time_past 1600 hours:
        return False
    return True

def process_order(new_order, positions_dict, clients_dict, instruments_dict):
    add_order(new_order, positions_dict, clients_dict, instruments_dict)
    time_pass = time_check(new_order)
    # check if ask price more than bid prices, if it is do nothing
    if !time_pass:
        if limit order:
            if the_new_order.price > bid_prices:
                continue
            else the_new_order_price <= bid_prices:
                update existing buy orders upwards from the matched price (and the new order)
        
            # do the same bid order (limit)
            if the_new_order.price < ask prices:
                continue
            elif the new order.price >= ask prices:
                update exisitng sell orders downwards from the matched price (and the new order)

        ## market sell order
        if market order:
            if market_order is a sell:
                start clearing the buy orders from the highest price (and update the market order qty)
            if market_order is a buy:
                start clearing the sell orders from the lowest price (and update the market order qty)

    # i can return nothing as i modify the Book in place

