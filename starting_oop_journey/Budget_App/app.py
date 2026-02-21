class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
       
        
        # The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True
    
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, other_category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {other_category.name}")
        other_category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*")
        lines = [title]

        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            lines.append(f"{desc}{amt}")
        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)



        


def create_spend_chart(categories):
    # total spent per category (withdraw only)
    spent = []
    for cat in categories:
        cat_spent = sum(-item["amount"] for item in cat.ledger if item["amount"])
        spent.append(cat_spent)
    
    total_spent = sum(spent)

    # percentages rounded Down to nearest 10
    percents = []
    for s in spent:
        pct = 0 if total_spent == 0 else int((s / total_spent) * 100)
        pct = (pct // 10) * 10
        percents.append(pct)

    lines = ["Percentage spent by category"]

    # chart bars
    lines.append("   " + "-" * len(categories) + 1)

    # vertical labels
    names = [cat.name for cat in categories]
    max_len = max(len(n) for n in names)

    for i in range(max_len):
        line = "   "
        for n in names:
            line += (n[i] if i < len(n) else "") + " "
        lines.append(line.rstrip)

    return "\n".join(lines)


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

print(create_spend_chart(food, clothing))