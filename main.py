"""Aktualisierung von Lagerbeständen mit Transaktionen.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu05/aufgaben/args3
"""

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
    demo_inventory = {'Apfel': 10, 'Birne': 5}
    demo_transactions = [Transaction('Apfel', 3), Transaction('Birne', -2)]
    update_inventory(demo_inventory, *demo_transactions)
    print(demo_inventory)  # Erwarteter Output: {'Apfel': 13, 'Birne': 3}
