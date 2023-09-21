import argparse

# Setting up Argparse

def parse_args():

    parser = argparse.ArgumentParser(description='Bruteforcing subdomain tool')

    parser.add_argument('-u', '--url', help='Target domain', required=True)
    parser.add_argument('-w', '--wordlist', default='wordlists/top.txt', help='Wordlist file (default: top.txt)')
    return parser.parse_args()

