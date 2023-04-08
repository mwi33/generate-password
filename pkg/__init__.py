import click
import pkg.main as main
import pkg.wordlist as word
import pkg.special_characters as characters
import pyfiglet


@click.command()
@click.option(
    "--numberpasswords", default=10, help="How many passwords are to be created"
)
@click.option("--words", default=4, help="Number of words to include")
@click.option("--special", default=2, help="Number of special characters to include")
@click.option(
    "--exclude", default=" ", help="Special characters that should be excluded.  e.g @#"
)
@click.option(
    "--digits", default=2, help="Number of digits to be included.  Default is 2"
)

def cli(words, special, exclude, digits, numberpasswords):


    art = pyfiglet.figlet_format("Generate Password")
    print(art)

    word_list = word.dictionary
    special_characters = characters.special_characters 
 
    entropy = main.calculate_entropy(special, exclude, digits, words, special_characters, word_list)
    print("--------------------------------------")
    print("Password Entropy is - " + str(entropy))

    for password in range(numberpasswords):

        password = main.construct_password(
        words, word_list, special, exclude, special_characters, digits
        )

        been_pwned = main.pwned(password)
        print("-------------------------------")
        print("Password is " + str(password))

        print("Has this password been cracked?: " + str(been_pwned))
        print("-------------------------------")
    
