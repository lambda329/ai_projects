#!/bin/bash

# Translate text to a specified language using Google Translate API
# Usage: ./translate.sh <input-file> <target-language>
# Replace "your_google_api_key" with your actual Google API key.

API_KEY="your_google_api_key"
INPUT_FILE=$1
TARGET_LANG=$2

# Check if both input file and target language are provided
if [[ -z $INPUT_FILE || -z $TARGET_LANG ]]; then
  echo "Usage: $0 <input-file> <target-language>"
  exit 1
fi

# Read the content of the file
TEXT=$(<"$INPUT_FILE")

# Send request to Google Translate API
TRANSLATION=$(curl -s -X POST "https://translation.googleapis.com/language/translate/v2" \
  -H "Content-Type: application/json" \
  -d '{
        "q": "'"$TEXT"'",
        "target": "'"$TARGET_LANG"'",
        "format": "text",
        "key": "'"$API_KEY"'"
      }' | jq -r '.data.translations[0].translatedText')

echo "Translation:"
echo "$TRANSLATION"
