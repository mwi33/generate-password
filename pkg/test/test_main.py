import pytest
import pkg.main as main
import pkg.wordlist as word
import pkg.special_characters as characters

def test_generate_random_numbers():
    """ Testing objectives

    1.  The correnct number of integers has been created.
    2.  The upper limit has not been exceeded.
    3.  A type 'list' is returned.
    
    """

    #### Arrange ####

    ## NONE

    #### Act ####

    ## NONE ##

    # This is how many integers are required
    required_quantity = 10

    # Of the integers that are randomly created the largest cannot be larger than this value
    range_upper = 25

    #### Assert ####
    assert len(main.generate_random_numbers(required_quantity, range_upper)) == 10
    assert max(main.generate_random_numbers(required_quantity, 25)) <= 25
    assert type(main.generate_random_numbers(required_quantity, range_upper)) == list

    #### Cleanup ####

    ## NONE

def test_construct_words():
    """ Testing objectives

    1. Create a list of words from the specified wordlist
    2. A type 'list' is returned
    
    """

    #### Arrange ####

    ## NONE ##

    #### Act ####

    # Set wordlist
    wordlist = word.dictionary
    words = 5

    #### Assert ####
    assert len(main.construct_words(words, wordlist)) == 5
    assert type(main.construct_words(words, wordlist)) == list

    #### Cleanup ####

    ## NONE ##

def test_construct_special_characters():
    """ Testing objectives

    1.  Ensure that the correct number of caracters is provided.
    2.  Ensure that excluded characters are not included in the list.
    3.  ENsure that a type 'list' is returned.
    
    """

    #### Arrange ####

    #### Act ####
    # set special characters wordlist
    special_characters = characters.special_characters

    # number of special characters
    special = 3

    # characters to exclude
    exclude = '!'

    #### Assert ####

    assert len(main.construct_special_characters(special, exclude, special_characters)) == 3
    assert type(main.construct_special_characters(special, exclude, special_characters)) == list
    assert exclude not in main.construct_special_characters(special, exclude, special_characters)
    
    #### Cleanup ####

    ## NONE ##

def test_construct_digits():
    """ Testing objectives
    
    1. Ensure the correct number of digits is provided.
    2. Returns a list
    
    """

    #### Arrange ####

    ## NONE ##

    #### Act ####
    digits = 3

    #### Assert ####
    assert(len(main.construct_digits(digits))) == 3
    assert(type(main.construct_digits(digits))) == list

    #### Cleanup ####
    
    ## NONE ##

def test_construct_password():
    """ Testing objectives

    1.  Returns a string
    
    """
    #### Arrange ####

    ## NONE ##

    #### Act ####

    words = 7
    word_list = word.dictionary
    special = 3
    exclude = '%'
    special_characters = characters.special_characters 
    digits = 2

    #### Assert ####
    assert type(main.construct_password(words, word_list, special, exclude, special_characters, digits)) == str

    #### Cleanup ####

    ## NONE ##

def test_calculate_entropy():

    pass

def test_pwned():
    """ Testing objectives

    1.  Pass a password that is known to be comprimised to the 'have i been pwned' API.
    2.  Pass a password that is known to not be comprimised to the 'have i been pwned' API.
    3.  Retuns a string
    
    """
    #### Arrange ####

    ## NONE ##

    #### Act ####

    known_password = "password123"
    unknown_password = "dufRC#Hk6a85uC8!!utr"

    #### Assert ####
    assert main.pwned(known_password) == "Cracked"
    assert main.pwned(unknown_password) == "Not Cracked"
    assert type(main.pwned(known_password)) == str
    assert type(main.pwned(unknown_password)) ==  str

    #### Cleanup ####

    ## NONE ##

    def test_generate_password():
        """  Testing objectives
        1.  Run a single test which runs each indiviudal test 
        in a logical sequence and provides an overall view of 
        the application.

        2.  Return a pass/fail for each individual test case
        and for the entire application.
        
        """