def count_vowels(string):
    vowels = ["A", "E", "I", "O", "Y", "U"]
    num_of_vowels = 0

    for x in string:
        for y in vowels:
            if x.upper() == y:
                num_of_vowels += 1

    print(f"Number of vowels: {num_of_vowels}")


count_vowels(input())