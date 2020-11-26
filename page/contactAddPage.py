from time import sleep

from PO_lianx.page.Basege import Basege


class ContactAddPage(Basege):

    def edit_username(self, username):
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(username)

        return self

    def edit_gender(self, sex):
        self.driver.find_element_by_xpath("//*[@text='性别']/..//*[@text='男']")
        if sex == '女':
            self.driver.find_element_by_xpath("//*[@text='男']")
        else:
            self.driver.find_element_by_xpath("//*[@text='女']")

        return self

    def edit_phone(self, phone):

        self.driver.find_element_by_xpath("//*[contains(@text,'手机')]/..//*[@text='手机号']")
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='手机号']").send_keys(phone)
        return self

    def click_save(self):
        from PO_lianx.page.memberInvitepage import MemberInvitepage
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='保存']").click()
        sleep(2)
        return MemberInvitepage(self.driver)
