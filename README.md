# Sentiment Analysis

A Python project that analyzes customer feedback using NLP and classifies it as **Positive 😊**, **Neutral 😐**, or **Negative 😞**.

## About

This project uses Natural Language Processing (NLP) to detect the sentiment of customer reviews and feedback. It processes text input, calculates polarity and subjectivity scores, and returns an emoji-based classification.

## Features

- Classifies feedback into Positive, Neutral, or Negative
- Emoji reaction for each result 😊 😐 😞
- Displays polarity and subjectivity score
- Batch analysis for multiple feedbacks
- Interactive mode — user can type feedback live
- Summary report at the end

## Technologies Used

- Python 3
- TextBlob (NLP Library)

## Installation

```bash
pip install textblob
python -m textblob.download_corpora
```

## How to Run

```bash
python sentiment_analysis.py
```

## Sample Output

```
=======================================================
  Feedback    : Great quality and very fast shipping!
  Sentiment   : 😊  Positive
  Polarity    : 0.65
  Subjectivity: 0.6
=======================================================
```

## Project Structure

```
sentiment-analysis/
│
├── sentiment_analysis.py   # Main Python file
└── README.md               # Project documentation
```

## Submitted By

- **Roll No:** 2K24/SWEE/5
- **Name:** Abdul Wasay
- **Department:** Software Engineering
- **Subject:** Artificial Intelligence
- **Teacher:** Sir Rafique Ahmed Bhutto
