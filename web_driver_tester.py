from selenium import webdriver

# Path to the Chrome WebDriver executable
webdriver_path = 'C:\chromedriver\chromedriver_win32\chromedriver.exe'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=webdriver_path)

# Open a webpage
driver.get('https://www.google.com')

# Get the page title
page_title = driver.title

# Verify the page title(in this case i am visiting google.com as the test page hence i am expecting Google as a potential header)
expected_title = 'Google'
if page_title == expected_title:
    print("Page title is correct.")
else:
    print(f"Page title is incorrect. Expected: {expected_title}, Actual: {page_title}")

# Close the browser
driver.quit()
