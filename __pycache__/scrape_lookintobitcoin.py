from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
import os

def scrape_lookintobitcoin(chart_url):
    try:
        print("Launching Edge browser...")

        # Path to Edge WebDriver in Downloads
        driver_path = "C:/Users/phili/Drivers/msedgedriver.exe"
        if not os.path.exists(driver_path):
            raise FileNotFoundError(f"Edge WebDriver not found at {driver_path}")

        options = Options()
        options.use_chromium = True
        options.add_argument("--disable-gpu")
        # options.add_argument("--headless")  # Optional for silent scraping

        service = Service(driver_path)
        driver = webdriver.Edge(service=service, options=options)

        print("Opening chart page...")
        driver.get(chart_url)
        time.sleep(6)

        print("Attempting to locate chart elements...")
        tooltip_elements = driver.find_elements(By.CLASS_NAME, "tv-lightweight-charts")
        if tooltip_elements:
            print("Chart loaded. Tooltip scraping not yet implemented.")
        else:
            print("Could not locate Mayer Multiple value.")

        driver.quit()
        return None

    except Exception as e:
        print(f"Error scraping Mayer Multiple: {e}")
        return None

# Test run
if __name__ == "__main__":
    scrape_lookintobitcoin("https://www.lookintobitcoin.com/charts/bitcoin-investor-tool/")
