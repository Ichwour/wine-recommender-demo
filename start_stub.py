def run_start_menu():
    command_map = {
        "1": lambda: print("Launching parser (stub)"),
        "2": lambda: print("Launching statistics module (stub)"),
        "3": lambda: print("Launching VW module (stub)"),
        "4": lambda: print("Launching clustering module (stub)"),
        "5": lambda: print("Launching CatBoost training (stub)"),
        "6": lambda: print("Launching recommender (stub)"),
        "7": custom_conditions
    }

    while True:
        print("\nProject Components Menu:")
        print(" 1 — parser.py (data preprocessing and parsing)")
        print(" 2 — statistic.py (sales statistics)")
        print(" 3 — rabbit.py (VW: popularity model)")
        print(" 4 — cluster.py (wine clustering)")
        print(" 5 — cat.py (CatBoost training)")
        print(" 6 — recommender.py (recommendation generation)")
        print(" 7 — custom_conditions (custom query input)")
        print(" 0 — exit")

        choice = input("Enter option number: ").strip()
        if choice == "0":
            print("Exiting.")
            break

        command = command_map.get(choice)
        if command:
            command()
        else:
            print("Invalid choice. Try again.")

def custom_conditions():
    print("\nEnter any query text (e.g. 'dry rosé under 20 euro from france'):")
    input(">> ")
    print("Stub: conditions.json would be generated here.")

if __name__ == "__main__":
    run_start_menu()
