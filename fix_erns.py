import re

html_path = r"c:\Users\NHNcommerce\Desktop\folder\me\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

new_html = """<div id="tab-erns" class="tab-content hidden animate-fade-in transition-opacity duration-300">
  <div class="mb-6">
    <h3 class="text-[22px] md:text-[24px] font-bold text-[#191f28] mb-2 flex items-center gap-2">
      <span class="material-symbols-rounded text-[#059669]">domain</span> 
      복합 제조지시서 통합 전산화 및 AI OCR 혁신
    </h3>
    <div class="flex items-center gap-2 mb-3 mt-1">
      <span class="px-2.5 py-1 bg-[#191f28] text-white rounded-[6px] text-[12px] font-bold tracking-wide">ERNS PI팀</span>
      <span class="text-[#6b7684] text-[13px] font-medium border-l border-[#e5e8eb] pl-2">주임 / 기획 총괄</span>
    </div>
    <p class="text-[15px] text-[#4e5968]">500여 개의 수기 엑셀을 단일 웹 표준으로 통합하고 AI 기반 검토 자동화 체계 구축</p>
  </div>

  <div class="bg-white p-6 md:p-8 rounded-[24px] shadow-sm ring-1 ring-[#f2f4f6]">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
      <div class="bg-[#f9fafb] p-4 rounded-[16px] border border-[#f2f4f6]">
        <span class="text-[#6b7684] text-[12px] block mb-1">전체 업무 효율</span>
        <span class="text-[20px] font-bold text-[#059669]">30% 향상</span>
      </div>
      <div class="bg-[#f9fafb] p-4 rounded-[16px] border border-[#f2f4f6]">
        <span class="text-[#6b7684] text-[12px] block mb-1">심사 검토 시간</span>
        <span class="text-[20px] font-bold text-[#059669]">40% 절감</span>
      </div>
      <div class="bg-[#f9fafb] p-4 rounded-[16px] border border-[#f2f4f6]">
        <span class="text-[#6b7684] text-[12px] block mb-1">연간 매출 기여</span>
        <span class="text-[20px] font-bold text-[#191f28]">1.5억 증대</span>
      </div>
    </div>

    <p class="text-[16px] text-[#4e5968] leading-[1.6] mb-6">
      초기 500개 이상의 개별 엑셀 시트로 운영되던 제조지시서를 집중 분석하여 <strong class="text-[#191f28]">단일 웹 표준 양식(ERP)</strong>으로 통합 기획했습니다. 특히 기존 OCR 엔진의 낮은 정확도를 개선하기 위해 <strong class="text-[#059669]">새로운 AI 기반 OCR 시스템</strong>을 전사 도입하며, 단순 전산화를 넘어 데이터 검증 프로세스의 완전 자동화를 실현했습니다.
    </p>

    <!-- Edge Cases & Technical Depth -->
    <div class="mt-6 p-5 bg-[#f9fafb] rounded-[16px] border border-[#e5e8eb] shadow-sm mb-6">
      <h4 class="text-[14px] font-bold text-[#191f28] mb-4 flex items-center gap-2">
        <span class="material-symbols-rounded text-[#059669] text-[18px]">rule_folder</span>
        기획자로서 이해관계자 조율 및 시스템 혁신
      </h4>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="bg-white p-4 rounded-[12px] shadow-sm ring-1 ring-[#f2f4f6]">
          <strong class="text-[#059669] text-[13px] block mb-1.5">이해관계 충돌 조율 및 데이터 표준화</strong>
          <p class="text-[13px] text-[#4e5968] leading-[1.6]">COSMAX NBT 연구소와 QA팀 등 다양한 현업 부서 간의 상충되는 요구사항이 빗발쳤습니다. 주도적으로 정기 협의체를 운영하며 각 부서의 데이터를 분석하고, 최적의 우선순위를 도출하여 <strong class="text-[#191f28]">가장 합리적인 범용 표준 양식</strong>을 하나로 정립했습니다.</p>
        </div>
        <div class="bg-white p-4 rounded-[12px] shadow-sm ring-1 ring-[#f2f4f6]">
          <strong class="text-[#059669] text-[13px] block mb-1.5">UX 설계를 통한 신기술 거부감 돌파</strong>
          <p class="text-[13px] text-[#4e5968] leading-[1.6]">보수적인 인원들의 AI 기반 신기술 도입에 대한 큰 거부감을 해소해야 했습니다. 이를 위해 기존 업무 루틴에 매끄럽게 녹아드는 <strong class="text-[#191f28]">'클립보드 다이렉트 업로드'</strong> 기능을 기획했고, 탁월한 편의성(UX)으로 기술 저항을 이겨내고 성공적으로 전사 도입을 이끌었습니다.</p>
        </div>
      </div>
    </div>

    <!-- AI OCR Flowchart Diagram -->
    <div class="mt-5 p-5 bg-white rounded-[16px] border border-[#e5e8eb] shadow-sm">
      <h4 class="text-[14px] font-bold text-[#191f28] mb-4 flex items-center gap-2">
        <span class="material-symbols-rounded text-[#059669] text-[18px]">account_tree</span>
        AI OCR 자동 검증 파이프라인 아키텍처
      </h4>
      <div class="mermaid flex justify-center text-[12px] w-full overflow-x-auto">
      flowchart LR
          classDef analysis fill:#ffffff,stroke:#e5e8eb,stroke-width:2px,color:#4e5968,rx:12px,ry:12px,font-weight:bold;
          classDef design fill:#fff4e6,stroke:#fbbf24,stroke-width:2px,color:#d97706,rx:12px,ry:12px,font-weight:bold;
          classDef core fill:#ecfdf5,stroke:#059669,stroke-width:2px,color:#047857,rx:16px,ry:16px,font-weight:bold;
          classDef result fill:#e9fbf3,stroke:#00b06b,stroke-width:2px,color:#059669,rx:12px,ry:12px,font-weight:bold;

          A[1. 문제 분석<br/>500개 엑셀 전수 조사]:::analysis --> B[2. 표준화 설계<br/>Web 통합 양식 도출]:::design
          B --> C[3. AI 엔진 도입<br/>OCR 이미지 정형 인식]:::core
          C --> D[4. 무결성 검증<br/>노이즈 필터링 로직]:::core
          D --> E[5. ERP 자동 연동<br/>심사 시간 40% 절감]:::result
      </div>
    </div>
  </div>
</div>
</section>"""

# Find strictly `<div id="tab-erns"` to `</section>`
pattern = re.compile(r'<div id="tab-erns".*?</section>', re.DOTALL)
new_text = pattern.sub(new_html, text)

# Just in case tab-erns is currently visible (class="tab-content block"), but it should start hidden
# Let's ensure the first tab is visible and others are hidden. But for now we just clean it.

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Done replacing.")
