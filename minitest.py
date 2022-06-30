import minium
import minium.miniprogram.base_driver.page
from main import minium_init
# mini = minium.WXMinium()
# mini.connect_dev_tool()
# mini =minium_init()
mini = minium.Minium({
    "project_path": r"C:\Users\carbine_san\Documents\630zsh\dist",
    "dev_tool_path": r"C:\Program Files (x86)\Tencent\微信web开发者工具\cli.bat"
})
system_info = mini.get_system_info()
app_info =mini.get_app_config()
page_info =mini.app.get_current_page()
current_page=mini.app.navigate_to('/pages/landingCommonHandler/verifyEmployee?scene=%7B%22redirect%22%3A%7B%22title%22%3A%22%22%2C%22content%22%3A%7B%22type%22%3A%22INNER%22%2C%22options%22%3A%7B%22type%22%3A%22NO_AUTH%22%2C%22path%22%3A%22%2Fpages%2Fmine%2Findex%22%2C%22shareTitle%22%3A%22%22%2C%22shareImageSrc%22%3A%22%22%2C%22allowShare%22%3Afalse%7D%7D%2C%22useReplace%22%3Atrue%2C%22entryAuthType%22%3A%5B%22PHONE%22%5D%7D%2C%22channel%22%3A%22TravelWith%22%7D')
ele = page_info.get_element('.index-module__title___2mxTG',max_timeout=10).inner_text
# ele = current_page.page.get_element('#_n_10')
# print(system_info)
# print(app_info)
# print(page_info)
# print(ele)
# mini.app.switch_tab('/pages/house/index')
# mini.app.mock_wx_method()
class miniTest(minium.MiniTest):
    def test_get_title(self):
        # self.app.navigate_to("pages/home/index")
        sys_title = self.page.get_element(".index-module__title___2mxTG").inner_text
        print(sys_title)
# if __name__=="__main__":
#     miniTest.test_get_title()