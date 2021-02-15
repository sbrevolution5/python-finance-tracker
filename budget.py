import math

# uses a User class to allow multiple users to access app.  App will come with demo user as well. 
class User(object):
    def __init__(self, name):
        super(User, self).__init__()
        self.name = name
        self.assets = []
        self.liabilities = []
        self.total_assets = 0.00
        self.total_liabilities = 0.00
        self.net_worth = 0.00
        self.accounts = []
        self.cash = 0.00

    def add_asset(self, name, value):
        self.assets.append({name: name, value: value})
        self.total_assets += value
        #updates networth when it is called
        self.get_networth()
        return self

    def add_liability(self, name, value):
        self.liabilities.append({name: name, value: value})
        self.total_liabilities += value
        self.get_networth()
        return self
    
    def add_account(self, account_object):
          self.accounts.append(account_object)
          return self

    def get_networth(self):
          self.net_worth = self.total_assets - self.total_liabilities
          return self


class Account(object):
    def __init__(self, name, initial):
        super(Account, self).__init__()
        self.name = name
        self.ledger = []  # TODO initialize with the initial amount and date
        self.total = initial
        self.intrest = 0
    
    def deposit(self, amount, desc="", category="deposit"): #this method may not have a category.
        self.ledger.append({"amount": amount, "description": desc})
        self.total += amount
        # should update the category child object as well
        return self

    def withdrawl(self, amount, desc="", category="general"):
        self.ledger.append({"amount": amount, "description": desc})
        self.total += amount
        #should update category object
        return self


class Category(object):
    """docstring for category."""
    #allow changing a record from one category to another
    def __init__(self, name):
        super(Category, self).__init__()
        self.name = name
        self.ledger = []
        self.total = 0
        self.spent = 0

    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": amount, "description": desc})
        self.total += amount
        return self

    def withdraw(self, amount, desc=""):
        if self.check_funds(amount):
            self.spent += amount
            amount = 0-amount
            self.ledger.append({"amount": amount, "description": desc})
            self.total += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.total

    def transfer(self, amount, objName):
        objNameVar = objName.name
        if not self.withdraw(amount, f"Transfer to {objNameVar}"):
            return False
        elif not objName.deposit(amount, f"Transfer from {self.name}"):
            return False
        return True

    def check_funds(self, amount):
        if amount > self.total:
            return False
        else:
            return True

    def __str__(self):
        resultStr = ""
        resultStr += self.name.center(30, '*')
        resultStr += "\n"
        i = 0
        for line in self.ledger:
            resultStr += f"{self.ledger[i]['description'][0:23]:23}" + \
                f"{self.ledger[i]['amount']:>7.2f} \n"
            i += 1
        resultStr += f"Total: {self.get_balance()}"
        return resultStr


def split_word(str):
    return [char for char in str]


def create_spend_chart(arg):
    print("Percentage spent by category")
    num = len(arg)
    totalSpent = 0
    # num is how many categories we are charting
    # we need an array of the category's name (this also gets a total to work with )
    wordList = []
    for item in range(num):
        wordList.append(list(arg[item].name))
        totalSpent += arg[item].spent
       # we need to know percentage for each Category
    pctList = []
    for item in range(num):
        pctList.append(math.floor(arg[item].spent/totalSpent * 10))
        ht = 10
    while ht >= 0:
        print(f"{(ht*10):3d}| ", end="")
        for p in range(num):
            if pctList[p-1] >= ht:
                print("o  ", end="")
            else:
                print("", end="   ")
        print()
        ht -= 1
    print(" "*4+"-"*(num*3+1))  # bottom axis
    # print each letter, one per word, until you reach longest word.
    l = len(max(wordList, key=len))
    x = 0
    while x < l:  # while x is less than your longest word (vertical length)
        print("     ", end="")  # beginning of the line
        i = 0
        while i < num:
            # for each row of the word (3x)
            try:
                print(wordList[i][x], end="  ")
            except IndexError:
                print("   ", end="")
            i += 1
        print("")
        x += 1
    return
