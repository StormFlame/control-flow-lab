prompt = input("Input a dog's age in human years: ")

human_age = int(prompt)
dog_age = 0

if human_age / 10 >= 2:
    dog_age+=2
    human_age-=20
elif human_age / 10 >= 1:
    dog_age+=1
    human_age-=10
dog_age += human_age/7

print(f"The dog's age in dog years is {round(dog_age, 1)}")
    