
"""
Mariam Ammar
Class: CS 521 - Summer 2
Date: 08/20/21
Final Project 

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
    
    def __len__(self):
        return len(self.journal_entry)
    
    def __repr__(self):
        return f"{self.name} has a mood score of {self.mood}."
    
    def __write_in_journal(self, file_name = "journal.txt"):
        self.journal_entry = input("\n Go ahead and let your thoughts flow!\n ")

        try:
            new_file = open(file_name, 'a')
        except FileNotFoundError:
            print('Sorry, the file your are trying to write to was not found. \n' 
            'Please make sure you used the right name and filepath. \n')

        else:     
            new_file.write(f"\n{datetime.now()}\n" + self.journal_entry)
            new_file.close() 
            print(f'''Wow, that was {len(self)} characters. Great work! You entry was saved in '{file_name}' .''')
        
        