import requests

def text_from_url(url):
    return requests.get(url).text

def words_from_text(text, first_line = 0, last_line = -1):
    lines = text.splitlines()[first_line:last_line]
    return [word for line in lines for word in line.split()]

def count_words(hamlet_words):
    hamlet_counts = {}
    for word in hamlet_words:
        if word not in hamlet_counts:
            hamlet_counts[word] = 0
        hamlet_counts[word] += 1
    return hamlet_counts

def features_from_counts(counts):
    feature_words = ['you', 'thou']
    return dict([(word, counts[word]) for word in feature_words])

def normalize_counts(counts):
    total_count = sum(counts.values())

    counts_copy = {}
    for k in counts.iterkeys():
        counts_copy[k] = float(counts[k]) / total_count

    return counts_copy
 
def distance(features1, features2):
    normalized1 = normalize_counts(features1)
    normalized2 = normalize_counts(features2)

    all_keys = normalized1.keys() + normalized2.keys()
    differences = {}
    for k in all_keys:
        differences[k] = normalized2.get(k, 0) - normalized1.get(k, 0)

    distance = sum([abs(diff) for diff in differences.values()])

    return distance
    
def extract_features(url, first_line = 0, last_line = -1):
    text = text_from_url(url)
    words = words_from_text(text)
    counts = count_words(words)
    features = features_from_counts(counts)
    return features

hamlet_features = extract_features('http://www.gutenberg.org/cache/epub/1524/pg1524.txt', first_line = 290, last_line = -7)
huck_finn_features = extract_features('http://www.gutenberg.org/cache/epub/76/pg76.txt', first_line = 572, last_line = -352)
old_man_features = extract_features('http://www.gutenberg.ca/ebooks/hemingwaye-oldmanandthesea/hemingwaye-oldmanandthesea-00-t.txt', first_line = 77, last_line = -30)

print "old man: %s" % old_man_features
print "hamlet: %s" % hamlet_features
print "huck finn: %s" % huck_finn_features

hamlet_distance = distance(old_man_features, hamlet_features)
huck_finn_distance = distance(old_man_features, huck_finn_features)

authors = ["Shakespeare", "Twain"]
if huck_finn_distance < hamlet_distance:
    authors.reverse()

print
print "Hemingway's writing is more similar to %s's than %s's" % tuple(authors)
