import json

# Define your data
data = {
    'diagonal-radial': diagonalR  # Assume diagonalR is previously defined
}

# Specify the filename
category_filename = 'output.json'

# Write the data to a file in JSON format
with open(category_filename, mode='w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Data written to {category_filename}")
