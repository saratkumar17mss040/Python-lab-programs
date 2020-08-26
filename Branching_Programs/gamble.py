def profitable_gamble(prob, prize, pay):
    if prob * prize > pay:
        return True
    return False


print(profitable_gamble(4,8,12))