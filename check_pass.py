import requests
import hashlib
import sys


def api_res_check(input):
    url = 'https://api.pwnedpasswords.com/range/' + input
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching API, returned error code: {res.status_code}')
    return res


def pwnd_pass_check(hash_list, hash_to_be_checked):
    hash_list = (hash.split(':') for hash in hash_list.text.splitlines())
    for h, count in hash_list:
        if h == hash_to_be_checked:
            return count
    return 0


def pass_count(password):
    sha_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5char, tail = sha_pass[:5], sha_pass[5:]
    response = api_res_check(first5char)
    return pwnd_pass_check(response, tail)


def main(arguments):
    for pass1 in arguments:
        count = pass_count(pass1)
        if count:
            print(f'{pass1} was found {count} times.....Its time to change it')
        else:
            print(f'You\'re password {pass1} is safe')
    return 'done'

main(sys.argv[1:])









