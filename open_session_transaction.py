def open_session(Book):
    mkt_bid_qty = 0
    mkt_sell_qty = 0
    max_price = 0
    if Book.MB:
        for item in Book.MB:
            mkt_bid_qty += item.quantity
        for item in Book.LS:
            if item.quantity <= mkt_bid_qty:
                Book.LS.pop(0)
                mkt_bid_qty -= item.quantity
                if mkt_bid_qty == 0:
                    Book.MB.pop(0)
            else:
                item.quantity -= mkt_bid_qty
            max_price = item.price
    if Book.MS:
        for item in Book.MS:
            mkt_sell_qty += item.quantity
        for item in Book.LB:
            if item.quantity <= mkt_sell_qty:
                Book.LB.pop(0)
                mkt_sell_qty -= item.quantity
                if mkt_sell_qty == 0:
                    Book.MS.pop(0)
            else:
                item.quantity -= mkt_sell_qty
            max_price = max(max_price, item.price)


def open_session2(Book):
    LB_price = [item.price for item in Book.LB]
    LS_price = [item.price for item in Book.LS]
    
    min_ls = {}

    prices = LB_price + LS_price
    prices = list(set(prices))     

    for price in prices:
        if price not in LS_price:
            continue
        else:
            mkt_qty = 0
            for item in Book.MB:
                mkt_qty += item.quantity
            min_ls[price] += min(Book.LS.queue[0].quantity, mkt_qty)