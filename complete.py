from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui as py

TIME_MULTIPLIER = 1
# 쿠폰을 발행할 회원의 페이지
PAGE_FROM =1 
PAGE_TO =3

video_lectures = [None,
                      '소설번역의 방법',
                      '영상번역가를 위한 번역의 원리',
                      '독해 및 번역을 위한 문법 총정리 및 클리닉',
                      '일본어 고전문법',
                      '번역가를 위한 한글 맞춤법 (심화)',
                      '번역가를 위한 한글 맞춤법 (입문)',
                      '번역가를 위한 외래어 표기법 (심화)',
                      '번역가를 위한 외래어 표기법 (입문)',
                      'Subtitle Edit 강의 (심화)']
SELECTED_VIDEO_LECTURE = '일본어 고전문법'

lectures = [ None,
                '일어출판번역 - 입문', 
                '일어출판번역 - 실전', 
                '영어출판번역 - 입문', 
                '동화작가 - 심화(등록용)', 
                '일어영상번역 - 심화(등록용)', 
                '중국어영상번역 - 심화(등록용)', 
                '일본어출판번역 - 심화(등록용)',
                '중국어영상번역 - 입문',
                '일어영상번역 - 입문',
                '동화작가반 - 입문',
                '영어영상번역 - 입문(화)',
                '영어영상번역 - 입문(수)',
                '영어영상번역 - 입문(토)',
                '영어출판번역 - 입문(23년 9월)',
                '중국어영상번역 - 실전',
                '영어영상번역 - 심화(수)',
                '영어출판번역 - 심화',
                '영어영상번역 - 심화(목)',
                '영어영상번역 - 심화(토)',
                '동화작가반 - 실전',
                '영어영상번역 - 실전',
                '영어출판번역 - 실전(금)',
                '영어영상더빙특강(후반)',
                '웹소설가',
                '중국어컨텐츠반',
                '한일미디어(금)',
                '일어영상번역 - 실전',
                '영어출판번역 - 실전(토)'
                ]
SELECTED_LECTURE = '일어출판번역 - 입문'

driver = webdriver.Chrome()
driver.get("http://www.glbab.com/manage/") ## 사이트 접속

py.sleep(1)

## 로그인하기
id_input = driver.find_element(By.ID,"id")
id_input.send_keys("admin")
password_input = driver.find_element(By.ID,"password")
password_input.send_keys("glbab1018@")

login_btn = driver.find_element(By.CLASS_NAME, "login_btn" )
login_btn.click()

for i in range(PAGE_FROM, PAGE_TO + 1):
  py.sleep(1)

  ## 쿠폰관리 페이지 이동
  driver.get("http://www.glbab.com/manage/coupon/mng/write.jsp")
  py.sleep(2)

  ## 강의 선택

  lecture = Select(driver.find_element(By.CSS_SELECTOR, 'select#sproductName'))
  lecture.select_by_index(lectures.index(SELECTED_LECTURE))

  #################################################### 결제기간 입력
  from_date = '2023-12-01'
  to_date = '2024-01-31'
  
  driver.find_element(By.ID, 'p_orderDay1').click()
  py.press('backspace', presses=10)
  driver.find_element(By.ID, 'p_orderDay1').send_keys(from_date)

  driver.find_element(By.ID, 'p_orderDay2').click()
  py.press('backspace', presses=10)
  driver.find_element(By.ID, 'p_orderDay2').send_keys(to_date)

  #################################################### 사용가능 기간 입력
  from_date = '2024-03-27'
  to_date = '2024-04-30'

  driver.find_element(By.ID, 'p_startDay').click()
  py.press('backspace', presses=10)
  driver.find_element(By.ID, 'p_startDay').send_keys(from_date)

  driver.find_element(By.ID, 'p_endDay').click()
  py.press('backspace', presses=10)
  driver.find_element(By.ID, 'p_endDay').send_keys(to_date)
  py.press('enter')

  ## 쿠폰 사용가능 강좌 선택
  lecture_for_coupon = Select(driver.find_element(By.NAME, 'productFk'))
  lecture_for_coupon.select_by_index(3)

  ## 쿠폰명
  coupon_name = '쿠폰명'
  driver.find_element(By.NAME, 'couponName').send_keys(coupon_name)

  ## 쿠폰금액
  # discount_price = 1000
  # driver.find_element(By.ID, 'discountPrice').clear()
  # driver.find_element(By.ID, 'discountPrice').send_keys(discount_price)


  ## 발행대상 선택하기
  Select(driver.find_element(By.ID, 'onoType')).select_by_index(1) # 결제완료회원 선택
  py.sleep(1*TIME_MULTIPLIER)
  driver.find_element(By.ID, 'memberFind2').click() # 회원 목록 버튼 선택
  py.sleep(1*TIME_MULTIPLIER)
  
  
  if (i!=1):
    pages = driver.find_element(By.CLASS_NAME, 'page').find_elements(By.TAG_NAME, 'a')
    pages[i-2].click() # 페이지 이동
    py.sleep(1*TIME_MULTIPLIER)

  driver.find_element(By.CLASS_NAME, 'b_first_c').click() # 전체목록 선택
  py.sleep(1*TIME_MULTIPLIER)
  btns = driver.find_element(By.CSS_SELECTOR, 'div.btn').find_elements(By.TAG_NAME, 'a')
  btns[1].click() # 추가버튼 클릭
  btns[0].click() # 닫기버튼 클릭

  py.sleep(2*TIME_MULTIPLIER)
  driver.find_element(By.CLASS_NAME, 'btns_wrap').find_element(By.CLASS_NAME, 'btns_blue').click() # 저장 클릭
  py.sleep(1 *TIME_MULTIPLIER)
  py.press('enter') # alert 창 닫기


py.sleep(10)

driver.quit()