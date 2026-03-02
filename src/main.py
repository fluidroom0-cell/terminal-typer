import curses
import requests
from curses import window, wrapper


typing_test_examples = [
        # // Easy Level: Short sentences and common words
        "The cat runs through the garden.",
        "I like to eat pizza on Fridays.",
        "The sun shines in the blue sky.",
        "Tomorrow will be a very special day.",

        # // Medium Level: Punctuation and longer words
        "Technology advances quickly; we must learn to use it.",
        "Have you seen the new book I bought at the bookstore?",
        "Cooking is an art that requires a lot of patience and love.",
        "Success is not the end, failure is not fatal.",

        # // Difficult Level: Special characters and grammatical complexity
        "L'oiseau sings on the branch (France, 1992).",
        "The source code (main.js) has an error on line 42.",
        "Incredible! The price went up 15% this month ($150.00).",
        "Functional programming is a computing paradigm."
    ]

def getQuote():
    # try:
    #     res = requests.get("https://zenquotes.io/api/random")
    #     data = res.json()
    #     return data[0]['q']
    # except:
    #     return typing_test_examples[0]
    return typing_test_examples[0]
    


def main(stdscr):

    curses.curs_set(0)  
    # colors
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK) 
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK) 

    MAGENTA = curses.color_pair(1)
    GREEN = curses.color_pair(2)
    RED = curses.color_pair(3)
    TITLE = "Type the example you see correctly"
    current_color = GREEN
    current_quote = getQuote()
    usr_attempts = 0 
    usr_errors = 0
    usr_hits = 0
    replacement_str = ""

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        XTITTLE, YTITTLE = ((width//2) - (len(TITLE)//2)), 2 
        XQUOTE, YQUOTE = abs((width//2) - (len(current_quote)//2)), height//2
        XERRORS, YERRORS = width//15, height - 5
        XHITS, YHITS = width//15, height - 4
        XATTEMP, YATTEMP = width//15, height - 3
        stdscr.addstr(YTITTLE, XTITTLE, TITLE, MAGENTA)
        stdscr.addstr(YQUOTE, XQUOTE, current_quote)
        stdscr.addstr(YQUOTE, XQUOTE, replacement_str, current_color)
        stdscr.addstr(height - 3, width - 15, f"[{width}, {height}]")
        stdscr.addstr(YERRORS, XERRORS, f"Errors > {usr_errors}", RED)
        stdscr.addstr(YHITS, XHITS, f"Hits > {usr_hits}", GREEN)
        stdscr.addstr(YATTEMP, XATTEMP, f"Attemps > { usr_attempts}", GREEN)
        stdscr.refresh()

        if usr_attempts == len(current_quote):
            stdscr.clear()
            stdscr.refresh()
            usr_attempts = 0 
            replacement_str = ""
            current_color = GREEN
            current_quote = getQuote()
            continue

        key = stdscr.getch()

        if ord(current_quote[usr_attempts]) == key:
            replacement_str += current_quote[usr_attempts]
            usr_attempts += 1
            usr_hits += 1
            current_color = GREEN
            
        else:
            replacement_str += current_quote[usr_attempts]
            usr_attempts += 1 
            usr_errors += 1 
            current_color = RED 

if __name__ == '__main__':
    wrapper(main)

