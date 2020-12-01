class MyATM:
    
    def __init__(self):
        self.cust = Customer()
        self.acc = Account()
        self.bal = 1000000

    def getStart(self, numCard):
        self.cust.numAcc = numCard
        col = 1
        pin = int(input('Enter pin code'))
        while col < 3:    
            if pin == self.acc.bc[numCard]['pin']:
                print('Ready')
                break
            else:
                pin = int(input('Enter pin code'))
                col += 1
        else:
            print('ended attempts')

    def cash(self, summ):
        if summ > self.bal:
            print('Insufficient funds at the ATM')
        elif self.acc.withdrawal(summ, self.cust):
            self.bal -= summ
            print('Take your money')
        else:
            print('Insufficient funds in the account')  
    def balance(self):
        print(self.acc.balAcc(self.cust))


class Customer:

    def __init__(self):
        self.numAcc = None

class Account:
    bc = {6666666666666666: {'pin': 7777, 'bal': 10000}}

    def withdrawal(self, s, acc):
        if s <= self.bc[acc.numAcc]['bal']:
            self.bc[acc.numAcc]['bal'] = self.bc[acc.numAcc]['bal'] - s
            return True

    def  balAcc(self, acc):
        return self.bc[acc.numAcc]['bal']     

if __name__ == '__main__':
    x = MyATM()
    x.getStart(6666666666666666)
    x.cash(5000)
    x.balance
    
    

