# -*- coding:utf-8 -*-

if __name__ == "__main__":

    demo_str = " 我的前 后 和 中 间 都有空格 "
    print(demo_str)
    #去掉前面的空格
    lstr = demo_str.lstrip()
    print (lstr)
    #去掉后面的空格
    rstr = demo_str.rstrip()
    print (rstr)
    #去除前后的空格
    str = demo_str.strip()
    print (str)
    #去除中间的空格
    mstr = demo_str.replace(' ', '')
    print (mstr)

