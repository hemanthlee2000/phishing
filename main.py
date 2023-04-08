import re
from bs4 import BeautifulSoup
import requests
import bs4
import urllib.parse
from urllib.parse import urlparse
import ssl
import datetime
import webbrowser
import socket
import whois
from datetime import datetime, timedelta


#############-------testing urls--------------##############################

main_url = "https://irp-cdn.multiscreensite.com/cc407b53/your-connection-is-not-secure-screenshot-min.png"

# url = "https://www.stern.nyu.edu/faculty/search_name_form"  #anchor links
# url = "https://www.freecodecamp.org/news/building-chrome-extension"  #contains '-'
# url = "http://colab.research.google.com/#scrollTo=pZ1oefxcqFdm"  #http
url = "https://web.whatsapp.com"   # secure
# url = "https://web.whats@app.com"  # contains "@"
# url = "https:.//www.instagram.ac.in"  # unknown url
# url = "https://www.inst.a.gram.com"  #more than 3 dots
# url = input("enter the url: ")
# url = "https://www.google.com/"        #safe port
# url = "https://example.com:445"        #safe port



################------dataset-------------#############

# url = input("Enter the URL: ")
blacklist_path = "/Users/hemanthkumar/Desktop/phishing/links1/blacklist1.txt"
domain_path = "/Users/hemanthkumar/Desktop/phishing/links1/domain1.txt"
# link_path = "/Users/hemanthkumar/Desktop/phishing/links1/links.txt"
phisher_path = "/Users/hemanthkumar/Desktop/phishing/links1/phisher.txt"
port_path = "/Users/hemanthkumar/Desktop/phishing/links1/port.txt"

def comparing(url):

    with open(blacklist_path) as f:
        blacklist = f.read().splitlines()

    with open(domain_path) as f:
        domain = f.read().splitlines()

    # with open(link_path) as f:
    #     link = f.read().splitlines()

    with open(phisher_path) as f:
        phisher = f.read().splitlines()

    if url in blacklist or url in domain or url in phisher:
        return True
    else:
        return False


#################-------domian------------####################

domain = urllib.parse.urlparse(url).netloc

########################--------@----------########################

def at_test(url):
    if re.search('@', url):
        return True
    else:
        return False

########################----------dash----------#######################

def dash_test(url):
    if re.search('-', url):
        return True
    else:
        return False

########################-----------dot-------------#######################

def dot_test(url):
    domain = urlparse(url).netloc
    dot_count = domain.count('.')
    if dot_count > 3:
        return True
    else:
        return False

#######################----------anchor test---------------########################

def anchor_test(url):
    try:
        soup = BeautifulSoup(requests.get(url).content, "html.parser").find_all("a")
        bio_links = []
        for a in soup:
            if 'href' in a.attrs and 'bio' in a['href']:
                bio_links.append(a['href'])
        return bio_links
    except requests.exceptions.ConnectionError:
        print("URL is unknown or cannot be accessed.")

######################-----------https or http test---------#######################

CA_BUNDLE = '/path/to/mozilla_certs.pem'

def https_test(url):
    scheme = urlparse(url).scheme
    if scheme == 'http':
        return scheme

#################-----------port test---------#######################

def test_secure_port(url):
    # Parse the URL to get the hostname and port number
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    port = parsed_url.port or 443  # Use default port 443 if port number is not provided
    port_number = port

    # Create a socket object and connect to the server
    with socket.create_connection((hostname, port)) as sock:
        # Wrap the socket with an SSL context
        ssl_context = ssl.create_default_context()
        with ssl_context.wrap_socket(sock, server_hostname=hostname) as ssl_socket:
            # Test if the SSL handshake was successful
            try:
                ssl_socket.getpeername()
                return True, port_number
            except ssl.SSLError:
                return False
            finally:
                ssl_socket.close()

port_number = test_secure_port(url)

############----------domain age----------##############

def domain_age(url):
    try:
        w = whois.whois(domain)
        if w.creation_date is not None:
            if isinstance(w.creation_date, list):
                creation_date = w.creation_date[0]
            else:
                creation_date = w.creation_date
            now = datetime.now()
            age = (now - creation_date).days
            if age < 30:
                return True
            else:
                return False
    except Exception as e:
        print("Error occurred while checking domain age:", e)
        return None
    
####################---------running defs----------#####################

def run_defs(url):
    messages = []
    if not urlparse(url).netloc:
        messages.append("URL is unknown")
        return messages
    if at_test(url):
        messages.append("URL contains '@' symbol")
    if dash_test(url):
        messages.append("URL contains '-' symbol")
    if dot_test(url):
        messages.append("URL contains more than 3 dots in domain")
    if anchor_test(url):
        messages.append("Page contains anchor links")
    scheme = https_test(url)
    if scheme:
        messages.append(scheme)
    if comparing(url):
        messages.append("phishing site")
    if not test_secure_port(url):
        messages.append("port appeared")
    if domain_age(url):
        messages.append("phishing")
    return messages

def append_url(url, port):
    with open(phisher_path, "a") as f:
        f.write('\n' + url)
    with open(port_path, 'a') as f:
        f.write('\n' + str(port))

def main():
    messages = run_defs(url)
    if messages:
        print("Warning: " + ', '.join(messages))
        append_url(url,port_number)
        webbrowser.open(main_url)
    else:
        print("URL is safe.")
        webbrowser.open(url)
        

main()

####################--------end of tests-------------#######################
