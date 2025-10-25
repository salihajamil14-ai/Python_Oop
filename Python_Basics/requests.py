import requests

# Make the request and store the Response object in a variable
response = requests.get('https://www.google.com')
# Check the status code
print(response.status_code)
# Output: 200

# You can also use a boolean property:
print(response.ok)
# Output: True (if status code is between 200 and 400)
# Print the content (HTML) of the webpage
print(response.text)
# Search for 'requests python' on Google (just an example)
search_parameters = {
    'q': 'requests python',
    'hl': 'en'  # Language English
}
response = requests.get('https://www.google.com/search', params=search_parameters)

# The URL sent would be similar to: https://www.google.com/search?q=requests+python&hl=en
print(response.url)

# Data to be 'posted' to the server
payload = {
    'username': 'CornyShay',
    'password': 'my-secret-password'
}
# Replace example.com with a real endpoint for sending data
response = requests.post('https://httpbin.org/post', data=payload)

# The response content will often confirm the data you sent
print(response.text)

# Using a public API endpoint for example
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
todo_item = response.json()

# Access data just like a regular Python dictionary
print(f"User ID: {todo_item['userId']}")
print(f"Title: {todo_item['title']}")
image_url = 'https://i.imgur.com/z10oAyr.jpg'
response = requests.get(image_url, stream=True)

# Check the headers to get the file type
print(response.headers['Content-Type'])

with open('my_downloaded_image.jpg', 'wb') as f:
    f.write(response.content)

print("Image downloaded successfully!")