#!/bin/bash

# Caption an image using Hugging Face API
# Usage: ./caption_image.sh <image-file>
# Replace "your_huggingface_api_key" with your actual Hugging Face API key.

API_KEY="your_huggingface_api_key"
IMAGE_PATH=$1

# Check if image file is provided
if [[ -z $IMAGE_PATH ]]; then
  echo "Usage: $0 <image-file>"
  exit 1
fi

# Encode the image as base64
IMAGE_BASE64=$(base64 "$IMAGE_PATH" | tr -d '\n')

# Send request to Hugging Face for captioning
CAPTION=$(curl -s -X POST "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "inputs": "'"$IMAGE_BASE64"'"
      }' | jq -r '.[0].generated_text')

echo "Caption:"
echo "$CAPTION"
