import random

class Game:
    def __init__(self):
        self.money = 10
        self.food = 5
        self.inventory = []
        self.day = 1
        self.items = ["Old Coin", "Broken Watch", "Rusty Key", "Silver Ring", "Ancient Book"]
        self.town_places = ["Market", "Abandoned House", "Library", "Park", "Cafe"]

    def explore(self):
        place = random.choice(self.town_places)
        print(f"Mark explores the {place}...")
        
        if random.random() < 0.7:
            found_item = random.choice(self.items)
            self.inventory.append(found_item)
            print(f"He finds a {found_item} and takes it with him!")
        else:
            print("He finds nothing of value today.")

    def sell_items(self):
        if not self.inventory:
            print("Mark has nothing to sell.")
            return
        
        print("Mark visits the market to sell his items.")
        earnings = len(self.inventory) * random.randint(3, 7)
        self.money += earnings
        print(f"He sells his finds for {earnings} coins.")
        self.inventory.clear()

    def buy_food(self):
        if self.money >= 5:
            self.food += 3
            self.money -= 5
            print("Mark buys food at a cafe and feels satisfied.")
        else:
            print("Not enough money to buy food.")

    def status(self):
        print(f"Day: {self.day} | Money: {self.money} | Food: {self.food} | Inventory: {self.inventory}")

    def next_day(self):
        self.day += 1
        self.food -= 1
        if self.food <= 0:
            print("Mark has run out of food and collapses from hunger. Game Over.")
            return False
        print("A new day begins...")
        return True

    def play(self):
        print("Mark arrives in the town of Karberg and starts his journey.")
        while True:
            self.status()
            print("\n1. Explore the town\n2. Sell items\n3. Buy food\n4. End day")
            choice = input("Choose an action: ")
            if choice == "1":
                self.explore()
            elif choice == "2":
                self.sell_items()
            elif choice == "3":
                self.buy_food()
            elif choice == "4":
                if not self.next_day():
                    break
            else:
                print("Invalid choice, try again.")
        print("Game over.")

if __name__ == "__main__":
    game = Game()
    game.play()
