# ItemToPurchase class from Milestone 1
class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0, item_description = ''):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        
    def print_item_cost(self):
        print('{} \n                {} @ ${:.2f} = ${:.2f}'.format(self.item_name, self.item_quantity, self.item_price, self.total_cost()))
        
    def total_cost(self):
        return self.item_price * self.item_quantity
        
    def get_description(self):
        return '{}:\n              - {}'.format(self.item_name, self.item_description)
        
 
# ShoppingCart class from Milestone 2 
class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart = []
    
    def add_item(ItemToPurchase):
        # TO DO IN ASSIGNMENT 8
        print('    Adding Items...')
        print()
        return
        
    def remove_item(string):
        # TO DO IN ASSIGNMENT 8
        print('    Removing Items...')
        print()
        return
        
    def modify_item(ItemToPurchase):
        # TO DO IN ASSIGNMENT 8
        print('    Modifying Items...')
        print()
        return
        
    def get_num_items_in_cart(self):
        return sum([i.item_quantity for i in self.cart])
    
    def get_cost_of_cart(self):
        return sum([i.total_cost() for i in self.cart])
    
    def print_total(self):
        num_items = self.get_num_items_in_cart()
        print('          SHOPPING CART - CART CONTENTS')
        print('-------------------------------------------------')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items\'s: ', num_items)
        print('-------------------------------------------------')
        if num_items > 0:
            for item in self.cart:
                print('             ◊', end=' ')
                item.print_item_cost()
            print('\n              ********************')
            print('                 Total: ${:.2f}'.format(self.get_cost_of_cart()))
            print('              ********************')
        else:
            print('             SHOPPING CART IS EMPTY!')
        print()
        
    def print_descriptions(self):
        print('        SHOPPING CART - ITEM DESCRIPTIONS')
        print('-------------------------------------------------')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('-------------------------------------------------')
        num_items = self.get_num_items_in_cart()
        if num_items > 0:
            for item in self.cart:
                print('           ◊', end=' ')
                print(item.get_description())
        else:
            print('             SHOPPING CART IS EMPTY!')
        print()
    
    # Added for Testing Purposes    
    def add_random_items_for_testing(self):
        item1 = ItemToPurchase('Hot Dog', 2.00, 2, 'A sort of sandwhich')
        item2 = ItemToPurchase('Beats By Dre', 267.00, 1, 'Headphones by Dr Dre')
        item3 = ItemToPurchase('Eggs', 3.49, 12, 'Baby Chickens')
        self.cart.append(item1)
        self.cart.append(item2)
        self.cart.append(item3)
        
# main
    
def print_menu(cart):
    option = ''
    while option != 'q':
        print('''
                      MENU
    ----------------------------------------
        a - Add item to cart
        r - Remove item from cart
        c - Change item quantity
        i - Output items\' descriptions
        o - Output shopping cart
        q - Quit
    ----------------------------------------''')
        option = input('    Choose an option: ')
        print('\n')
        
        if option == 'a':
            cart.add_item()
        elif option == 'r':
            cart.remove_item()
        elif option == 'c':
            cart.modify_item()
        elif option == 'i':
            cart.print_descriptions()
        elif option == 'o':
            cart.print_total()
        elif option == 't':
            cart.add_random_items_for_testing()
        elif option != 'q':
            print('Invalid option, choose from the menu.')

def main():
    cart = ShoppingCart('Jimmy Johnson', 'Sept. 16th, 2024')
    print_menu(cart)
    

# Start Program
main()
    
