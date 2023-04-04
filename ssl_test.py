# # import re
# # import requests
# # import whois
# # import ssl
# # from datetime import datetime
# # from bs4 import BeautifulSoup
# # from tldextract import extract
# # import urllib.request

# # url = input('Enter URL: ')






# # #testing 1


# # def check_ssl(url):
# #     try:
# #         response = urllib.request.urlopen(url, timeout=10)
# #         if response:
# #             return True
# #     except:
# #         pass
# #     return False

# # def check_phishing(url):
# #     # Extract the domain from the URL

# #     def main():
# #         # url = input('Enter URL: ')
# #         is_phishing = check_phishing(url)
# #         if is_phishing:
# #             print(f'{url} is a phishing URL')
# #         else:
# #             print(f'{url} is not a phishing URL')


# #     ext = extract(url)
# #     domain = '{}.{}'.format(ext.domain, ext.suffix)

# #     # Check if domain is in a blacklist of known phishing sites
# #     with open('blacklist.txt') as f:
# #         blacklist = f.read().splitlines()
# #     if domain in blacklist:
# #         return True

# #     # Check if domain was recently registered (less than 1 year ago)
# #     try:
# #         w = whois.whois(domain)
# #         if w.creation_date:
# #             creation_date = w.creation_date[0]
# #             delta = (datetime.now() - creation_date).days
# #             if delta < 365:
# #                 return True
# #     except:
# #         pass

# #     # Check if URL has a suspicious format
# #     suspicious_formats = ['ip_address', 'long_number', 'double_slash', 'dash_count']
# #     if any(fmt in url for fmt in suspicious_formats):
# #         return True

# #     # Check if website contains suspicious keywords
# #     keywords = ['verify', 'security', 'banking', 'account', 'login']
# #     try:
# #         page = requests.get(url)
# #         soup = BeautifulSoup(page.content, 'html.parser')
# #         for keyword in keywords:
# #             if soup.find(text=re.compile(keyword, re.IGNORECASE)):
# #                 return True
# #     except:
# #         pass

# #     # Check if SSL certificate is present
# #     if not check_ssl(url):
# #         return True

# #     return False

# # def main():
# #     # url = input('Enter URL: ')
# #     is_phishing = check_phishing(url)
# #     if is_phishing:
# #         print(f'{url} is a phishing URL')
# #     else:
# #         print(f'{url} is not a phishing URL')

# # if __name__ == '__main__':
# #     main()




# # #testing 2





# # # import re
# # # import requests
# # # import whois
# # # import ssl
# # # import urllib
# # # from bs4 import BeautifulSoup
# # # from datetime import datetime
# # # from tldextract import extract


# # # # def main():
# # # #     url = input('Enter URL: ')
# # # #     is_phishing = check_phishing(url)
# # # #     if is_phishing:
# # # #         print(f'{url} is a phishing URL')
# # # #     else:
# # # #         print(f'{url} is not a phishing URL')

# # # if __name__ == '__main__':
# # #     main()



# # # def check_phishing(url):
# # #     # Extract the domain from the URL

# # #     def main():
# # #     url = input('Enter URL: ')
# # #     is_phishing = check_phishing(url)
# # #     if is_phishing:
# # #         print(f'{url} is a phishing URL')
# # #     else:
# # #         print(f'{url} is not a phishing URL')

# # # if __name__ == '__main__':
# # #     main()

    

# # #     # url = check_phishing('https://google.com')
# # #     ext = extract(url)
# # #     domain = '{}.{}'.format(ext.domain, ext.suffix)

# # #     # Check if domain is in a blacklist of known phishing sites
# # #     with open('blacklist.txt') as f:
# # #         blacklist = f.read().splitlines()
# # #     if domain in blacklist:
# # #         return True

# # #     # Check if domain was recently registered (less than 1 year ago)
# # #     try:
# # #         w = whois.whois(domain)
# # #         if w.creation_date:
# # #             creation_date = w.creation_date[0]
# # #             delta = (datetime.now() - creation_date).days
# # #             if delta < 365:
# # #                 return True
# # #     except:
# # #         pass

# # #     # Check if URL has a suspicious format
# # #     suspicious_formats = ['ip_address', 'long_number', 'double_slash', 'dash_count']
# # #     if any(fmt in url for fmt in suspicious_formats):
# # #         return True

# # #     # Check if website contains suspicious keywords
# # #     keywords = ['verify', 'security', 'banking', 'account', 'login']
# # #     try:
# # #         page = requests.get(url)
# # #         soup = BeautifulSoup(page.content, 'html.parser')
# # #         for keyword in keywords:
# # #             if soup.find(text=re.compile(keyword, re.IGNORECASE)):
# # #                 return True
# # #     except:
# # #         pass

# # #     # Check for SSL certificate
# # #     try:
# # #         # Use urllib to check SSL certificate
# # #         context = ssl.create_default_context()
# # #         with urllib.request.urlopen(url, context=context) as u:
# # #             pass
# # #     except ssl.SSLCertVerificationError:
# # #         return True
# # #     except:
# # #         pass

# # #     return False






# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# import joblib
# import re

# # Load the dataset
# data = pd.read_csv("phishing_dataset.csv")

# # Feature engineering
# def get_length(url):
#     return len(url)

# def get_special_char_count(url):
#     return len(re.findall("[!@#$%^&*(),.?\":{}|<>]", url))

# data["length"] = data["url"].apply(get_length)
# data["special_char_count"] = data["url"].apply(get_special_char_count)

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(data[["length", "special_char_count"]], data["label"], test_size=0.2, random_state=42)

# # Train the model
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# # Evaluate the model
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)

# # Save the model
# joblib.dump(model, "phishing_model.joblib")


with open("/Users/hemanthkumar/Desktop/phishing/links/domains.txt", "r") as infile, open("domain1.txt", "w") as outfile:
    lines = infile.readlines()
    for line in lines:
        line = line.replace("||", "")
        line = line.replace("^", "")
        line = "https://www." + line.strip()
        outfile.write(line + "\n")
