# coding:utf-8
import random


def roll_dice(num=3, points=None):
    print("<<<<< ROLL THE DICE! >>>>>")
    if points is None:
        points = []
    while num > 0 :
        point = random.randrange(1,7)
        points.append(point)
        num = num -1
    return points


def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'


def start_game():
    print('<<<<< GAME STARTS! >>>>>')
    choices = ['Big', 'Small']
    your_choice = input('Big or Small:')
    if your_choice in choices:
        points = roll_dice()
        total = sum(points)
        you_win = your_choice == roll_result(total)
        if you_win:
            print('The points are ', points, 'You Win! ')
        else:
            print('The points are', points, 'You Lose! ')
    else:
        print('Invalid word!')
        start_game()


start_game()
