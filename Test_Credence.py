from selenium import webdriver


class Test_Credence:
    def test_sum_001(self):
        a=3
        b=7
        sum=a+b
        if sum==10:
            print("sum of a and b is:"+str(sum))
            assert True
        else:

           assert False



def test_credence_002 (self):
    driver=webdriver.Chrome()
    driver.get("http://https://credence.in/")
    if driver.title=="credence":
        print("you are at credence.in")
    else:
        print("wrong site")

