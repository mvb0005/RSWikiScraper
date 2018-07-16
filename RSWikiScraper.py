from bs4 import BeautifulSoup
import re
import requests

r = requests.get('http://2007rshelp.com/quests.php?id=122')
soup = BeautifulSoup(r.text, 'html.parser')


url = 'https://www.runehq.com/oldschoolquest'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

links = []

for tr in soup.find_all(href=re.compile('oldschoolquest/')):
    links.append((tr['href']))

print(links)

url = 'https://www.runehq.com'

for link in links:
    r = requests.get(url + link)
    soup = BeautifulSoup(r.text, 'html.parser')
    s = soup.find(text=re.compile('Skill/Other'))
    parsed_s = [c.split() for c in s.parent.next_sibling.text.split("\r\n")]
    skill_output = {}
    for o in parsed_s:
        if o[0] == "Level":
            o = o[1:]
        if o[0].isdigit():
            skill_output[o[1].upper()] = int(o[0])

    soup = BeautifulSoup(r.text, 'html.parser')
    s = soup.findAll(text=re.compile(
        'Items Needed to Complete Quest|Items Needed at Quest Start:'))
    items = []
    [items.extend(c.parent.next_sibling.text.split(",")) for c in s]
    print(link[16:], items)
    #print(link[16:], output)
