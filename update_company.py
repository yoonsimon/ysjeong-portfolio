import re

html_path = r"c:\Users\NHNcommerce\Desktop\folder\me\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

badge_html = r"""
            <div class="flex items-center gap-2 mb-3 mt-1">
              <span class="px-2.5 py-1 bg-[#191f28] text-white rounded-[6px] text-[12px] font-bold tracking-wide">NHN Commerce</span>
              <span class="text-[#6b7684] text-[13px] font-medium border-l border-[#e5e8eb] pl-2">Technical PO</span>
            </div>
            """

# Tab 1
html = re.sub(
    r'(<h3[^>]*>.*?개발소스관리: 스테이징 및 배포 파이프라인.*?</h3>)',
    r'\1' + badge_html,
    html
)

# Tab 2
html = re.sub(
    r'(<h3[^>]*>.*?결제 API 중앙화 \(Toss Pay\).*?</h3>)',
    r'\1' + badge_html,
    html
)

# Tab 3
html = re.sub(
    r'(<h3[^>]*>.*?글로벌 간편 로그인 \(Google OAuth\) 아키텍처.*?</h3>)',
    r'\1' + badge_html,
    html
)

# Tab 4
html = re.sub(
    r'(<h3[^>]*>.*?BMAD 방법론 \(AI-Native Process\).*?</h3>)',
    r'\1' + badge_html,
    html
)

# Clean up old scattered badges in Tab 2 and 3
# Tab 2 old:
old_tab2 = """      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4">
        <div class="flex items-center gap-3">
          <span class="px-3 py-1 bg-[#f2f4f6] text-[#4e5968] rounded-[8px] text-[13px] font-bold">NHN Commerce</span>
          <span class="text-[#3182f6] text-[15px] font-bold">대형 가맹점 전환율 고도화</span>
        </div>
        <span class="text-[13px] text-[#6b7684] font-medium">Technical PO</span>
      </div>"""
html = html.replace(old_tab2, "")

# Tab 3 old:
old_tab3 = """      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4">
        <div class="flex items-center gap-3">
          <span class="px-3 py-1 bg-[#f2f4f6] text-[#4e5968] rounded-[8px] text-[13px] font-bold">NHN Commerce</span>
          <span class="text-[#3182f6] text-[15px] font-bold">엔터프라이즈 플랫폼 방어 및 글로벌 확장</span>
        </div>
      </div>"""
html = html.replace(old_tab3, "")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated Index HTML")
