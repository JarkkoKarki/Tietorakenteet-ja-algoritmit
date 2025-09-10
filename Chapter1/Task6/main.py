

def collection_of_numbers():
    total = 0.0

    while True:
        try:
            num = float(input())
            if num == 0:
                print(f"The grand total is {total}")
                break
            else:
                total += num
                print(f"The total is now {total}")
        except ValueError:
            print("That wasn’t a number.")

collection_of_numbers()