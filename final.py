#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


from datetime import datetime
import random 
import vlc
from User import User
import sys 


#Prompts for user input and reprompts if user input invalid. 
name = input("Please input your first name.")
close_contact = input("Who's the closest living person to you?")

print(f"Hi {name}! Welcome to be Moodbot. We have just a few more questions for you.")

while True:
    year = input('When is your birthday? [YY] ')
    month = input('When is your birthday? [MM] ')
    day = input('When is your birthday? [DD]')

    try:
        year, month, day = int(year), int(month), int(day)
        birthday = datetime(year,month,day)
        break

    except:
        print("Sorry, try again! Please make sure your number entries follow the right criteria and format.")

    
while True:
    mood = input("Rate the way you feel right now from 1-10 with 10 being the best possible score.")
    try:
        mood = int(mood)
        while mood not in range (1,11):
            mood = int(input("Sorry, try again and make sure you input a number from 1-10.")) 
        break
    except:
        print("Sorry! Looks like you didn't input a number. Please try again.")
        
        
p1 = User(name, close_contact, birthday, mood)


while True: 
    
    sad_options = (1, "Listen to a Song"), (2, "Write about it"), (3, "Meditate"),     (4, "Read an inspirational quote"), (5, "Get some tips")

    happy_options = (1, "Listen to a Song"), (2, "Write a letter to your future self"),     (3, "Take note of some great ideas"), (4, "Plan your birthday celebration"), (5, "Have a dance party")

    if mood < 3 :
        print(f'''
        \n Wow. Looks like you're really upset. 
        Make sure to seek out help and think of how {close_contact}
        would think if knew you were feeling like this!
        How about giving them a call? 
        Or you can...\n''')
        for i in sad_options:
            print(i[0],i[1])

    if 2 < mood < 5:
        print(f'''
        \n Why so blue? Your birthday is only {p1.calculate_days_till_bday(p1.birthday)} days away!
        Prepare a celebration or choose one of the options below.''')
        for i in sad_options:
            print(i[0],i[1])

    if mood > 4:
        print('''Nice to hear you are at least doing ok!
    Which option would you like to choose?''')
        for i in happy_options:
            print(i[0], i[1])

    selection = input("Input a number to select an option.")
    try:       
        selection = int(selection)
        while selection not in range (1,6):
            selection = int(input("Sorry, try again and make sure you enter a number according to one of the options.")) 
            break

    except:
        print("Sorry, try again. You need to input a number.")


    dict_happy_options = dict(happy_options)
    dict_sad_options = dict(sad_options)



    tips =     {"1. Take a few really deep, controlled breaths.",
    "2. Call a good friend.",
    "3. Go for a walk.",
    "4. Do something outside.",
    "5. Exercise!",
    "6. Eat healthy - food is linked to both physical and mental health.",
    "7. Get at least 8 hours of sleep a day.",
    "8. Make time for yourself and include relaxing rituals into your day.",
    "9. Stay away from smoking and limit your alcohol intake."}



    quotes =     ['"To anyone out there who’s hurting — it’s not a sign of weakness to ask for help. It’s a sign of strength." —Barack Obama',
    "The only time you fail is when you fall down and stay down.",
    "Every day may not be good... but there’s something good in every day.",
    '"Soak up the views. Take in the bad weather and the good weather. You are not the storm." —Matt Haig',
    "A journey of 1000 miles always begins with a single step."]


    p = vlc.MediaPlayer("theclimb.mp3")
    sad_song = "theclimb.mp3"
    happy_song = "toosieslide.mp3"
    meditation = "meditation.mp3"
    dance_party = "dance_party.mp3"

    def play_audio(filename):   
        p = vlc.MediaPlayer(filename)
        p.play()
        while True:
            user_input = input("Press 's' to end audio.")
            if user_input == 's':
                return p.stop()
                break
            else:
                print("Sorry, you can only press 's' to stop the audio.")

    if mood < 5 and selection == 1:
        play_audio(sad_song)
    elif mood < 5 and selection == 2:
        p1._User__write_in_journal()
    elif mood < 5 and selection == 3:
        play_audio(meditation)
    elif mood < 5 and selection == 4:
        index = random.randrange(0, 5)
        print(quotes[index-1])
    elif mood < 5 and selection == 5:
        for i in sorted(tips):
            print(i)

    if mood > 4 and selection == 1:
        play_audio(happy_song)
    elif mood > 4 and selection == 2:
        p1._User__write_in_journal()
    elif mood > 4 and selection == 3:
        p1._User__write_in_journal()
    elif mood > 4 and selection == 4:
        print(f'''Wow! Only {p1.calculate_days_till_bday(p1.birthday)} till your birthday.
        How will you celebrate and who will you invite?''')
        p1._User__write_in_journal()
    elif mood > 4 and selection == 5:
        play_audio(dance_party)

    user_input = input("Press 'b' to go back to the main menu or another character to exit the program.")

    if user_input == 'b':
        continue
    else:
        sys.exit(0)


# In[ ]:




