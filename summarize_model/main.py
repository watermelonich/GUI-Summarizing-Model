import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():

    nltk.download('punkt')

    url = utext.get('1.0', "end").strip()

    # Example:
    # url = 'https://edition.cnn.com/2020/09/13/tech/microsoft-tiktok-bytedance/index.html'

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    # print(f'Title: {article.title}')
    # print(f'Author/s: {article.authors}')
    # print(f'Publication date: {article.publish_date}')
    # print(f'Summary: {article.summary}')

    title.config(state='normal')
    author.config(state='normal')
    pubdate.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', "end")
    title.insert('1.0', article.title)

    author.delete('1.0', "end")
    author.insert('1.0', article.authors)
    
    pubdate.delete('1.0', "end")
    pubdate.insert('1.0', article.publish_date)

    summary.delete('1.0', "end")
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    pubdate.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

    # analysis = TextBlob(article.text)
    # print(analysis.polarity)

    # print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

root = tk.Tk()
root.title("Article Summarizer Model")
root.geometry('1200x600')

# Title
tlabel = tk.Label(root, text='Title')
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

# Author
alabel = tk.Label(root, text='Author/s')
alabel.pack()
author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

# Publication date
plabel = tk.Label(root, text='Publication Date')
plabel.pack()
pubdate = tk.Text(root, height=1, width=140)
pubdate.config(state='disabled', bg='#dddddd')
pubdate.pack()

# Summary
slabel = tk.Label(root, text='Summary')
slabel.pack()
summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

# Sentiment Analysis
selabel = tk.Label(root, text='Sentiment Analysis')
selabel.pack()
sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

# URL
ulabel = tk.Label(root, text='URL')
ulabel.pack()
utext = tk.Text(root, height=1, width=140)
utext.config(state='disabled', bg='#dddddd')
utext.pack()

# Summarize Button
btn = tk.Button(root, text="Summarize")
btn.pack()

root.mainloop()