# # Example 1
# def greet(name):
#     print("Hello", name)

# greet("Neha")

# # Example 2
# def add(a, b):
#     return a + b

# result = add(5, 3)
# print(result)

# def big(a ,b):
#     if(a>b):
#         print(a)
#     else:
#         print(b)
# big(10,9)

# a = int(input("enter number:"))
# def even(a):
#     if(a%2 == 0):
#         print("number is even :",a)
#     else:
#         print("number is odd : ",a)
# even(a)

#(p*r*t)/100

# P = int(input("Enter Original amount: "))
# R = int(input("Enter Rate :"))
# T = int(input("Enter time :"))

# def SI(P,R,T):
#     print("Simple interst is ")
#     print((P*R*T)/100)

# SI(P,R,T)

#loop
# l = ["Mango","Apple","Banana","Kiwi","Watemelon"]
# for item in l:
#     print(l)

# in this code we learn that item is placeholder that contain one item each at a time and prints list

# l = ["Mango","Apple","Banana","Kiwi","Watemelon"]
# l.insert(1,"cherry")
# l.pop(3)
# print(l)

#prime 1oritself
#string replaced

# l = [1,2,4,4,5]
# print(max(l))

# numbers = [5, 3, 9, 1, 7]
# largest = numbers[0]

# for num in numbers:
#     if num>largest:
#         largest = num

# print("Largest:", largest)

# def count_letter(word, letter):
#     count = 0
#     for ch in word:
#         if ch == letter:
#             count += 1
#     return count

# print(count_letter("banana", "a"))  # 3

# def count_letter(word,letter):
#     count = 0
#     for ch in word:
#         if ch == letter:
#             count+=1
#     return count
# print(count_letter("banana","b"))

# a,b = 0, 1
# a,b=0,1
# for i in range(10):
#     print(a, end=" ")
#     a, b = b, a + b
# # 0 1 1 2 3 5 8 13 21 34

# a,b = 0,1
# for i in range(10):
#     print(a,end=" ")
#     a,b = b,a+b

# def is_palindrome(s):
#     s = s.lower()
#     for i in range(len(s) // 2):
#         if s[i] != s[len(s) - 1 - i]:
#             return False
#     return True

# print(is_palindrome("non"))  # True
# print(is_palindrome("hello"))    # False

# def is_palindrome(s):
#     s = s.lower()
#     for i in range(len(s) // 2):
#         if s[i] != s[len(S) - 1 - i]:
#             return False

def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
# [1, 2, 3, 4, 5]

