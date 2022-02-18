import random

def game():
    user = input("Whats your choise:\n'r' for rock, 'p' for Paper, 's' for sissors\n").lower()
    computer = random.choice(['r','p','s'])
    print(f"You are {user} and computer is {computer}")

    if user ==computer:
        return 'It\'s a tie'
    
    # r>s, s>p, p>r
    if is_win(user,computer):
        return "You won!"

    return "You Lost!"

def is_win(player,opponent):
    # return true if player wins
    # r>s, s>p, p>r
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True
    
print(game())