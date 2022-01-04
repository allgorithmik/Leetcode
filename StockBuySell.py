def stockBuySell(lis) -> int:
    buy_index = lis.index(min(lis))
    buy_value = lis[buy_index]
    new_lis = lis[buy_index : ]
    sell_index = new_lis.index(max(new_lis))
    sell_value = new_lis[sell_index]
    return sell_value - buy_value


stockBuySell() #Pass list with integer values