from imports import *
import uuid


chrome_options = Options()
chrome_options.headless = False

driver = webdriver.Chrome(options=chrome_options)

def genrate_random_file_name():
    return str(uuid.uuid4())



def get_image(url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"FFVAD"))) 
    soup = BeautifulSoup(driver.page_source, "lxml")
    source = soup.find("img", class_="FFVAD")   
    image = requests.get(source['src'],allow_redirects=True)
    if 'image' in (image.headers)['Content-type']:
        genrate_random_file_name()
        open(genrate_random_file_name()+'.jpeg','wb').write(image.content)
    driver.close()
    return "Image"

def get_video(url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"_5wCQW")))
    soup = BeautifulSoup(driver.page_source, "lxml")
    source = soup.find("video", class_="tWeCl")
    video = requests.get(source['src'],allow_redirects=True)
    if 'video' in (video.headers)['Content-type']:
        genrate_random_file_name()
        open(genrate_random_file_name()+'.mp4','wb').write(video.content)
    driver.close()


def get_igtv(url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"_5wCQW")))
    soup = BeautifulSoup(driver.page_source, "lxml")
    source = soup.find("video", class_="tWeCl")
    video = requests.get(source['src'],allow_redirects=True)
    if 'video' in (video.headers)['Content-type']:
        genrate_random_file_name()
        open(genrate_random_file_name()+'.mp4','wb').write(video.content)
    driver.close()


def get_file(url, type_):
    if type_ == 'Image':
        get_image(url)
    elif type_ == 'Video':
        get_video(url)
    elif type_ == "IGTV":
        get_igtv(url)
