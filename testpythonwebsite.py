import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestPythonWebSite(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_search_in_python_org(self): #arama işlemleri
        driver = self.driver
        driver.get("http://pypi.org/")
        #print(driver.title)
        self.assertIn("PyPI", driver.title) #driver.title içinde PyPI geçip geçmediğini test eder.
        elem = driver.find_element(By.NAME,"q")
        elem.send_keys("selenium")
        elem.send_keys(Keys.RETURN) #entere basma kısmı
        assert "There were no results for" not in driver.page_source #driver.page_source içinde değilse bunu assert et

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
