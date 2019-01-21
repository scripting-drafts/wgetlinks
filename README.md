# wgetlinks
This program is URL specific. Tweak it to make it work properly on other URL's.

It still lacks the Wget function. Meanwhile you can print a list of URL's and filenames.

Usage;
- Write your URL: "url = YOUR_URL".
- Write a regex aproximation of the download links URL's to this bit of the script: "links = re.findall(r'https://REGEX_URL', stringLinks, re.IGNORECASE)".

Provisional because unnecessary;
- Append the last file you downloaded at "lastBook = *** " and "if len(links) == 1 and lastBook >= *** " writing the number of the last file you were able to download.
- Write the number of files you're going to download at:"cnt = NUMBER", append it at "if len(links) == 1 and cnt <= NUMBER" and uncomment "cnt +=1"
- If you try the wget failures use the sleep function to prevent the interpreter's demise.

Dependencies;
- Python
- Wget
- Beautiful Soup

Aditional - Convert your url to regex with this [http://www.regexlab.com/wild2regex].

The Idea: To fetch download links and filenames from URL's and wget them.
