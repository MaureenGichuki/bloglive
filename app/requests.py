import urllib.request,json
from .models import Quote

def get_quote():
    with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_results = None

        if get_quote_response:
            quote = get_quote_response.get('quote')
            author = get_quote_response.get('author')
            quote_results = Quote(quote,author)

            return quote_results