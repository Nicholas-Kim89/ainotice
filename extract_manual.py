import base64
import re

with open('AIVox_최종_통합공지.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const base64Data = "([^"]+)";', content)
if match:
    manual_content = base64.b64decode(match.group(1)).decode('utf-8')
    with open('manual_extracted.html', 'w', encoding='utf-8') as f:
        f.write(manual_content)
    print("Manual extracted to manual_extracted.html")
else:
    print("Base64 manual not found")
