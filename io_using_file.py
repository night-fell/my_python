#coding=UTF-8


poem = '''\
Programming is fun
when the work is done
if you wanna make your work also fun:
    use python!
'''
#打开文件以编辑
f = open('poem.txt', 'w')
#向文件中编写文本
f.write(poem)
#关闭文件
f.close()

#如果没有特别指定，假定启用阅读模式
f = open('poem.txt')
while True:
    line = f.readline()
    #零长度指示EOF
    if len(line) == 0:
        break

    print (line)

f.close()

