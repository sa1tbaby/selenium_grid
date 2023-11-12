import time

import selenium.webdriver.firefox.remote_connection
from pytest import fixture
from selenium import webdriver
from page_app import PageObject
from bs4 import BeautifulSoup




DRIVER_URL = 'http://192.168.1.157:4444/wd/hub'

DRIVER_OPTION = webdriver.ChromeOptions()

NODE_OPTION_chrome = {"browserName":"chrome",
               "browserVersion":"119.0",
               "platformName":"linux",
               "se:noVncPort":7900,
               "se:vncEnabled":True}

NODE_OPTION_firefox = {"browserName":"firefox",
               "browserVersion":"119.0",
               "platformName":"linux",
               "se:noVncPort":7900,
               "se:vncEnabled":True}


def get_element(
        page: str,
        element_tag: str,
        element_attr: dict
):
    for element in BeautifulSoup(page, 'html.parser').find_all(element_tag, element_attr):
        yield element


def browser():

    for key, value in NODE_OPTION_chrome.items():
        DRIVER_OPTION.set_capability(key, value)

    driver = webdriver.Remote(
        command_executor=DRIVER_URL,
        options=DRIVER_OPTION
    )

    yield driver


    driver.quit()

brwsr = browser()
#s.get('http://uitestingplayground.com/sampleapp')

attrs = ['type',
         'aria-expanded', 'aria-controls',
         'data-target', 'data-toggle',
         'type', 'aria-label', 'same']

for inst in brwsr:
    page_instance = PageObject(driver=inst)

    cort = 'class name', 'navbar-toggler'
    cortww = 'class name', 'row'
    twae = page_instance.find_element_in_dom(cort, 10)
    for i in page_instance.find_elements_in_dom(cortww, 10):
        aaadsd = i.location
    aasd = twae.text
    dsgsgfaf = twae.tag_name
    for j in attrs:
        axcxzxvc = twae.get_attribute(j)

    sd =2




    """
    html_page = page_instance.driver.page_source
    extra = {
        'element_1':{"start_counter":"<div",
                     "end_counter": "</div>"},
        'element_2':{"start_counter": "<div",
                     "end_counter": "</div>"},
        'element_3':{"start_counter": "<input",
                     "end_counter": "/>"},
        'element_target':{"start_counter": 'id="',
                     "end_counter": '" '}
    }
    sss = page_instance.get_dynamic_attr_from_html_element(
        html_page,
        'div',
        {'class':'row'},
        10,
        **extra

    )

    print(sss)
    for i in sss:
        print(i)

   
    qqq = get_element(ww, 'div', {'class':'row'})

    while qqq:
        try:
            print(next(qqq))
        except StopIteration:
            print('ok')
            break
    """

