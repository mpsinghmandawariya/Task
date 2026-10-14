from collections import Counter, defaultdict
from spellchecker import SpellChecker
import re
spell=SpellChecker()
WORD_RE=re.compile(r"[A-Za-z']+")
CORPUS=[
"the quick brown fox jumps over the lazy dog","the weather is nice today","i am going to the market","i am going to school",
"i want to learn machine learning","i want to learn programming","this is a good day","this is a great project",
"artificial intelligence helps people","machine learning predicts the next word","please send me the details","thank you for your help",
"how are you doing today","i will be there soon","we are working on a project","the application is working correctly",
"i need to finish my work","have a nice day","good morning how are you","please let me know when you arrive",
"i would like to write a sentence","the next word prediction model","we can improve this application","thank you very much"]
bigrams=defaultdict(Counter);trigrams=defaultdict(Counter)
def tokenize(text):return WORD_RE.findall(text.lower())
for sentence in CORPUS:
 w=tokenize(sentence)
 for i in range(len(w)-1):bigrams[w[i]][w[i+1]]+=1
 for i in range(len(w)-2):trigrams[(w[i],w[i+1])][w[i+2]]+=1
def correct_text(text):
 corrections=[];corrected=text
 for token in dict.fromkeys(tokenize(text)):
  if len(token)<3:continue
  candidate=spell.correction(token)
  if candidate and candidate.lower()!=token.lower():
   corrections.append({"original":token,"corrected":candidate})
   corrected=re.sub(rf"\b{re.escape(token)}\b",candidate,corrected,flags=re.IGNORECASE)
 return corrected,corrections
def predict_next_words(text,limit=5):
 words=tokenize(text)
 if not words:return []
 candidates=trigrams.get((words[-2],words[-1]),Counter()).copy() if len(words)>=2 else Counter()
 if not candidates:candidates=bigrams.get(words[-1],Counter()).copy()
 if not candidates:candidates=Counter({"the":1,"and":1,"to":1,"you":1,"is":1})
 total=sum(candidates.values()) or 1
 return [{"word":word,"score":round(count/total,3)} for word,count in candidates.most_common(limit)]
