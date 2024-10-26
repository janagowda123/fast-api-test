from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Optional: starts Chrome maximized

# Set up the Chrome driver using the updated method
#service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.google.com")

# Print the title of the page
print("Page title:", driver.title)

# Close the browser
driver.quit()
