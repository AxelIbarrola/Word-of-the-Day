from termcolor import colored
from connect_api import get_word
from validations import get_user_word, strip_colors
def main():
    
    print('\nThe word of the day was selected, try to guess it!\n')
    
    print(f'{'RULES'.center(50, '-')}\n')
    print(f'{colored('Red letter', 'red')}: The letter is not found in the word of the day')
    print(f'{colored('Green letter', 'green')}: The letter is found in the word of the day and is in the same position where you entered it')
    print(f'{colored('Yellow letter', 'yellow')}: The letter is in the word of the day but it is not in the same position where you entered it\n')
    print('You have 10 chances to find the word\n')

    
    word_of_the_day = get_word()
    print(f'The word of the day contains {len(word_of_the_day)} letters')
    
    attemps = 10
    
    while attemps > 0:
        
        word_of_the_day_user = ''
        user_word = get_user_word(word_of_the_day=word_of_the_day)
        
        for index in range(len(user_word)):
            if user_word[index] in word_of_the_day and user_word[index] == word_of_the_day[index]:
                    word_of_the_day_user += colored(user_word[index], 'green')
            elif user_word[index] in word_of_the_day and user_word[index] != word_of_the_day[index]:
                    word_of_the_day_user += colored(user_word[index], 'yellow')
            else:
                    word_of_the_day_user += colored(user_word[index], 'red')
         
        print()           
        print(word_of_the_day_user)
        print()
        
        striped_word = strip_colors(word_of_the_day_user)
        if striped_word == word_of_the_day:
            print('\nCongratulations, you guessed the word of the day!\n')
            break
        else:
            attemps -= 1
            print(f'\nYou have {attemps} chances left\n')
    
    if attemps == 0:
        print('I\'m sorry, your chances are over.\n')
        print(f'The word of the day was: {word_of_the_day}\n')               

main()
    
    
    
    