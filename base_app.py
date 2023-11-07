from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Remote
from bs4 import BeautifulSoup
from find_func import slice_str, rslice_str


class BasePage:
    BASE_URL = 'http://uitestingplayground.com/sampleapp'
    ERROR_MESSAGE = 'WE CANT FIND THE ELEMENT '

    def __init__(
            self,
            driver: Remote
    ):

        self.driver = driver
        self.go_to_base_page

    def find_element_in_dom(
            self,
            locator: tuple[str: str],
            wait: float
    ):

        return WebDriverWait(
            driver=self.driver,
            timeout=wait
        ).until(
            method=EC.presence_of_element_located(locator),
            message=self.ERROR_MESSAGE
        )

    def find_elements_in_dom(
            self,
            locator: tuple[str, str],
            wait: float
    ):

        return WebDriverWait(
            driver=self.driver,
            timeout=wait
        ).until(
            method=EC.presence_of_all_elements_located(locator),
            message=self.ERROR_MESSAGE
        )

    def wait_to_be_clickable(
            self,
            locator: tuple[str, str],
            wait: float
    ):

        WebDriverWait(
            driver=self.driver,
            timeout=wait
        ).until(
            method=EC.element_to_be_clickable(locator),
            message=self.ERROR_MESSAGE
        )

        return self.find_element_in_dom(locator, wait)

    def get_html_element(
            self,
            page: str,
            element_tag: str,
            element_attr: dict
    ):
        """

        :param page: some str html page
        :param element_tag: some tag. #"div", "li", ...
        :param element_attr: some attribute. #{'class':'row'}, ....
        :return:
        """

        for element in BeautifulSoup(page, 'html.parser').find_all(element_tag, element_attr):
            yield element




    def get_dynamic_attr_from_html_element(
            self,
            page: str,
            element_tag: str,
            element_attr: dict,
            wait: float,
            **extra
    ):
        """


        :param page: some str html page
        :param element_tag: some tag. #"div", "li", ...
        :param element_attr: some attribute. #{'class':'row'}, ....
        :param wait: some timeout in sec
        :param extra: {"element_(some_name)":["start_counter":"element_tag", "end_counter": "element_tag"],..}
            параметр используется для облегчения поиска html элементов при условии глубокой вложенности,
            элементы должны перечисляться в глубину
        :return:
        """
        element = self.get_html_element(page, element_tag, element_attr)

        while element:
            try:
                http_element: str = str(next(element))

            except StopIteration:
                print('end of http element')
                break

            else:

                for http_element_counters in extra.values():

                    element_text = slice_str(http_element)
                    start_counter = http_element_counters['start_counter']
                    end_counter = http_element_counters['end_counter']

                    http_element = slice_str(
                        mess=http_element,
                        subj=start_counter
                    )
                    http_element = rslice_str(
                        mess=http_element,
                        subj=end_counter,
                        option='rfind'
                    )

                http_element = rslice_str(
                    mess=http_element,
                    subj=end_counter
                )

                yield element_text, http_element














    @property
    def go_to_base_page(self):
        return self.driver.get(self.BASE_URL)



