import urllib.request
import xml.etree.ElementTree as ET
import sys
import os

url = "http://export.arxiv.org/api/query?search_query=cat:math.NT+OR+cat:math.AG&sortBy=submittedDate&sortOrder=desc&max_results=5"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        xml_data = response.read()

    root = ET.fromstring(xml_data)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    for entry in root.findall('atom:entry', ns):
        title = entry.find('atom:title', ns).text.strip()
        authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)]
        summary = entry.find('atom:summary', ns).text.strip()
        id_val = entry.find('atom:id', ns).text
        print(f"ID: {id_val}")
        print(f"Title: {title}")
        print(f"Authors: {', '.join(authors)}")
        print(f"Summary: {summary[:200]}...\n")
except Exception as e:
    print("Error:", e)
    # try looking for a fallback file
    for f in ["real_arxiv_feed.xml", "arxiv_results.xml"]:
        if os.path.exists(f):
            print(f"Found local fallback {f}")
            with open(f, 'r') as file:
                print(file.read()[:1000])
