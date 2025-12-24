class Shop:
    
    def __init__(self,item_name, item_quantity, item_price):   #intializes item details when object is created
        self.item_name = item_name   #name of item     
        self.item_quantity = item_quantity  #quantity of item
        self.item_price = item_price    #price of the item 
       
    def add_item(self, added_quantity):   #to add more quantity to item
        self.item_quantity += added_quantity
        #return self.item_quantity   #no need because we are just updating the value
    
    #to calculate total value of items
    def total_value(self):
        return self.item_quantity * self.item_price

#creating an object of Shop class    
item1 = Shop("Book", 10, 30)
print(item1.item_quantity)
item1.add_item(10)   #passing the argument to add quantity of item

print(item1.item_name)
print(item1.item_quantity)
print(item1.item_price)
print(item1.total_value())
        