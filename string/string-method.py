# coding:utf-8

phone_number = '131-6339-8683'
hiding_number = phone_number.replace(phone_number[:9], '*'*9)
# replace(,) 被替代部分,将要替代部分
print(hiding_number)

search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'

print(search + ' is at ' + str(num_a.find(search)) + ' to ' + str(num_a.find(search) + len(search)) + ' of number_a')
print(search + ' is at ' + str(num_b.find(search)) + ' to ' + str(num_b.find(search) + len(search)) + ' of number_b')

city = input("Please enter the name of city:")
url = "http://***{}".format(city)
# format('');format('','').format(a = '',b = '')
print(url)
