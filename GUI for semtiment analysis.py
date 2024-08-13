import tkinter as tk
from tkinter import filedialog, messagebox
from nltk.tokenize import sent_tokenize
import fitz  # PyMuPDF
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from transformers import pipeline
import pandas as pd
from afinn import Afinn
import os

vader_analysis = SentimentIntensityAnalyzer()
transformer_analysis = pipeline('sentiment-analysis')
affin_analysis = Afinn()


my_dict = {}

def append_to_dict(key, value):
    if key not in my_dict:
        my_dict[key] = []
    my_dict[key].append(value)


def upload_files():
    global filepaths
    try:
        filepaths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    except:
        messagebox.showerror("Error", "Please select a PDF file")
    else:
        sentiment_analysis()

def sentiment_analysis():
    for filepath in filepaths:
        try:
            pdf = fitz.open(filepath)
            text = ""
            for page in pdf:
                text += page.get_text()
        except Exception as e:
            messagebox.showerror(f"Error", f"Failed to extract text: {e}")
        else:
            sentences = sent_tokenize(text)
            vader_scores = []
            textblob_scores = []
            transformer_scores = []
            affin_scores =[]
            for sentence in sentences:
                if sentence.strip():
                    vader_score = vader_analysis.polarity_scores(sentence)['compound']
                    textblob_score = TextBlob(sentence).sentiment.polarity
                    transformer_score = transformer_analysis(sentence)[0]['label']
                    affin_score = affin_analysis.score(sentence)

                    vader_scores.append(vader_score)
                    textblob_scores.append(textblob_score)
                    transformer_scores.append(transformer_score)
                    affin_scores.append(affin_score)

            avg_vader = sum(vader_scores) / len(vader_scores)
            avg_textblob = sum(textblob_scores) / len(textblob_scores)
            avg_affin = sum(affin_scores) / len(affin_scores)
            transformer_sentiments = transformer_scores.count('POSITIVE') - transformer_scores.count('NEGATIVE')

            vader_sign = avg_vader > 0
            textblob_sign = avg_textblob > 0
            affin_sign = avg_affin > 0
            transformer_sign = transformer_sentiments > 0

            conflict_exists = (
                    vader_sign != textblob_sign or
                    textblob_sign != affin_sign or
                    affin_sign != vader_sign or
                    transformer_sign != vader_sign or
                    transformer_sign != textblob_sign or
                    transformer_sign != affin_sign
            )
            append_to_dict("Vader", avg_vader)
            append_to_dict("Textblob", avg_textblob)
            append_to_dict("Afinn", avg_affin)
            append_to_dict("Transformer",transformer_sentiments)
            append_to_dict("Conflict Exists", conflict_exists)
            append_to_dict("File Name",os.path.basename(filepath))

    save_results_to_excel(my_dict)



def save_results_to_excel(my_dict, filename='sentiment_analysis_results_GUI.xlsx'):
    df = pd.DataFrame(my_dict)
    flag = df.to_excel(filename, index=False)
    if flag:
        messagebox.showerror("Error", "Something went wrong")
    else:
        messagebox.showinfo("Success", "Results saved successfully")
        exit()



window = tk.Tk()
window.title('Sentiment Analysis')
window.geometry('500x500')
upload_button = tk.Button(window, text="Upload PDFs", command=upload_files)
upload_button.pack(pady=20)
window.mainloop()

