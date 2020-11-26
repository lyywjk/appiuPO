class MemberInvitepage:
    def __init__(self, driver):
        self.driver = driver

    def add_member_menual(self):
        from PO_lianx.page.contactAddPage import ContactAddPage
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='手动输入添加']").click()

        return ContactAddPage(self.driver)

    def get_result(self):
        ttoast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        return ttoast
