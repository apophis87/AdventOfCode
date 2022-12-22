"""
                [B] [L]     [J]
            [B] [Q] [R]     [D] [T]
            [G] [H] [H] [M] [N] [F]
        [J] [N] [D] [F] [J] [H] [B]
    [Q] [F] [W] [S] [V] [N] [F] [N]
[W] [N] [H] [M] [L] [B] [R] [T] [Q]
[L] [T] [C] [R] [R] [J] [W] [Z] [L]
[S] [J] [S] [T] [T] [M] [D] [B] [H]
 1   2   3   4   5   6   7   8   9
"""

stacks = [list('SLW'),
          list('JTNQ'),
          list('SCHFJ'),
          list('TRMWNGB'),
          list('TRLSDHQB'),
          list('MJBVFHRL'),
          list('DWRNJM'),
          list('BZTFHNDJ'),
          list('HLQNBFT')]

stacks2 = stacks.copy()

with open('input.txt') as file:
    # Read the values
    moves = file.read().splitlines()

    # n = amount of crates to move
    # s = source stack
    # d = destination stack

    for m in moves:
        ml = m.split()
        n = int(ml[1])
        s = int(ml[3])-1
        d = int(ml[5])-1

        stacks[d] = stacks[d] + stacks[s][-n:][::-1]  # add n last items to destination stack (reversed order)
        stacks[s] = stacks[s][:-n]  # update source stack with leftover items

        stacks2[d] = stacks2[d] + stacks2[s][-n:]  # add n last items to destination stack (normal order)
        stacks2[s] = stacks2[s][:-n]  # update source stack with leftover items

    answer = ''
    for stack in stacks:
        answer += stack.pop()

    answer2 = ''
    for stack in stacks2:
        answer2 += stack.pop()

    print("Solution part 1: ", answer)
    print("Solution part 2: ", answer2)

