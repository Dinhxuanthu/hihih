class Account:
    def __init__(self, id: int, balance: float, pin: int):
        self.__id = id         # Private attribute
        self.balance = balance # Public attribute
        self.__pin = pin       # Private attribute

    def get_id(self, pin: int) -> str:
       
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin: int, new_pin: int) -> str:
        
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"

# Test Code
account = Account(8827312, 100, 3421)
print(account.get_id(1111))          # Output: Wrong pin
print(account.get_id(3421))          # Output: 8827312
print(account.balance)               # Output: 100
print(account.change_pin(2212, 4321))# Output: Wrong pin
print(account.change_pin(3421, 1234))# Output: Pin changed
