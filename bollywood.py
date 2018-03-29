from threading import Thread
from time import sleep
import pygame
import os

already_typed = []


def win_sound():
        laugh_sound = pygame.mixer.Sound('music/win_laugh.wav')
        laugh_sound.play()


def lose_sound():
        laugh_sound = pygame.mixer.Sound('music/lose_laugh.wav')
        laugh_sound.play()


def get_question():
    question = raw_input("\n\nEnter the movie name : ")
    user_inputs = []
    print "Hiding the movie name..."
    question = list(question)
    count = -1
    for item in question:
        count += 1
        user_inputs.insert(count, item)
    count = -1
    for item in question:
        count += 1
        user_inputs[count] = "_"
        if question[count] in ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u',' '):
            user_inputs[count] = question[count]

    sleep(0.3)
    os.system("clear")
    return question, user_inputs


def start_guessing(question, user_inputs):
    attempts_left = 12
    global already_typed
    print_current_status(attempts_left, user_inputs)
    while attempts_left > 0:
        ans = raw_input("\nEnter your choice : ")
        already_typed.append(ans)
##        if ans == "O":
##                attempts_left += 3
        if len(ans) > 1:
            if len(ans) == len(question):
                temp_count = -1
                for item in question:
                    temp_count += 1

                    if item == ans[temp_count]:
                        pass
                    else:
                        temp_count = False

                if temp_count is False:
                    print "You guessed Wrong movie name.."
                    print "You have got a punishment.. Attemps reduced by 3!!!!!"
                    sleep(1)
                    attempts_left -= 2

                else:
                    win_sound_thread = Thread(target = win_sound)
                    win_sound_thread.start()
                    print "Congo! You won!!!"
                    raw_input("\n\nPress enter to restart the game..")
                    return True
            else:
                print "You guessed Wrong movie name.."
                print "You have got a punishment.. Attemps reduced by 3!!!!!"
                sleep(1)
                attempts_left -= 2

        attempts_left -= 1
        count = -1
        for item in question:
            count += 1
            if item == ans:
                print "Your choice is correct!!"
                sleep(0.3)
                user_inputs[count] = item

        if question == user_inputs:
            print_current_status(attempts_left, user_inputs)
            win_sound_thread = Thread(target = win_sound)
            win_sound_thread.start()
            raw_input("Congo!!! You won the game!!")

            return True
        print_current_status(attempts_left, user_inputs)

    print "You lost the game :("
    lose_sound_thread = Thread(target = lose_sound)
    lose_sound_thread.start()
    print "\nThe movie was : ",
    for item in question:
        print item,
    raw_input("\n\nPress enter to restart the game..")
    os.system("clear")
    #playsound("/home/ghanshyam/game_over.mp3")


def print_current_status(attempts_left, user_inputs):
    global already_typed
    os.system("clear")
    print "\nYour Progress is : "
    for item in user_inputs:
        print item,

    print "\n\nYou have already typed : ",
    for item in already_typed:
        print item,
        print " ",

    print "\n\nNumber of Attempts left = " + str(attempts_left)
    print "\n\n"


if __name__ == '__main__':
    pygame.init()
    try:
        while True:
            print "\n\nGet ready to play the game...\n\n"
            #playsound("/home/ghanshyam/start_music.mp3")
            question, user_inputs = get_question()
            start_guessing(question, user_inputs)
            os.system("clear")
            already_typed = []
    except:
        pygame.quit()
        exit()
