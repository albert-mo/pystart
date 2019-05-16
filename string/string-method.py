# coding:utf-8

phone_number = '131-6339-8683'
hiding_number = phone_number.replace(phone_number[:9], '*'*9)
# replace(,) 被替代部分,将要替代部分
print(hiding_number)
