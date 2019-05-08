from django.shortcuts import render
from random import choice
# from django.http import HttpResponse

# Create your views here.

#def index(request):
#    return HttpResponse('<h1> Im so new to Django!! </h1>')

keyboard_char='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!#@%&*'
keyboard_lower_char = 'abcdefghijklmnopqrstuvwxyz'
keyboard_upper_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
keyboard_int_char = '1234567890'
keyboard_symbol_char = "!@#$%^&*_-'"

def index(requests):

    return render(requests, 'djPassApp/index.html')


def main(request):
    removeSym = request.GET.get('removeSymbol', 'off')
    removeNum = request.GET.get('removeNumbers', 'off')
    removeLow = request.GET.get('removeLowercase', 'off')
    removeUpp = request.GET.get('removeUppercase', 'off')
    alldefault = request.GET.get('DEFAULT')
    allgg = request.GET.get('customRadio', 'default')
    all_pass_char = request.GET.get('customRadioInline', 'default')

    # Could be used for debugging
    # print(removeSym)
    # print(removeNum)
    # print(removeUpp)
    # print(removeLow)
    # print(alldefault)
    # print(allgg)

    hard_pass = ''

    if all_pass_char == '9D':
        ran_keyboard_char = ''
        ran_keyboard_lower_char = ''
        ran_keyboard_upper_char = ''
        ran_keyboard_symbol_char = ''
        ran_keyboard_int_char = ''

        for j in range(2):
            #hard_pass += choice(keyboard_char)
            ran_keyboard_char = ran_keyboard_char + choice(keyboard_char)
        for j in range(2):
            ran_keyboard_lower_char = ran_keyboard_lower_char + choice(keyboard_lower_char)
        for j in range(2):
            ran_keyboard_upper_char = ran_keyboard_upper_char + choice(keyboard_upper_char)
        for j in range(1):
            ran_keyboard_symbol_char = ran_keyboard_symbol_char + choice(keyboard_symbol_char)
        for j in range(2):
            ran_keyboard_int_char = ran_keyboard_int_char + choice(keyboard_int_char)

        hard_pass = str(ran_keyboard_char+ran_keyboard_lower_char+ran_keyboard_upper_char+ran_keyboard_symbol_char+ran_keyboard_int_char)

        if allgg == 'ExLwr':
            hard_pass = ''
            left_choice = keyboard_upper_char+keyboard_int_char+keyboard_symbol_char
            for j in range(9):
                hard_pass += choice(left_choice)

        elif allgg == 'ExUpr':
            hard_pass = ''
            left_choice = keyboard_lower_char+keyboard_symbol_char+keyboard_int_char
            for j in range(9):
                hard_pass += choice(left_choice)
                print("value is", hard_pass)

        elif allgg == 'ExInt':
            hard_pass = ''
            left_choice = keyboard_upper_char+keyboard_symbol_char+keyboard_lower_char
            for j in range(9):
                hard_pass += choice(left_choice)

        elif allgg == 'ExSymbol':
            hard_pass = ''
            left_choice = keyboard_upper_char + keyboard_int_char + keyboard_lower_char
            for j in range(9):
                hard_pass += choice(left_choice)

    elif all_pass_char == '8D':
        ran_keyboard_char = ''
        ran_keyboard_lower_char = ''
        ran_keyboard_upper_char = ''
        ran_keyboard_symbol_char = ''
        ran_keyboard_int_char = ''

        for j in range(2):
            #hard_pass += choice(keyboard_char)
            ran_keyboard_char = ran_keyboard_char + choice(keyboard_char)
        for j in range(2):
            ran_keyboard_lower_char = ran_keyboard_lower_char + choice(keyboard_lower_char)
        for j in range(1):
            ran_keyboard_upper_char = ran_keyboard_upper_char + choice(keyboard_upper_char)
        for j in range(1):
            ran_keyboard_symbol_char = ran_keyboard_symbol_char + choice(keyboard_symbol_char)
        for j in range(2):
            ran_keyboard_int_char = ran_keyboard_int_char + choice(keyboard_int_char)

        hard_pass = str(ran_keyboard_char+ran_keyboard_lower_char+ran_keyboard_upper_char+ran_keyboard_symbol_char+ran_keyboard_int_char)

        if allgg == 'ExLwr':
            hard_pass = ''
            left_choice = keyboard_upper_char+keyboard_int_char+keyboard_symbol_char
            for j in range(8):
                hard_pass += choice(left_choice)

        elif allgg == 'ExUpr':
            hard_pass = ''
            left_choice = keyboard_lower_char+keyboard_symbol_char+keyboard_int_char
            for j in range(8):
                hard_pass += choice(left_choice)
                print("value is", hard_pass)

        elif allgg == 'ExInt':
            hard_pass = ''
            left_choice = keyboard_upper_char+keyboard_symbol_char+keyboard_lower_char
            for j in range(8):
                hard_pass += choice(left_choice)

        elif allgg == 'ExSymbol':
            hard_pass = ''
            left_choice = keyboard_upper_char + keyboard_int_char + keyboard_lower_char
            for j in range(8):
                hard_pass += choice(left_choice)

    elif all_pass_char == '12D':
        ran_keyboard_char = ''
        ran_keyboard_lower_char = ''
        ran_keyboard_upper_char = ''
        ran_keyboard_symbol_char = ''
        ran_keyboard_int_char = ''

        for j in range(2):
            #hard_pass += choice(keyboard_char)
            ran_keyboard_char = ran_keyboard_char + choice(keyboard_char)
        for j in range(2):
            ran_keyboard_lower_char = ran_keyboard_lower_char + choice(keyboard_lower_char)
        for j in range(3):
            ran_keyboard_upper_char = ran_keyboard_upper_char + choice(keyboard_upper_char)
        for j in range(3):
            ran_keyboard_symbol_char = ran_keyboard_symbol_char + choice(keyboard_symbol_char)
        for j in range(2):
            ran_keyboard_int_char = ran_keyboard_int_char + choice(keyboard_int_char)

        hard_pass = str(ran_keyboard_char+ran_keyboard_lower_char+ran_keyboard_upper_char+ran_keyboard_symbol_char+ran_keyboard_int_char)

        if allgg == 'ExLwr':
            hard_pass = ''
            left_choice = keyboard_upper_char+keyboard_int_char+keyboard_symbol_char
            for j in range(12):
                hard_pass += choice(left_choice)

        elif allgg == 'ExUpr':
            hard_pass = ''
            left_choice = keyboard_lower_char+keyboard_symbol_char+keyboard_int_char
            for j in range(12):
                hard_pass += choice(left_choice)
                print("value is", hard_pass)

        elif allgg == 'ExInt':
            hard_pass = ''
            left_choice = keyboard_upper_char+keyboard_symbol_char+keyboard_lower_char
            for j in range(12):
                hard_pass += choice(left_choice)

        elif allgg == 'ExSymbol':
            hard_pass = ''
            left_choice = keyboard_upper_char + keyboard_int_char + keyboard_lower_char
            for j in range(12):
                hard_pass += choice(left_choice)


    elif all_pass_char == '16D':
        ran_keyboard_char = ''
        ran_keyboard_lower_char = ''
        ran_keyboard_upper_char = ''
        ran_keyboard_symbol_char = ''
        ran_keyboard_int_char = ''

        for j in range(3):
            ran_keyboard_char = ran_keyboard_char + choice(keyboard_char)
        for j in range(4):
            ran_keyboard_lower_char = ran_keyboard_lower_char + choice(keyboard_lower_char)
        for j in range(5):
            ran_keyboard_upper_char = ran_keyboard_upper_char + choice(keyboard_upper_char)
        for j in range(1):
            ran_keyboard_symbol_char = ran_keyboard_symbol_char + choice(keyboard_symbol_char)
        for j in range(3):
            ran_keyboard_int_char = ran_keyboard_int_char + choice(keyboard_int_char)

        hard_pass = str(ran_keyboard_char+ran_keyboard_lower_char+ran_keyboard_upper_char+ran_keyboard_symbol_char+ran_keyboard_int_char)

        if allgg == 'ExLwr':
            hard_pass = ''
            left_choice = keyboard_upper_char+keyboard_int_char+keyboard_symbol_char
            for j in range(16):
                hard_pass += choice(left_choice)

        elif allgg == 'ExUpr':
            hard_pass = ''
            left_choice = keyboard_lower_char+keyboard_symbol_char+keyboard_int_char
            for j in range(16):
                hard_pass += choice(left_choice)
                print("value is", hard_pass)

        elif allgg == 'ExInt':
            hard_pass = ''
            left_choice = keyboard_upper_char+keyboard_symbol_char+keyboard_lower_char
            for j in range(16):
                hard_pass += choice(left_choice)

        elif allgg == 'ExSymbol':
            hard_pass = ''
            left_choice = keyboard_upper_char + keyboard_int_char + keyboard_lower_char
            for j in range(16):
                hard_pass += choice(left_choice)


    params = {'modulated': hard_pass}
    return render(request, 'djPassApp/about.html', params)
    # return HttpResponse("<h1> Hey I'm hello world App </h1>")





