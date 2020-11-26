from PO_lianx.page.app import App


class TestWork:
    def setup(self):
        self.app = App()

    def test_addcontact(self):
        username = 'nh'
        sex = '男'
        phone = '18810979570'
        toast = self.app.main().goto_addresslist().click_addmember() \
            .add_member_menual().edit_username().edit_gender() \
            .edit_phone().click_save().get_result()

        assert "添加成功" == toast
