# coding:utf-8
def get_ven(num):
    for i in range(1, num):
        remainder = i % 2
        if remainder == 0:
            print(i)


get_ven(100)

