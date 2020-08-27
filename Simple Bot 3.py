import random

def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")

def guess_age_y_n():
    print("Let me guess the number you are thinking between 1 - 20")
    print("""I will give you a number:
    If it is too high enter "h"
    If it too low enter "l"
    If it is your number enter "x"
    """)
    print("This is my guess:")
    n = random.randint(1,20)
    print(n)
    print("is my guess too high or too low? or perhaps i guessed it it my last attemp?")
    count = 1
    while True:
        close = input()
        count += 1
        if close == 'h':
            n -= 1
            print(n)
            print("is my guess too high or too low? or perhaps i guessed it it my last attemp?")
        elif close == 'l':
            n += 1
            print(n)
            print("is my guess too high or too low? or perhaps i guessed it it my last attemp?")
        elif close == 'x':
            print("Wow, it took me ", (count - 1), "tries.")
            break


def count():
    print('Now I will prove to you that I can count to any number you want.')
    print('Until what number would you like me to count?')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("What is my favorite anime/manga (Its SAO btw) ?")

    # print out all the options 
    print("""1. SAO
2. That time I got reincarnated as a slime
3. Overlord
4. Solo Leveling""")
    print("Enter your guess: 1, 2, 3 or 4?")
    
    # Make a while loop that stops when the asnwer is selected (in this case is int(1) "SAO")
    while True:
        choice = int(input())
        if choice == 1:
            print("You got It, have a nice day!")
            break
        else:
            print("Please, try again.")


    


def end():
    print('Congratulations, have a nice day!')


greet('Kayaba', '2020')  # change it as you need
remind_name()
guess_age()
guess_age_y_n()
count()
test()
end()