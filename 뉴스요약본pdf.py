from fpdf import FPDF

# 한글 폰트를 사용하기 위한 설정
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# 한글 폰트 설정 (나눔고딕 폰트를 사용한다고 가정)
pdf.add_font('NanumGothic', '', 'C:/Windows/Fonts/NanumGothic.ttf', uni=True)  # 폰트 파일 경로 확인
pdf.set_font('NanumGothic', '', 12)

# 제목 추가
pdf.cell(200, 10, txt="2024년 중앙부처 및 지자체 창업지원사업 개요", ln=True, align='C')

# 추가 여백
pdf.ln(10)

# 본문 내용
content = """
2024년 창업지원사업 개요

2024년 중앙부처 및 지자체 창업지원사업은 총 3조 7,121억원 규모로, 397개 사업이 포함되어 있습니다.
예산은 전년 대비 514억원이 증가했으며, 중소벤처기업부가 가장 큰 예산을 배정받고 있습니다.
창업지원사업의 주요 지원 항목은 융자, 사업화, 기술개발 등입니다.

주요 지원사업

1. 융자･보증: 총 예산의 약 55.3%인 2조 546억원이 융자 및 보증 지원에 할당됩니다.
2. 사업화: 7,931억원이 사업화 지원에 사용되며, 창업기업의 제품 출시 및 시장 확장을 돕습니다.
3. 기술개발: 기술 기반 스타트업의 성장을 지원하기 위해 5,442억원이 배정되었습니다.

주요 프로그램

1. 팁스(TIPS) 프로그램: 민간 벤처캐피털과 협력하여 유망 창업기업을 발굴하고, 정부가 사업화 자금 및 연구개발(R&D)을 지원합니다.
   2023년에 비해 예산이 대폭 증가하여 1,925개 기업에 4,715억원을 지원합니다.
2. 초격차 스타트업1000+: 시스템반도체, 바이오·헬스 분야의 창업기업을 지원합니다. 총 505개 기업에 1,031억원이 지원됩니다.
3. 글로벌 진출 지원: 해외 진출을 목표로 하는 창업기업을 위해 430억원 규모의 글로벌 기업 협업사업과 154.4억원 규모의 K-스타트업 센터 사업이 운영됩니다.

창업자 맞춤형 지원

- 청년창업: 청년 창업자에게 51.34억원의 사업화 자금과 교육을 제공합니다.
- 재창업: 실패한 창업자가 재도전을 할 수 있도록 1,000억원 규모의 융자자금이 지원됩니다.
- 메이커 스페이스: 창업자들이 제품을 시제품화할 수 있도록 211억원 규모의 시제품 제작 지원이 제공됩니다.
"""

pdf.multi_cell(0, 10, content)

# PDF 파일 저장
output_path = "2024_창업지원사업.pdf"
pdf.output(output_path)

print(f"PDF 파일이 저장되었습니다: {output_path}")
