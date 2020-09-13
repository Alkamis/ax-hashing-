import hashlib
import pyfiglet

from termcolor import cprint

cprint(pyfiglet.figlet_format('HASHING', font='starwars'),
       'blue', attrs=['bold'])

mnue = 1

while True:

    try:
        mnue = int(input("Choose The Hash Type : \n 1- md5sum \n 2- sha1sum \n 3- sha256sum \n 4- Exit \n "))

    except ValueError:
        print("Oops! that was no valid input. please try again...\n")
        break






    if mnue == 1:
        text = str(input("Enter The Text You Want To Hash It : "))
        # the user will enter value to hash it

        # encoding text  using encode()
        # then sending to md5()
        result = hashlib.md5(text.encode())

        # printing hash value
        print("The md5sum Hash is : ", end='')
        print(result.hexdigest()) # end if 1
        print("--------------------------------md5sum-----------------------------------")

    elif mnue == 2:
        text = str(input("Enter The Text You Want To Hash It : "))
        # the user will enter value to hash it

        # encoding text  using encode()
        # then sending to sha1()
        result = hashlib.sha1(text.encode())

        # printing the equivalent hexadecimal value.
        print("The sha1sum Hash is : ", end='')
        print(result.hexdigest())  # end elif
        print("--------------------------------sha1sum-----------------------------------")

    elif mnue == 3 :
        text = str(input("Enter The Text You Want To Hash It : "))
        # the user will enter value to hash it

        # encoding text  using encode()
        # then sending to sha256()
        result = hashlib.sha256(text.encode())

        # printing the equivalent hexadecimal value.
        print("The sha256sum Hash is : ", end='')
        print(result.hexdigest())  # end elif 2
        print("--------------------------------sha256sum----------------------------------")

    else:
        cprint(pyfiglet.figlet_format('See You :)', font='starwars'),
               'blue', attrs=['bold'])
        break






