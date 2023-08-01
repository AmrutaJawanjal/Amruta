

class Test_Credence23:
    def test_sub_005(self):
        a = 12
        b = 7
        sub = a - b
        print("Subtraction of a from b is :" + str(sub))
        if sub == 5:
            assert True
        else:
            assert False


        a=2
        b=3
        mul=a*b
        print("multiplication of a from b is:" +str(mul))
        if mul == 6:
            assert True
        else:
            assert False

        def test_Creditcard_009(self):
            driver.maximize_window()

        from selenium import webdriver
        from selenium.webdriver.common.by import By

        driver = webdriver.Chrome()
        driver.get("https://phptravels.net/admin/login.php")
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("admin@phptravels.com")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("demoadmin")
        driver.find_element(By.XPATH, "//button[@id='submit']").click()
        try:
            driver.find_element(By.XPATH, "//p[@class='m-0 page_title'] ").click()
            print("login testcase is passed")
        except:
            print("login testcase is failed")
        time.sleep(10)


