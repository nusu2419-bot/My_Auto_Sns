import time, pyperclip, config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# 카카오 로그인 페이지 접속
driver.get("https://accounts.kakao.com/login/?continue=https%3A%2F%2Fwww.tistory.com%2Fauth%2Flogin")
time.sleep(2)

# 아이디/비번 복사 붙여넣기 (보안 우회)
def paste_text(element_name, text):
    pyperclip.copy(text)
    driver.find_element(By.NAME, element_name).send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

paste_text("loginId", config.USER_ID)
paste_text("password", config.USER_PW)
driver.find_element(By.CLASS_NAME, "btn_g.highlight.submit").click()

# 로그인 완료 대기 후 글쓰기 페이지 이동
time.sleep(5) 
driver.get(config.BLOG_URL)