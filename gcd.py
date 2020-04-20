# -*- coding: utf-8 -* 
import sys
# 判断函数，判断m和n是否互素，并求出u，v使um+vn=gcd(m,n)
def ex_gcd(m,n,u,v):
    # 筛选n为0的情况
    if n == 0:
        u = 1
        v = 0
        return (m,u,v)    
    a1 = b = 1
    a = b1 = 0
    c = m
    d = n
    # 计算初始q、r
    q = int(c / d)
    r = c % d
    # 辗转相除法
    while r:
        c = d
        d = r
        t = a1
        a1 = a
        a = t - q * a
        t = b1
        b1 = b
        b = t - q * b
        q = int(c / d)
        r = c % d
    u = a
    v = b
    return (d,u,v)
# 主函数
if __name__ == '__main__':
    m = int(input("输入m(m>n)："))
    n = int(input("输入n(m>n)："))
    result = ex_gcd(m,n,0,0)   # 调用ex_gcd函数
    if result[0]==1:
        print("gcd(%d,%d) = %d"%(m,n,result[0]) + "\n互素")
    else:
        print("gcd(%d,%d) = %d"%(m,n,result[0]) + "\n不互素")
        print("u = %d\nv = %d"%(result[1],result[2]))
