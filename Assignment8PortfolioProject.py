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
        
    def print_item(self):
        print('{} - {}\nX{} @ ${:.2f}'.format(self.item_name, self.item_description, self.item_quantity, self.item_price))
        
 
# ShoppingCart class from Milestone 2 
class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart = []
    
    def add_item(self, new_item):
        self.cart.append(new_item)
        print('The item: {} has been added to your cart.'.format(new_item.item_name))
        print('\n')
        return
        
    def remove_item(self, item_name):
        self.cart = [item for item in self.cart if item.item_name != item_name]
        print('The item: {} has been removed from your cart.'.format(item_name))
        print()
        return
        
    def modify_item(self, modified_item):
        for item in self.cart:
            if item.item_name == modified_item.item_name:
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                if modified_item.item_description != '':
                    item.item_description = modified_item.item_description
                print('\nItem has been modified.')
                item.print_item()
                print('\n')
                break
        else:
            print('\nThe item: {} was not found in the cart, nothing has been modified.\n\n'.format(modified_item.item_name))
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
        
# main
    
def print_menu(cart):
    option = ''
    while option != 'q':
        print('''
                      MENU
    ----------------------------------------
        a - Add item to cart
        r - Remove item from cart
        c - Change item price, quantity, and/or description
        i - Output items\' descriptions
        o - Output shopping cart
        q - Quit
    ----------------------------------------''')
        option = input('    Choose an option: ')
        print('\n')
        
        if option == 'a':
            print('ADD AN ITEM')
            item_name = input('Enter the name of the item to add:\n')
            item_description = input('Enter a description for the item:\n')
            item_price = float(input('Enter the price of the item:\n'))
            item_quantity = int(input('Enter how many of the item to add:\n'))
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(new_item)
        elif option == 'r':
            print('REMOVE AN ITEM')
            if len(cart.cart) == 0:
                print('The shopping cart is empty, Nothing to remove.\n\n')
            else:
                item_name = input('Enter the name of the item to remove:\n')
                cart.remove_item(item_name)
        elif option == 'c':
            print('MODIFY AN ITEM')
            if len(cart.cart) == 0:
                print('The shopping cart is empty, please add an item first.\n\n')
            else:
                item_name = input('What is the name of the item you would like to modify?\n')
                modify_choice = input('What would you like to modify (d - description, p - price, q - quantity, a - all, n - nevermind): \n')
                
                if modify_choice == 'd':
                    new_description = input('Enter the new description:\n')
                    modified_item = ItemToPurchase(item_name = item_name, item_description = new_description)
                elif modify_choice == 'p':
                    new_price = float(input('Enter the new price:\n'))
                    modified_item = ItemToPurchase(item_name = item_name, item_price = new_price)
                elif modify_choice == 'q':
                    new_quantity = int(input('Enter new new quantity:\n'))
                    modified_item = ItemToPurchase(item_name = item_name, item_quantity = new_quantity)
                elif modify_choice == 'a':
                    new_description = input('Enter the new description:\n')
                    new_price = float(input('Enter the new price:\n'))
                    new_quantity = int(input('Enter new new quantity:\n'))
                    modified_item = ItemToPurchase(item_name, new_price, new_quantity, new_description)
                elif modify_choice == 'n':
                    print('Going back to the main menu...\n\n')
                    continue
                else:
                    print('{} is not a valid choice, going back to the main menu...\n\n'.format(modify_choice))
                    continue
                    
                cart.modify_item(modified_item)
        elif option == 'i':
            cart.print_descriptions()
        elif option == 'o':
            cart.print_total()
        elif option != 'q':
            print('Invalid option, choose from the menu.')

def main():
    print('Hi! Welcome to your Shopping Cart.')
    name = input('To start, please enter your name: ')
    date = input('Thanks {}, what is today\'s date: '.format(name))
    print('\n')
    
    cart = ShoppingCart(name, date)
    print_menu(cart)
    

# Start Program
main()
    