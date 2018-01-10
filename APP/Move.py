

#处理升级文件名字

def sp_tan(a):

    b = str.maketrans(' ', ' ', '[')

    x = a.translate(b)

    c = str.maketrans(']', ',')

    new_x = x.translate(c)

    p = new_x.split(',')

    return p