import re
import base64

with open('AIVox_최종_통합공지.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Revert CSS of feature-grid to 2 columns
html = html.replace('grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));', 'grid-template-columns: 1fr 1fr;')

# 2. Remove the "Mobile Usage" column from AIVox_최종_통합공지.html
# It was added after the translation column
html = re.sub(r'<!-- 모바일 활용 영역 -->.*?</div>\s*</div>\s*</div>', '', html, flags=re.DOTALL)

# 3. Extract manual, update height, and re-inject
match = re.search(r'const base64Data = "([^"]+)";', html)
if match:
    manual_html = base64.b64decode(match.group(1)).decode('utf-8')
    
    # Update height: current is 720px, 3/4 is 540px
    manual_html = manual_html.replace('--guide-height: 720px;', '--guide-height: 540px;')
    # Ensure min-height/height are updated if they were hardcoded differently
    manual_html = manual_html.replace('min-height: 720px;', 'min-height: 540px;')
    manual_html = manual_html.replace('height: 720px;', 'height: 540px;')
    
    new_b64 = base64.b64encode(manual_html.encode('utf-8')).decode('utf-8')
    html = re.sub(r'const base64Data = "[^"]+";', f'const base64Data = "{new_b64}";', html)

with open('AIVox_최종_통합공지.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Main page reverted and manual height updated.")
