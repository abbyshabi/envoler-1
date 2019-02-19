import urllib.request,json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def configure_request(app):
    global api_key,base_url
