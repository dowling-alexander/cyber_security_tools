import telnetlib
import sys

def smtp_enum(host, port, wordlist):
    try:
        with open(wordlist, 'r') as file:
            users = file.readlines()
    except FileNotFoundError:
        print(f"Wordlist file '{wordlist}' not found.")
        return

    for user in users:
        user = user.strip()
        try:
            tn = telnetlib.Telnet(host, port)
            tn.read_until(b"\n")  # Read and discard the initial banner
            tn.write(b"HELO example.com\r\n")  # Send HELO command
            tn.read_until(b"\n")  # Read and discard the response to HELO
            tn.write(f"VRFY {user}\r\n".encode('ascii'))  # Send VRFY command
            response = tn.read_until(b"\n").decode('ascii')  # Read the response to VRFY
            tn.close()
            print(response)
            # Check for specific response codes
            if response.startswith("252") or response.startswith("250"):
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
