from base_app import BasePage


class PageObject(BasePage):

    def send_text(
            self,
            locator,
            text,
            wait=10
    ):

        element = self.find_element_in_dom(locator, wait)
        element.click()
        element.send_keys(text)

        return element

    def click_element(
            self,
            locator,
            wait=10
    ):

        element = self.wait_to_be_clickable(locator, wait)
        element.click()

        return element

    def double_click_element(
            self,
            locator,
            wait=10
    ):
        element = self.click_element(locator, wait)
        element.click()

        return element

