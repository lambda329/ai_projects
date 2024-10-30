#!/bin/bash

# Sentiment Analysis on a text file using Hugging Face Transformers
INPUT_FILE=$1

# Check if input file is provided
if [[ -z $INPUT_FILE ]]; then
  echo "Usage: $0 <text-file>"
  exit 1
fi

# Run sentiment analysis using Python and Hugging Face Transformers
python3 - <<EOF
from transformers import pipeline

# Load the sentiment-analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Read the input file
with open("$INPUT_FILE", "r") as file:
    text = file.read()

# Perform sentiment analysis
result = sentiment_analyzer(text)
print("Sentiment Analysis Result:", result)
EOF
