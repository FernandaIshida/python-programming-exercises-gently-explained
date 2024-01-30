def is_even(number):
    if (number % 2 == 0):
        return True
        print
    else:
        False

def is_odd(number):
    if (number % 2 == 0):
        return False
    else:
        True

def main():
    '''Function which executes the program'''
    number = int(input('Insert the number: '))
    if is_even(number):
        print('The number is even')
    else:
        print('The number is odd')

if __name__ == '__main__':
    main()