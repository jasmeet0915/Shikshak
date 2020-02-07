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
    'Content-Length': '838',
    'Connection': 'keep-alive',
    'TE': 'Trailers'
}

url = "https://api.smrzr.io/summarize?ratio=0.15"

data = """When you’re working with Python, you don’t need to import a library in order to read and write files. It’s handled natively in the language, albeit in a unique manner.

The first thing you’ll need to do is use Python’s built-in open function to get a file object.

The open function opens a file. It’s simple.

When you use the open function, it returns something called a file object. File objects contain methods and attributes that can be used to collect information about the file you opened. They can also be used to manipulate said file.

For example, the mode attribute of a file object tells you which mode a file was opened in. And the name attribute tells you the name of the file that the file object has opened.

You must understand that a file and file object are two wholly separate – yet related – things."""

r = requests.post(url=url, headers=headers, data=json.dumps(data))
print(r)
print(r.text)
