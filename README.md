# generate-password

## Overview
'generate-password' is a Command Line Application (CLI) built with python and the ['Click'](https://palletsprojects.com/p/click/) framework.  Click is developed and supported by the ['Pallets Project'](https://palletsprojects.com/).

The rationale behind this project is to create simpler passwords for users whilst retaining high password entropy.  It utilises randomly selected words, special characters and digits, rather than just a selection of characters.  Password [entropy is calculated]('Calculating_entropy.md) for each password that is returned.

This application takes several arguments and returns a specified number of password options.  These passwords are constructed from two python dictionaries (words and special characters) contained in separate python modules as well as digits.

The user can configure this password by specifying: how many words should be used; how many special characters should be used; any special characters that should be excluded; and how many digits should be used.  It also allows the use to specify how many password options should be returned.