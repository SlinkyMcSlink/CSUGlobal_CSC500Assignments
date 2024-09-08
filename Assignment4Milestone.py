# Portfolio Milestone - Week 4 Assignment

# Part One - Build a ItemToPurchase class
class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        
    def print_item_cost(self):
        print('{} {} @ ${:.2f} = ${:.2f}'.format(self.item_name, self.item_quantity, self.item_price, self.total_cost()))
        
    def total_cost(self):
        return self.item_price * self.item_quantity
        

# Part Two - Prompt user for two items and create two objects of the class
item1_name = input('Please enter the item name:\n')
item1_price = float(input('Please enter the item price:\n'))
item1_quantity = int(input('How many of these items are there?\n'))

item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)
print('Item created: ')
item1.print_item_cost()

item2_name = input('\nPlease enter another item name:\n')
item2_price = float(input('Please enter the item price:\n'))
item2_quantity = int(input('How many of these items are there?\n'))

item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)
print('Item created: ')
item2.print_item_cost()

print()

# Part Three - Add together and print total
print('\nTOTAL COST')
item1.print_item_cost()
item2.print_item_cost()
print('Total: ${:.2f}'.format(item1.total_cost() + item2.total_cost()))

