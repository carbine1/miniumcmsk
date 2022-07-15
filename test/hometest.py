from case.base import loader
from case.base.basecase import BaseCase
from case.pages.homepage import HomePage
import minium


class HomePageTest(minium.MiniTest):
    def __init__(self, methodName='runTest'):
        super(HomePageTest, self).__init__(methodName)
        self.homePage = HomePage(self)

    """
    case1:测试页面路径
    """

    def test_01_home_page_path(self):
        self.homePage.check_homepage_path()

    def test_02_home_element(self):
        self.homePage.check_homepage_base_element()

    def test_03_home_element_click(self):
        self.homePage.get_city_select_element()


if __name__ == '__main__':
    mini = minium.Minium({
        "project_path": r"C:\Users\carbine_san\Documents\630zsh\dist",
        "dev_tool_path": r"C:\Program Files (x86)\Tencent\微信web开发者工具\cli.bat"
    })
    mini.connect_dev_tool()
    loader.main(module="hometest", config="../config.json", generate_report=True)
