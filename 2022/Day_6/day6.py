with open('input.txt') as file:
    # Read the values
    stream = file.read()

    MESSAGE = 14  # part 2
    PACKET = 4  # part 1

    window_length = MESSAGE
    for index in range(len(stream) - window_length + 1):
        window_items = stream[index:index + window_length]
        if len(set(window_items)) == window_length:
            marker_index = (index + window_length)
            break

    print(f"Solution: ", marker_index)
