#!/usr/bin/env python3
import sys
from search_word import *

def main():
    
    if len(sys.argv) > 2:
        word    = sys.argv[1]
        api_key = sys.argv[2]
        
        if word.isalpha():
            result  = webster_search(word, api_key)
            print(parse_word(result))
        else:
            print("Error: the string word must be only characters")
    else:
        print("Usage: {0} <word> <webster_api_key>".format(sys.argv[0]))

if __name__ == "__main__":
    main()