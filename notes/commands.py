re.findall(r'[A-z][a-z]*', exampleString)

re.sub(r"[^a-zA-Z0-9]", " ", text)

from nltk.tokenize import word_tokenize

words = word_tokenize(text)
sentences = sent_tokenize(text)

