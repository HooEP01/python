# OOP
class PlayerCharacter:
    # class object attribute / non-dynamic / static
    membership = True

    # constructor
    def __init__(self, name='anonymous', age=0):
        if age > 18:
            self.name = name  # attributes
            self.age = age

    def shout(self):
        return f'my name is {self.name}'

    def run(self):
        return f'my name is {self.name}'

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Cindy', 30)
print(player1.shout())
print(PlayerCharacter.adding_things(2, 3))

# self = reference to something haven't created
