import random

def lotto_gen():
    lotto_numb = []

    ind = 0
    while ind < 6:
        random_ = random.randint(1,49)
        if random_ not in lotto_numb:
            lotto_numb.append(random_)
            ind += 1
        lotto_numb.sort()
    return lotto_numb
def lotto_check():
    checker = lotto_gen()
    win = 0
    lott = []
    inde = 0
    while inde < 6:
        try:
            number = int(input("Enter a number: "))
            if number in lott:
                print("The number is allready in the lotto, chose diffrent: ")
            elif number > 49:
                print("The number is to big!")
            else:
                lott.append(number)
                inde += 1
        except ValueError:
            print("Invalid")
    lott.sort()
    print(lott)
    print(checker)

    for numbers in lott:
        if numbers in checker:
            win = win+1

    if win < 3:
        print("You didt win anything")
    elif win == 4:
        print("Nice a 4!")
    elif win == 5:
        print("Lucky 5")
    elif win == 6:
        print("Godlike 6/6")



lotto_check()