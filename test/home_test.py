import minium

from case.base import loader
from case.pages.homepage import HomePage


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

    def test_04_home_scroll(self):
        self.homePage.scroll_page()
        # self.capture()

    def test_05_home_model(self):
        self.homePage.cmpark_modal()


if __name__ == '__main__':
    mini = minium.Minium({
        "project_path": r"C:\Users\carbine_san\Documents\aixingzou\dist",
        "dev_tool_path": r"C:\Program Files (x86)\Tencent\微信web开发者工具\cli.bat"
    })
    # mini.connect_dev_tool()
    loader.main(module="home_test", config="../config.json", generate_report=True)
