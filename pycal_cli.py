#! /bin/python3
import math

# functions

def percentage():
    value1 = input("Value: ")
    value2 = input("Value: ")

    deciminal = float(value1)/float(value2)
    percent = deciminal * 100
    percent = str(round(percent, 3))
    print(f"{percent}%")

def percentageincrease():
    y = input("Intial value: ")
    x = input("Final value: ")

    z1 = float(x)-float(y)
    z2 = z1/float(y)
    z3 = z2 * 100
    z4 = str(round(z3, 3))
    print(f"{z3}% increase.")

def percentagedecrease():
    y = input("Intial value: ")
    x = input("Final value: ")

    z1 = float(y)-float(x)
    z2 = z1/float(x)
    z3 = z2 * 100
    z4 = str(round(z3, 3))
    print(f"{z3}% decrease.")

def addition():
    while True:
        value1 = input("Selecetion: ")
        try:
            value1 = float(value1)
            break
        except:
            print("Please select a number!\n")
            continue
    while True:
        value2 = input("Selection: ")
        try:
            value2 = float(value2)
            break
        except:
            print("Please select a number!\n")
            continue
    answer = float(value1) + float(value2)
    print(f"Answer = {answer}")

def subtraction():
    while True:
        value1 = input("Selecetion: ")
        try:
            value1 = float(value1)
            break
        except:
            print("Please select a number!\n")
            continue
    while True:
        value2 = input("Selection: ")
        try:
            value2 = float(value2)
            break
        except:
            print("Please select a number!\n")
            continue
    answer = float(value1) - float(value2)
    print(f"Answer = {answer}")

def multiply():
    while True:
        value1 = input("Selecetion: ")
        try:
            value1 = float(value1)
            break
        except:
            print("Please select a number!\n")
            continue
    while True:
        value2 = input("Selection: ")
        try:
            value2 = float(value2)
            break
        except:
            print("Please select a number!\n")
            continue
    answer = float(value1) * float(value2)
    print(f"Answer = {answer}")

def division():
    while True:
        value1 = input("Selecetion: ")
        try:
            value1 = float(value1)
            break
        except:
            print("Please select a number!\n")
            continue
    while True:
        value2 = input("Selection: ")
        try:
            value2 = float(value2)
            break
        except:
            print("Please select a number!\n")
            continue
    answer = float(value1) / float(value2)
    print(f"Answer = {answer}")

def power():
    while True:
        value1 = input("Selecetion: ")
        try:
            value1 = float(value1)
            break
        except:
            print("Please select a number!\n")
            continue
    while True:
        value2 = input("Selection: ")
        try:
            value2 = float(value2)
            break
        except:
            print("Please select a number!\n")
            continue
    answer = float(value1) ** float(value2)
    print(f"Answer = {answer}")

def remainder():
    while True:
        value1 = input("Selecetion: ")
        try:
            value1 = float(value1)
            break
        except:
            print("Please select a number!\n")
            continue
    while True:
        value2 = input("Selection: ")
        try:
            value2 = float(value2)
            break
        except:
            print("Please select a number!\n")
            continue
    answer = float(value1) % float(value2)
    print(f"{answer} remaining")

def banner():
    print("""
    #######################################
    ############## Pycal-Cli ##############
    #######################################
    ############ <T3chn1ci4n> #############
""")
def help():
    print (""" This is a calculator that was made in Python3.
    Commands: 
        a = addition
        s = subtraction
        m = multiply
        d = division
        p = powers
        r = remainder
        pe = percentage
        pe+ = percentage increase
        pe- = percentage decrease
        b = banner
        h = help
        q = quit
""")

# main program

banner()
while True:
    operation = input("+-*/:")
    if "a" in operation:
        addition()
    elif "s" in operation:
        subtraction()
    elif "m" in operation:
        multiply()
    elif "d" in operation:
        division()
    elif "p" == operation:
        power()
    elif "r" in operation:
        remainder()
    elif "%" == operation:
        percentage()
    elif "%+" == operation:
        percentageincrease()
    elif "%-" == operation:
        percentagedecrease()
    elif "b" in operation:
        banner()
    elif "q" in operation:
        quit()
    elif "h" in operation:
        help()
    else:
        print("ERROR: Unknown command, use h command to view commands\n")
