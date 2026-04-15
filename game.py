import random
import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

class JamestownGame:
    def __init__(self):
        self.days = 0
        self.food = 100
        self.settlers = 104
        self.morale = 100
        self.distance_to_virginia = 4828
        self.location = "Atlantic Ocean"

    def status(self):
        print("\n" + "="*30)
        print(f"DAY: {self.days} | LOCATION: {self.location}")
        print(f"SETTLERS: {self.settlers} | FOOD: {self.food} | MORALE: {self.morale}")
        print("="*30)

    def play(self):
        print_slow("--- WELCOME TO THE JAMESTOWN EXPEDITION (1606) ---")
        print_slow("You are in charge of three ships: The Susan Constant, the Godspeed, and the Discovery.")
        print_slow("Your goal: Don't let everyone perish before you find gold (Spoiler: There ain't no gold.)")

        while self.distance_to_virginia > 0 and self.settlers > 0:
            self.status()
            print("\nWhat is your command?")
            print("1. Ration food strictly")
            print("2. Fish from the side of the boat")
            print("3. Lead a prayer session")

            choice = input("> ")
            self.days += 7
            self.distance_to_virginia -= random.randont(161, 483)

            if choice == "1":
                self.food -= 5
                self.morale -= 10
                print_slow("The settlers are hungry, but the barrels are staying full.")
            elif choice == "2":
                self.food += random.randint(0, 10)
                print_slow("You caught some cod. It tastes like salt and sadness.")
            else:
                self.morale += 15
                print_slow("Spirituality is high, though stomachs are empty.")

            if random.random() < 0.2:
                print_slow("!!! SCURVY OUTBREAK !!!")
                lost = random.randint(1, 5)
                self.settlers -= lost
                print(f"You lost {lost} men to vitamin C deficiency.")

        if self.settlers > 0:
            self.location = "Jamestown Island"
            print_slow("\nYOU HAVE ARRIVED AT THE JAMES RIVER.")
            print_slow("It's a swamp. There are mosquitoes everywhere. Good luck.")

            for month in range(1, 5):
                self.status()
                print(f"\nMONTH {month} IN VIRGINIA")
                print("1. Search for gold (The Company wants it)")
                print("2. Plant corn (John Smith suggests this)")
                print("3. Dig a well (The river water is salty)")

                choice = input("> ")
                if choice == "1":
                    print_slow("You found shiny rocks! (Wait, it's just pyrite/fools gold). You found 0 food.")
                    self.food -= 30
                elif choice == "2":
                    print_slow("The corn is growing. It's not gold, but you can't eat gold.")
                    self.food += 20
                elif choice == "3":
                    print_slow("The water is slightly less brackish now. Morale improves.")
                    self.morale += 20

                if self.food <= 0:
                    lost = random.randint(10, 20)
                    self.settlers -= lost
                    print_slow(f"Starvation strikes! {lost} settlers didn't make it.")

        self.end_game()
    
    def end_game(self):
        print("\n--- RESULTS ---")
        if self.settlers > 0:
            print(f"Congratulations. {self.settlers} settlers survived. You founded a colony.")
            print("History will remember you, mostly for the harsh rationing.")
        else:
            print("Unfortunately, the colony has failed. The forest has reclaimed the fort.")

if __name__ == "__main__":
    game = JamestownGame()
    game.play()
