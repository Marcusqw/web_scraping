import json
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input and output file paths
input_file = os.path.join(script_dir, "C:/Users/Razer/Desktop/爬蟲/Supreme Court_ Table Of Contents _ Supreme Court _ US Law _ LII _ Legal Information Institute.json")

output_file = os.path.join(script_dir, "supreme_court_toc.jsonl")

def process_json(data):
    if isinstance(data, dict):
        if any(key.lower() in ['path', 'title', 'content'] for key in data.keys()):
            return data
        return {k: process_json(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [process_json(item) for item in data]
    else:
        return data

# Read the input JSON file
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Process the data
processed_data = process_json(data)

# Write the processed data to a JSON Lines file
with open(output_file, 'w', encoding='utf-8') as f:
    for item in processed_data:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')

print(f"Processed JSON Lines file has been saved as {output_file}")
