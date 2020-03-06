import wikipedia


def query(search_term):
    """
    Tests to see if the subdomain searched
    is a disambiguate page or a independent
    page.
    """
    try:
        wikipedia.summary(search_term)
        return "https://en.wikipedia.org/wiki/" + search_term
    except wikipedia.exceptions.DisambiguationError as e:
        return handle_disambiguate_options(e.options)    
    
def handle_disambiguate_options(options):
    """
    If the page is disambiguate, it will contain
    multiple links to related pages. Here we remove
    any quotes or replace spaces with underscores.
    
    Parameters
    ----------
    options : List
        The links the disambiguate page contains
        
    Returns
    -------
    links : List
        The web URLs for wikipedia on the disambiguate page
    """
    
    links = []
    
    for link in options:
        link = str(link).replace('"', '').replace(' ', '_')
        links.append("https://en.wikipedia.org/wiki/" + link)
    return links