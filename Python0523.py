#coding:utf-8
# 找出3-2w间的所有素数

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        return True

nums = list(filter(is_prime, range(3, 20000)))
print (nums)
print (len(nums))
