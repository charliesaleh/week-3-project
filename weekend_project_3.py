# Welcome to Bigger Pockets

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def sum_list(self):
        current_node = self.head
        total = 0
        while current_node is not None:
            total += current_node.value
            current_node = current_node.next
        return total

class RentalProperty():
    def __init__(self, rental_income, laundry, storage, misc_income, tax, insurance, utilities, 
                 hoa, lawn_snow, vacancy, repairs, c, property_mortage,
                 mortgage, cash_flow_income, cash_flow_expenses, down_payment, closing_costs, rehab_budget, misc_other):
        self.income = LinkedList()
        self.expenses = LinkedList()
        self.cash_flow = LinkedList()
        self.roi = LinkedList()
        self.rental_income = rental_income
        self.laundry = laundry
        self.storage = storage
        self.misc_income = misc_income
        self.tax = tax
        self.insurance = insurance
        self.utilities = utilities
        self.hoa = hoa
        self.lawn_snow = lawn_snow
        self.vacancy = vacancy
        self.repairs = repairs
        self.c = c
        self.property_mortage = property_mortage
        self.mortgage = mortgage
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.misc_other = misc_other

    def add_income(self, value):
        self.income.add_node(value)
        total_income = self.laundry + self.storage + self.misc_income
        return total_income

    def add_expense(self, value):
        self.expenses.add_node(value)
        total_expenses = self.tax + self.insurance + self.utilities + self.hoa + self.lawn_snow + self.vacancy + self.repairs + self.c + self.property_mortage + self.mortgage
        return total_expenses
    
    def total_monthly_income(self):
        return self.income.sum_list()

    def total_monthly_expenses(self):
        return self.expenses.sum_list()

    def monthly_cash_flow(self):
        return self.total_monthly_income() - self.total_monthly_expenses()

    def cash_on_cash(self):
        total_costs = self.down_payment + self.closing_costs + self.rehab_budget + self.misc_other + (self.mortgage * 12)
        return (self.monthly_cash_flow() * 365) / total_costs

property = RentalProperty(2000, 0, 0, 0, 150, 100, 0, 0, 0, 100, 100, 100, 200, 860, 2000, 1610, 40000, 3000, 7000, 0)
property.add_income(2687)
property.add_expense(1610)
property.add_income(2291)
property.add_expense(1200)



print("Total monthly income: $", property.total_monthly_income())
print("Total monthly expenses: $", property.total_monthly_expenses())
print("Total monthly cash flow: $", property.monthly_cash_flow())
print("Total yearly cash on cash roi:", property.cash_on_cash(), "%")
