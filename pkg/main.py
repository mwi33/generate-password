import random

from pkg import wordlist
import hashlib
import requests


def generate_random_numbers(quantity, range_upper):
    """ creates a list of random numers.

    Accepts arguments for the 'quantity' of numbers require and the upper limit of the range.
    Requires the 'random' library to be imported
    
    Returns list 'random_numbers'

    """

    random_numbers = [random.randint(0, range_upper) for x in range(0, quantity)]

    return random_numbers

def construct_words(words, wordlist):
    """ creates a list of random words.

    Accepts arguments for the number of required 'words' and a 'wordlist' to select the words from.

    Calls the 'generate_random_numbers' function and uses these to select words from the wordlist.

    Returns list 'password_words'    
    """
   
    password_words = [wordlist[index] for index in generate_random_numbers(words, len(wordlist)-1)]

    return password_words

def construct_special_characters(special, exclude, special_characters):
    """ creates a list of special characters

    Accepts arguments for the required number of 'special' characters, special characters to be excluded and the list of characters to 
    select special characters.

    Calls the 'generate_random_numbers' function and uses these to select the special characters.

    Returns list 'password_characters'
    """

    password_characters = []

    for character in exclude:
        
        if character in special_characters:

            special_characters.remove(character)

        else:
            
            break
        
    password_characters = [special_characters[index] for index in generate_random_numbers(special, len(special_characters)-1)]
    
    return password_characters

def construct_digits(digits):   
    """ creates a list of digits

    Accepts arguments for the required number of 'digits'.

    Calls the 'generate_random_numbers' function and uses these to select the digits.

    Returns list 'password_digits'
    """

    password_digits = []

    for x in range(0, digits):

        password_digits = generate_random_numbers(digits, 9)

    return password_digits

def construct_password(words, word_list, special, exclude, special_characters, digits):
    """ constructs the password

    Accepts arguments for words, word_list, special, excluded, special_characters and digits and assembles this into a 
    password string.

    Uses the 'randon.shuffle' method to shuffle the password items in the list.

    Returns string 'password'

    """
    password_list = construct_words(words, word_list) + construct_special_characters(special, list(exclude), special_characters) + construct_digits(digits)

    random.shuffle(password_list)

    password = ''.join(map(str, password_list))

    return password


def calculate_entropy(special, exclude, digits, words):
    """ Calculates the entropy of each password

    Accepts argumets for number of special characters, special characters to exclude, number of digits and number of words.

    returns integer 'possible_passwords'
    
    """

    password_space = len(wordlist.dictionary) + special + 10 # for digints

    password_length = words + (special - len(exclude)) + digits

    possible_passwords = pow(password_space, password_length)

    return possible_passwords

def pwned(password):
    """ checks to see if the generated password has been included in any known data breaches.

    Accepts an argument for the generated password.

    Calls the 'have i been pwned' API to check the password

    Returns a string indicating if the password has been cracked.
    """

    hash_list = []
    complete_hash = []

    # hash password sha1
    password_hash = hashlib.sha1(bytes(password, "utf-8")).hexdigest()

    # password the first 5 characters to the pwned api
    url =  "https://api.pwnedpasswords.com/range/" + str(password_hash[:5])

    request_response = requests.get(url)

    # create a list of the responses hashes
    hash_list = request_response.text.splitlines()

    # check each hash
    for hash in hash_list:
        
        complete_hash.append(password_hash[:5].upper() + hash[:35])

    if password_hash.upper() in complete_hash:

        return "Cracked"

    else:

        return "Not Cracked"