'''
'''
#perfect number in fumctions
import math as m
def isperfect(num):
    res=1
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            res+=i+num//i
    return res==num
num=int(input())
print(isperfect(num))
'''
#perfect number using recurtion
'''
import math as m
def isperfect(num,n):
    if n==int(m.sqrt(num)):
        if num%n==0:
            return n
        return 1
    if num%n==0:
        return n+num//n+isperfect(num,n+1)
    return 0+isperfect(num,n+1)
num=int(input())
print(num==isperfect(num,2))
'''
#lcm of two numbers in function

'''
def lcm(a,b):
    t=2
    res=1
    while a>=t and b>=t:
        if a%t==0 and b&t==0:
            a=a//t
            b=b//t
            res=res*t
        else:
            t+=1
    return res*a*b
a,b=map(int,input().split())
print(lcm(a,b))
'''

#lcm of two numbers in function using recuretion
'''
def lcm(a,b,t):
    if a<t or b<t:
        return a*b
    if a%t==0 and b%t==0:
        return t*lcm(a//t,b//t,t)
    else:
        return lcm(a,b,t+1)
a,b=map(int,input().split())
print(lcm(a,b,2))
'''
#lcm of two numbers in function in another method
'''
def lcm(a,b):
    m=max(a,b)
    while True:
        if m%a==0 and m%b==0:
            return m
        else:
            m+=1
a,b=map(int,input().split())
print(lcm(a,b))
'''
#lcm of two numbers in function in using for loop
'''
def lcm(a,b):
    m=max(a,b)
    for i in range(m,a*b+1):
        if i%a==0 and i%b==0:
            return i
a,b=map(int,input().split())
print(lcm(a,b))
'''
'''
#pronic number
def ispronic(num):
    for i in range(num):
        print(i)
        if i*(i+1)== num:
            return True
         if i*(i+1) > num
         return False
num=int(input())
print(ispronic(num))
'''
'''
from math import *
def ispronic(num):
    a=int(sqrt(num))
    return a*(a+1)==num
num=int(input())
print(ispronic(num))
'''
'''
DISARIUM NUMBER
175=1^1+7^2+5^3=175
def isdisarium(num):
    dc=0
    temp=num
    while(temp):
        temp=temp//10
        dc+=1
    temp=num
    res=0
    while temp:
        r=temp%10
        temp=temp//10
        res=res+pow(r,dc)
        dc-=1
    return res==num
num=int(input())
print(isdisarium(num))
'''

'''
HARSHAD NUMBER
18=1+8=9 and 18 is divisible by 9
def isharshad( num ) :
    sum = 0
    temp = num
    while temp > 0 :
        sum = sum + temp % 10
        temp = temp // 10
    return num % sum == 0
num=int(input())
print(isharshad(num))
'''

'''
ADDING TWO DIGITS PROGRAM IN LEETCODE
38=3+8=11=1+1=2
class Solution:
    def addDigits(self, num: int) -> int:
        s=0
        while num:
            r=num%10
            num//=10
            s+=r
            if num==0 and s>9:
                num=s
                s=0
        return s
'''

'''
COMPLEMENT OF BASE 10 INTEGER
5=101
5 COMPLEMENT=010=2_
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s=0
        t=0
        if n==0:
            return 1
        while n:
            r=n%2
            n=n//2
            if r==0:
                s=s+(2**t)
            t=t+1
        return s
'''

'''
ARRANGING COINS PROBLEM IN LEETCODE
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 0:
            raise ValueError('the input is invalid')
        if n == 0:
            return 0
        counter = 0
        row = 1
        while n - row >= 0:
            n -= row
            counter += 1
            row += 1
        return counter
'''

'''
BINARY NNUMBER WITH ALTERNATING BITS IN LEETCODE PROGRAM
5=101
TRUE
7=111
FALSE
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        d=n%2
        n=n//2
        while n:
            r=n%2
            n=n//2
            if(r==d):
                return False
            d=r
        return True
'''

'''
POWER OF FOUR PROGRAM IN LEETCODE
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        p=0
        while 4**p<n:
            p+=1
        return 4**p==n
'''

'''
NUMBER OF 1 BITS PROGRAM IN LEETCODE
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))
        print(n)
        one_count = 0
        for i in n:
            if i == "1":
                one_count+=1
        return one_count
