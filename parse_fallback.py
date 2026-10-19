import xml.etree.ElementTree as ET

try:
    with open('real_arxiv_feed.xml', 'r') as file:
        xml_data = file.read()

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
        print(f"Summary: {summary[:500]}\n")
except Exception as e:
    print("Error:", e)
