# Queues and Stacks

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards.

To solve this challenge, we must first take each character in S, enqueue it in a queue, and also push that same character onto a stack. Once that's done, we must dequeue the first character from the queue and pop the top character off the stack, then compare the two characters to see if they are the same; as long as the characters match, we continue dequeueing, popping, and comparing each character until our containers are empty (a non-match means S isn't a palindrome).