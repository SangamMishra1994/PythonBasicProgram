class ATMSimulator:
    balance = 0

    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return f"Your current balance is ${self.balance}"

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        return self.balance

    def withdrawl(self, withdrawl_amount):
        if self.balance < withdrawl_amount:
            return (
                "Withdrawl Amount is more than" + "\n"
                f"account balance ${self.balance}"
            )
        else:
            self.balance -= withdrawl_amount
            return f"Balance is ${self.balance}"


def main():
    current_balance = 0
    print("ATM Simulator")
    atm_simulator = ATMSimulator(1000)
    while True:
        print("1. Check balance")
        print("2. Deposit Amount")
        print("3. Withdrawl Amount")
        print("4. Exit")
        choice = input("Enter the choice:- ")

        match choice:
            case "1":
                balance = atm_simulator.check_balance()
                print(balance)
            case "2":
                amount = int(input("Enter the amount:- $"))
                if amount < 0:
                    print("Enter the amount more than 0")
                else:
                    print(
                        f"deposit amount is {amount}, and "
                        f"Balance = ${atm_simulator.deposit(amount)}"
                    )
            case "3":
                withdrawl_amount = int(input("Enter withdrawl amount:- $"))
                if withdrawl_amount < 0:
                    print("Enter positive amount")
                else:
                    current_balance = atm_simulator.withdrawl(withdrawl_amount)
                    print(current_balance)
            case "4":
                break
            case _:
                print("Wrong choice try again!!")


if __name__ == "__main__":
    main()
