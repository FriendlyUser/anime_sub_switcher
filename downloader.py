# youtube_dl download https://v4.szjal.cn/20200816/Pk8C9nha/index.m3u8
# youtube_dl download https://v4.szjal.cn/20200816/Pk8C9nha/1000k/hls/index.m3u8

import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver


def download(url):
    cmd = 'youtube_dl ' + url
    os.system(cmd)

# extracts m3u8 link from the video url
# 
def extract_url(video_url):
    if video_url.endswith('.m3u8'):
        return video_url
    else:
        return video_url + '/index.m3u8'

# read REMOTE_SELENIUM_KEY and REMOTE_SELENIUM_URL from environment variables

REMOTE_SELENIUM_KEY = os.environ.get('REMOTE_SELENIUM_KEY')
REMOTE_SELENIUM_USERNAME = os.environ.get('REMOTE_SELENIUM_USERNAME')

def make_webdriver(build_name="anime_sub_switcher"):
    # make a webdriver
    url = f"https://{REMOTE_SELENIUM_USERNAME}:{REMOTE_SELENIUM_KEY}@hub-cloud.browserstack.com/wd/hub"
    desired_cap = {
        "build": build_name,  # CI/CD job or build name
    }
    driver = webdriver.Remote(
        command_executor=url
    )
    return driver
# selenium browser

def get_ktkkt_video_url(ktkkt_url: str):
    driver = make_webdriver()
    # 
    time.sleep(5)

    # wait for the page to load
    driver.get(ktkkt_url)
    # switch to cciframe
    driver.switch_to.frame('cciframe')
    # wait for the video to load
    time.sleep(3)
    # save source to file
    with open('source.html', 'w') as f:
        f.write(driver.page_source)

    driver.quit()
