import pprint
import unittest


class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def __repr__(self) -> str:
        return f"{self.name:*^30}\n" + "\n".join([f"{item['description'][:23]:23}{item['amount']:>7.2f}" for item in self.ledger]) + f"\nTotal: {self.get_balance():.2f}"
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if amount > self.get_balance():
            return False
        else:
            self.deposit(-amount, description)
            return True
    
    def get_balance(self):
        return sum([item["amount"] for item in self.ledger])
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    
    def check_funds(self, amount):
        return self.get_balance() >= amount

def create_spend_chart(categories):
    to_return = "Percentage spent by category\n"
    percentages = []
    total_spent_all_categories = 0
    for category in categories:
        total_spent_all_categories += sum([item["amount"] for item in category.ledger if item["amount"] < 0])
    for category in categories:
        total_spent_by_category = sum([item["amount"] for item in category.ledger if item["amount"] < 0])
        percentages_spent_by_category = round(total_spent_by_category/total_spent_all_categories*100)
        percentages.append(percentages_spent_by_category)
    for i in range(100, -1, -10):
        to_return += f"{i:>3}|"
        for percentage in percentages:
            if percentage >= i:
                to_return += " o "
            else:
                to_return += "   "
        if i == 0:
            to_return+=" "
        if i > 0:
            to_return += " \n"
    to_return += f"\n{' '*4}{'---'*len(percentages)}-\n"
    for i in range(max([len(category.name) for category in categories])):
        to_return += f"{' '*4}"
        for category in categories:
            if i < len(category.name):
                to_return += f" {category.name[i]} "
            else:
                to_return += "   "
        to_return += " \n" if i < max([len(category.name) for category in categories])-1 else " "
    return to_return

if __name__ == "__main__":
    unittest.main(module='test', exit=False)