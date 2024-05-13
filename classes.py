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
                
    def execute_cont(self,order,position_dict):
        for MBorder in self.MB.queue:
            # Check limit orders until MBorder quantity runs out
            for LSorder in self.LS.queue:
                if MBorder.quantity > LSorder.quantity: # Limit sell order is less than market buy
                    # update MB order quantity
                    MBorder.quantity = MBorder.quantity - LSorder.quantity 
                    # update LS priority queue
                    self.LS.queue.pop(0)
                    # update position
                    position_dict[MBorder.instrument][MBorder.client] += LSorder.quantity
                    position_dict[MBorder.instrument][LSorder.client] -= LSorder.quantity

                elif MBorder.quantity < LSorder.quantity:
                    # update LS order quantity
                    LSorder.quantity = LSorder.quantity - MBorder.quantity
                    # update MB priority queue
                    self.MB.queue.pop(0)
                    # update position
                    position_dict[MBorder.instrument][MBorder.client] += MBorder.quantity
                    position_dict[MBorder.instrument][LSorder.client] -= MBorder.quantity
                    
                else: # equal
                    # update MB priority queue
                    self.MB.queue.pop(0)
                    # update LS priority queue
                    self.LS.queue.pop(0)
                    # update position
                    position_dict[MBorder.instrument][MBorder.client] += LSorder.quantity
                    position_dict[MBorder.instrument][LSorder.client] -= LSorder.quantity
                    
        for MSorder in self.MS.queue:
            # Check limit orders until MSorder quantity runs out
            for LBorder in self.LB.queue:
                if MSorder.quantity > LBorder.quantity: # Limit sell order is less than market buy
                    # update MB order quantity
                    MSorder.quantity = MSorder.quantity - LBorder.quantity 
                    # update LS priority queue
                    self.LB.queue.pop(0)
                    # update position
                    position_dict[MSorder.instrument][MSorder.client] += LBorder.quantity
                    position_dict[MSorder.instrument][LBorder.client] -= LBorder.quantity

                elif MSorder.quantity < LBorder.quantity:
                    # update LB order quantity
                    LSorder.quantity = LSorder.quantity - MBorder.quantity
                    # update MS priority queue
                    self.MS.queue.pop(0)
                    # update position
                    position_dict[MSorder.instrument][MSorder.client] += MSorder.quantity
                    position_dict[MSorder.instrument][LBorder.client] -= MSorder.quantity
                    
                else: # equal
                    # update MS priority queue
                    self.MS.queue.pop(0)
                    # update LB priority queue
                    self.LB.queue.pop(0)
                    # update position
                    position_dict[MSorder.instrument][MSorder.client] += LBorder.quantity
                    position_dict[MSorder.instrument][LBorder.client] -= LBorder.quantity
                

class PQueue:
    def __init__(self, sorting_func, clientDict):
        self.queue = []
        self.sort = sorting_func
        self.clientDict = clientDict
    
    def insert(self, order):
        self.queue.append(order)
        self.queue = self.sort(self.queue,self.clientDict)
        
