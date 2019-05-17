# coding:utf-8


def invest(amount, rate, time):
    for i in range(1, time + 1):
        total_amount = amount * pow((1 + rate), i)
        if i == 1:
            print('principal amount:', amount)
        print('year ', i, ': $', total_amount)


invest(1000, 0.05, 10)
