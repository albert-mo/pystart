# coding:utf-8
for i in range(1,10):
    path = 'D:/用户文件/09403/桌面/test/'
    full_path = path + str(i) + '.txt'
    file = open(full_path, 'w')
    file.write(str(i))
    file.close()
