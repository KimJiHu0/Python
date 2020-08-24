# -*- coding:utf-8 -*-


def write_file():
    pass

def read_file():
    pass

if __name__ == '__main__':
    select = int(input('1:write\n2:read\input select'))
    if select == 1:
        write_file()
    elif select == 2:
        read_file()
    else:
        print('end')
