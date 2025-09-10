def squares(lenght):
    squares = {}
    for x in range(lenght):
        squares[x+1] = (x+1)**2
    print(squares)

squares(int(input()))
