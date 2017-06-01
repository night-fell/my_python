# coding:utf-8

import os
import time

#1.需要备份的文件指定在列表中
source = ['"C:\\note"']

#2.备份文件必须存储在一个主备份目录中
target_dir = 'C:\\notes'

#3.备份文件将打包压缩成zip文件
#4.zip压缩文件的文件名由当前日期与时间构成
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

# 如果目录目标还不存在，进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 5.使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target,
                                      ''.join(source))

#运行备份
print('Zip command is:')
print(zip_command)
print ('Running:')
if os.system(zip_command) == 0:
    print ('Successful backup to', target)
else:
    print ('Backup FAILED')