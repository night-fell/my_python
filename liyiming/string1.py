# -*- coding:utf-8 -*-

if __name__ == "__main__":
    source_str = "it's my book,please show it, wa ka ka, yo yo yo!"

    #从左往右查找yo
    print ("从左往右查找yo")
    print (source_str.find("yo"))
    print (source_str.index("yo"))

    #从右往左查找yo
    print ("从右往左查找yo")
    print (source_str.rfind("yo"))
    print (source_str.rindex("yo"))

    #替换所有yo
    des_str = source_str.replace("yo","ha")
    print (des_str)

    #替换两次yo
    des_str = source_str.replace("yo", "ha", 2)
    print (des_str)
