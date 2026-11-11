import re

with open('riemann_hypothesis/inprogress/arxiv_feed.xml', 'r') as f:
    content = f.read()

entries = re.findall(r'<entry>(.*?)</entry>', content, re.DOTALL)
print(f"Found {len(entries)} entries")

used_authors = ["Viachaslau I. Murashka", "Miguel Gentili", "Masatoshi Suzuki", "Chuangqiang Hu", "Xiao-Min Huang", "Guorui Ma", "Dan Pomerleano", "Paul Seidel", "Andrzej Dąbrowski", "Salah Eddine Rihane", "Gökhan Soydan", "Paul M. Voutier", "Juno Kwon", "Rak-Kyeong Seong", "Taiwang Deng", "Dongming She", "Anwesh Ray", "Mishty Ray", "Dylan Butson", "Sujay Nair", "Yichuan Cao", "Dakai Guo", "Ruichen Qiu", "Ruyong Feng", "Xiao-Shan Gao"]

for entry in entries:
    title = re.search(r'<title>(.*?)</title>', entry).group(1)
    authors = re.findall(r'<name>(.*?)</name>', entry)
    summary = re.search(r'<summary>(.*?)</summary>', entry, re.DOTALL).group(1)

    # Check if this author has been used
    new = True
    for a in authors:
        if any(ua in a for ua in used_authors):
            new = False
            break
    if new:
        print(f"\nTitle: {title}")
        print(f"Authors: {', '.join(authors)}")
        print(f"Summary: {summary.strip()}")
