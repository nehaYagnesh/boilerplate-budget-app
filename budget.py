class Category():
    instances = []
    def __init__(self, category):
        self.category = category
        self.ledger = []

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
    
    def get_withdrawals(self):
        withdraw_total = 0
        for item in self.ledger:
            if item['amount'] < 0:
                withdraw_total += item['amount']
        return withdraw_total

def truncate(n):
    return int(n * 10) / 10  # where 10 is the multiplier

def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawals()
        breakdown.append(category.get_withdrawals())
    #Breakdown of spending rounded down to nearest 10th
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded

def create_spend_chart(categories):
    result_str = 'Percentage spent by category\n'
    count = 100
    totals = getTotals(categories)
    while count >= 0:
        cat_display = ' '
        for total in totals:
            if total * 100 >= count:
                cat_display += 'o  '
            else:
                cat_display += '   '
        result_str += str(count).rjust(3) + "|" + cat_display + ("\n")
        count -= 10
    
    dashes_line = '-' + '---'*len(categories)
    cat_names = []
    x_axis = ''
    for cat in categories:
        cat_names.append(cat.category)
    longest_cat = max(cat_names, key = len)
    
    for x in range(len(longest_cat)):
        nameStr = '     '
        for cat_name in cat_names:
            if x >= len(cat_name):
                nameStr += '   '
            else:
                nameStr += cat_name[x] + '  '
        if x < len(longest_cat) - 1:
            nameStr += '\n'
        x_axis += nameStr        
    result_str += dashes_line.rjust(len(dashes_line)+4) + '\n' + x_axis
    return result_str