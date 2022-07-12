import minium

from case.base import loader,route
from case.base.basecase import BaseCase
from case.pages.mallpage import MallPage


class MallPageTest(minium.MiniTest):
    # def __init__(self, methodName='runTest'):
    #     super(MallPageTest, self).__init__(methodName)
    #     self.mallPage = MallPage(self)
    #     # self.mallPage.go_mallpage()
    #     self.app.switch_tab(route.mallpage_route)

    def test_01_mall_page_path(self):
        self.app.switch_tab(route.mallpage_route)
        self.assertEqual(self.app.current_page.path, route.mallpage_route)


if __name__ == '__main__':

    loader.run(module="mallpagetest", config="../config.json", generate_report=True)
