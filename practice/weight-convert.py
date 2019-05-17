# coding:utf-8


def convert(g):
    kg = int(g)/1000
    result = 'Weight of kg is:'
    return result + str(kg)


weight_g = input('please input weight of g:')
print(convert(weight_g))

