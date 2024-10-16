import sys

names = ["Felipe", "Klenil", "Ana Julia", "Michele", "Lara", "Karla", "Pitoco"]

name = input("Name: ")

for n in names:
    if name == n:
        print("Found!")
        sys.exit(0)


print("Not found :(")
sys.exit(1)
