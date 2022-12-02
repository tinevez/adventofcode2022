select_scores = {
    'X': 1,  # Rock
    'Y': 2,  # Paper
    'Z': 3  # Scissors
}

# Oponent -> me.
win_scores = {
    'A':  # Rock
    {'X': 3, 'Y': 6, 'Z': 0},
    'B':  # Paper
    {'X': 0, 'Y': 3, 'Z': 6},
    'C':  # Scissors
    {'X': 6, 'Y': 0, 'Z': 3}
}


def score(opponent_choice, my_choice):
    sel = select_scores[my_choice]
    win = win_scores[opponent_choice][my_choice]
    return sel+win


total_score = 0
with open('input.txt') as f:
    for line in f:
        tokens = line.split()
        opponent_choice = tokens[0]
        my_choice = tokens[1]
        sc = score(opponent_choice, my_choice)
        total_score = total_score + sc

print('Total score: %d' % total_score)
