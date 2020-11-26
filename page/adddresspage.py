from PO_lianx.page.memberInvitepage import MemberInvitepage


class Addresslist:
    def __init__(self, driver):
        self.driver = driver

    def click_addmember(self):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()

        return MemberInvitepage(self.driver)
