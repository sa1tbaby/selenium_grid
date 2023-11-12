import pandas

from base_app import BasePage
from bs4 import BeautifulSoup
from pandas import DataFrame
class PageObject(BasePage):





    def choice_ec_method(
            self,
            method,
            **extra
    ):
        try:
            match method:

                case 'find_element_in_dom':
                    return self.find_element_in_dom(**extra)

                case 'find_elements_in_dom':
                    return self.find_elements_in_dom(**extra)

                case 'find_element_with_compare':
                    return self.find_element_with_compare(**extra)

                case 'wait_to_be_clickable':
                    return self.wait_to_be_clickable(**extra)

                case 'check_staleness':
                    pass

        except:
            print('some_exception')

        else:
            print('some_exception')
            raise ValueError

    def choice_action(
            self,
            element,
            method,
            **extra
    ):

        match method:

            case 'click':
                result = self.click_element(element)

            case 'double_click':
                result = self.click_element(element)
                result = self.click_element(result)

            case 'send_keys':
                result = self.send_text(element, **extra)

            case 'wait_state':

            case 'switch_to_new_window':
                

            case 'upload_file':
                result = self.upload_file(element, **extra)



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

    def run_pipe(
            self,
            pipe_path
    ):
        pipe = pandas.read_excel(pipe_path, index_col=0)

        for pipes in pipe.iterrows():

            element = self.choice_ec_method(method=pipes[1].iloc['EC_Method'])

            element = self.choice_action(element, method=pipes[1].iloc['action'])







