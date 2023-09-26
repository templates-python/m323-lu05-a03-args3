class Transaction:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

def update_inventory(inventory, *transactions):
    """Updates the inventory based on the provided transactions."""
    for transaction in transactions:
        if transaction.product in inventory:
            inventory[transaction.product] += transaction.quantity
        else:
            inventory[transaction.product] = transaction.quantity

if __name__ == '__main__':
    # Teste deine Funktion
    inventory = {'Apfel': 10, 'Birne': 5}
    transactions = [Transaction('Apfel', 3), Transaction('Birne', -2)]
    update_inventory(inventory, *transactions)
    print(inventory)  # Erwarteter Output: {'Apfel': 13, 'Birne': 3}