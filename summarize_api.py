import requests
import json

headers = {
    'Host': 'api.smrzr.io',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://smrzr.io/',
    'Content-Type': 'raw/text',
    'Origin': 'https://smrzr.io',
    'Content-Length': '2753',
    'Connection': 'keep-alive',
    'TE': 'Trailers'
}

url = "https://api.smrzr.io/summarize?ratio=0.15"

data = """ 
Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you'd expect to be involved in anything strange or mysterious, because they just didn't hold with such nonsense.
Mr. Dursley was the director of a firm called Grunnings, which made
drills. He was a big, beefy man with hardly any neck, although he did
have a very large mustache. Mrs. Dursley was thin and blonde and had
nearly twice the usual amount of neck, which came in very useful as she
spent so much of her time craning over garden fences, spying on the
neighbors. The Dursleys had a small son called Dudley and in their
opinion there was no finer boy anywhere. """

r = requests.post(url=url, headers=headers, data=json.dumps(data))
print(r)

print(r.text)



