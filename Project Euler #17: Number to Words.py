#!/bin/python3

import sys

ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten","Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
notation = [ "Thousand", "Million", "Billion", "Trillion"]

def word_under_1000(n):
    text = ""
    
    # Get Hudreds words
    if n//100 != 0:
        text += "{} Hundred ".format(ones[n//100])
        n %= 100
    
    # Get 1-99 words
    if n>0 and n <= 19:
        text += ones[n]
    elif n <=99:
        text += tens[n//10]
        n %= 10
        if n != 0:
            text += " {}".format(ones[n])
            
    return text.strip()

# for i in range(999):
#     print(word_under_1000(i))

def word(n):
    text = []
    
    if n == 0:
        return "Zero"
    
    # Get under 1000
    if n%1000 != 0:
        text.append(word_under_1000(n%1000))
    
    # Get Thousands
    if (n//1000)%1000 != 0:
        text.append("Thousand")
        text.append(word_under_1000((n//1000)%1000))
        
    # Get Million
    if (n//1000000)%1000 != 0:
        text.append("Million")
        text.append(word_under_1000((n//1000000)%1000))
       
    # Get Billion
    if (n//1000000000)%1000 != 0:
        text.append("Billion")
        text.append(word_under_1000((n//1000000000)%1000))
     
    # Get Trillion
    if (n//1000000000000)%1000 != 0:
        text.append("Trillion")
        text.append(word_under_1000((n//1000000000000)%1000))
    
    return " ".join(text[::-1])

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(word(n))