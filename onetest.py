import minium.miniprogram.base_driver.page

# mini = minium.WXMinium()
# mini.connect_dev_tool()
# mini =minium_init()
mini = minium.Minium({
    "project_path": r"C:\Users\carbine_san\Documents\630zsh\dist",
    "dev_tool_path": r"C:\Program Files (x86)\Tencent\微信web开发者工具\cli.bat"
})
system_info = mini.get_system_info()
app_info = mini.get_app_config()
page_info = mini.app.get_current_page()
# current_page=mini.app.navigate_to('/pages/home/index')
ele = page_info.get_element('.index-module__title___2mxTG', max_timeout=10).inner_text
page_info.get_element('view.index-module__city___3CrKD').click()
mini.app.get_current_page().get_element("view.index-module__atIndexesListNameInner___20dLK", inner_text='北京').click()

pagedata = mini.app.get_current_page().data
mini.app.relaunch('/pages/home/index')
# ele = current_page.page.get_element('#_n_10')
# print(system_info)
# print(app_info)
# print(page_info)
# print(ele)
# mini.app.switch_tab('/pages/house/index')
# mini.app.mock_wx_method()
print(pagedata)


class MiniTest(minium.MiniTest):
    def test_get_title(self):
        # self.app.navigate_to("pages/home/index")
        sys_title = self.page.get_element(".index-module__title___2mxTG").inner_text
        print(sys_title)
# if __name__=="__main__":
#     miniTest.test_get_title()
