def check_balance(text):
    parentheses = {"(": ")", "{": "}", "[": "]"}
    stack = []
    count = 0
    # iteroidaan char
    for pos, char in enumerate(text):
        if char in parentheses:  # avonainen kaari
            stack.append((char, pos)) # tallennetaan char ja pos
        elif char in parentheses.values():  # suljettu kaari
            if len(stack) == 0: # Jos tyhjä
                return f"Match error at position {pos}"
            top_char, top_pos = stack.pop() # poistetaan kaari
            if parentheses[top_char] != char: # vastaavaa ei löytynyt
                return f"Match error at position {pos}"
            count += 1 # löytyi lisätään löydettyjen määrää

    if stack:  # Ei tasa määrä
        _, first_pos = stack[0]
        return f"Match error at position {first_pos}" # palautetaan paikka

    return f"Ok - {count}" #palautetaan määrä

"""
stack = saves opening brackets and their positions.
count = counts the number of matched pairs found
pos =  position of the character in the text
char = current character

"""