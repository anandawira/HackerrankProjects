
import sys, math
from typing import Counter
from functools import reduce
from math import sqrt

# def factors(n):
#         step = 2 if n%2 else 1
#         return set(reduce(list.__add__,
#                     ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

# def get_first_comb(a):
#     cur = 2
#     while True:
#         pow = math.log(a, cur)
#         if pow%1 == 0:
#             return cur, int(pow)
#         cur += 1
        
# def generate_skip_list(a, b, n):
#     skip_list = list()
#     for i in range(2, (b//2)+1):
#         if b%i == 0:
#             new_a = a**i
#             new_b = b//i
#             if new_a <= n and new_b<= n:
#                 skip_list.append((new_a, new_b))
#             else:
#                 break
#     return skip_list
    
# def Solve(n):
#     skip_list = list()
    
#     for a in range(2, n+1):
#         for b in range(2, n+1):
#             if (a, b) in skip_list:
#                 continue
            
#             skip_list += generate_skip_list(a, b, n)
    
#     return ( (n-1)**2 ) - len(skip_list)
           
def check_is_first(a, b, n):
    for i in range(2, (a//2)+1):
        pow = math.log(a, i)
        if pow%1 == 0:
            if pow*b <= n:
                return False
    return True

def Solve(n):
    # distinct = set()
    counter = 0
    for a in range(2, n+1):
        for b in range(2, n+1):
            if check_is_first(a, b, n):
                counter += 1
                # distinct.add(str(a**b))
    
    return(counter)

n = int(input().strip())
print(Solve(n))

# def is_first_comb(a, b, n):
#     factor_list = factors(a)
    
#     for factor in factor_list:
#         if factor == 1 or factor == a:
#             continue
        
#         pow = math.log(a, factor)
        
#         if pow%1 == 0:
#             if pow * b <= n:
#                 return False
        
#     return True

# def Solve(n):
#     count = 0
#     for a in range(2, n+1):
#         for b in range(2, n+1):
#             if is_first_comb(a, b, n):
#                 count += 1
#     return count

# def Solve(n):
#     Counter = 0
#     for a in range(2, n+1):
#         divisors = factors(a)
#         exps = []
#         for num in divisors:
#             if num == 1 or num == a:
#                 continue
            
#             pow = math.log(a, num)
            
#             if pow%1 ==0:
#                 exps.append(int(pow))
                
#         distinct = [False] * 2 + [True] * (n-1)
        
#         for exp in exps:
#             for i in range(exp, n+1, exp):
#                 distinct[i//exp] = False
                
#         Counter += sum(distinct)
        
#         # start = 2
        
#         # if exp > 1:
#         #     start = (n//exp) + 1
        
#         # for b in range(start, n+1):
#         #     Counter += 1
#     return Counter

