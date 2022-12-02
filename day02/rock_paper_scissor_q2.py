# Unsubtle.


win_scores = {
    'X': 0,  # loose
    'Y': 3,  # draw
    'Z': 6   # win
}

# select Rock:      1
# select Paper:     2
# select Scissors:  3

# Oponent -> should I win or not -> what do I select -> score of what I select.
selection_scores = {
    'A':  # Rock
    {
        'X': 3, # must loose -> select Scissors
        'Y': 1, # must draw -> select Rock
        'Z': 2  # must win -> select Paper
    },
    'B':  # Paper
    {
        'X': 1, # must loose -> select Rock
        'Y': 2, # must draw -> select Paper
        'Z': 3  # must win -> select Scissors
    },
    'C':  # Scissors
    {
        'X': 2, # must loose -> select Paper
        'Y': 3, # must draw -> select Scissors
        'Z': 1  # must win -> select Rock
    }
}


def score(opponent_choice, outcome):
    sel = selection_scores[opponent_choice][outcome]
    win = win_scores[outcome]
    return sel+win


total_score = 0
with open('input.txt') as f:
    for line in f:
        tokens = line.split()
        opponent_choice = tokens[0]
        outcome = tokens[1]
        sc = score(opponent_choice, outcome)
        total_score = total_score + sc

print('Total score: %d' % total_score)
