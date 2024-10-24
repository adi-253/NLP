# Sentiment Analysis and Aspect-Based Labeling of Financial News

This repository contains two Jupyter notebooks for performing sentiment analysis and aspect-based labeling on financial news datasets. The goal of the project is to provide sentiment scores at two levels:
1. **Overall sentiment of the news**.
2. **Aspect-specific sentiment, categories, and labels**.

## Contents

- `sentiment-score.ipynb`: This notebook provides sentiment scores for entire sentences within financial news articles to capture the overall sentiment of the news piece.
- `aspect-extraction.ipynb`: This notebook focuses on aspect-based labeling, where aspects (keywords) in the news articles are extracted, categorized, and their associated sentiment scores are determined.

## Notebooks Overview

### 1. **sentiment-score.ipynb**
   - **Objective**: The goal of this notebook is to assign a sentiment score to the entire sentence from a financial news article.
   - **Approach**: 
     - Sentiment analysis is performed at the sentence level to gauge the overall sentiment (positive, negative, neutral) of the news article.
     - The sentiment scoring does not focus on specific aspects or words but rather evaluates the sentiment of the sentence as a whole.
     - This can help in understanding the general mood conveyed by the news.
   
   - **Usage**: 
     - **Input**: Financial news dataset containing full sentences.
     - **Output**: Sentiment score for each sentence in the dataset.

### 2. **aspect-extraction.ipynb**
   - **Objective**: The purpose of this notebook is to perform **aspect-based sentiment analysis** on financial news articles.
   - **Approach**:
     - The code extracts key aspects (topics or entities) from each financial news sentence.
     - Each aspect is categorized, and sentiment scores are assigned specifically to these aspects.
     - This provides detailed insight into the sentiment associated with specific parts of the news (e.g., companies, sectors, products, etc.).
   
   - **Usage**:
     - **Input**: Financial news dataset containing full sentences.
     - **Output**: A detailed table or list that includes:
       - Extracted aspects from the news.
       - Aspect categories.
       - Sentiment scores for each aspect.
