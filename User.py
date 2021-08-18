#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Mariam Ammar
Class: CS 521 - Summer 2
Date: 08/20/21
Final Project 
Defines the 'User' class which
with instance attributes name, close contact, 
birthday, and mood. Includes methods that 
calculate days till user birthday, allow user to generate
a madlib, counts the characters and unique words in a journal
input, 
"""



from datetime import datetime 


class User():
    
    def __init__(self, name, close_contact, birthday, mood):
        self.name = name
        self.__close_contact = close_contact
        self.birthday = birthday
        self.mood = mood
        self.journal_entry = ''

    def calculate_days_till_bday(self, original_date, now = datetime.now()):
        delta1 = datetime(now.year, original_date.month, original_date.day)
        delta2 = datetime(now.year+1, original_date.month, original_date.day)
        return ((delta1 if delta1 > now else delta2) - now).days
    
    
    def mad_lib(self, n1, n2, adj1, adj2, adj3):
        return f'''
        There was an {adj1} {n1} that lived in a {n2}. She was {adj3},
        lived life without a care, and had very long, {adj2} hair.'''
        
    
    def __len__(self):
        return len(self.journal_entry)
    
    def __repr__(self):
        return f"{self.name} has a mood score of {self.mood}"
    
    def __write_in_journal(self, text = ' ', file_name = "journal.txt"):
        text = input("\n Go ahead and let your thoughts flow!\n ")
        self.journal_entry = text

        try:
            new_file = open(file_name, 'a')
        except FileNotFoundError:
            print('Sorry, the file your are trying to write to was not found. \n' 
            'Please make sure you used the right name and filepath. \n')

        else:     
            new_file.write(f"\n{datetime.now()}\n" + self.journal_entry)
            new_file.close()
            words_lst = set([word for word in self.journal_entry.split()])
            if len(words_lst) < 2:
                return        f'''Wow, that was {len(self)} characters and {len(words_lst)} unique word.
        Great work! You entry was saved in '{file_name}' .'''
            else: 
                        return        f'''Wow, that was {len(self)} characters and {len(words_lst)} unique words.
        Great work! You entry was saved in '{file_name}' .'''
                  
          
        
if __name__ == "__main__":
    birthday = datetime.now()
    p1 = User("Mariam","Lorena", birthday, 7)
    assert p1.calculate_days_till_bday(birthday) == 364
    n1, n2, adj1, adj2, adj3 = "chair","tree","yellow","angry","hungry"
    assert n1; n2; adj1; adj2; adj3 in p1.mad_lib(n1, n2, adj1, adj2, adj3)
    assert len(p1) == len(p1.journal_entry)
    p1._User__write_in_journal()
    test_file = open("journal.txt")
    test_file_lines = test_file.readlines()
    assert input("Input previous text.") in test_file_lines
    test_file.close()
    print(f"{p1} and all methods in the User class are working successfully.")

