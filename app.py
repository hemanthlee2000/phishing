from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
    url = input("Enter the URL: ")
    url1 = "https://chat.openai.com/chat/31df4c4a-4318-4dc3-af8d-5877e69b5a06"
    blacklist_path = "/Users/hemanthkumar/Desktop/phishing/links/blacklist.txt"
    domain_path = "/Users/hemanthkumar/Desktop/phishing/links/domains.txt"
    inactive_path = "/Users/hemanthkumar/Desktop/phishing/links/inactive.txt"
    link_path = "/Users/hemanthkumar/Desktop/phishing/links/links.txt"
    active_path = "/Users/hemanthkumar/Desktop/phishing/links/active.txt"

    with open(blacklist_path) as f:
        blacklist = f.read().splitlines()

    with open(domain_path) as f:
        domain = f.read().splitlines()

    with open(inactive_path) as f:
        inactive = f.read().splitlines()

    # with open(link_path) as f:
    #     link = f.read().splitlines()

    with open(active_path) as f:
        active = f.read().splitlines()

    if url in blacklist or url in domain or url in inactive :
        return redirect(url1)
    elif url in active:
        return redirect(url)

    

if __name__ == "__main__":
    app.run()

