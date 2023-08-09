import os


def nmap(ip):
    var = f"nmap -A -p- -Pn {ip} -v"
    print(f'Running nmap against {var}')
    os.system(var)
    os.system(f'dirb {ip}')


nmap(input('What IP would you like to scan>>> '))
