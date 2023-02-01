# Question: Determine if a string has all Unique Characters
# Article reference: https://www.geeksforgeeks.org/determine-string-unique-characters/

# Using a dictonary
# Time complexity - O(n)
# Space complexity - O(n)


def uniqueCharacters(s):
    uniqueCharacters = {}
    for c in s:
        if c in uniqueCharacters:
            return False
        else:
            uniqueCharacters[c] = 1
    return True

# Bit vector solution
# Time complexity - O(n)
# Space complexity - O(1)


def uniqueCharactersBitVector(string):
    # Assuming string can have characters
    # a-z this has 32 bits set to 0
    checker = 0

    for i in range(len(string)):
        bitAtIndex = ord(string[i]) - ord('a')

        print('bitAtIndex  ', bitAtIndex)

        # If that bit is already set in
        # checker, return False
        if ((bitAtIndex) > 0):
            print('(checker & ((1 << bitAtIndex)))  ',
                  (checker & ((1 << bitAtIndex))))
            if ((checker & ((1 << bitAtIndex))) > 0):
                return False
            print('1 << bitAtIndex  ', 1 << bitAtIndex)
            # Otherwise update and continue by
            # setting that bit in the checker
            print('checker | (1 << bitAtIndex)  ',
                  checker | (1 << bitAtIndex))
            checker = checker | (1 << bitAtIndex)

    # No duplicates encountered, return True
    return True


# Driver Code
if __name__ == '__main__':

    input = "geekforgeeks"

    if (uniqueCharacters(input)):
        print("The String " + input +
              " has all unique characters")
    else:
        print("The String " + input +
              " has duplicate characters")
