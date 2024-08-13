# Sentiment Analysis GUI Tool

This project is a Python-based GUI tool for performing sentiment analysis on text extracted from PDF files. The tool uses various sentiment analysis techniques and libraries, including VADER, TextBlob, Afinn, and a transformer-based model from the Hugging Face library. The results are saved in an Excel file.

## Features

- GUI Interface: A simple and user-friendly interface built with Tkinter.
- Multiple Sentiment Analysis Tools: Utilizes VADER, TextBlob, Afinn, and Transformer models for sentiment analysis.
- Conflict Detection: Identifies if there is a conflict in the sentiment analysis results among the different tools.
- PDF Text Extraction: Extracts text from uploaded PDF files using the PyMuPDF (fitz) library.
- Excel Export: Saves the sentiment analysis results into an Excel file.

## Requirements

Ensure you have the following Python packages installed:
`pip install nltk pymupdf vaderSentiment textblob transformers pandas afinn tk`

## How to Use

1. Clone the Repository: `git clone https://github.com/yourusername/sentiment-analysis-gui.git` and navigate to the directory.
2. Run the Script.
3. Upload PDF Files: Click the "Upload PDFs" button to select one or more PDF files from your system.
4. Sentiment Analysis: The tool will automatically extract the text from the selected PDF files, perform sentiment analysis using multiple tools, and detect any conflicts in the sentiment results.
5. Save Results: The results, including average sentiment scores and any detected conflicts, will be saved to an Excel file named `sentiment_analysis_results_GUI.xlsx` in the same directory as the script.

## Notes

- Sentiment Analysis Tools:
  - VADER: Provides a compound score ranging from -1 (negative) to +1 (positive).
  - TextBlob: Provides a polarity score ranging from -1 (negative) to +1 (positive).
  - Afinn: Provides a sentiment score based on word affinities.
  - Transformer: Uses a pre-trained transformer model for sentiment classification (positive/negative).
- Conflict Detection: The tool identifies conflicts when different sentiment analysis tools produce conflicting sentiment signs (e.g., one tool shows positive sentiment while another shows negative sentiment).

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

