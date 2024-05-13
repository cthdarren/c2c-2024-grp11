class Order:
    def __init__(self, orderId, time, client, instrument, side, price, quantity):
        self.orderId = orderId
        self.time = time
        self.client = client 
        self.instrument = instrument
        self.side = side
        self.price = price
        self.quantity = quantity
        
class Instrument:
    def __init__(self, instrumentId, currency, lotSize):
        self.instrumentId = instrumentId 
        self.currency = currency
        self.lotSize = lotSize 

class Client:
    def __init__(self, clientId, currencies, positioncheck, rating):
        self.clientId = clientId
        self.currencies = currencies 
        self.positioncheck = positioncheck
        self.rating = rating


    def getClientId(self):
        return self.clientId
