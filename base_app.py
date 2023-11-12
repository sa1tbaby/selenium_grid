from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement
class BasePage:
    BASE_URL = 'http://uitestingplayground.com/sampleapp'
    ERROR_MESSAGE = 'WE CANT FIND THE ELEMENT '
    START_PAGE = ''

    def __init__(
            self,
            driver: Remote
    ):

        self.driver = driver
        self.go_to_base_page
        self.update_window_handle()

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

    def find_element_with_compare(
            self,
            locator,
            wait,
            attributes
    ):
        """

        :param locator:
        :param wait:
        :param attributes: {attr:value} element attributes which may find in html cofr
        :return:
        """

        for element in self.find_elements_in_dom(locator, wait):

            state = True
            for key, value in attributes:

                if value != element.get_attribute(key):
                    state = False
                    break

            if not state:
                continue

            return element

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

    def send_text(
            self,
            element: WebElement,
            keys,
    ):
        element.click()
        element.send_keys(keys)

        return element

    def click_element(
            self,
            element
    ):

        element.click()

        return element

    def upload_file(
            self,
            element: WebElement,
            file_path: str
    ):

        with open(file_path, 'r') as file:
            element.send_keys(file.read())

        return element

    def switch_on_another_tab(
            self,
            window_count,
            wait
    ):

        WebDriverWait(
            driver=self.driver,
            timeout=wait
        ).until(
            method=EC.number_of_windows_to_be(window_count),
            message=self.ERROR_MESSAGE
        )

    def update_window_handle(
            self
    ):
        self.START_PAGE = self.driver.current_window_handle

    @property
    def go_to_base_page(self):
        return self.driver.get(self.BASE_URL)



