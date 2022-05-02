# 고유식별정보 - 5
resident_registration_num = '(\d{6}[ ,-]-?[1-4]\d{6})|(\d{6}[ ,-]?[1-4])'
passport_num = '([a-zA-Z]{1}|[a-zA-Z]{2})\d{8}'
Alien_registration_num = '([01][0-9]{5}[[:space:]~-]+[1-8][0-9]{6}|[2-9][0-9]{5}[[:space:]~-]+[1256][0-9]{6})'
driver_license_num ='(\d{2}-\d{2}-\d{6}-\d{2})'


name = '^[가-힣]{2,3}$'
addr = {"road_name_addr":'(([가-힣A-Za-z·\d~\-\.]{2,}(로|길).[\d]+)|([가-힣A-Za-z·\d~\-\.]+(읍|동)\s)[\d]+)',
'land_num_addr':'(([가-힣A-Za-z·\d~\-\.]+(읍|동)\s)[\d-]+)|(([가-힣A-Za-z·\d~\-\.]+(읍|동)\s)[\d][^시]+)'}

phone_num = '(\d{2,3}[ ,-]-?\d{2,4}[ ,-]-?\d{4})'                                       # 전화번호
bank_account_num = '([0-9,\-]{3,6}\-[0-9,\-]{2,6}\-[0-9,\-])'                           # 계좌번호
health_insurance_num = '[1257][-~.[:space:]][0-9]{10}'                                  # 건강보험번호
credit_card_num = '[34569][0-9]{3}[-~.[ ]][0-9]{4}[-~.[ ]][0-9]{4}[-~.[ ]][0-9]{4}'     # 신용카드번호
car_num1 = '^[가-힣]{2}\\d{2}[가-힣]{1}\\d{4}$'                                         # 자동차 번호1
car_num2 = '^\\d{2}[가-힣]{1}\\d{4}$'                                                   # 자동차 번호2

URL = '(http(s)?:\/\/)([a-z0-9\w]+\.*)+[a-z0-9]{2,4}'
MAIL = '(([\w!-_\.])*@([\w!-_\.])*\.[\w]{2,3})'
IPv4 = '(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}'
IPv6 = '(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'
MAC = '([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}'
ID = '^[A-Za-z]{1}[A-Za-z0-9]{3,19}$'
military_serial_num = '^[0-9a-zA-Z]+([_0-9a-zA-Z]+)*$'                          # 군번
business_registration_num = '^(\d{3,3})+[-]+(\d{2,2})+[-]+(\d{5,5})'            # 사업자등록번호


#https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=1257&ccfNo=1&cciNo=1&cnpClsNo=1
# 학력사항
# - 학교명
# - 학위
# - 전공
# - 학점
# - 소재지
# 자격증 및 교육사항
# - 자격/면허
# - 취득일자
# - 자격 및 교육명
# - 발급 기관
# - 점수/등급
# 수상경력
# 경력사항
# 회사명
# 근무기간
# 근무부서
# 직위
# ※ 출처 : 행자부‧KISA "김대리, 개인정보보호 달인되기" 15면
# 일반정보 – 성명, 주민등록번호, 주소 연락처 등
# 경제정보 – 소득, 재산상황, 신용, 부채 등
# 사회정보 – 학력, 성적, 병역, 직업, 자격 등
# 통신정보 – 전자우편, 통화내용, 인터넷 IP 등
# 민감정보 – 사상, 신념, 노동조합, 정당의 가입탈퇴, 정치적 견해, 건강, 성생활정보 등