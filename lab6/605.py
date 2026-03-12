

S = input()


vowels = set('aeiou')

has_vowel = any(char.lower() in vowels for char in S)


if has_vowel:
    print("Yes")
else:
    print("No")