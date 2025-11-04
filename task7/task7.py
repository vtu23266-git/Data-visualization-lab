from wordcloud import WordCloud
import nltk, re
from nltk.corpus import stopwords

text = open("text_data.txt","r").read().lower()
text = re.sub(r'[^a-z\s]', '', text)

stop = set(stopwords.words("english"))
words = [w for w in text.split() if w not in stop]
cleaned_text = " ".join(words)

wordcloud = WordCloud(width=800, height=400).generate(cleaned_text)
plt.imshow(wordcloud); plt.axis('off'); plt.show()

# WordTree and InfraNodus → (User Upload Step Only)
