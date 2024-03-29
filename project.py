class Bikeshop:
    def __init__(self, stock):
        self.stock = stock

    def displaybike(self):
        print("Total bikes:", self.stock)

    def rentforbike(self, q):
        if q <= 0:
            print("Enter a positive value greater than zero.")
        elif q > self.stock:
            print("Not enough stock available.")
        else:
            print("Total price:", q * 100)
            self.stock -= q
            print("Remaining bikes:", self.stock)


while True:
    obj = Bikeshop(100)
    uc = int(input('''
1. Display stocks
2. Rent a bike
3. Exit
'''))
    if uc == 1:
        obj.displaybike()
    elif uc == 2:
        n = int(input("Enter the quantity: "))
        obj.rentforbike(n)
    else:
        break
