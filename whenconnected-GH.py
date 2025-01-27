# Send IP if and when we are connected
# Used to run at boot.

import smtplib
import requests
import urllib.request
import socket
import time
import platform
import distro

#############################################################################
# lets see if we can get a local ip 
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '0.0.0.0'
    finally:
        s.close()
    return IP
#############################################################################
# lets get the ip seen on the outside
def get_ip_address():
       url = 'https://api.ipify.org'
       response = requests.get(url)
       ip_address = response.text
       return ip_address
#############################################################################
# this looks for and waits for a connection
def wait_for_internet_connection():
    while True:
        try:
            # Attempt to connect to a well-known website
            response = urllib.request.urlopen('http://www.google.com', timeout=5)
            return
        except urllib.error.URLError:
            # print("No internet connection. Retrying in 5 seconds...")
            time.sleep(5)
#############################################################################
# This is the main function.
def main():
    # print("Waiting for internet connection...")
    wait_for_internet_connection()
    # print("Internet connection established. Proceeding with the script...")

    # lets get the OS info that this script is running on
    osname = distro.name()
    ostype = platform.platform()
    
    # We have a connection. lets let the admin know the IP to connect to PI, using API.
    string = osname + "\n"
    string = string + ostype + "\n"
    string = string + "WAN IP: " + get_ip_address() + "\n"
    string = string + "LOCAL IP: " + get_local_ip() + "\n"

    email = 'WHOITSFROM@gmail.com'
    receiver_email = 'WHOWILLGETEMAIL@gmail.com'

    subject = osname + ' is Online'
    message = string

    bodytext = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login(email,"YOUR API KEY")

    server.sendmail(email,receiver_email,bodytext)

# Once we are connected and the job is done, program ends..
# 

if __name__ == "__main__":
    main()

