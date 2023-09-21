import socket

# Setting up classes and functions

class SubdomainEnumerator:
    def __init__(self, domain, wordlist):
        self.domain = domain
        self.wordlist = wordlist

    def enumerate_subdomains(self):
        try:
            print(f'\nUsing wordlist: {self.wordlist}\n')
            with open(self.wordlist, 'r') as wordlist_file:
                for line in wordlist_file:
                    subdomain = line.strip()
                    dns = f'{subdomain}.{self.domain}'
                    try:
                        ip_address = socket.gethostbyname(dns)
                        print(f'{dns} --> {ip_address}')
                    except socket.gaierror:
                        pass
        except FileNotFoundError:
            print(f'Wordlist file "{self.wordlist}" not found.') 
