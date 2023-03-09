import os
import time
from datetime import datetime


def get_connection_list():
    """List of connections"""
    file = open("ip_list.txt")
    connections = file.read()
    connection_list = connections.splitlines()
    file.close()
    return connection_list
        
    
def send_error_message(unreachable_ip):
    """Sending a message to inform the administrator that a certain IP is unreachable"""
    error_message = str(unreachable_ip) + ' is unreachable!'
            

if __name__ == '__main__':
    
    connection_list = get_connection_list()
    failure_count_dict = {ip:0 for ip in connection_list}
    
    while True:
        for ip in connection_list:
            response = os.popen(f"ping -c 1 {ip} ").read()
            if "100% packet loss" in response:
                failure_count_dict[ip] = failure_count_dict[ip] + 1
                    
        for ip in failure_count_dict:
            if failure_count_dict[ip] == 5:
                send_error_message(ip)
                failure_count_dict[ip] = 0
        
        time.sleep(5)
