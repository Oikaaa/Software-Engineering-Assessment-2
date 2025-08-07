import string

def test(text):
    word_freq = {}
    words = text.lower().split()
    words = list(map(lambda word: ''.join(char for char in word if char not in string.punctuation), words))
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

with open('/Users/thangjimmy/Documents/Visual Code Folders/CS/dictionary/hamlet.txt', 'r') as f:
    content = f.read()
print(test(content))
