class MyATM:    
    
    def __init__(self):    #Внедрить экземпяры Customer, Account
        self.cust = Customer()
        self.acc = Account()
        self.bal = 1000000

    def getStart(self, numCard):    #Считать номер карты ,запросить пин, заполнить атрибут Customer
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

    def cash(self, summ):    #Снятие денег, проверка наличия в банкомате, запрос наличия на счете
        if summ > self.bal:
            print('Insufficient funds at the ATM')
        elif self.acc.withdrawal(summ, self.cust):
            self.bal -= summ
            print('Take your money')
        else:
            print('Insufficient funds in the account')  
    def balance(self):    #Запрос баланса на счете ,вывод
        print(self.acc.balAcc(self.cust))


class Customer:    #Создает экземпляры клиентов с атрибутом номер карты

    def __init__(self):
        self.numAcc = None

class Account:    #Хранит информацию о счетах
    bc = {6666666666666666: {'pin': 7777, 'bal': 10000}}

    def withdrawal(self, s, acc):    #Получает запрос о снятии средств,проверяет наличие 
        if s <= self.bc[acc.numAcc]['bal']:
            self.bc[acc.numAcc]['bal'] = self.bc[acc.numAcc]['bal'] - s
            return True

    def  balAcc(self, acc):    #Получает запрос по остатку для экземпляра клиента,возвращает остаток
        return self.bc[acc.numAcc]['bal']     

if __name__ == '__main__':
    x = MyATM()
    x.getStart(6666666666666666)
    x.cash(5000)
    x.balance
    
    

