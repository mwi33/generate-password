# Entropy

Entropy is a concept that describes the randomness of something and in this application can be used to estimate how long it would take to brute-force an unknown password.  The higher the entropy the longer it will take to crack.

In computer science, password entropy is quantified as a number of bits.  A password entropy of 0 bits is a know password.  A password that requires at worst two guesses has an entropy of 1 bit.  A password with 'n' bits of entropy requires 2^n guesses to guarantee that the password will be found.

A 10 character long password that utilises upper and lower case letters and digits.  This means that the number of guesses to guarantee that the password will be found is 62^10.  62 is obtained from 26 lowercase letters, 26 uppercase letters and 10 digits.  The 10 is obtained from the number of characters in the password.

Finding the bits of entropy is calculated using the following:
 
 e = L * log(C)/log(2)
 
 Where 'L' = the length of the password; and 'C' =  the length of the character set 

Length = the number of words + the number of digits + the number of special characters
Character set = the length of the wordlist + 10 + (length of special characters - length of excluded)



## References
http://www.securitycentric.com.au/blog/bits-of-entropy-the-importance-of-complex-passwords

https://iocane.com.au/talking-passwords-and-entropy/

https://generatepasswords.org/how-to-calculate-entropy/
