    
from factory import factorytransporte

def main():
    transporte1= factorytransporte.get_transporte("barco","corolla")
    transporte2=factorytransporte.get_transporte("camion","susuki")
    transporte1.entrega()
    transporte2.entrega()

main()    