from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
import time

# 設置 Chrome 選項
options = Options()
# 可以根據需要進行其他設置，如無頭模式（不顯示 Chrome 視窗）
# options.add_argument("--headless")

# 自動安裝和更新適用於當前 Chrome 版本的 ChromeDriver
service = Service(ChromeDriverManager().install())

# 初始化 WebDriver，並傳遞選項和服務
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open YouTube
    driver.get("https://www.youtube.com")

    # Wait for the page to load
    time.sleep(5)

    # Find the search bar element and input 'abc'
    search_bar = driver.find_element(By.NAME, 'search_query')
    search_bar.send_keys('abc')

    # Press Enter to perform the search
    search_bar.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(5)

    # Find the first video element and get its title
    first_video = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="video-title"]'))
        #EC.presence_of_element_located.這是 Selenium 中的預期條件（Expected Condition），用來等待一個元素出現在頁面上。具體來說，它會持續檢查頁面直到該元素在 DOM 結構中存在（不管元素是否可見，只要它在頁面中出現）。
        #(By.XPATH, '//*[@id="video-title"]')：這是用來定位元素的方式。By.XPATH 表示使用 XPath 查找元素，而 '//*[@id="video-title"]' 是一個 XPath 表達式，用來選擇具有 id 屬性為 video-title 的元素。在 YouTube 頁面中，這通常指的是每個視頻標題的元素。
    )
    video_title = first_video.get_attribute('title')
    video_link = first_video.get_attribute('href')
    thumbnail_image = first_video.find_element(By.XPATH, '//*[@id="thumbnail"]/yt-image/img').get_attribute('src')

    print("Title of the first video:", video_title)
    print("Link of the first video:", video_link)
    print("Thumbnail image URL of the first video:", thumbnail_image)

finally:
    # Close the browser
    driver.quit()
