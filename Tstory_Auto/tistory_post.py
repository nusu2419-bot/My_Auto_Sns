import time

from playwright.sync_api import sync_playwright

import config

def post_tistory():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="auth.json") #
        page = context.new_page()

        page.goto(config.BLOG_URL) 
        time.sleep(10) # 로딩 대기

        try:
            # 1. 카테고리 선택 (전과 동일)
            page.click("i.mce-txt:has-text('카테고리')")
            time.sleep(2)
            page.click("span.mce-text:has-text('- 생활정보')")
            time.sleep(2)

            # 2. 제목 한 글자씩 입력 (delay: 밀리초 단위, 100ms = 0.1초)
            page.click("#post-title-inp")
            page.type("#post-title-inp", "한 글자씩 타이핑하는 테스트 제목입니다.", delay=150)
            time.sleep(2)

            # 3. 본문 한 글자씩 입력 (iframe 내부)
            editor_frame = page.frame_locator("#editor-tistory_ifr")
            editor_frame.locator("#tinymce").click()
            time.sleep(1)
            # 본문도 0.1초 간격으로 타이핑
            editor_frame.locator("#tinymce").type("이 내용은 사람이 직접 입력하는 것처럼 천천히 작성되고 있습니다.", delay=100)
            time.sleep(3)

            # 4. 태그 한 글자씩 입력
            page.click("#tagText")
            page.type("#tagText", "파이썬,자동화,타이핑테스트", delay=120)
            page.keyboard.press("Enter")
            time.sleep(2)

            # 5. 비공개 저장 프로세스
            page.click("#publish-layer-btn")
            time.sleep(3)
            page.click("#publish-btn")
            print("한 글자씩 입력하여 비공개 저장 완료!")

        except Exception as e:
            print(f"오류 발생: {e}")

        time.sleep(5)
        browser.close()

if __name__ == "__main__":
    post_tistory()