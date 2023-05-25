# Installation

## Installation overview

generate-password is a command line application, which is built on the 'Click' framework.  

Broadly, installation of the application requires the following steps:

1.  Clone this repository 'https://github.com/mwi33/Notes.git';
2.  Create a virtualenv and activate;
3.  Install the required libraries using the provided 'requirements.txt'; and
4.  Initialise the 'click' framework.

### Clone the repository
``` bash

# clone the generate-password repository
git clone https://github.com/mwi33/generate-password.git

```
### Create a virtual environment and install dependencies

``` bash

# from within the application directory
# create a virtual environment
virtualenv v-gp

# navigate to the 'bin' directory and activate the virtualenv
# v-gp/bin

source activate

# navigate to the generate-password directory and
# install the required libaries
pip install requirements.txt

# initialise the 'click' framework
# this only has to be undertaken the first time

```
### Activate the 'Click' framework

``` bash

# initialise the 'click' framework
# this only needs to be done once

pip install --editable .

```
