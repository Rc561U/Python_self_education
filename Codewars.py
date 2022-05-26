# from itertools import permutations as per
#
#
# def permutations(string):
#     perm = per(string)
#     result = [''.join(i) for i in list(perm)]
#     return list(set(result))
#
# print(permutations('aabb'))
#-------------------------------
# class add(int):
#     def __call__(self, n):
#         return add(self + n)
#
#
# print(add(1)(2)(3)(4))
#-------------------------------
# base = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
# 4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
# 9099459979:[("Ermes", "Angela"), ("Dallas", "Teias")],
# 6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
# 7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
#
# def check(name):
#     global base
#     return base[name] if name in base else False
#
# #user_input = int(input())
# result = (check(4199392609))
# result2 = (check(123))
# print(f'{result[0][0]} {result[0][1]} from {result[1][0]}, {result[1][1]}' if result else 'No valid date')
# print(f'{result2[0][0]} {result2[0][1]} from {result2[1][0]}, {result2[1][1]}' if result2 else 'No valid date')
#----------------------------------------
# def exp_sum(n):
#   if n < 0:
#     return 0
#   dp = [1]+[0]*n
#   for num in range(1,n+1):
#     for i in range(num,n+1):
#       dp[i] += dp[i-num]
#   return dp[-1]
#
#
# print(exp_sum(100))
#----------------------------------------

def strip_comments(strng, markers):
    # while markers in strng:
    #     strng.replace(markers[0],'')
    #     strng.replace(markers[1],'')
    return strng.replace(markers[0],'')

print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))