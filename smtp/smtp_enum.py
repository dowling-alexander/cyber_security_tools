import telnetlib
import sys

def smtp_enum(host, port, wordlist):
    try:
        with open(wordlist, 'r') as file:
            users = file.readlines()
    except FileNotFoundError:
        print(f"Wordlist file '{wordlist}' not found.")
        return

    #goes through each user in the list, uses the VRFY command to see if the user is found, uses specific 252,250 code to verify this. 
    for user in users:
        user = user.strip()
        try:
            tn = telnetlib.Telnet(host, port)
            tn.read_until(b"220")
            tn.write(f"VRFY {user}\r\n".encode('ascii'))
            response = tn.read_until(b"\r\n").decode('ascii')
            tn.close()
            if "252" in response or "250" in response:
                print(f"User found: {user}")
            else:
                print(f"User not found: {user}")
        except Exception as e:
            print(f"Error connecting to {host}:{port} - {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python smtp_enum.py <host> <port> <wordlist>")
    else:
        smtp_enum(sys.argv[1], int(sys.argv[2]), sys.argv[3])
