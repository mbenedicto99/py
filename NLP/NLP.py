import string

text = open("read.txt", encoding="utf-8").read()
lower = text.lower()
upper = text.upper()

#Em str.maketrans (str1, str2, str3)
#str1 = Caraxteres que serão substituidos
#str2 = Caracteres que substituirão
#str3 = Caracteres deleteados.

cleaned_text = lower.translate(str.maketrans('','',string.punctuation))
cleaned_text_str = lower.translate(str.maketrans('ea','wy',string.punctuation))

splittxt = cleaned_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

print('letras normais ->', text)
print('letras minusculas ->', lower)
print('letras maiusculas ->', upper)
print ('caracteres especiais ->', string.punctuation)
print ('tira especiais ->', cleaned_text)
print ('substitui caracteres->', cleaned_text_str)
print ('quebra texto em strings->', splittxt)