import re

def get_user_word(word_of_the_day):
    
    while True:
        
        user_word = input('Enter the word: ')
        
        if not user_word.isalpha():
            print('The value entered must be a word')
        elif not len(user_word) == len(word_of_the_day):
            print(f'The word must be {len(word_of_the_day)} letters long')
        else:
            break
    
    return user_word


def strip_colors(word_of_the_day_user):
    return re.sub(r'\x1b\[\d+m', '', word_of_the_day_user)