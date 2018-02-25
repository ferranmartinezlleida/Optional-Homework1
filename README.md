# Optional-Homework1
This Python Script uses html scrapping to find out which book of the day packtpub is giving away daily. It also sends an email to the parameter provided mail adress, using a gmail server through smtplib python library.  

This scripts needs at least two parameters besides its name. The first one should be a gmail adress, and the second one its password. The third one is optional and is used to send the e-mail to a different e-mail adress. If one doesn't put this last parameter, the destination adress will be by default the gmail adress provided as the first parameter. 

To be able to use the script properly, not having a gmail adress, this dummy one is provided to be used in tests.

user: dummydumber@gmail.com

password: 12345678G


Parameter Ex:

./freebooks dummydumber9@gmail.com 12345678G <- The email will be sent to dummydumber9@gmail.com

./freebooks dummydumber9@gmail.com 12345678G exampleadress@mail.com <- The email will be sent to exampleadress@mail.com
