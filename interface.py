from typing import Callable

# ANSI codes
def clear():
    print("\033[2J", end="")

def home():
    print("\033[H", end="")

def red(text):
    return f"\033[31m{text}\033[0m"

def green(text):
    return f"\033[32m{text}\033[0m"


def choice(opts: list[str], descr: list[str]|None = None, num_keys: bool = False, prompt: str|None = None) -> str:
    '''
    get the user to choose an option from <opts>.

    if passed, descr is a list of long-form descriptions corresponding to each key.

    if <num_keys>, use numeric keys. the user types the number of
    that choice rather than the literal string.

    If provided, use the given prompt, otherwise a generic prompt.
    '''

    # helper functions
    def print_opts():
        if prompt == None:
            print("choose one of the options below:")
        else:
            print(prompt)
        print()
        for i, opt in enumerate(opts):
            if num_keys:
                print(f"{i+1}. ", end="")
            print(opt)
        print()

    def validate(usr_choice):
        if num_keys:
            return validate_num(usr_choice)

        for opt in opts:
            if opt.lower().strip() == usr_choice.lower().strip():
                return True, opt

        return False, "Invalid choice. type one of the listed options."

    def validate_num(usr_choice):
        i = 0
        try:
            i = int(usr_choice)
        except ValueError:
            return False, f"Not a number. Enter a number {1}-{len(opts)}."

        if i < 1 or i > len(opts):
            return False, f"Enter a number {1}-{len(opts)}."

        return True, opts[i-1]

    #input validation
    if descr != None and len(opts) != len(descr):
        raise ValueError(f"provided number of options ({len(opts)}) and descriptions ({len(descr)}) does not match.")

    usr_choice = ""
    clear()
    home()
    try:
        while True:
            print_opts()
            usr_choice = input(">>> ")
            valid, res = validate(usr_choice)
            if valid:
                return res
            clear()
            home()
            print(red(res))
    except KeyboardInterrupt:
        print()
        return ""

def open_response(prompt: str, validator: Callable[[str], bool])-> str:
    '''
    get a user selected string and run it against the given validator
    function. The validator can safely print output to stdout and it will
    display logically.
    '''
    clear()
    home()
    usr_string = ""
    try:
        while True:
            print(prompt)
            usr_string = input(">>> ")
            clear()
            home()
            if validator(usr_string):
                return usr_string
    except KeyboardInterrupt:
        print()
        return ""
