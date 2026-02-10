from playwright.sync_api import sync_playwright
from services.logger_config import logger
import traceback

def save_auth():
    """
    saving codewars authorising data for future work with it
    """
    browser = None
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://www.codewars.com/users/sign_in")
            
            print("Please. Login in browser")

            page.wait_for_timeout(20000) # timeout 60 second
            

            context.storage_state(path="auth.json")
            print("Authorisation is saved in auth.json")
            browser.close()
    except Exception:
        logger.error(f"Exception occurred:\n", traceback.format_exc())
    finally:
        if browser:
            browser.close()

if __name__ == "__main__":
    save_auth()