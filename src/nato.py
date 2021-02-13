# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 18:40:24 2021

@author: seaty
"""
nato_spelling = {
    "a": "Álfa",
    "b": "Brávo",
    "c": "Chárlie",
    "d": "Délta",
    "e": "Écho",
    "f": "Fóxtrot",
    "g": "Gólf",
    "h": "Hotél",
    "i": "Índia",
    "j": "Júliett",
    "k": "Kílo",
    "l": "Líma",
    "m": "Mike",
    "n": "Novémber",
    "o": "Óscar",
    "p": "Papá",
    "q": "Quebéc",
    "r": "Rómeo",
    "s": "Siérra",
    "t": "Tángo",
    "u": "Úniform",
    "v": "Víctor",
    "w": "Whísky",
    "x": "X-ray",
    "y": "Yánkee",
    "z": "Zúlu",
}

import argparse
import sys

def parseArguments():
    # Create argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('inputString', nargs='?', default="", help="Optional argument - if not provided, the program will prompt for a string.")
    return parser.parse_args()
    
    
def main():
    inputString = parseArguments().inputString
    while True:
        if inputString == "":
            inputString = input("Enter a String to be converted into the NATO Alphabet, or type exit:\n")
        inputString = inputString.lower()
        if inputString == "exit":
            sys.exit()
        for letter in inputString:
            print(letter + "\t" + nato_spelling.get(letter, letter))
        inputString = ""
            

if __name__ == "__main__":
    main()