
#!/bin/bash

# Summarize a text file using OpenAI's API
# Replace "your_openai_api_key" with your actual OpenAI API key.

API_KEY="your_openai_api_key"
INPUT_FILE=$1

# Check if input file is provided
if [[ -z $INPUT_FILE ]]; then
  echo "Usage: $0 <text-file>"
  exit 1
fi

# Read the content of the file
TEXT=$(<"$INPUT_FILE")

# Send request to OpenAI API for summarization
SUMMARY=$(curl -s https://api.openai.com/v1/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{
        "model": "text-davinci-003",
        "prompt": "Summarize the following text:\n\n'"$TEXT"'",
        "temperature": 0.5,
        "max_tokens": 100
      }' | jq -r '.choices[0].text')

echo "Summary:"
echo "$SUMMARY"
