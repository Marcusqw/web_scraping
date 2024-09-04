import json

# Read the content from output.txt
with open('output.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Create a dictionary with the required fields
data = {
    "path": "text_",
    "title": "PRICE v. MONTGOMERY COUNTY | Supreme Court | US Law | LII / Legal Information Institute",
    "content": content
}

# Convert the dictionary to a JSON string
json_string = json.dumps(data, ensure_ascii=False)

# Write the JSON string to a new file in JSONLines format
with open('output.jsonl', 'w', encoding='utf-8') as outfile:
    outfile.write(json_string + '\n')

print("Conversion complete. Output saved to output.jsonl")
