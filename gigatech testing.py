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
        time.sleep(1)
        try:
            section = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section[1]')))
            div_elements = section.find_elements(By.TAG_NAME, 'div')

            for div_element in div_elements:
                
                success = "User created successfully"
                text = div_element.text
                if text == "An user with this email already exists":
                    print("Invalid")
                    break
                elif text == success:
                    print("Valid")
                    break
                elif text != success:
                    print("Invalid")
                    time.sleep(3)
                    cross  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[1]/img"))) 
                    time.sleep(3)
                    cross.click()
                    break
        except TimeoutException:
            print("Invalid")
    except TimeoutException:
        print("Invalid")
        cross  = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[1]/img"))) 
        cross.click()
     
    time.sleep(3)




def makeUser():
    gotoUser()
    # createUser("T1","Male","NSU","Wasi123!","Annotator","tt1@gmail.com","1990-01-21","abc","01300000000")
    # createUser("T2","Male","NSU","Wasi123!","Manager","tt2@gmail.com","1990-01-21","abc","01300000000")
    # createUser("T3","Male","NSU","Wasi123!","Validator","tt3@gmail.com","1990-01-21","abc","01300000000")
    # createUser("T4","Male","NSU","Wasi123!","Guest","tt4@gmail.com","1990-01-21","abc","01300000000")
    # pass
    createUser("S6","Male","NSU","Wasi123!","Manager","tsas6@gmail.com","21/01/2000","abc","01300000000")


def createProject(Porject_Lable):
    Projects = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div/div[1]/div[1]/div/button'))) 
    Projects.click()
    Create_project = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[1]/button'))) 
    Create_project.click()

    Project_lable =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
    clear_input_field(Project_lable)
    Project_lable.send_keys(Porject_Lable)

    
    parent_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section/div/div")))
    nested_divs = parent_div.find_elements(By.TAG_NAME, "button")

    for nested_div in nested_divs[:-1]:
        nested_div.click()
        time.sleep(1)
        tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/div/div/div')))
        tag_btn = tag.find_elements(By.TAG_NAME, "button")
        for i in tag_btn:
            i.click()
        time.sleep(1)
        break
    time.sleep(2)

    button_xpath = '/html/body/div[3]/div/div/div[3]/button'
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        print("Button is clickable")
        create_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[3]/button'))) 
        create_button.click()

    except TimeoutException:
        print("Button is not clickable")
        close = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[1]/img'))) 
        close.click()

    time.sleep(1)

def navproject(Porject_Lable):
    try:
        Projects = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div/div[1]/div[1]/div/button'))) 
        Projects.click()
    except TimeoutException:
        print("In directory")

    project_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[2]/div[1]/div[2]/input')))
    clear_input_field(project_name)
    project_name.send_keys(Porject_Lable)
    time.sleep(2)

    eye_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr/td[9]/div/span[1]/a/img')))
    eye_icon.click()

    time.sleep(1)

def uploadfile():
    upload_btn  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[1]/div/div[2]/button[1]' ))) 
    upload_btn.click()

    annotation_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="1"]' ))) 
    annotation_box.click()

    browse_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section/div[2]/div/span/a' ))) 
    browse_file.click()

    time.sleep(1)

    Keyboard = Controller()
    Keyboard.type("C:\\Users\\Wasi\\Downloads\\1.xlsx")
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)

    time.sleep(1)

    upload_data = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[3]/button'))) 
    upload_data.click()
    
    time.sleep(2)

def creategroup(annotator, validator):
    create_grp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[4]/div/div/div[1]/button')))
    create_grp.click()

    groupname = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/input')))
    clear_input_field(groupname)
    groupname.send_keys("p1")

    annotator_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[1]/div/input')))
    clear_input_field(annotator_name)
    annotator_name.send_keys(annotator)
    time.sleep(2)

    select_annotator = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr/td[1]/button')))
    select_annotator.click()

    time.sleep(1)

    change_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[1]/button')))
    change_option.click()

    # change_option.send_keys(Keys.ARROW_DOWN)
    # Switch from annotator to validator is a problem


    time.sleep(2)


def navproject2(project_name): # navigate to project file for annotator and validator
    goto_project = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/aside/div/div/div/div[2]/a/div')))
    goto_project.click()


    search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div/div[1]/div/input')))
    search.send_keys(project_name)
    time.sleep(2)
    view = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/section/main/div[2]/div[2]/section/div/div[2]/div/table/tbody/tr/td[9]/div/a')))
    view.click()

    time.sleep(2)

def start_annotation(group_name):
    group = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/section/main/div[2]/div[2]/section/section[4]/div/div/div[1]/div/input')))
    group.send_keys(group_name)
    time.sleep(2)

    start_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[4]/div/div/div[2]/div/table/tbody/tr/td[9]/div/a')))
    start_btn.click()
    time.sleep(2)

    while True:
        try:
            tag_grid = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section[2]')))
            spans = tag_grid.find_elements(By.TAG_NAME, "span")

            if not spans:
                print("No spans found. Breaking the loop.")
                break
            for span in spans: #iterate over tags
                span.click()
                break
            actions = ActionChains(driver)
            sentence = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section[3]/div/div/div')))
            sentence_span = sentence.find_elements(By.TAG_NAME, "span")
            for span in sentence_span: #iterate over words
                actions.double_click(span).perform()
                break
            time.sleep(1)
            submit_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section[3]/div/div/footer/button[1]')))
            submit_btn.click()

        except TimeoutException:
            print("tag_grid not found. Breaking the loop.")
            break
    time.sleep(1)

