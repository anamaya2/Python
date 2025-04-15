class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def get_name(self):
        return self.name
    
    def get_number(self):
        return self.number
    
    def set_name(self, name):
        self.name = name

    def set_number(self, number):
        self.number = number

class ProductionWorker(Employee):
    def __init__(self, name, number, shift, pay_rate):
        super().__init__(name, number)
        self.shift = shift
        self.pay_rate = pay_rate

    def get_shift(self):
        return self.shift
    
    def get_pay_rate(self):
        return self.pay_rate
    
    def set_shift(self, shift):
        self.shift = shift

    def set_pay_rate(self, pay_rate):
        self.pay_rate = pay_rate

    
name = input("Enter employee's name: ")
number = input("Enter employee's number: ")
shift = input("Enter employee's shift (1 for day, 2 for night): ")
pay_rate = float(input("Enter employee's pay rate: "))

worker = ProductionWorker(name, number, shift, pay_rate)

print("\nDetails of Employee:")
print(f"Name: {worker.get_name()}")
print(f"Employee Number: {worker.get_number()}")
print(f"Shift: {'Day' if worker.get_shift() == 1 else 'Night'}")
print(f"Pay Rate: ${worker.get_pay_rate():.2f}")
