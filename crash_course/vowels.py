string = input("Enter a word ")

broke = list(string)

count_vowel = 0

count_consonant = 0

for char in string:
    if char in "aeiou":
        count_vowel += 1
    elif char.isalpha():
        count_consonant += 1

print("No of vowels = ",count_vowel)
print("No of consonants = ",count_consonant)