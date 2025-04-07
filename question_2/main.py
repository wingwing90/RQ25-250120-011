# main.py

from simulator import Simulator

def main():
    sim = Simulator()

    while True:
        print("Welcome to Auto Driving Car Simulation!\n")
        try:
            dims = input("Please enter the width and height of the simulation field in x y format:\n").strip()
            width, height = map(int, dims.split())
            sim.create_field(width, height)
            print(f"You have created a field of {width} x {height}.\n")
        except ValueError:
            print("Invalid input. Please enter two integers separated by space.\n")
            continue

        while True:
            print("Please choose from the following options:")
            print("[1] Add a car to field")
            print("[2] Run simulation")
            choice = input().strip()

            if choice == "1":
                name = input("Please enter the name of the car:\n").strip().upper()

                try:
                    pos = input(f"Please enter initial position of car {name} in x y Direction format:\n").strip()
                    x, y, d = pos.split()
                    x, y = int(x), int(y)
                    d = d.upper()
                    if d not in {'N', 'S', 'E', 'W'}:
                        raise ValueError("Invalid direction")
                except ValueError:
                    print("Invalid input. Please enter values like: 1 2 N\n")
                    continue

                commands = input(f"Please enter the commands for car {name}:\n").strip().upper()
                if not all(c in {'L', 'R', 'F'} for c in commands):
                    print("Invalid command string. Only L, R, F are allowed.\n")
                    continue

                sim.add_car(name, x, y, d, commands)

                print("\nYour current list of cars are:")
                for car in sim.list_cars():
                    print(f"- {car}")
                print()

            elif choice == "2":
                print("\nYour current list of cars are:")
                for car in sim.list_cars():
                    print(f"- {car}")
                print("\nAfter simulation, the result is:")
                sim.run()
                print("\nPlease choose from the following options:")
                print("[1] Start over")
                print("[2] Exit")

                next_choice = input().strip()
                if next_choice == "1":
                    sim.reset()
                    break
                elif next_choice == "2":
                    print("Thank you for running the simulation. Goodbye!")
                    return
                else:
                    print("Invalid choice. Exiting.")
                    return
            else:
                print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
