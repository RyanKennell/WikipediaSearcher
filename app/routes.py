from app import app
from app.search_wikipedia import *
from flask import json, current_app

app.config["SERVER_NAME"] = "wiki-search.com:5000"


@app.route("/", subdomain="<term>")
def username_index(term):
    """
    Handles any subdomain routing
    
    Parameters
    ----------
    term : string
        subdomain being searched for on wikipedia
        
    Return
    ------
    JSON
        json data of the link of or disabiguate links for the subdomains page
    
    """
    result = query(term)
    print(result);
    return current_app.response_class(json.dumps( { "links" : result } ), mimetype="application/json")