class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

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
        # Title: 30 chars, name centered, filled with *
        output = self.name.center(30, "*") + "\n"

        # Each ledger line: description (max 23, left) + amount (right, 7 wide, 2 decimals)
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            output += f"{desc:<23}{amt:>7}\n"

        output += f"Total: {self.get_balance():.2f}"
        return output


def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    # Compute spending per category (withdrawals only)
    spent = []
    for cat in categories:
        total = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)

    total_spent = sum(spent)

    # Percentages rounded down to nearest 10
    percents = []
    for s in spent:
        pct = 0 if total_spent == 0 else int((s / total_spent) * 100)
        pct = (pct // 10) * 10
        percents.append(pct)

    # Build chart lines (keep trailing spaces!)
    chart = title
    for y in range(100, -1, -10):
        line = f"{y:>3}| "
        for p in percents:
            line += "o  " if p >= y else "   "
        chart += line + "\n"

    # Horizontal line: 3 dashes per category + 1 extra (goes 2 chars past last bar area)
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical labels
    names = [cat.name for cat in categories]
    max_len = max(len(n) for n in names)

    for i in range(max_len):
        line = "     "
        for name in names:
            line += (name[i] if i < len(name) else " ") + "  "
        # IMPORTANT: no .rstrip() here, keep spacing exact
        chart += line + ("\n" if i != max_len - 1 else "")

    return chart


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

print(create_spend_chart(food, clothing))