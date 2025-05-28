def run():
    print("\nVW Popularity Module (stub)")
    while True:
        print(" 1 — Generate training file (vw_train.txt)")
        print(" 2 — Train model (vw_popularity.model)")
        print(" 3 — Predict popularity for wines")
        print(" 4 — Forecast total sales by month")
        print(" 0 — Exit")

        action = input("Select action: ").strip()
        if action == "0":
            break
        elif action == "1":
            print("Would process sales and count daily wine occurrences")
            print("Would generate VW-format training file with date features")
        elif action == "2":
            print("Would train Vowpal Wabbit in Docker using squared loss")
        elif action == "3":
            print("Would apply trained model to current wines and assign popularity scores")
        elif action == "4":
            print("Would forecast daily sales and aggregate monthly totals")
        else:
            print("Invalid input.")

if __name__ == "__main__":
    run()
