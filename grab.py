import requests

hamlet_url = 'http://www.gutenberg.org/cache/epub/1524/pg1524.txt'
hamlet_page = requests.get(hamlet_url)
hamlet_text = hamlet_page.text

hamlet_start = 290
hamlet_end = -7

hamlet_lines = hamlet_text.splitlines()[hamlet_start:hamlet_end]
hamlet_words = [word for line in hamlet_lines for word in line.split()]

def count_words(hamlet_words):
    hamlet_counts = {}
    for word in hamlet_words:
        if word not in hamlet_counts:
            hamlet_counts[word] = 0
        hamlet_counts[word] += 1
    return hamlet_counts

hamlet_counts = count_words(hamlet_words)
hamlet_total = sum(hamlet_counts.values())

feature_words = ['you', 'thou']

hamlet_data_tuples = [(word, hamlet_counts[word]) for word in feature_words]

hamlet_data = dict(hamlet_data_tuples + [('total', sum([tup[1] for tup in hamlet_data_tuples]))])

old_man_url = 'http://www.classic-enotes.com/american-literature/american-novel/ernest-hemingway/the-old-man-and-the-sea/full-text-of-the-old-man-and-the-sea-by-ernest-hemingway/'
old_man_page = requests.get(old_man_url)
old_man_html = old_man_page.text

old_man_lines = old_man_html.splitlines()
old_man_words = [word for line in old_man_lines for word in line.split()]
old_man_counts = count_words(old_man_words)

print old_man_counts

old_man_data_tuples = [(word, old_man_counts[word]) for word in feature_words]
old_man_data = dict(old_man_data_tuples + [('total', sum([tup[1] for tup in old_man_data_tuples]))])

def thou_to_you(d):
    return float(d['thou'])/d['you']

def distance(a, b):
    a_thou_to_you = thou_to_you(a)
    b_thou_to_you = thou_to_you(b)
    return a_thou_to_you-b_thou_to_you
