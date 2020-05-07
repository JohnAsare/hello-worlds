# John Asare
# Date: Apr 13, 2020

""" Writing the first code for the Google Python Certificate """


def check_push(name):

    if name.isalpha:
        print("Howdy World!, I will call you by {}" .format(name))
    else:
        print("Please type a name")


check_push(name=input("What is your name? "))




