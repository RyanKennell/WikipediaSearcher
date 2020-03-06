# WikipediaSearcher
A python web application that offers a way to search wikipedia

## Install
This solution requires flask and wikipedia to be installed
```
pip install flask
pip install wikipedia
```
To test locally, you need to add these entries to your windows `hosts` file
### Hosts file:
```
127.0.0.1 wiki-search.com 
127.0.0.1 dogs.wiki-search.com
127.0.0.1 ordinary.wiki-search.com
```

### Run
In the directory of the project, execute the following commands
```
export FLASK_APP=wikisearch.py
flask run
```
You can then either execute the `testcases.py` file or access the urls via a web browser.
