# coding:utf-8
import random


def roll_dice():
    print("<<<<< ROLL THE DICE! >>>>>")
    dice_list = [random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7)]
    return dice_list


def judge_result(dice_list, bigness):
    if sum(dice_list) <= 10:
        if bigness == 'Small':
            return 'You Won!'
        else:
            return 'You Lose!'
    else:
        if bigness == 'Big':
            return 'You Won!'
        else:
            return 'You Lose!'


print("<<<<< GAME STARTS >>>>>")
guess = input("Big or Small:")

list_result = roll_dice()
play_result = judge_result(list_result, guess)
print("The points are [{}, {}, {}] {}".format(list_result[0], list_result[1], list_result[2], play_result))
