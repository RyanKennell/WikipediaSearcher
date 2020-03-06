"""Test cases for the local host server
The server name and subdomains are defined
in the hosts file in order to make the web application work"""
r = requests.get("http://dogs.wiki-search.com:5000")
print(r.json())

r = requests.get("http://ordinary.wiki-search.com:5000")
print(r.json())