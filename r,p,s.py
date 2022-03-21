import random
def play():
    user=input("Rock\nPaper\nScissor\n:")
    comp=random.choice(["r","p","s"])
    if user==comp:
        return print('its a tie')
    if  win(user,comp):
        print(f"the computer chose {comp} ")
        return print('you won')
    print(f"the computer chose {comp} ")
    return print('you lost')


def win(user,comp):
    if (user=='r' and comp=='s') or (user=='s' and comp=='p') or (user=='p' and comp=='r'):
        return True
play()