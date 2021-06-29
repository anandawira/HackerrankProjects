#!/bin/python3

import sys, itertools, time, functools

n, k = [int(num) for num in input().strip().split(' ')]

def Interserciton(a, b):
    isc = set([int(num) for num in str(a)]).intersection([int(num) for num in str(b)])
    isc.discard(0)
    return isc

for numerator in range(10**(n-1), 10**n):
    for denominator in range(numerator+1, 10**n):
        isc = Interserciton(numerator, denominator)
        if len(isc)<k:
            continue

# itertools.combinations_with_replacement()
# start_time = time.time()

# cancel_list = list()
# remainder_list = list()

# def TupleToInt(intTuple):
#     return int(functools.reduce(lambda a, b: a+str(b), intTuple, ''))

# pairs = set()

# for cancel in itertools.combinations_with_replacement(list(range(1,10)), r=k):
#     for remainder_1 in itertools.combinations_with_replacement(list(range(10)), r=n-k):
#         for remainder_2 in itertools.combinations_with_replacement(list(range(10)), r=n-k):
#             for numerator_order in itertools.permutations(list(range(n)), r=n):
#                 for denominator_order in itertools.permutations(list(range(n)), r=n):
#                     number1 = cancel + remainder_1
#                     number2 = cancel + remainder_2
                    
#                     numerator_tuple = tuple(number1[idx] for idx in numerator_order)
#                     denominator_tuple = tuple(number2[idx] for idx in denominator_order)
                    
#                     if numerator_tuple[0] == 0 or denominator_tuple[0]==0:
#                         continue
                    
#                     numerator = TupleToInt(numerator_tuple)
#                     denominator = TupleToInt(denominator_tuple)
                    
#                     # if numerator == 253 and denominator == 451:
#                     #     print('here')
                    
#                     if not numerator<denominator:
#                         continue
                    
#                     remainder_numerator = TupleToInt(tuple(numerator_tuple[idx] for idx, order in enumerate(numerator_order) if order>=k))
#                     remainder_denominator = TupleToInt(tuple(denominator_tuple[idx] for idx, order in enumerate(denominator_order) if order>=k))
                    
#                     if not remainder_numerator<remainder_denominator:
#                         continue
                    
#                     if numerator/denominator == remainder_numerator/remainder_denominator:
#                         pairs.add((numerator, denominator))

# sum_numerator = functools.reduce(lambda a, b: a + b[0], pairs, 0)
# sum_denominator = functools.reduce(lambda a, b: a + b[1], pairs, 0)

# print(sum_numerator, sum_denominator)

# print(time.time()-start_time)