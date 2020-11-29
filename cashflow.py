
class CashFlow :
    def __init__(self) :
        self.name = "Jou"
        self.assets = 10000
        self.cashflow = [10000,]
        
    def set_name(self, name:str) :
        self.name = name
        
    def set_assets(self, assets:int) :
        self.assets = assets
        
    def income(self, income) :
        self.assets += income
        
    def expanse(self, expanse) :
        if expanse > self.assets  :
            print("Can't afford ")
        else :
            self.cashflow.append(-1 * expanse)
            self.assets -= expanse
                  
    def print_cashflow(self) :
        for i in self.cashflow :
            print(i)
            
if __name__ == "__main__" :

    c = CashFlow()
    c.print_cashflow()
    c.expanse(500)
    c.print_cashflow()