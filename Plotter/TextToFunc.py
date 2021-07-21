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

def prepString(string : str) -> str:
    string = string.replace(" ","")
    string = string.lower()
    return string

# Find all words in the string and check if all are allowed:
def checkFuncInput(string : str):
    string = prepString(string)
    if string == "":
        return "Empty function string"
    else:
        # Checks all words to make sure it's in the allowed word list.
        # Returns true if the string is clean. Returns a message to be displayed in a message box otherwise.
        for word in re.findall('[a-zA-Z_]+', string):
            if word not in allowedWords:
                return f"{word} is not valid to use in math expression"
        return True

def evalFunction(string : str):
    string = prepString(string)
    for oldWord, newWord in replacements.items():
        string = string.replace(oldWord, newWord)
    def func(x):
        try:
            return eval(string)
        except (TypeError,SyntaxError,NameError):
            return False
    return func

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

    if evalFunction(mathText) == False:
        print("invalid inputs. Please check again.")
    else:
        if lowerBound >= upperBound: 
            print("Lower bound must be explicitly lower than the upper bound")
        else:
            if numberOfSamples <= 0: 
                print("Number of samples must be a positive integer")
            else:
                mathFunction = evalFunction(mathText)
                xValues = np.linspace(start = lowerBound, stop = upperBound, num = numberOfSamples)
                plt.plot(xValues, mathFunction(xValues))
                plt.xlim(lowerBound, upperBound)
                plt.show()