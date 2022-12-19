# 1. practice #1 (class)
# class Human:
#     def __init__(self, name):
#         self.name = name

#     def say_hello(self):
#         print(f"hello! {self.name}")


# class Player(Human):
#     def __init__(self, name, xp):
#         super().__init__(name)
#         self.xp = xp


# class Fan(Human):
#     def __init__(self, name, fav_team):
#         super().__init__(name)
#         self.fav_team = fav_team


# shin_player = Player("shin", 1000)
# print(shin_player.name, shin_player.xp)
# shin_player.say_hello()
# shin_fan = Fan("shinbi", "T1")
# print(shin_fan.name, shin_fan.fav_team)
# shin_fan.say_hello()

# 2. practice #2 (class -> super)
# class Dog:
#     def woof(self):
#         print("woof woof")


# class Beagle(Dog):
#     def cry(self):
#         super().woof()


# beagle = Beagle()
# beagle.cry()

# 3. practice #3 (underscore, overiding)

# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         # print(super().__str__())
#         return f"hello {self.name}"
#         return f"Dog: {self.name}"

#     def __getattribute__(self, name):
#         print(f"hello shin ")
#         return "😀"


# jia = Dog("jia")
# # print(dir(jia))
# print(jia.name)
# paul = Dog("paul")
# print(paul)
