# wgetlinks
This program is URL specific. Tweak it to make it work properly on other URL's.

It still lacks the Wget function. Meanwhile you can print a list of URL's and filenames.


Fetch download links and filenames from URL's and wget them.


Usage;
- Write your URL: "url = YOUR_URL".
- Write a regex aproximation of the download links URL's to this bit of the script: links = re.findall(r'https://REGEX_URL).
Protip - Convert your url to regex with [http://www.regexlab.com/wild2regex].

Dependencies;
- Python
- Wget
- Beautiful Soup
