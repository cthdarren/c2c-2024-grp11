from datetime import datetime
def LS_sort(queue:list, clientDict) -> list:
    return sorted(queue,key = lambda order:(float(order.price),
                                            clientDict[order.client].rating,
                                            datetime.strptime(order.time,'%H:%M:%S')))

def LB_sort(queue:list,clientDict) -> list:
    return sorted(queue,key = lambda order:(-float(order.price),
                                            clientDict[order.client].rating,
                                            datetime.strptime(order.time,'%H:%M:%S')))

def MS_sort(queue:list,clientDict) -> list:
    return sorted(queue,key = lambda order:(clientDict[order.client].rating,
                                            datetime.strptime(order.time,'%H:%M:%S')))
                  
def MB_sort(queue:list,clientDict) -> list:
    return sorted(queue,key = lambda order:(clientDict[order.client].rating,
                                            datetime.strptime(order.time,'%H:%M:%S')))
