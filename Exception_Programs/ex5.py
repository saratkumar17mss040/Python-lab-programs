class OutofProductsException(Exception):
    pass

def productException(numberOfProducts):
    try:
        if numberOfProducts < 100:
            print("Products our available in our market !")
        else:
            raise OutofProductsException
    except OutofProductsException:
            print('Out of products in our market !')
              


numberOfProducts = int(input('Enter number of products to buy:'))
productException(numberOfProducts)

