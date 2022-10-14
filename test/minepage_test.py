import minium
from case.base import route
from case.base import loader
from case.pages.minepage import MinePage


class MinePageTest(minium.MiniTest):

    def __init__(self, methodName='runTest'):
        super(MinePageTest, self).__init__(methodName)
        self.minepage = MinePage(self)

    def setUp(self) -> None:
        self.minepage.mini.app.switch_tab(route.minepage_route)

    # def test_01_check_minepage_path(self):
    #     self.minepage.check_mine_page_path()
    #
    # def test_02_minepage_element(self):
    #     self.minepage.check_mine_page_base_element()

    def test_03_minepage_scroll(self):
        self.minepage.mine_page_scroll()


if __name__ == '__main__':
    mini = minium.Minium({
        "project_path": r"C:\Users\carbine_san\Documents\aixingzou\dist",
        "dev_tool_path": r"C:\Program Files (x86)\Tencent\微信web开发者工具\cli.bat"
    })
    # mini.connect_dev_tool()
    # loader.main(module="home_test", config="../config.json", generate_report=True)

    loader.main(module="minepage_test", config="../config.json", generate_report=True)
