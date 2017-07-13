# -*- coding:utf-8 -*-

if __name__ == "__main__":
    str_1 = "1234567890"
    str_2 = "abccdefABCDEF"
    str_3 = "12345abcdeABCDE"
    str_4 = "abcdef"
    str_5 = "ABCDEF"
    str_6 = "   "
    str_7 = " sfsdf "

    print (str_1.isdigit())
    print (str_2.isalpha())
    print (str_3.isalnum())
    print (str_4.islower())
    print (str_4.isupper())
    print (str_5.isupper())
    print (str_6.isspace())
    print (str_7.isspace())