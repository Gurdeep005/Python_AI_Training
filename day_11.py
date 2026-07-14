#Python virtualenv scraping: fetching, parsing HTML, cleaning text, removing duplicates, saving output.--

import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the page
response = requests.get("https://www.w3schools.com/python/python_virtualenv.asp")

# Step 2: Parse the HTML
# soup = BeautifulSoup(response.text, 'html5lib')
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Remove tags that only contain junk (nav menus, scripts, ads, etc.)
for tag in soup(['nav', 'footer', 'script', 'style', 'header', 'aside']):
    tag.decompose()

# Step 4: Try to grab just the main content area; fall back to body if not found
content = soup.find(id="main")
if content is None:
    content = soup.body

# Step 5: Extract text, separating each tag's text with a newline
raw_text = content.get_text(separator='\n')

# Step 6: Split into lines, strip whitespace from each, and drop empty ones
lines = [line.strip() for line in raw_text.split('\n') if line.strip() != '']

# Step 7: Remove consecutive duplicate lines
clean_lines = []
for line in lines:
    if not clean_lines or clean_lines[-1] != line:
        clean_lines.append(line)

# Step 8: Join everything back into one clean string
clean_text = '\n'.join(clean_lines)

# Step 9: Save to file
with open("file.txt", "w", encoding="utf-8") as file:
    file.write(clean_text)

print(f"Saved {len(clean_lines)} clean lines to file.txt")