def start_validation(group_name):
    group = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/section/main/div[2]/div[2]/section/section[4]/div/div/div[1]/div/input')))
    group.send_keys(group_name)
    time.sleep(2)

    start_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[4]/div/div/div[2]/div/table/tbody/tr/td[9]/div/a')))
    start_btn.click()
    time.sleep(2)

    cnt = 0
    while len(driver.find_elements(By.CLASS_NAME, '_like-edit-section_1ctbc_32')) > 0:
        print("size ")
        print(len(driver.find_elements(By.CLASS_NAME, '_like-edit-section_1ctbc_32')))

        like_edit_divs = driver.find_elements(By.CLASS_NAME, '_like-edit-section_1ctbc_32')
        like_edit_div = like_edit_divs[0]
        like_btn_div = like_edit_div.find_element(By.CLASS_NAME, '_like-btn_1ctbc_42')
        edit_btn_div = like_edit_div.find_element(By.CLASS_NAME, '_edit-btn_1ctbc_50')

        if cnt%2 == 0:
            time.sleep(1)
            like_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_like-button_1ctbc_77')))
            like_btn.click()
            time.sleep(1)
        else:
            edit_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_edit-btn_1ctbc_50')))
            edit_btn.click()
            time.sleep(1)

            # After clicking edit button
            # class = _annotation-type-container_1bu34_10 col-lg-3 col-md-4 tag containner
                # tag name in class = _annotation-type-title_1bu34_16
                # class = _ner-sub-category-badge-selected_1bu34_22 badge bg-transparent selected tag
                # class = _ner-sub-category-badge_1bu34_22 badge bg-transparent not selected tag
            # _ner-annotaion-text_1bu34_44

            tag_classes = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, '_annotation-type-container_1bu34_10.col-lg-3.col-md-4')))

            clicked = False
            for tag_class in tag_classes:
                try:
                    span_element = tag_class.find_element(By.CLASS_NAME, '_ner-sub-category-badge_1bu34_22.badge.bg-transparent')
                    span_element.click()
                    clicked = True
                    time.sleep(2)
                except NoSuchElementException:
                    print("No span found in this div")
                if clicked:
                    break
            

            annotaion_text_div = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, '_ner-annotaion-text_1bu34_44'))
            )

            # Find and iterate over the mark and span tags
            mark_tag = annotaion_text_div.find_element(By.TAG_NAME, 'mark')
            driver.execute_script("arguments[0].click();", mark_tag)
            time.sleep(1)
            span_tags = annotaion_text_div.find_elements(By.TAG_NAME, 'span')
            first_span_tag = span_tags[0]
            actions = ActionChains(driver)
            actions.double_click(first_span_tag).perform()
            time.sleep(1)

            submit_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/section[2]/div/div/div[2]/button[1]')))
            submit_btn.click()

            time.sleep(1)                                                                                
        cnt = cnt + 1


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

    new_url = driver.current_url
    if new_url == "http://182.163.99.86/dashboard":
        print("Valid.")
    else:
        print("Invalid.")
        
            
def Logout():
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "radix-:r5:")))
    button.click()
    time.sleep(4) 
    logout_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-radix-collection-item] > img[alt='logout']")))

    logout_button.click()
    time.sleep(2)

# Testcases for login
def test_login():
    
    # Test cases for login (admin)    
    # Test Case 1
    print("Test Case 1: ")
    Login("admin@gigatech.com","Abc@123")
    Logout()
    
    # Test Case 2
    print("Test Case 2: ")
    Login("admim@gigatech.com","Abc@123")
    
    # Test Case 3
    print("Test Case 3: ")
    Login("","Abc@123")
    
    # Test Case 4
    print("Test Case 4: ")
    Login("admin@gigatech.com","Abcd@123")
    
    # Test Case 5
    print("Test Case 5: ")
    Login("admin@gigatech.com","")
    
    # Test Case 6
    print("Test Case 6: ")
    Login("","")
    
    # Test Case 7
    print("Test Case 7: ")
    Login("admin@","Abc@123")
    
    # Test Case 8
    print("Test Case 8: ")
    Login("@gigatech","Abc@123")

def test_logout():
    Login("admin@gigatech.com","Abc@123")
    Logout()
    print("Test Case 1: ")
    new_url = driver.current_url
    if new_url == "http://182.163.99.86/login":
        print("Valid.")
    else:
        print("Invalid.")


if __name__ == '__main__':

    project_name = "Porject_Lable"
    group_name = "Abdc"
    # Admin Login
    # makeUser()
    # Logout()
    # Login("tt2@gmail.com","Wasi123!")  #Admin /  Manager Part
    Login("admin@gigatech.com","Abc@123")
    # createProject(project_name)  # creates a project
    # navproject(project_name)  # nav to project
    # uploadfile()  #upload data
    #creategroup("T1","T3") # error
    # Logout()

    # Annotator Part
    # Login("tt1@gmail.com","Wasi123!")
    # navproject2(project_name)
    # start_annotation(group_name)
    # Logout()


    #Validator Part
    # Login("tt3@gmail.com","Wasi123!")
    # navproject2(project_name)
    # start_validation(group_name)
    # Logout()    
    
    #test_login()
    #test_logout()
    

    

    
   

    

    