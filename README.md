# Generate-Password


## Table of Contents
1. Overview of the application
2. [Installation](Installation.md) of the application
3. [Implementation](Implementation.md)
4. [Calculating Entropy](Calculating%20Entropy.md)
5. [Unit testing](Unit%20Testing.md)

## Overview
'generate-password' is a Command Line Application (CLI) built with python and the ['Click'](https://palletsprojects.com/p/click/) framework.  Click is developed and supported by the ['Pallets Project'](https://palletsprojects.com/).

The rationale behind this project is to create simpler passwords for users whilst retaining high password entropy.  It utilises randomly selected words, special characters and digits, rather than just a selection of characters.  Password [entropy is calculated]('Calculating_entropy.md) for each password that is returned.

This application takes several arguments and returns a specified number of password options.  These passwords are constructed from two python dictionaries (words and special characters) contained in separate python modules as well as digits.

The user can configure this password by specifying: how many words should be used; how many special characters should be used; any special characters that should be excluded; and how many digits should be used.  It also allows the use to specify how many password options should be returned.