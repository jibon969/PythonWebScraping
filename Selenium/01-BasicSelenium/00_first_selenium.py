from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="D:/CodingProgramming/PythonProgramming/PythonWebScraping/Selenium/00-ChromeDriver/"
)

driver.get("https://www.google.com/")
driver.maximize_window()

