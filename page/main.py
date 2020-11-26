from PO_lianx.page.adddresspage import Addresslist


class MianPage:
    def __init__(self, driver):
        self.driver = driver

    def goto_addresslist(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
        return Addresslist(self.driver)

    def goto_message(self):
        pass

    def goto_workbench(self):
        pass
