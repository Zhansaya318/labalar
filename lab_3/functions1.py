import random
''' function to convert grams to ounces. ounces = 28.3495231 * grams '''
def ounces(grams):
    print(grams * 28.3495231)  

grams = int(input())
ounces(grams)
 

'''C = (5 / 9) * (F - 32)'''
def temp(F):
    C = (5/9) * (F - 32)
    print(C)

F = int(input())
temp(F)

'''filter_prime'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_prime():
    numbers = input().split()
    primes = []
    for num in numbers:
        num = int(num)
        if is_prime(num):
            primes.append(num)
    print(primes)

filter_prime()


''' string from user and print all permutations of that string.'''
def print_permutations(word):
    def permute(s, answer):
        if len(s) == 0:
            print(answer)
            return
        
        for i in range(len(s)):
            ch = s[i]
            left = s[:i]
            right = s[i+1:]
            rest = left + right
            permute(rest, answer + ch)
    
    permute(word, "")

word = int(input(""))
print_permutations(word)

''' reverse'''
def reverse_words(sentence):
    words = sentence.split()  
    words.reverse()  
    return " ".join(words)  


sentence = input("") 
print(reverse_words(sentence))  


''' 333'''
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False

''' 007'''
def spy_game(nums):
    n = 0  
    for num in nums:
        if num == 0 and n == 0:  
            n = 1
        elif num == 0 and n == 1:  
            n = 2
        elif num == 7 and n == 2:  
            return True  
    return False  

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  

''' sphere'''
def sphere_volume(r):
    return (4/3) * 3.14159 * r**3

r = int(input(""))
print(sphere_volume(r))


''' unique elements'''
def unique_elements(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

numbers = input("").split()
numbers = [int(i) for i in numbers] 
print(unique_elements(numbers))


''' palindrome'''
def palindrome(text):
    return text == text[::-1]  

word = input("") 
print(palindrome(word)) 

''' histogram'''
def histogram(l):
    for num in l:
        print('*' * num)  


numbers = input("").split()
numbers = [int(i) for i in numbers] 
histogram(numbers)

'''Guess the number'''
print("Hello! What is your name?")  
name = input()  
secret_number = random.randint(1, 20)  
print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")  
guesses = 0  
while True:  
    print("Take a guess.")  
    guess = int(input())  
    guesses += 1  
    if guess < secret_number:  
        print("Your guess is too low.")  
    elif guess > secret_number:  
        print("Your guess is too high.")  
    else:  
        print(f"Good job, {name}! You guessed my number in {guesses} guesses!")  
        break  
