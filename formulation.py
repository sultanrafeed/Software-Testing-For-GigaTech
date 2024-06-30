import time
import sys
sys.stdout.reconfigure(encoding='utf-8')
from pynput.keyboard import Key, Controller

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)


def clear_input_field(input_element):
    input_element.send_keys(Keys.CONTROL + 'a')
    input_element.send_keys(Keys.DELETE)

def gotoUser():
    element_xpath = '//*[@id="root"]/section/main/aside/div/div/div/div[3]/a/div'
    element = driver.find_element(By.XPATH, element_xpath)
    element.click()
    time.sleep(1)

def createUser(name,gender,ins,password,role,mail,date,qua,num):
    flag=0
    element_xpath = '//*[@id="root"]/section/main/div[2]/div[2]/section/div[2]/button'
    element = driver.find_element(By.XPATH, element_xpath)
    element.click()
    time.sleep(1)

    full_name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'full_name')))
    gender_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'gender')))
    institution_name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'institution_name')))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
    role_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'role')))
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
    dob_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'dob')))
    qualification_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'qualification')))
    mobile_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'mobile')))

    clear_input_field(full_name_input)
    clear_input_field(institution_name_input)
    clear_input_field(password_input)
    clear_input_field(email_input)
    clear_input_field(qualification_input)
    clear_input_field(mobile_input)

    full_name_input.send_keys(name)
    gender_select.send_keys(gender)
    institution_name_input.send_keys(ins)
    password_input.send_keys(password)
    role_select.send_keys(role)
    email_input.send_keys(mail)
    dob_input.send_keys(date)
    qualification_input.send_keys(qua)
    mobile_input.send_keys(num)

    try:
        add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add']")))
        add_button.click()
        # print("Button Clicked")
        time.sleep(1)
        try:
            section = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section[1]')))
            div_elements = section.find_elements(By.TAG_NAME, 'div')
            is_printed = False
            for div_element in div_elements:
                text = div_element.text
                if text:
                    # print(text)
                    if text == "User created successfully":
                        print("Valid")
                        is_printed = True
                    else :
                        print("Invalid")
                        is_printed = True
                        if "exists" not in text:
                            cross  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[1]/img"))) 
                            cross.click()
                if is_printed:
                    break


        except TimeoutException:
            print("Invalid")
    except TimeoutException:
        print("Invalid")
        cross  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[1]/img"))) 
        cross.click()

    time.sleep(2)
    
def Login(id, password):
    driver.get("http://182.163.99.86/login")
    username = id
    password = password

    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password'))) 
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign in']")))

    username_input.send_keys(username)
    password_input.send_keys(password)
    
    button.click()
    time.sleep(2)

    # new_url = driver.current_url
    # if new_url == "http://182.163.99.86/dashboard":
    #     print("Valid.")
    # else:
    #     print("Invalid.")
        
