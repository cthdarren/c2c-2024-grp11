clientsfile = open("datasets/input_clients.csv")
instrumentsfile = open("datasets/input_instruments.csv")
ordersfile = open("datasets/input_orders.csv")

clientDict = {}
instrumentsDict = {}
ordersDict = {} 

firstLine = True

for clientline in clientsfile.readlines():
    if firstLine:
        firstLine = False
        continue
    if "\"" in clientline:
        clientarray = clientline.split("\"")
        position_and_rating = clientarray[2].split(",")

        clientId = clientarray[0]
        currencies = clientarray[1].split(",")
        positioncheck = position_and_rating[1]
        rating = position_and_rating[2].replace("\n","")

        clientDict[clientId] = {
            "currencies": currencies,
            "positioncheck": positioncheck,
            "rating": rating
        }
    else:
        clientarray = clientline.split(",")

        clientId = clientarray[0]
        currencies = clientarray[1].split(",")
        positioncheck = clientarray[2]
        rating = clientarray[3].replace("\n","")

        clientDict[clientId] = {
            "currencies": currencies,
            "positioncheck": positioncheck,
            "rating": rating
        }

firstLine = True
for orderline in ordersfile.readlines():
    if firstLine:
        firstLine = False
        continue
    orderarray = orderline.split(",")

    ordertime = orderarray[0]
    orderId = orderarray[1]
    instrument = orderarray[2]
    qty = orderarray[3]
    clientId = orderarray[4]
    price = orderarray[5]
    side = orderarray[6].replace("\n","")

    ordersDict[orderId] = {
        "orderTime": ordertime,
        "clientId": ordertime,
        "instrument": ordertime,
        "side": side,
        "price": ordertime,
        "quantity": ordertime
    }

print(ordersDict)
