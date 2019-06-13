# coding:utf-8
import random


def roll_dice(num=3, points=None):
    print("<<<<< ROLL THE DICE! >>>>>")
    if points is None:
        points = []
    while num > 0:
        point = random.randrange(1, 7)
        points.append(point)
        num = num - 1
    return points


def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'


def start_game():
    your_money = 1000
    while your_money > 0:
        print('<<<<< GAME STARTS! >>>>>')
        choices = ['Big', 'Small']
        your_choice = input('Big or Small:')
        if your_choice in choices:
            your_bet = int(input('How much you wanna bet? - '))
            points = roll_dice()
            total = sum(points)
            you_win = your_choice == roll_result(total)
            if you_win:
                your_money = your_money + your_bet
                print('The points are ', points, 'You Win! ')
                print('You gained {},you have {} now'.format(your_bet, your_money))
            else:
                your_money = your_money - your_bet
                print('The points are', points, 'You Lose! ')
                print('You lost {},you have {} now'.format(your_bet, your_money))
        else:
            print('Invalid word!')
    else:
        print('GAME OVER!')


start_game()
