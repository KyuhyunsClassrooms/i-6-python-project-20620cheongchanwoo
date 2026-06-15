# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20620 정찬우
# 프로젝트 주제: 화학 공장 폐수 오염도 및 정화 공정 시뮬레이터

# ============================================================
# 사용 안내
# ------------------------------------------------------------
# 이 파일은 예시 골격입니다.
# 그대로 제출하지 말고, 반드시 자신의 주제에 맞게 수정하세요.
#
# 필수 조건
# 1. 2차원 리스트 사용
# 2. 함수 2개 이상, 가능하면 3개 이상 분리
# 3. 조건문 사용
# 4. 반복문 사용
# 5. 실행 결과 출력
# ============================================================


# ------------------------------------------------------------
# 1. 데이터 준비: 2차원 리스트
# ------------------------------------------------------------
# 아래 예시는 "활동 추천 프로그램"입니다.
# 자신의 주제에 맞게 data를 만드세요.
#
# 현재 열의 의미:
# 0번 열: 오염 물질명
# 1번 열: 배출허용기준치 (ppm)
# 2번 열: 1ppm 초과당 약품량 (g)
# 3번 열: 처리 약품명
# ------------------------------------------------------------

pollution_standards = [
    ["Heavy Metal", 0.5, 10, "Chelating Agent"],   # 중금속 (킬레이트제)
    ["Organic Matter", 20.0, 2, "Oxidizing Agent"], # 유기물 (산화제)
    ["Acid Substance", 5.0, 4, "Neutralizer"],      # 산성 물질 (중화제)
    ["Cyanide", 0.1, 15, "Destruction Reagent"],    # 시안화물 (분해제)
    ["Suspended Solids", 10.0, 1, "Coagulant"]      # 부유 물질 (응집제)
]


# ------------------------------------------------------------
# 2. 함수 정의
# ------------------------------------------------------------

def show_intro():
    """프로그램 제목과 안내를 출력한다."""
    print("=" * 50)
    print("   화학 공장 폐수 오염도 및 정화 공정 시뮬레이터")
    print("   (실시간 모니터링 및 정화 약품 투여량 계산)")
    print("=" * 50)


def check_pollution_status(current_value, standard_value):
    """현재 농도가 배출허용기준치를 초과했는지 판정한다."""
    if current_value > standard_value:
        return True
    else:
        return False
    # 만약 current_value가 standard_value보다 크다면 True를 반환(return)하고, 그렇지 않다면 False를 반환함.


def calculate_purifier_amount(current_value, standard_value, unit_amount):
    """기준치 초과 시 필요한 정화 약품의 총 무게를 산출한다."""
def calculate_purifier_amount(current_value, standard_value, unit_amount):
    """기준치 초과 시 필요한 정화 약품의 총 무게를 산출한다."""
    # 1. 현재 농도에서 기준치를 빼서 '초과된 양'을 구합니다.
    over_value = current_value - standard_value
    
    # 2. 초과된 양에 1ppm당 필요한 약품량을 곱해 총 약품량을 구합니다.
    total_purifier = over_value * unit_amount
    
    # 3. 계산된 최종 약품량을 반환합니다.
    return total_purifier


def main():
    show_intro()
    
    # 모든 물질을 검사했는데 오염된 물질이 하나도 없는 예외 상황을 처리하기 위한 플래그 변수
    is_dirty = False 
    
    print("\n[공정 분석 시작] 각 물질의 현재 농도를 입력하세요.")
    
    # 2차원 리스트를 반복문으로 하나씩 순회
    for row in pollution_standards:
        material_name = row[0]
        standard_value = row[1]
        unit_amount = row[2]
        purifier_name = row[3]
        
        # 사용자에게 현재 물질의 농도를 입력받음
        current_value = float(input(f"- {material_name}의 현재 농도(ppm): "))
        
        # [예외 처리] 만약 사용자가 음수를 입력했다면 0으로 보정
        if current_value < 0:
            print("  [경고] 농도는 음수일 수 없습니다. 안전을 위해 0ppm으로 처리합니다.")
            current_value = 0.0
            
        # 오염 여부 판정 함수 호출
        is_polluted = check_pollution_status(current_value, standard_value)
        
        if is_polluted == True:
            # 하나라도 기준을 초과했으므로 플래그 변수를 True로 변경!
            is_dirty = True 
            
            if is_polluted == True:
            # 하나라도 기준을 초과했으므로 플래그 변수를 True로 변경!
                is_dirty = True 
            
            required_purifier = calculate_purifier_amount(current_value, standard_value, unit_amount)
            
            print(f"  ▶ [기준 초과 - 경고] {material_name}이 기준치({standard_value}ppm)를 초과했습니다!")
            print(f"  ▶ [정화 지시] {purifier_name} 약품을 {required_purifier:.2f}g 투여해야 합니다.\n")
            
            
        else:
            print(f"  ▶ [정상] {material_name} 상태 안전\n")
            
    # [예외 처리] 모든 물질의 검사가 끝난 후, 오염된 물질이 단 하나도 없다면 최종 방류 승인
    if is_dirty == False:
        print("=" * 50)
        print("[최종 판정] 모든 측정 항목이 배출허용기준치 이하로 안전합니다.")
        print("정화 공정을 생략하고 폐수를 외부로 안전하게 방류합니다.")
        print("=" * 50)

# -------------------------------
# -----------------------------
# 3. 프로그램 실행
# ------------------------------------------------------------
main()
