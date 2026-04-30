import base64
import os

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:image/png;base64,{encoded_string}"

# 파일 경로 설정
css_path = "style.css"
js_path = "script.js"
html_template_path = "index.html"
output_path = "AI_도움말_통합가이드.html"

# 이미지 자산 경로
image_assets = {
    "assets/images/hero_bg.png": "HERO_BG",
    "assets/images/step1.png": "STEP1",
    "assets/images/step2.png": "STEP2",
    "assets/images/step3.png": "STEP3",
    "assets/images/step4.png": "STEP4",
    "assets/images/step5.png": "STEP5",
    "assets/images/step6.png": "STEP6",
}

# 1. CSS 읽기
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# 2. JS 읽기 및 이미지 경로를 Base64로 치환
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# 이미지 데이터를 Base64로 변환하여 JS 내 경로 치환
for path, placeholder in image_assets.items():
    if os.path.exists(path):
        b64_data = get_base64_image(path)
        js_content = js_content.replace(path, b64_data)

# 3. HTML 템플릿 읽기 및 결합
with open(html_template_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# 외부 참조 태그 제거 및 내부 삽입
# <link rel="stylesheet" href="style.css"> 제거
html_content = html_content.replace('<link rel="stylesheet" href="style.css">', f'<style>\n{css_content}\n</style>')

# <script src="script.js"></script> 제거
html_content = html_content.replace('<script src="script.js"></script>', f'<script>\n{js_content}\n</script>')

# 초기 이미지 경로 치환 (HTML 내에 있는 경우)
for path, placeholder in image_assets.items():
    if os.path.exists(path):
        b64_data = get_base64_image(path)
        html_content = html_content.replace(path, b64_data)

# 4. 최종 파일 저장
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully created: {output_path}")