if __name__ == '__main__':

        # test case 1
    Login("admin@gigatech.com","Abc@123")
    gotoUser()
    # print("Test case 1:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.sulta1314n10u069@northsouth.edu","21/01/2000", "Undergrad","01732073478")
    
    # # test case 2
    # print("Test case 2:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Validator","rafeed.suasdgaelta69n1@northsouth.edu","21/01/2000", "Undergrad","01732073478")
    
    
    # # test case 3
    # print("Test case 3:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.sultan2@gmail.com","21/01/2000", "Undergrad","01732073478")
    
    
    # # test case 4
    # print("Test case 4:")
    # createUser("R","Male","North South University","Abc@123","Annotator","rafeed.suhagae69ltan@gmail.com","21/01/2000", "Undergrad","01732073478")
    
    
    # # test case 5
    # print("Test case 5:")
    # createUser("Rafeed123123","Male","North South University","Abc@123","Annotator","raf69eed.sulagegegtan2@gmail.com","21/01/2000", "Undergrad","01732073478")
    
    
    # # test case 6
    # print("Test case 6:")
    # createUser("Rafeed-Mohammad S’ultan@","Male","North South University","Abc@123","Annotator","rafe69ed.sultaaeggnyyy@gmail.com","21/01/2000", "Undergrad","01732073478")
    
    
    # # test case 7
    # print("Test case 7:")
    # createUser("RS","Male","North South University","Abc@123","Annotator","ra69feed.sulagagt69an3@gmail.com","21/01/2000", "Undergrad","01732073478")
    
    
    # # test case 8
    # print("Test case 8:")
    # createUser("","Male","North South University","Abc@123","Annotator","rafe69ed.su69ltgaregany@gmail.com","21/01/2000", "Undergrad","01732073478")
    
    
    
    # # test case 9
    # print("Test case 9:")
    # createUser("Rafeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd","Male","North South University","Abc@123","Annotator","rafeed.sult34aerrtgg343anl@gmail.com","21/01/2000", "Undergrad","01732073478")
    
    
    # # test case 10
    # print("Test case 10:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","","21/01/2000", "Undergrad","01732073478")
    
    
    # test case 11
    # print("Test case 11:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.sultan","21/01/2000", "Undergrad","01732073478")
    
    
    # # test case 12
    # print("Test case 12:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.sultan@","21/01/2000", "Undergrad","01732073478")
   
    
    # # test case 13
    # print("Test case 13:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","@rafeed.sultan32_,#$@gmail.com","21/01/2000", "Undergrad","01732073478")
   
    
    # # test case 14
    # print("Test case 14:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.sultan@gmail","21/01/2000", "Undergrad","01732073478")
    
    
    # # test case 15
    # print("Test case 15:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","@gigatech.com","21/01/2000", "Undergrad","01732073478")
    
    
    # # test case 16
    # print("Test case 16:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.sul45345tan@northsouth.edu","21/01/2000", "Undergrad","dasdasdasd")
    
    
    # # test case 17
    # print("Test case 17:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.sult2422345an@northsouth.edu","21/01/2000", "Undergrad","$#_.Dasdasdasd")
    
    
    # # test case 18
    # print("Test case 18:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.sul235235tan@northsouth.edu","21/01/2000", "Undergrad","12312334432")
    
    
    # # test case 19 servercrash
    # print("Test case 19:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.su23525tan@northsouth.edu","", "Undergrad","00000000000")
    
    
    # test case 20
    # print("Test case 20:") crash
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.sul32sdfsf525tan@northsouth.edu","21/01/2000", "Undergrad","01035345345")
    
    
    # # # test case 21 crashserver
    # print("Test case 21:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.sulta135315n11@northsouth.edu","", "Undergrad","01732073478")
    
    
    # test case 22 crash
    # print("Test case 22:") 
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.sultasfsdf13515an12@northsouth.edu10","21/01/2000", "Undergrad","01732073478")
    
    
    # test case 23
    # print("Test case 23:")
    # createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.su113sdfasf35ltan13@northsouth9.edu","21/01/2000", "Sdijsdisdjaisjdndfdshnasdasda","01732073478")
    
    
    # test case 24
    print("Test case 24:")
    createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.su13sagdg1513ltan8@northsouth.edu","21/01/2000", "","01732073478")
    
    
    # test case 25
    print("Test case 25:")
    createUser("Rafeed Mohammad Sultan","Male","North South University astagashgasfuigasiugasi","Abc@123","Annotator","r23532afasgasgeed.sultan7@northsouth.edu","21/01/2000", "Undergrad","01732073478")
    
    
    # test case 26
    print("Test case 26:")
    createUser("Rafeed Mohammad Sultan","Male","","Abc@123","Annotator","rafeed.su23sdgaasd5235tan6@northsouth.edu","21/01/2000", "Undergrad","01732073478")
    
    
    # test case 27
    print("Test case 27:")
    createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@123","Annotator","rafeed.sultaasdgsadgn15@northsouth.edu","21/01/2000", "Undergrad","01732073478")
    
    
    # test case 28
    print("Test case 28:")
    createUser("Rafeed Mohammad Sultan","Male","North South University","sdadsdd@123","Annotator","rafeed.sulafbdbdtan@northsouth.edu","21/01/2000", "Undergrad","01732073478")
    
    
    # test case 29
    print("Test case 29:")
    createUser("Rafeed Mohammad Sultan","Male","North South University","@@@@#$#$__,.","Annotator","rafeed.sultafwfgwfan@northsouth.edu","21/01/2000", "Undergrad","01732073478")
    
    
    # test case 30
    print("Test case 30:")
    createUser("Rafeed Mohammad Sultan","Male","North South University","","Annotator","rafeed.sultahbndvan@northsouth.edu","21/01/2000", "Undergrad","01732073478")
    
    
    # test case 31
    print("Test case 31:")
    createUser("Rafeed Mohammad Sultan","Male","North South University","A1@sx","Annotator","rafeed.sultwgrban@northsouth.edu","21/01/2000", "Undergrad","01732073478")
    
    
    # test case 32
    print("Test case 32:")
    createUser("Rafeed Mohammad Sultan","Male","North South University","Abc@1234asd5678910!","Annotator","rafeed.sulbnsdvvtan@northsouth.edu","21/01/2000", "Undergrad","01732073478")
    