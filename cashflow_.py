

class CashFlow :
    def __init__(self) :
        self.name = "Jou"
        self.assets = 10000
        self.cashflow = []
        
    def set_name(self, name:str) :
        self.name = name
        
    def set_assets(self, assets:int) :
        self.assets = assets
        
    def income(self, income) :
        self.assets += income
        self.cashflow.append(income)
        
    def expense(self, expense) :
        if expense > self.assets  :
            print("Can't afford ")
        else :
            self.cashflow.append(-1 * expense)
            self.assets -= expense
                  
    def print_cashflow(self) :
        for i in self.cashflow :
            print(i,end=" ")
            
            
if __name__ == "__main__" :
    ajoucf = CashFlow()
    print(ajoucf.assets)
    ajoucf.set_assets(20000)
    ajoucf.set_name("ajoucf")
    print(ajoucf.name)
    print(ajoucf.assets)
    ajoucf.expense(20001)
    print(ajoucf.assets)
    ajoucf.income(3000)
    print(ajoucf.assets)
    ajoucf.expense(20001)
    print(ajoucf.assets)
    ajoucf.income(200)
    print(ajoucf.assets)
    ajoucf.expense(1500)
    print(ajoucf.assets)
    ajoucf.print_cashflow()