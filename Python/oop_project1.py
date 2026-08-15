from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(5000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdraw(1000)
Dave.withdraw(10)

Dave.transfer(1000, Sara)
Sara.transfer(100, Dave)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(1000, Sara)