'''


'''
PRIME NUMBER OF SET BITS IN BINARY REPRESENTATION IN LEETCODE PROGRAM
Input: left = 6, right = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def popcount(i):
            return bin(i)[2:].count('1')
        count = 0
        for j in range(left,right+1):
            if popcount(j) in [2,3,5,7,11,13,17,19]:
                 count +=1
        return count
'''

'''
HAPPY NUMBER IN LEETCODE PROGRAM
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
n=19
TRUE
1^2+9^2=82
8^2+2^2=68
6^2+8^2=100
1^2+0^2+0^2=1
class Solution:
    def isHappy(self, n: int) -> bool:
        return self.solve(n,{})
    def solve(self,n,visited):
        if n == 1:
            return True
        if n in visited:
             return False
        visited[n]= 1
        n = str(n)
        l = list(n)
        l = list(map(int,l))
        temp = 0
        for i in l:
            temp += (i**2)
        return self.solve(temp,visited)
'''        
'''
       
#OR
class Solution:
    def isHappy(self, n: int) -> bool:
        res=0
        while n:
            r=n%10
            n=n//10
            res+=pow(r,2)
            if n==0 and (res>=10 or res==7):
                print(res,end=" ")
                n=res
                res=0
        return res==1
'''

'''
Subtract the Product and Sum of Digits of an Integer leetcode problem
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s,p=0,1
        while n:
            r=n%10
            n=n//10
            s=s+r
            p=p*r
        return p-s
'''

'''        
Maximum 69 Number leetcode problem
class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
'''

'''
num=5
*****
*****
*****
*****
*****
num = int(input())
for i in range(num):
        for j in range(num):
                print("*",end = "")
        print()
'''

'''
num=5
12345
12345
12345
12345
12345
num = int(input())
for i in range(num):
        for j in range(num):
                print(j+1,end = "")
        print()
'''

'''
num=5
11111
22222
33333
44444
55555
num = int(input())
for i in range(num):
        for j in range(num):
                print(i+1,end = "")
        print()
'''

'''
num=5
54321
54321
54321
54321
54321
num = int(input())
for i in range(1,num+1):
        for j in range(num,0,-1):
                print(j,end = "")
        print()
'''

'''
num=5
12345
54321
12345
54321
12345
num=int(input())
for i in range(num):
        if i%2==0:
                for j in range(1,num+1):
                        print(j,end="")
        else:
                for j in range(num,0,-1):
                        print(j,end="")
        print()        
                
'''

'''
num=5
11111
12345
33333
12345
55555
num=int(input())
for i in range(num):
        if i%2==0:
                for j in range(1,num+1):
                        print(j,end="")
        else:
                for j in range(1,num+1):
                        print(i,end="")
        print()        
'''

'''
num=5
12345
22345
32345
42345
52345
num =int(input())
for i in range(1,num+1):
        for j in range(1,num+1):
                if j==1:
                        print(i,end="")
                else:
                        print(j,end = "")
        print()
'''

'''
num=5
54321
22222
54321
44444
54321
num=int(input())
for i in range(1,num+1):
        for j in range(1,num+1):
                if i%2:
                        print(num+1-j,end="")
                else:
                        print(i,end="")
        print()
'''

'''
num=5
10101
10101
10101
10101
10101
num=int(input())
for i in range(1,num+1):
        for j in range(1,num+1):
                if j%2==0:
                        print(0,end="")
                else:
                         print(1,end="")
        print()
'''

'''
num=5
10101
01010
10101
01010
10101
num=int(input())
t=0
for i in range(1,num+1):
        for j in range(1,num+1):
                if t==0:
                        t=1
                        print(t,end="")
                else:
                        t=0
                        print(t,end="")
        print()
'''

