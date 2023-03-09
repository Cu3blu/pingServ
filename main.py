import os
import time
from datetime import datetime


def get_connection_dict():
    """List of connections"""
    file = open("ip_list.txt")
    connections = file.read()
    connection_list = connections.splitlines()
    connection_dict = {key.split()[0]:key.split()[1] for key in connection_list}
    file.close()
    return connection_dict

    
def send_error_message(hub_code):
    """Sending a message to inform the administrator that a certain IP is unreachable"""
    error_message = str(hub_code) + ' is unreachable!'
            

if __name__ == '__main__':
    
    connection_dict = get_connection_dict()
    failure_count_dict = {ip:0 for ip in connection_dict.keys()}
    
    while True:
        for ip in connection_dict:
            response = os.popen(f"ping -c 1 {ip} ").read()
            if "100% packet loss" in response:
                failure_count_dict[ip] = failure_count_dict[ip] + 1
                    
        for ip in failure_count_dict:
            if failure_count_dict[ip] == 5:
                send_error_message(connection_dict[ip])
                failure_count_dict[ip] = 0
        
        time.sleep(5)
