# Read the list of inputs saved in input.txt
with open('input.txt') as file:
    # Read the values
    cal_list_raw = file.read().splitlines()
    # Typecast to int
    cal_list = [int(i) if i != '' else '' for i in cal_list_raw]

    # Make sublists
    cal_list_len = len(cal_list)
    indices_sublists = [idx + 1 for idx, val in enumerate(cal_list) if val == '']
    index_pairs_sublists = zip([0] + indices_sublists, indices_sublists + [cal_list_len + 1])
    cal_sublists = [cal_list[i:j - 1] for (i, j) in index_pairs_sublists]

    # Generate list of the sums of the sublists
    cal_list_sums = [sum(sublist) for sublist in cal_sublists]

    # Get the max in the list of list of sum of sublists
    print("Result part 1: ", max(cal_list_sums))

    list_top_3 = sorted(cal_list_sums)[-3:]
    print("Result part 2: ", sum(list_top_3))
