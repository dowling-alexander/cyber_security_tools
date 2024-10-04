Easy smtp enumeration script, need a user list, easiest to have in same directory as python script.

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
