class Date:
    def __init__(self, month=12, day=20):
        self.month = month
        self.day = day

    def adding_month(self):
        if(self.month + 2 <= 12):
            self.month += 2
        else:
            raise ValueError("month number cannot be greater than 12")

    def date_decrease(self):
        if(self.day > 25):
            self.day -= 25
        else:
            difference = self.day - 25
            self.day = 30 + difference
            if(self.month == 1):
                self.month = 12
            else:
                self.month -= 1


    def info(self):
        return f"month: {self.month}\nday: {self.day}"

"""
dt = Date(1, 22)
print(dt.info())
dt.date_decrease()
print(dt.info())
"""

print("enter month:")
m = int(input())
print("enter day:")
d = int(input())
date1 = Date(m, d)
print("to add 2 months to the current date, enter add, and to subtract 25 days from the current date, enter dcs:")
if(input() == "add"):
    date1.adding_month()
else:
    date1.date_decrease()
print(date1.info())