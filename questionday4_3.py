'''
You are given a string containing words separated by spaces. Your task is to write a
function or program that reverses the order of words in the string.
Sample Input:
Hello World
Sample Output:
World Hello






'''
def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string
s = input()
print(reverse_words(s))




