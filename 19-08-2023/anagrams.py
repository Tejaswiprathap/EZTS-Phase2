'''write a fn to validate if the provided two strings are anagrams or not.if the 2 strings are anagrams,then return 'yes'.otherwise, return 'no'.
INPUT:
input 1: 1st string---->Listen
input 2: 2nd string---->Silent
OUTPUT:
if they are anagrams the function will return 'yes'.otherwise it will return 'no'.'''
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return 'yes' if sorted(str1) == sorted(str2) else 'no'

string1 = "listen"
string2 = "silent"
result = are_anagrams(string1, string2)
print(result)
