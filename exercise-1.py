vowels = ['a', 'e', 'i', 'o', 'u', 'y']

promt = input('Please enter a letter from the alphabet (a-z or A-Z)')


for letter in promt:
    if letter in vowels:
        print(f'The letter {letter} is a vowel')
    else:
        print(f'The letter {letter} is a consonant')

