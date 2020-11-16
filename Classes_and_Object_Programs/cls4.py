class Products:

    # object as arg - 2 default arg 
    def __init__(self,item,quantity,productList = {}):
        self.item = item
        self.quantity = quantity
        self.productList = productList

    def addProducts(self):
        self.productList[self.item] = self.quantity
        return self.productList


p = Products('Shampoo', 2)
print(p.addProducts())
p = Products('Soap', 2)
print(p.addProducts())



        
