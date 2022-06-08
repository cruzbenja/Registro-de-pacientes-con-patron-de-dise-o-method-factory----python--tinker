def getOrderTotal(order,pais):
    total=0
    for item in order:
        total= total + item['precio']* item ['cantidad']
    

    if(pais == "BO"):
        total += total * 0.13 
    elif(pais == "EU"):
        total += total * 0.20 
    return total  
          

productos=[{'precio':500,'cantidad':7, 'nombre':'impresora'},
{'precio':100, 'cantidad':3, 'nombre':'flash memory 15bg'},
{'precio':35, 'cantidad':9, 'nombre':'microfono huavi sencillo'}]
pais="BO"
print(getOrderTotal(productos,pais))