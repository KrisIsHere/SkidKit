import httplib as http
import sys

#this script uses HTTP headers to check if a website is hiding behind CloudFlare

CF_LOG = {'headers_found': 0, 'headers': []}

    
def check_get_headers(URL):
    conn = http.HTTPConnection(URL)
    conn.request("GET", "/")
    r1 = conn.getresponse()
    headers = r1.getheaders()
    return headers

def check_all_headers(headers):
    key_words = ['cf-ray', 'cloudflare', 'cfduid']
    for header in headers:
        if any(keys in header[0] or keys in header[1] for keys in key_words):
            CF_LOG['headers_found'] += 1
            CF_LOG['headers'].append(header)

def final_answer():
    if CF_LOG['headers_found'] > 0:
        print "CloudFlare found using the following headers:\n"
        for h in CF_LOG['headers']: print str(h)
    else:
        print "No CloudFlare found!"

def get_arguments():
    if len(sys.argv[1]) > 0:
        URL = sys.argv[1]
        check_all_headers(check_get_headers(URL))
    else:
        print "usage: python main.py xxx.com"
        
if __name__ == '__main__':
    get_arguments()
    final_answer()

