import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui as py
import threading
stop_signal = False


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



# 선택된 항목을 처리하는 함수
def handle_video_lecture_selection(event):
    selected_video_lecture = video_lecture_var.get()
    print(f"선택된 비디오 강의: {selected_video_lecture}")

def handle_lecture_selection(event):
    selected_lecture = lecture_var.get()
    print(f"선택된 강의: {selected_lecture}")

# 애플리케이션 초기화
app = tk.Tk()
app.title("GUI 애플리케이션")

# 변수 설정
time_multiplier_var = tk.IntVar(value=1)
page_from_var = tk.IntVar(value=1)
page_to_var = tk.IntVar(value=1)

# TIME_MULTIPLIER 입력 필드
time_multiplier_label = ttk.Label(app, text="TIME_MULTIPLIER")
time_multiplier_label.pack()
time_multiplier_entry = ttk.Entry(app, textvariable=time_multiplier_var)
time_multiplier_entry.pack()

# PAGE_FROM 입력 필드
page_from_label = ttk.Label(app, text="PAGE_FROM")
page_from_label.pack()
page_from_entry = ttk.Entry(app, textvariable=page_from_var)
page_from_entry.pack()

# PAGE_TO 입력 필드
page_to_label = ttk.Label(app, text="PAGE_TO")
page_to_label.pack()
page_to_entry = ttk.Entry(app, textvariable=page_to_var)
page_to_entry.pack()



# video_lectures 드롭다운 메뉴
video_lecture_var = tk.StringVar()
video_lecture_label = ttk.Label(app, text="비디오 강의 선택:")
video_lecture_label.pack()
video_lecture_dropdown = ttk.Combobox(app, textvariable=video_lecture_var)
video_lecture_dropdown['values'] = video_lectures
video_lecture_dropdown.bind("<<ComboboxSelected>>", handle_video_lecture_selection)
video_lecture_dropdown.pack()

# lectures 드롭다운 메뉴
lecture_var = tk.StringVar()
lecture_label = ttk.Label(app, text="강의 선택:")
lecture_label.pack()
lecture_dropdown = ttk.Combobox(app, textvariable=lecture_var)
lecture_dropdown['values'] = lectures
lecture_dropdown.bind("<<ComboboxSelected>>", handle_lecture_selection)
lecture_dropdown.pack()

# 결제기간 및 사용기간 입력 필드 추가
payment_from_var = tk.StringVar(value='2023-12-01')
payment_to_var = tk.StringVar(value='2023-01-31')
service_from_var = tk.StringVar(value='2024-03-27')
service_to_var = tk.StringVar(value='2024-04-30')

payment_from_label = ttk.Label(app, text="결제기간 시작 (예: YYYY-MM-DD)")
payment_from_label.pack()
payment_from_entry = ttk.Entry(app, textvariable=payment_from_var)
payment_from_entry.pack()

payment_to_label = ttk.Label(app, text="결제기간 종료 (예: YYYY-MM-DD)")
payment_to_label.pack()
payment_to_entry = ttk.Entry(app, textvariable=payment_to_var)
payment_to_entry.pack()

service_from_label = ttk.Label(app, text="사용기간 시작 (예: YYYY-MM-DD)")
service_from_label.pack()
service_from_entry = ttk.Entry(app, textvariable=service_from_var)
service_from_entry.pack()

service_to_label = ttk.Label(app, text="사용기간 종료 (예: YYYY-MM-DD)")
service_to_label.pack()
service_to_entry = ttk.Entry(app, textvariable=service_to_var)
service_to_entry.pack()

def stop_script():
    global stop_signal
    stop_signal = True
    print("스크립트 중지 요청됨")
def on_stop_clicked():
    stop_thread = threading.Thread(target=stop_script)
    stop_thread.start()

def run_script():
    global stop_signal
  # GUI에서 선택된 값들을 가져옴
    payment_from = payment_from_var.get()
    payment_to = payment_to_var.get()
    service_from = service_from_var.get()
    service_to = service_to_var.get()

    TIME_MULTIPLIER = time_multiplier_var.get()
    PAGE_FROM = page_from_var.get()
    PAGE_TO = page_to_var.get()
    SELECTED_VIDEO_LECTURE = video_lecture_var.get()
    SELECTED_LECTURE = lecture_var.get()
    
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

      driver.find_element(By.ID, 'p_orderDay1').click()
      py.press('backspace', presses=10)
      driver.find_element(By.ID, 'p_orderDay1').send_keys(payment_from)

      driver.find_element(By.ID, 'p_orderDay2').click()
      py.press('backspace', presses=10)
      driver.find_element(By.ID, 'p_orderDay2').send_keys(payment_to)

      #################################################### 사용가능 기간 입력

      driver.find_element(By.ID, 'p_startDay').click()
      py.press('backspace', presses=10)
      driver.find_element(By.ID, 'p_startDay').send_keys(service_from)

      driver.find_element(By.ID, 'p_endDay').click()
      py.press('backspace', presses=10)
      driver.find_element(By.ID, 'p_endDay').send_keys(service_to)
      py.press('enter')

      ## 쿠폰 사용가능 강좌 선택
      lecture_for_coupon = Select(driver.find_element(By.NAME, 'productFk'))
      lecture_for_coupon.select_by_index(video_lectures.index(SELECTED_VIDEO_LECTURE))

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
      # driver.find_element(By.CLASS_NAME, 'btns_wrap').find_element(By.CLASS_NAME, 'btns_blue').click() # 저장 클릭
      # py.sleep(1 *TIME_MULTIPLIER)
      # py.press('enter') # alert 창 닫기


    py.sleep(10)

    driver.quit()

# 실행 버튼 (여기에 실제 스크립트 실행 로직을 추가)
run_button = ttk.Button(app, text="실행", command=run_script)
run_button.pack()


# 중지 버튼
stop_button = ttk.Button(app, text="중지", command=on_stop_clicked)
stop_button.pack()

# 애플리케이션 실행
app.mainloop()
