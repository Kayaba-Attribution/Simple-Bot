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


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("What is my favorite anime/manga (Its SAO btw) ?")

    # save the options in a variable to later change the value of the variable to match the input    
    answer_1 = "1. SAO"
    answer_2 = "2. That time I got reincarnated as a slime"
    answer_3 = "3. Overlord"
    answer_4 = "4. Solo Leveling"

    print(answer_1)
    print(answer_2)
    print(answer_3)
    print(answer_4)

    # the correct one is answer_1
    answer_1 = "1"
    answer_2 = "2"
    answer_3 = "3"
    answer_4 = "4"
    counter = 1
    while counter:
        choice = input()
        if choice == answer_1:
            print("Completed, have a nice day!")
            break
        else:
            print("Please, try again.")


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()