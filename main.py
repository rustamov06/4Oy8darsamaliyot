# 4 Oy 8 dars Mavzu: Amaliyot

# 1 vazifa

# from collections import namedtuple
#
# users = [
#     {"id": 1, "name": "Toxir","medal": 12, "tur": "boks"},
#     {"id": 2, "name": "Sobir", "tur": "boks", "medal": 15}
# ]
#
# Person = namedtuple("Person", ["id", "name", "tur", "medal"])
# for user in users:
#     person = Person(**user)
#     a = person.medal
#     if a < person.medal:
#         a = person.medal
# print(f"Eng ko'p yutuqga ega bo'lgan  bokschi medali soni: {a}, Ismi: {person.name}, Sport turi: {person.tur}")


#----------------------------------------------------------------------------------------

# 2 vazifa

# nums = []
# count = 0
# def orta_qiymat(nums):
#     global count
#     print(f"Kiritgan sonlaringizng orta qiymati: {sum(nums)/count}")
# while True:
#     num = input("Son kiriting: ")
#     if num == "stop":
#         break
#     elif num.isdigit():
#         num = int(num)
#         count += 1
#         nums.append(num)
# orta_qiymat(nums)


#----------------------------------------------------------------------------------------

# 3 vazifa

# import math
# class SimpleIterator:
#     def __init__(self, limit):
#         self.current = 1
#         self.limit = limit
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current <= self.limit:
#             value = self.current
#             self.current += 1
#             return value
#         else:
#             raise StopIteration
# limit = int(input("Nechinchi songacha sonlardi kvadrati kerak: "))
# iterator = SimpleIterator(limit)
# for number in iterator:
#     print(f"{number}:{math.pow(number, 2)}")


#----------------------------------------------------------------------------------------

# 4 vazifa

# text = "assalomu aleykum"
# unli = ["o", "i", "e", "u", "a", "o'"]
# inter_user = iter(text)
#
# for i in text:
#     a = next(inter_user)
#     if a in unli:
#         print(a)


#----------------------------------------------------------------------------------------

# 5 vazifa

# def custom_range(start, stop, step=2):
#
#     current = start
#     while current < stop:
#         yield current
#         current += step
#
# for num in custom_range(0, 100, 2):
#     print(num)


#----------------------------------------------------------------------------------------

# 6 vazifa

# count = 0
# def ab(text):
#     def bc():
#         global count
#         for i in text:
#             count += 1
#     return bc
# text = input("Matn kiriting: ")
# b = ab(text)
# b()
# print(f"siz kiritgan matn uzunligi: {count}")
