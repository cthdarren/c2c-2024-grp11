from sorting import LS_sort, LB_sort, MS_sort, MB_sort 
import datetime

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

class ClientInstrument:
    def __init__(self, instrumentId, clientId, position):
        self.instrumentId = instrumentId
        self.clientId = clientId
        self.position = position

class Book:
    def __init__(self, instrumentDict, orderDict, clientDict, instrumentId):
        self.instrument = instrumentDict[instrumentId]
        self.orderDict = orderDict
        self.clientDict = clientDict
        self.create_queues()
    
    def create_queues(self, LS_sort=LS_sort, LB_sort=LB_sort, MS_sort=MS_sort, MB_sort=MB_sort):
        self.LS = PQueue(LS_sort,self.clientDict)
        self.LB = PQueue(LB_sort,self.clientDict)
        self.MS = PQueue(MS_sort,self.clientDict)
        self.MB = PQueue(MB_sort,self.clientDict)
    
    def insert_order(self,order):
        if order.instrument != self.instrument.instrumentId:
            return 
        if order.side == 'Buy':
            if order.price == 'Market':
                self.MB.insert(order)
                print(f"{vars(order)} inserted in Market Buy")
            else:
                self.LB.insert(order)
                print(f"{vars(order)} inserted in Limit Buy")
        elif order.side == 'Sell':
            if order.price == 'Market':
                self.MS.insert(order)
                print(f"{vars(order)} inserted in Market Sell")
            else:
                self.LS.insert(order)
                print(f"{vars(order)} inserted in Limit Sell")
                
    
class PQueue:
    def __init__(self, sorting_func, clientDict):
        self.queue = []
        self.sort = sorting_func
        self.clientDict = clientDict
    
    def insert(self, order):
        self.queue.append(order)
        self.queue = self.sort(self.queue,self.clientDict)
        
