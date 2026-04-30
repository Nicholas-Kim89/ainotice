import base64
import os

# 파일 경로
bullet_path = "bullet.html"
manual_path = "AI_도움말_통합가이드.html"
webex_img_path = "assets/images/webex_monitor_screen.png"
ai_img_path = "assets/images/ai_minutes.png"
output_path = "AIVox_최종_통합공지.html"

# 1. 매뉴얼 파일을 Base64로 변환
with open(manual_path, "rb") as f:
    manual_base64 = base64.b64encode(f.read()).decode('utf-8')

# 2. 기능 카드 이미지들을 Base64로 변환
with open(webex_img_path, "rb") as f:
    webex_base64 = base64.b64encode(f.read()).decode('utf-8')
    webex_data_uri = f"data:image/png;base64,{webex_base64}"

with open(ai_img_path, "rb") as f:
    ai_base64 = base64.b64encode(f.read()).decode('utf-8')
    ai_data_uri = f"data:image/png;base64,{ai_base64}"

# 3. bullet.html 읽기 및 리소스 치환
with open(bullet_path, "r", encoding="utf-8") as f:
    content = f.read()

# 이미지 경로를 Base64 데이터로 치환
content = content.replace("assets/images/webex_monitor_screen.png", webex_data_uri)
content = content.replace("assets/images/ai_minutes.png", ai_data_uri)

# 4. 다운로드 기능 및 버튼 디자인 (헤더에 삽입)
button_style = """
    <style>
        .manual-download-container {
            width: 100%;
            text-align: center;
            margin-top: 40px;
            padding-bottom: 20px;
        }
        .download-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background: linear-gradient(135deg, #2563eb, #4f46e5);
            color: white !important;
            padding: 10px 24px;
            border-radius: 50px;
            font-size: 14px;
            font-weight: 600;
            text-decoration: none !important;
            box-shadow: 0 4px 10px rgba(37, 99, 235, 0.3);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border: none;
            cursor: pointer;
            animation: pulse-button 2s infinite;
        }
        @keyframes pulse-button {
            0% { transform: scale(1); box-shadow: 0 4px 10px rgba(37, 99, 235, 0.3); }
            50% { transform: scale(1.03); box-shadow: 0 6px 15px rgba(37, 99, 235, 0.5); }
            100% { transform: scale(1); box-shadow: 0 4px 10px rgba(37, 99, 235, 0.3); }
        }
        .download-btn:hover {
            transform: translateY(-5px) scale(1.08);
            filter: brightness(1.2);
        }
    </style>
"""

download_script = f"""
    <script>
        function downloadManual() {{
            try {{
                const base64Data = "{manual_base64}";
                const link = document.createElement('a');
                link.href = 'data:text/html;base64,' + base64Data;
                link.download = 'AI_도움말_통합가이드.html';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            }} catch (e) {{
                alert("다운로드 중 오류가 발생했습니다.");
            }}
        }}
    </script>
"""

# </head> 앞에 삽입
content = content.replace('</head>', f'{button_style}{download_script}</head>')

# 5. 버튼 HTML (가장 하단 </footer> 바로 앞에 삽입)
button_html = """
    <div class="manual-download-container">
        <button onclick="downloadManual()" class="download-btn">
            <span>📥</span> 이용 매뉴얼(가이드) 다운로드
        </button>
    </div>
"""

# </footer> 태그 바로 앞에 버튼을 넣어 확실하게 보이도록 함
content = content.replace('</footer>', f'{button_html}</footer>')

# 6. 최종 파일 저장
with open(output_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully finalized: {output_path}")
