Easy smtp enumeration script, it will quary an SMTP service against a user list.

For an explanation of SMTP codes:
https://serversmtp.com/smtp-error/
explains why 250 and 252 are the correct responses.

===========================================================================================
run command ---> pentester$ ./enum_smtp.py <ip> <port> <wordlist>
550 5.1.1 <james>: Recipient address rejected: User unknown in local recipient table

User not found: james
252 2.0.0 robin

User found: robin
550 5.1.1 <sally>: Recipient address rejected: User unknown in local recipient table

User not found: sally
===========================================================================================

Output will say if a user is found or is not found.

Thanks to HTB for the inspiration to make this script in there host enumeration course.

TODO:
Telnetlib is being depreciated, need to fix/replace
move to argparser maybe if features etc are required.
