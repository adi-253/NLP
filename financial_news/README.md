# Dataset Description for Financial News

## Overview

This document provides a detailed description of the dataset used for analyzing financial news articles. The primary dataset file is `reliance.csv`, which is part of a broader collection that includes datasets for Apollo and Tata as well.

## Common Columns Across Datasets

The following columns are shared across the `reliance.csv`, `apollo.csv`, and `tata.csv` datasets:

1. **Date**: 
   - **Format**: `dd/mm/yy`
   - **Description**: The date on which the news article was published.

2. **news**: 
   - **Description**: The content of the financial news article.

3. **predicted Sentiment**: 
   - **Description**: The overall sentiment of the news article, categorized as positive, negative, or neutral.

4. **aspect_labelling**: 
   - **Description**: Contains a list of sets for each news article, detailing:
     - Aspect words: Key terms or entities referenced in the article.
     - Categories: Categories associated with each aspect (e.g., Finance, Market).
     - Sentiment: The sentiment associated with each aspect (positive, negative, neutral).
     - Sentiment Score: A numerical value representing the sentiment strength for each aspect.

## Additional Columns in `reliance.csv`

In addition to the common columns, the `reliance.csv` dataset includes the following specific columns:

5. **syntactic_embeddings**: 
   - **Description**: This column contains syntactic embeddings generated for each news article. These embeddings capture the syntactic structure of the text, enhancing analysis capabilities.

6. **cleaned text**: 
   - **Description**: This column contains the preprocessed version of the news articles. Preprocessing steps may include tokenization, removal of stop words, and normalization of text.
