# coding:utf-8


def convert(g):
    kg = int(g)/1000
    result = 'Weight of kg is:'
    return result + str(kg)


def cal_edge(a, b):
    side1 = int(a)
    side2 = int(b)
    hypotenuse = pow(side1*side1 + side2*side2, 0.5)
    result = 'The right triangle third side\'s length is:'
    return result + str(hypotenuse)


weight_g = input('please input weight of g:')
print(convert(weight_g))
side1 = input('please input side1:')
side2 = input('please input side2:')
print(cal_edge(side1, side2))
