import socket
import ssl
from urllib.parse import urlparse

def test_secure_port(url):
    # Parse the URL to get the hostname and port number
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    port = parsed_url.port or 443  # Use default port 443 if port number is not provided

    # Create a socket object and connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostname, port))

    # Wrap the socket with an SSL context
    ssl_context = ssl.create_default_context()
    ssl_socket = ssl_context.wrap_socket(sock, server_hostname=hostname)

    # Test if the SSL handshake was successful
    try:
        ssl_socket.getpeername()
        return True
    except ssl.SSLError:
        return False
    finally:
        # Close the SSL socket
        ssl_socket.close()

# Example usage
url = input("Enter the URL: ")
if test_secure_port(url):
    print(f"Port is secure for {url}")
else:
    print("random")
