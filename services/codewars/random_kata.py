import traceback
from playwright.sync_api import sync_playwright
import random
import requests
from pathlib import Path
import sys
ROOT_PATH = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_PATH))

from services.logger_config import logger



def get_difficult(kata_id):
    """parse difficult from random kata using codewars API"""
    url = f"https://www.codewars.com/api/v1/code-challenges/{kata_id[6:]}"
    response = requests.get(url)
    try:
        data = response.json()
        return data.get("rank").get("name")
    except Exception as e:
        logger.error(e)


def get_random_kata():
    """parse random kata from codewars using playwright"""
    try:
        with sync_playwright() as p:
            # upload browser with 'autorisation file 'auth.json''
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(storage_state="auth.json")
            page = context.new_page()

            # url where we parse kata
            url = "https://www.codewars.com/kata/search/my-languages?q=&r%5B%5D=-6&r%5B%5D=-7&order_by=sort_date+desc&sample=true"
            
            page.goto(url)

            try:
                
                
                selector = "div.list-item-kata"
                # waiting for selector set timeout 100000
                page.wait_for_selector(selector, timeout=10000)

                # find all katas by selector
                katas = page.locator(selector).all()
                
                if katas:
                    # choice random kata
                    random_kata = random.choice(katas)
                    # parsing title
                    title = random_kata.get_attribute("data-title")
                    # find a ling for kata
                    link = random_kata.locator("a").first.get_attribute("href")


                    difficult = get_difficult(link)
                    
                    return {
                        "title": title,
                        "difficulty": difficult,
                        "link": f"https://www.codewars.com{link}"

                    }
            except Exception as e:
                logger.error(f"Error: {e}. Maybe session in auth.json is deprecated")
            finally:
                browser.close()

    except Exception as e:
        logger.error(f"Exception occured:\n {traceback.format_exc()}")


