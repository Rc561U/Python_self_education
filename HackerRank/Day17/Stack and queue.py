#
# from collections import deque
#
# from functools import lru_cache
# class Solution:
#     character = []
#     lst = deque([])
#
#     def pushCharacter(self, char):
#         self.character.append(char)
#
#     def enqueueCharacter(self, char):
#         self.lst.append(char)
#
#     def popCharacter(self):
#         return self.character.pop()
#
#     def dequeueCharacter(self):
#         return self.lst.popleft()
#
#
# if __name__ == '__main__':
#     # read the string s
#     s = input()
#     # Create the Solution class object
#     #s= 'racecar'
#     obj = Solution()
#
#     l = len(s)
#     # push/enqueue all the characters of string s to stack
#     for i in range(l):
#         obj.pushCharacter(s[i])
#         obj.enqueueCharacter(s[i])
#
#     isPalindrome = True
#     '''
#     pop the top character from stack
#     dequeue the first character from queue
#     compare both the characters
#     '''
#     for i in range(l // 2):
#         if obj.popCharacter() != obj.dequeueCharacter():
#             isPalindrome = False
#             break
#     # finally print whether string s is palindrome or not.
#     if isPalindrome:
#         print("The word, " + s + ", is a palindrome.")
#     else:
#         print("The word, " + s + ", is not a palindrome.")
#
from functools import lru_cache


@lru_cache
def fib(x):
    return fib(x-1) + fib(x-2) if x > 1 else x