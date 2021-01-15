class Category():
    def __init__(self, category):
        self.category = category
        self.ledger = list()

    def __str__(self):
        title = f"{self.category.center(30, '*')}\n"
        items = ''
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" \
                     + f"{item['amount']:>7.2f}\n" 
            total += item['amount']
        return f"{title}{items}Total: {total}"

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:     
            return False

    def get_balance(self):
        current_bal = 0
        for item in self.ledger:
            current_bal += item['amount']
        return current_bal

    def transfer(self, amount, destination_category):
        destination_ledger = destination_category.ledger
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -amount, "description": f'Transfer to {destination_category.category}'})
            destination_ledger.append({"amount": amount, "description": f'Transfer from {self.category}'})
            return True
        else:
            return False
    
    def check_funds(self, amount):
        funds = 0
        for item in self.ledger:
            funds += item['amount']
        if funds - amount < 0:
            return False
        else:
            return True
        

def create_spend_chart(categories):
    return ''

# food = Category("Food")
# entertainment = Category("Entertainment")
# business = Category("Business")
