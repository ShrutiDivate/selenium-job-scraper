from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

print("🚀 Step 1: Setting up Chrome browser (visible mode)...")

options = Options()
options.add_argument("--start-maximized")   # opens browser full screen
# NOTE: No headless mode here — browser will be visible

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), 
    options=options
)

print("✅ Chrome launched successfully!")

# ----------------------------------------------------
print("\n🚀 Step 2: Opening the job listing website...")
url = "https://realpython.github.io/fake-jobs/"
driver.get(url)

time.sleep(2)
print("✅ Website opened successfully!")

# ----------------------------------------------------
print("\n🚀 Step 3: Waiting for page content to load...")
time.sleep(2)
print("⏳ Job cards loading...")

# ----------------------------------------------------
print("\n🚀 Step 4: Extracting job details...")

titles = driver.find_elements(By.CLASS_NAME, "title.is-5")
companies = driver.find_elements(By.CLASS_NAME, "subtitle.is-6.company")
locations = driver.find_elements(By.CLASS_NAME, "location")
links = driver.find_elements(By.XPATH, "//a[text()='Apply']")

print(f"📌 Found {len(titles)} jobs!")

# ----------------------------------------------------
print("\n🚀 Step 5: Reading each job entry...")

data = []
for i in range(len(titles)):
    print(f"   ➤ Extracting job {i+1}/{len(titles)}...")

    data.append({
        "title": titles[i].text,
        "company": companies[i].text,
        "location": locations[i].text,
        "apply_link": links[i].get_attribute("href")
    })
    time.sleep(0.2)

# ----------------------------------------------------
print("\n🚀 Step 6: Saving data to CSV...")

df = pd.DataFrame(data)
df.to_csv("selenium_job_scrape.csv", index=False)

print("📄 CSV saved as selenium_job_scrape.csv")

# ----------------------------------------------------
print("\n🚀 Step 7: Closing the browser...")
time.sleep(2)
driver.quit()
print("❌ Browser closed!")

# ----------------------------------------------------
print("\n🎉 Scraping complete! Check your selenium_job_scrape.csv file.")
