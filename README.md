# generate-password

## Overview
'generate-password' is a Command Line Application (CLI) built with python and the ['Click'](https://palletsprojects.com/p/click/) framework.  Click is developed and supported by the ['Pallets Project'](https://palletsprojects.com/).

The rationale behind this project is to create simpler passwords for users whilst retaining high password entropy.  It utilises randomly selected words, special characters and digits, rather than just a selection of characters.  Password [entropy is calculated]('Calculating_entropy.md) for each password that is returned.

This application takes several arguments and returns a specified number of password options.  These passwords are constructed from two python dictionaries (words and special characters) contained in separate python modules as well as digits.

The user can configure this password by specifying: how many words should be used; how many special characters should be used; any special characters that should be excluded; and how many digits should be used.  It also allows the use to specify how many password options should be returned.

## Installation

Clone repository

Create virtualenv

Activate virtualenv

pip install --editable .
pip install requests

run the generate-password command

~~~ bash
# clone repository
mwi33@mwi33:~/projects$ git clone https://github.com/mwi33/generate-password.git

mwi33@mwi33:~/projects$ cd generate-password

# create virtualenv v-gp
mwi33@mwi33:~/projects/generate-password$ virtualenv v-gp

mwi33@mwi33:~/projects/generate-password$ cd v-gp/bin

# activate virtual environment
mwi33@mwi33:~/projects/generate-password/v-gp/bin$ source activate

# enable the 'Click' application
mwi33@mwi33:~/projects/generate-password$ pip install --editable .

# return to home directory
(v-gp) mwi33@mwi33:~/projects/generate-password/v-gp/bin$ cd ../../

# run the command
mwi33@mwi33:~ generate-password

~~~



## Use