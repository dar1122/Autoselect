a = 51
b = '2'


try:
    if a<b:
        print(1)
    else:
        print(3)
except TypeError:
    print('请输入数字')