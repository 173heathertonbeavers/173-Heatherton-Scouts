import os
import json
import re

# Root folder containing all galleries
images_root = "images"

# Supported file extensions
extensions = (
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".mp4"
)

# Natural sorting (1,2,3,10 instead of 1,10,2)
def natural_key(name):
    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split(r"(\d+)", name)
    ]

# Loop through every folder inside images/
for gallery in os.listdir(images_root):

    gallery_path = os.path.join(images_root, gallery)

    # Skip anything that isn't a folder
    if not os.path.isdir(gallery_path):
        continue

    media = []

    # Sort nicely
    files = sorted(os.listdir(gallery_path), key=natural_key)

    for filename in files:

        if filename.lower().endswith(extensions):

            caption = os.path.splitext(filename)[0]

            # Make captions prettier
            caption = (
                caption
                .replace("_", " ")
                .replace("-", " ")
            )

            media.append({
                "file": filename,
                "caption": caption
            })

    # Write media.json into this gallery folder
    with open(
        os.path.join(gallery_path, "media.json"),
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(media, f, indent=4, ensure_ascii=False)

    print(f"✓ {gallery}: {len(media)} items")