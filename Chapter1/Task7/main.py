def custom_encoder(string):
    string = str(string.lower())
    positions = []
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    for x in string:
        positions.append(reference_string.find(x))
    return positions