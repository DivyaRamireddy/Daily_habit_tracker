# Daily Habit Tracker 🕒

def add_habit():
    habit = input("Enter a new habit you want to track: ").capitalize()
    with open("habits.txt", "a") as file:
        file.write(f"{habit} - Not Done\n")
    print(f"✅ '{habit}' added to your habit list!\n")


def view_habits():
    try:
        with open("habits.txt", "r") as file:
            habits = file.readlines()
            if not habits:
                print("No habits found yet!\n")
                return
            print("📋 Your Habits:")
            for line in habits:
                print("   " + line.strip())
    except FileNotFoundError:
        print("No habits found yet!\n")


def mark_done():
    try:
        with open("habits.txt", "r") as file:
            habits = [line.strip() for line in file.readlines()]

        if not habits:
            print("No habits to mark!\n")
            return

        print("\nSelect a habit to mark as done:")
        for i, h in enumerate(habits, start=1):
            print(f"{i}. {h}")

        choice = int(input("\nEnter habit number: ")) - 1

        if 0 <= choice < len(habits):
            habit, status = habits[choice].split(" - ")
            habits[choice] = f"{habit} - Done ✅"
            with open("habits.txt", "w") as file:
                for h in habits:
                    file.write(h + "\n")
            print(f"🎉 Marked '{habit}' as done!\n")
        else:
            print("Invalid choice!\n")
    except FileNotFoundError:
        print("No habits found yet!\n")


def main():
    while True:
        print("\n=== Daily Habit Tracker ===")
        print("1. Add Habit")
        print("2. View Habits")
        print("3. Mark Habit as Done")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_habit()
        elif choice == "2":
            view_habits()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            print("👋 Keep growing, see you tomorrow!")
            break
        else:
            print("Invalid option! Try again.\n")


if __name__ == "__main__":
    main()
