from Recordable import Recordable
from Account import Account

class Accounts(Recordable):

    def __init__(self) -> None:
        super().__init__()
        self.accounts = []


    def addAccount(self, account: Account) -> None:
        self.accounts.append(account)

    
    def getAccounts(self) -> list:
        return self.accounts



    def toJson(self) -> None:
        result = []
        for account in self.accounts:
            result.append(account.toJson())
        
        super().write({"accounts": result})

    
    def fromJson(self) -> None:
        data = super().read()
        for entry in data["accounts"]:
            account = Account(entry["username"], entry["password"], entry["tasks"])
            self.addAccount(account)