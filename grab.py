import requests

hamlet_url = 'http://www.gutenberg.org/cache/epub/1524/pg1524.txt'
hamlet_page = requests.get(hamlet_url)
hamlet_text = hamplet_page.text

for line in hamlet_text.splitlines():
  print(line)
