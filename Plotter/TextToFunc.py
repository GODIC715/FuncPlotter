import matplotlib.pyplot as plt
import numpy as np
import re

replacements = {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**'}

allowedWords = [
    'x',
    'sin',
    'cos',
    'sqrt',
    'exp']

def checkFuncInput(string : str):
    # find all words in the string and check if all are allowed:
    string = string.replace(" ","")
    if string == "":
        return "Empty function string"
    else:
        string = string.lower()
        for word in re.findall('[a-zA-Z_]+', string):
            if word not in allowedWords:
                return f"{word} is not valid to use in math expression"
        return True

def evalFunction(string : str):
    string = string.replace(" ","")
    for oldWord, newWord in replacements.items():
        string = string.replace(oldWord, newWord)
    def func(x):
        try:
            return eval(string)
        except (TypeError,SyntaxError):
            return False
    return func

def mainFunc(string : str):
    if checkFuncInput(string):
        return evalFunction(string)
    else:
        return False

if __name__ == '__main__':
    mathText = input('enter function: f(x) = ')
    if mathText == "":
        print("Empty/invalid function input.")
        exit()
    try:
        lowerBound = float(input('enter lower limit: '))
        upperBound = float(input('enter upper limit: '))
        numberOfSamples = int(input('enter number of samples to generate: '))
    except ValueError:
        print("Invalid inputs in bounds and/or number of samples")
        exit()

    if mainFunc(mathText) == False:
        print("invalid inputs. Please check again.")
    else:
        if lowerBound != upperBound:
            if lowerBound < upperBound:
                if numberOfSamples > 0:
                    mathFunction = mainFunc(mathText)
                    xValues = np.linspace(start = lowerBound, stop = upperBound, num = numberOfSamples)
                    plt.plot(xValues, mathFunction(xValues))
                    plt.xlim(lowerBound, upperBound)
                    plt.show()
                else:
                    print("Number of samples must be a positive integer")
            else:
                print("Lower bound must be lower than the upper bound")
        else:
            print("The lower bound must not equal the upper bound")