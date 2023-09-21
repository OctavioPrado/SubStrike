# Main code

from loader import SubdomainEnumerator
from arg_parser import parse_args
from logo import logo

def main():
    logo()
    args = parse_args()

    if args.url:
        subdomain_enumerator = SubdomainEnumerator(args.url, args.wordlist)
        subdomain_enumerator.enumerate_subdomains()

if __name__ == '__main__':
    main()

