from classes import Client, Instrument, Order

def getClients(filename):
    clientsDict = {}
    clientsfile = open(filename)

    firstLine = True
    for clientline in clientsfile.readlines():
        if firstLine:
            firstLine = False
            continue
        if "\"" in clientline:
            clientarray = clientline.split("\"")
            position_and_rating = clientarray[2].split(",")

            clientId = clientarray[0].replace(",","")
            currencies = clientarray[1].split(",")
            positioncheck = position_and_rating[1]
            rating = position_and_rating[2].replace("\n","")

        else:
            clientarray = clientline.split(",")

            clientId = clientarray[0]
            currencies = clientarray[1].split(",")
            positioncheck = clientarray[2]
            rating = clientarray[3].replace("\n","")

        clientsDict[clientId] = Client(clientId, currencies, positioncheck, rating)

    return clientsDict

def getOrders(filename):
    ordersDict = {} 
    ordersfile = open(filename)

    firstLine = True
    for orderline in ordersfile.readlines():
        if firstLine:
            firstLine = False
            continue
        orderarray = orderline.split(",")

        ordertime = orderarray[0]
        orderId = orderarray[1].replace(",","")
        instrument = orderarray[2]
        qty = orderarray[3]
        clientId = orderarray[4]
        price = orderarray[5]
        side = orderarray[6].replace("\n","")

        ordersDict[orderId] = Order(orderId, ordertime, clientId, instrument, side, price, qty)

    return ordersDict

def getInstruments(filename):
    instrumentsDict = {}
    instrumentsfile = open(filename)
    firstLine = True
    for instrumentline in instrumentsfile.readlines():
        if firstLine:
            firstLine = False
            continue
        instrumentarray = instrumentline.split(",")

        instrumentId = instrumentarray[0]
        currency = instrumentarray[1]
        lotSize = instrumentarray[2].replace("\n","")

        instrumentsDict[instrumentId] = Instrument(instrumentId, currency, lotSize)
    return instrumentsDict
