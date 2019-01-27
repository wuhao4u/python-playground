import urllib

urls = ['http://www.yahoo.com', 'http://www.reddit.com']
results = map(urllib.request.urlopen, urls)

for r in results:
    print(r.read())
