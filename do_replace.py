import sys

html_path = r"c:\Users\NHNcommerce\Desktop\folder\me\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_html = r"""            <p class="text-[15px] text-[#4e5968]">파편화된 500개 수기 엑셀을 단일 웹 양식으로 표준화하고 심사 검토 파이프라인을 자동화</p>
        </div>
        
    <div class="bg-white p-6 md:p-8 rounded-[24px] shadow-sm ring-1 ring-[#f2f4f6]">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4">
        <div class="flex items-center gap-3">
          <span class="text-[#059669] text-[15px] font-bold">전사적 데이터 표준화 및 신기술(AI) 도입</span>
        </div>
      </div>
      <p class="text-[16px] text-[#4e5968] leading-[1.6] mb-4">
        초기 500개 엑셀 시트로 파편화된 제조지시서를 단일 표준화된 웹 기반 형태(ERP 전산화)로 통합 기획했습니다. 이후 데이터 검증 단계를 고도화하기 위해 <strong>새로운 AI 기반 OCR 시스템</strong>을 성공적으로 정착시켜 기업 전반의 생산성을 본질적으로 끌어올렸습니다.
      </p>
      <div class="p-4 bg-[#f9fafb] rounded-[16px] text-[14px]">
        <div class="flex flex-col md:flex-row md:items-center gap-2 md:gap-4">
          <span class="text-[#191f28] font-bold shrink-0">비즈니스 임팩트</span>
          <span class="text-[#6b7684]">업무 소요 시간 <strong class="text-[#059669]">30% 단축</strong> / AI 검토 도입으로 심사 시간 <strong class="text-[#059669]">40% 절감</strong> / <strong>연 1억 5천만 원</strong>의 매출 증대.</span>
        </div>
      </div>

      <!-- Edge Cases & Technical Depth -->
      <div class="mt-6 p-5 bg-[#f9fafb] rounded-[16px] border border-[#e5e8eb] shadow-sm mb-6">
        <h4 class="text-[14px] font-bold text-[#191f28] mb-4 flex items-center gap-2">
          <span class="material-symbols-rounded text-[#059669] text-[18px]">rule_folder</span>
          기획자로서 이해관계자 조율 및 리스크 통제
        </h4>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="bg-white p-4 rounded-[12px] shadow-sm ring-1 ring-[#f2f4f6]">
            <strong class="text-[#059669] text-[13px] block mb-1.5">이해관계 충돌 조율 및 데이터 표준화</strong>
            <p class="text-[13px] text-[#4e5968] leading-[1.6]">COSMAX NBT의 QA팀 및 연구원 간의 상충되는 요구사항이 잦았습니다. 주도적으로 정기 협의를 개최하고 데이터를 철저히 분석하여 우선순위에 따른 <strong class="text-[#191f28]">합리적 타협안(표준 양식)</strong>을 성공적으로 통과시켰습니다.</p>
          </div>
          <div class="bg-white p-4 rounded-[12px] shadow-sm ring-1 ring-[#f2f4f6]">
            <strong class="text-[#059669] text-[13px] block mb-1.5">UX 설계를 통한 신기술 거부감 돌파</strong>
            <p class="text-[13px] text-[#4e5968] leading-[1.6]">새로운 AI 기반 OCR 도입 시 보수적인 부서의 반발이 컸습니다. 이를 극복하고자 <strong class="text-[#191f28]">'클립보드 다이렉트 업로드'</strong> 등 철저히 사용자 편의 중심의 UX를 기획해 부서 간 신뢰 구축과 기술 도입율을 끌어냈습니다.</p>
          </div>
        </div>
      </div>

      <!-- AI OCR Flowchart Diagram (Generated Live) -->
      <div class="mt-5 p-5 bg-white rounded-[16px] border border-[#e5e8eb] shadow-sm">
        <h4 class="text-[14px] font-bold text-[#191f28] mb-4 flex items-center gap-2">
          <span class="material-symbols-rounded text-[#059669] text-[18px]">document_scanner</span>
          AI OCR 자동화 파이프라인
        </h4>
        <div class="mermaid flex justify-center text-[12px] w-full overflow-x-auto">
graph LR
    classDef file fill:#ffffff,stroke:#4e5968,stroke-width:1.5px,rx:8px,ry:8px;
    classDef ai fill:#ecfdf5,stroke:#059669,stroke-width:2px,rx:8px,ry:8px,font-weight:bold;
    classDef filter fill:#fff4e6,stroke:#fbbf24,stroke-width:2px,rx:8px,ry:8px;
    classDef result fill:#e9fbf3,stroke:#00b06b,stroke-width:2px,rx:8px,ry:8px,font-weight:bold;

    A[사용자 편의성 극대화<br/>클립보드 맵핑 UX]:::file -->|이미지 인식| B(신규 AI 기반<br/>OCR 엔진):::ai
    B -->|데이터 포맷팅| C{노이즈 필터링 로직}:::filter
    C -->|심사시간 40% 절감| D[정형 데이터 추출<br/>통합 ERP 연동]:::result
        </div>
      </div>
    </div>
      </div>
  </div>
"""

out = []
skip = False
for i, line in enumerate(lines):
    if line.strip() == '<p class="text-[15px] text-[#4e5968]">파편화된 500개 수기 엑셀을 한 번에 통합하고 심사 자동화 로직을 고도화</p>':
        skip = True
        out.append(new_html)
    elif skip and line.strip() == '</div>':
        # Need to detect the end of tab-erns. We will check index.
        pass

    if not skip:
        out.append(line)

# Since purely line based is fragile if skip is not turned off properly, I'll do string replacement entirely.
with open(html_path, "r", encoding="utf-8") as f:
    full_text = f.read()

import re
pattern = r'<p class="text-\[15px\] text-\[#4e5968\]">파편화된 500개 수기 엑셀을 한 번에 통합하고 심사 자동화 로직을 고도화</p>.*?</section>'
replacement = new_html + "\n</section>"

full_text = re.sub(pattern, replacement, full_text, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_text)

print("Replacement successful")
