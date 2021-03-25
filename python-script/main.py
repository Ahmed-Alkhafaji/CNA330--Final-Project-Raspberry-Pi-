# This code is to ping my Raspberry Pi

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Luma")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    Pi = Server('10.0.0.12')
    # Call Ping method and print the results
    print(Pi.ping())
