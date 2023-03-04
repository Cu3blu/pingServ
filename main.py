import os
from datetime import datetime


def connList() -> list:
    """List of connections"""
    with open("ip_list.txt") as file:
        park = file.read()
        park = park.splitlines()
    return park


def start() -> None:
    park = connList()
    for ip in park:
        response = os.popen(f"ping -c 1 {ip} ").read()
        # Pinging each IP address 1 times
        # saving some ping output details to output file
        if ("Request timed out." or "unreachable") in response:
            f = open("ip_output.txt", "a")
            f.write(datetime.now() + '' + str(ip) + ' link is down' + '\n')
            f.close()




