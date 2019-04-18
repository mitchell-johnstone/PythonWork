# Each character on a computer is assigned a unique code and the preferred
# standard is ASCII (American Standard Code for Information Interchange).
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file,
# convert the bytes to ASCII, then XOR each byte with a given value,
# taken from a secret key. The advantage with the XOR function is that using
# the same encryption key on the cipher text, restores the plain text;
# for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message,
# and the key is made up of random bytes. The user would keep the encrypted message
# and the encryption key in different locations, and without both "halves",
# it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users,
# so the modified method is to use a password as a key. If the password is
# shorter than the message, which is likely, the key is repeated cyclically
# throughout the message. The balance for this method is using a
# sufficiently long password key for security, but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three
# lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'),
# a file containing the encrypted ASCII codes, and the knowledge that
# the plain text must contain common English words, decrypt the message and
# find the sum of the ASCII values in the original text.

# ^ is bitwise XOR
# & is bitwise and
# | is bitwise or

# ord() gets the ascii val of a character
# chr() turns the int into a char

def main():
    original = ""
    f = open("C:\\Programming\\Work\\Python\\PE\\P059_cipher.txt")
    for line in f:
        chars = line.split(",")
        for char in chars:
            original += chr(int(char))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char1 in alphabet:
        val1 = ord(char1)
        for char2 in alphabet:
            val2 = ord(char2)
            for char3 in alphabet:
                val3 = ord(char3)
    # for key in range(1*3, 3000*3):
                totalASCII = 0
                possibleAnswer = ""
                current = 0
                key = 0
                for i in original:
                    if(current%3==0):
                        key = val1
                    elif(current%3==1):
                        key = val2
                    elif(current%3==2):
                        key = val3
                    current+=1
                    i = ord(i)
                    ascii = i^key
                    totalASCII += ascii
                    possibleAnswer += chr(ascii)
                if("the" in possibleAnswer and "and" in possibleAnswer):
                    print()
                    print(possibleAnswer)
                    print(totalASCII)
                    print()
    return

if __name__ == '__main__':
    main()
