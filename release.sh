#!/bin/bash

REPO="AxionAOSP/AxionOS_Pixels"

read -p "Enter tag name (e.g., 1.2): " TAG_NAME
RELEASE_NAME="Version $TAG_NAME"

read -p "Enter release body (leave empty to use default): " RELEASE_BODY
if [ -z "$RELEASE_BODY" ]; then
    RELEASE_BODY="$(date '+%B %Y') Security Update"
fi

echo "Creating or updating GitHub release..."
if ! gh release view "$TAG_NAME" --repo "$REPO" &>/dev/null; then
    gh release create "$TAG_NAME" --repo "$REPO" --title "$RELEASE_NAME" --notes "$RELEASE_BODY" || echo "Release tag already exists, continuing..."
else
    echo "Release already exists, continuing..."
fi

echo "Checking for already uploaded files..."
UPLOADED_FILES=$(gh release view "$TAG_NAME" --repo "$REPO" --json assets -q '.assets[].name')

UPLOAD_STARTED=false
for FILE in *.zip; do
    if echo "$UPLOADED_FILES" | grep -q "^$FILE$"; then
        echo "Skipping already uploaded file: $FILE"
        continue
    fi

    UPLOAD_STARTED=true

    echo "Uploading: $FILE"
    python3 progress.py "$FILE" "$TAG_NAME" "$REPO"
    
    if [ $? -ne 0 ]; then
        echo "Upload failed or canceled."
        exit 1
    fi
done

if [ "$UPLOAD_STARTED" = true ]; then
    echo "All uploads completed!"
fi
