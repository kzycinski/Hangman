from random_words import RandomWords
import curses


k = 'a'

def get_random_word():
    rw = RandomWords()
    word = rw.random_word()
    return word


def get_word():
    word = get_random_word()
    return word


def game(stdscr):
    guessed = ''
    wrong = ''
    word = ''
    word = get_word()

    tries = 10
    guessed_number = 0


    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.clear()
    height, width = stdscr.getmaxyx()

    stdscr.clear()
    stdscr.refresh()

    while(tries != 0 and guessed_number != len(word)):

        stdscr.clear()
        stdscr.refresh()
        stdscr.attron(curses.color_pair(1))
        stdscr.attron(curses.A_BOLD)

        #printing word
        start_x_word = int((width // 2) - (len(word)))
        start_y_word = 11

        tmp = ""

        for letter in word:
            if letter in guessed:
                tmp += letter
            else:
                tmp += "-"
            tmp += " "

        stdscr.addstr(start_y_word, start_x_word, tmp)

        #print statusbar
        statusbarwrong = "Wrong letters: {} ".format(wrong)
        statusbartries = "Tries left: {}".format(tries)
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(height - 2, 0, statusbarwrong)
        stdscr.addstr(height - 2, 65, statusbartries)

        enter_message = "Enter your guess: "

        stdscr.addstr(1, 1, enter_message)

        curses.echo()
        stdscr.move(1,1+len(enter_message))


        tmp = stdscr.getstr(1,1+len(enter_message), 1)
        guess = tmp.decode("utf-8")
        curses.noecho()

        if not guess.isalpha():
            message = "Please enter valid character :c"
        elif guess in guessed or guess in wrong:
            message = "You already tried "
            message += guess
        elif guess in word:
            message = "Guess correct! :)"
            guessed += guess
            guessed_number += word.count(guess)
        else:
            message = "Wrong guess :("
            wrong += guess
            wrong += ' '
            tries -= 1

        press = "Press any key to continue"

        start_x_message = int((width // 2) - (len(message) // 2) - len(message) % 2)
        start_x_press = int((width // 2) - (len(press) // 2) - len(press) % 2)

        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(4, start_x_message, message)
        stdscr.attroff(curses.A_BOLD)
        stdscr.addstr(6, start_x_press, press)
        stdscr.attron(curses.A_BOLD)

        tmp = ""

        for letter in word:
            if letter in guessed:
                tmp += letter
            else:
                tmp += "-"
            tmp += " "

        stdscr.attron(curses.color_pair(1))

        stdscr.addstr(start_y_word, start_x_word, tmp)

        statusbarwrong = "Wrong letters: {} ".format(wrong)
        statusbartries = "Tries left: {}".format(tries)

        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(height - 2, 0, statusbarwrong)
        stdscr.addstr(height - 2, 65, statusbartries)
        stdscr.move(0,0)


        stdscr.attroff(curses.A_BOLD)
        stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()

    if tries == 0:
        stdscr.clear()
        stdscr.refresh()
        msg = "You lost :("
        word_msg = "Missing word: " + word
        try_or_quit = "Press 'q' to quit or 't' to try again!"

        start_x_msg = int((width // 2) - (len(msg) // 2) - len(msg) % 2)
        start_x_word_msg = int((width // 2) - (len(word_msg) // 2) - len(word_msg) % 2)
        start_x_try = int((width // 2) - (len(try_or_quit) // 2) - len(try_or_quit) % 2)

        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(4, start_x_msg, msg)
        stdscr.addstr(12, start_x_word_msg, word_msg)
        stdscr.addstr(20, start_x_try, try_or_quit)
        stdscr.move(0, 0)
        global k
        curses.noecho()
        k = stdscr.getch()
        stdscr.attroff(curses.A_BOLD)
        stdscr.attroff(curses.color_pair(1))

    else:
        stdscr.clear()
        stdscr.refresh()
        msg = "You won! :D"
        word_msg = "Missing word: " + word
        try_or_quit = "Press 'q' to quit or 't' to try again!"

        start_x_msg = int((width // 2) - (len(msg) // 2) - len(msg) % 2)
        start_x_word_msg = int((width // 2) - (len(word_msg) // 2) - len(word_msg) % 2)
        start_x_try = int((width // 2) - (len(try_or_quit) // 2) - len(try_or_quit) % 2)

        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(4, start_x_msg, msg)
        stdscr.addstr(12, start_x_word_msg, word_msg)
        stdscr.addstr(20, start_x_try, try_or_quit)
        stdscr.move(0, 0)
        curses.noecho()
        k = stdscr.getch()
        stdscr.attroff(curses.A_BOLD)
        stdscr.attroff(curses.color_pair(1))



def print_menu(stdscr):

    cursor_x = 0
    cursor_y = 0

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.clear()
    height, width = stdscr.getmaxyx()

    stdscr.clear()
    stdscr.refresh()


    title = "HANGMAN"[:width-1]
    subtitle = "Written by Krystian Życiński"[:width-1]
    press = "Press any key to continue"[:width-1]


    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
    start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
    start_x_press = int((width // 2) - (len(press) // 2) - len(press) % 2)

    start_y = int((height // 2) - 2)

    stdscr.attron(curses.color_pair(2))
    stdscr.attron(curses.A_BOLD)

    stdscr.addstr(start_y, start_x_title, title)

    stdscr.attroff(curses.color_pair(2))
    stdscr.attroff(curses.A_BOLD)

    stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
    stdscr.addstr(start_y + 3, start_x_press, press)

    stdscr.move(cursor_y, cursor_x)

    stdscr.refresh()

    stdscr.getch()

def main(stdscr):
    curses.wrapper(print_menu)

    height, width = stdscr.getmaxyx()

    stdscr.clear()
    stdscr.refresh()
    global k
    while(k != ord('q')):
        curses.wrapper(game)
        if k == ord('q'):
            return
        if k == ord('t'):
            continue
        else:
            while(k != ord('q') and k != ord('t')):
                stdscr.clear()
                stdscr.refresh()
                title = "Press 'q' to quit or 't' to try again!"
                start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
                stdscr.attron(curses.color_pair(1))
                stdscr.attron(curses.A_BOLD)

                stdscr.addstr(11,start_x_title,title)

                stdscr.attroff(curses.color_pair(1))
                stdscr.attroff(curses.A_BOLD)
                curses.noecho()
                curses.cbreak()
                k = stdscr.getch()


curses.wrapper(main)




