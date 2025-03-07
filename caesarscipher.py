from operator import index
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. 
# You should be able to test the code and encrypt a message.
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
# TODO-5: Import and print the logo from art.py when the program starts.
# TODO-6: What happens if the user enters a number/symbol/space?
# TODO-7: Can you figure out a way to restart the cipher program?
# TODO-8: Call the caesar() function and pass in the user inputs.


#The encrypt() function takes the inputs of "original_text" and "shift".
#It will process a for loop towards the text input, take the number index of the letter from the alphabet 
# list and add the shift amount to it. For example, if the text input is "hello", the first letter is "h"
# which is at position 7 of the alphabet list. If we add 3 to 7, we get 10, which is at 
# position 10 of the alphabet list, which is the letter "k". 
# So the first letter of the encrypted text is "k".
def encrypt(original_text, shift_amount):
    cipher_text = "" #empty string to store the encrypted text

    for letter in original_text: #goes through all the letters from the original input text
        shifted_position = alphabet.index(letter) + shift_amount

        # If user tries to shift the letter "z" forward, it will have an out of bounds error. 
        # To keep us in the range of 0-25 of the alphabet list, we use the modelo operator
        shifted_position %= len(alphabet) 
        cipher_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")


#The decrypt function is the opposite of the encrypt function. 
#It will process a for loop towards the text input, take the number index of the letter from the alphabet 
# list and subtract the shift amount from it. For example, if the text input is "hello", the first letter is "h"
# which is at position 7 of the alphabet list. If we subtract 3 from 7, we get 4, which is at 
# position 4 of the alphabet list, which is the letter "e". 
# So the first letter of the decrypted text is "e".
def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the decrypted result: {cipher_text}")



#The encrypt() and decrypt() functions below can be ignored. 
#The caesar() function is the one we will use.
#The caesar() function is a more efficient way of writing the encrypt() and decrypt() functions.
#This function combines both the encrypt and decrypt functions.
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
                shift_amount *= -1
    #line 60 and 61 were originally placed inside for the loop below. 
    #This created an error which shifts the direction
    #from negative to positive every time the loop runs. 
    #So when we run the program back to back from encrypt to decrypt,
    #the output is incorrect.
    #By moving the lines 60 and 61 outside the for loop, we fix the error.

    for letter in original_text:
        if letter not in alphabet: #if the input is not from the alphabet, it will be included as is.
            output_text += letter
        else:    #if the input is from the alphabet, it will be shifted.

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")
    #adding the {encode_or_decode}d on line 66 will print out encode or decode in the past tense based 
    #on what the user chose.

should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to continue. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")

#after we combined the encrypt and decrypt functions into the caesar function, 
# we can call the caesar function and process the user inputs.
