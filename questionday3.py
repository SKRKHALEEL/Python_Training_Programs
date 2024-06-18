
'''
"happy fathers day"
extract the vowel which has max count.
'''
'''
s = "happy fathers day"
vowels = "aeiouAEIOU"
vowel_count = {}
for char in s:
    if char in vowels:
        if char in vowel_count:
            vowel_count[char]+=1
        else:
            vowel_count[char]=1
            max_vowel = max(vowel_count, key=vowel_count.get)
            print("The vowel with max count is", max_vowel)
'''

# from collections import Counter
str = "happy fathers day"
str = list(str)
# print(str)
for i in str:
    if i in "aeiou":
        s = i
        break
str.remove(s)
s1 = str.index(s)
print(s1+1)




