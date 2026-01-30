word = input("Enter a word:")
length = len(word)

number = []
for gela in range(length):
    num = int(input(f"Enter a number {gela + 1}:"))
    number.append(num)
    
def ave(number):
    total = 0
    for num in number:
        total = total + num
    return total / length

def values(length, word, average):
    if length > average:
        print(f"The length of the word '{word}' is greater than the average.")
    elif length < average:
        print(f"The length of the word '{word}' is less than the average.")
    else:
        print(f"The length of the word '{word}' is equal to the average.")


average = ave(number)

print(number)
print("The length of the word is", length)
print("The average of the numbers is", average)

result = values(length, word, average)
