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
    print(word_of_the_day)
    print(f'The word of the day contains {len(word_of_the_day)} letters')
    
    attemps = 10
    
    
    while attemps > 0:
        
        list_letter_guess = []
        word_of_the_day_user = ''
        user_word = get_user_word(word_of_the_day=word_of_the_day)
        
        for i in range(len(user_word)):
            
            if user_word[i] in word_of_the_day and user_word[i] == word_of_the_day[i]:
                    list_letter_guess.append(user_word[i])
        
        
        for i in range(len(user_word)):
            
            if user_word[i] in word_of_the_day and user_word[i] == word_of_the_day[i]:
                    word_of_the_day_user += colored(user_word[i], 'green')
                    
            elif not user_word[i] in word_of_the_day:
                word_of_the_day_user += colored(user_word[i], 'red')
                    
            elif user_word[i] in word_of_the_day and user_word[i] != word_of_the_day[i]:
                
                if list_letter_guess.count(user_word[i]) >= word_of_the_day.count(user_word[i]):
                    word_of_the_day_user += colored(user_word[i], 'red')
                else:
                    word_of_the_day_user += colored(user_word[i], 'yellow')
                    list_letter_guess.append(user_word[i])
         
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
    
    
    
    