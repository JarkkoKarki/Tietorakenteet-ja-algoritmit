def squares(lenght):
    squares = {}
    for x in (int(len(lenght))):
        squares[x] = x**2
    print(squares)

squares(input())