# importing Flask and other modules
from flask import Flask, request, render_template 
import bs4 as bs
import urllib.request 
from nltk.corpus import stopwords
import pandas as pd

# Flask constructor
app = Flask(__name__)   
  

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = url in HTML form
       nurl = request.form.get("url")       
       raw_html = urllib.request.urlopen(nurl)  #request URL
       raw_html = raw_html.read()

       article_html = bs.BeautifulSoup(raw_html, 'lxml')  #get page content

       article_paragraphs = article_html.find_all('p') #get all data which is in paragraph

       article_text = ''
 
       for para in article_paragraphs:  
         article_text += para.text 
       corpus =article_text .lower().split() # Tokenizing Article_text
       filtered_sentence = [w for w in corpus if not w in stopwords.words()] #use nltk to remove stopwords
       df = pd.DataFrame(filtered_sentence) #converting list to dataframe
       result = df.value_counts().head(10) # here value_counts() function will give unique count of the words
                                          # and head(10) will display max used 10 words from url
       print(result)

       return article_text
    return render_template("index.html")
  
if __name__=='__main__':
   app.run()
  

 
