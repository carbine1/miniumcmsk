from case.base import loader, route
from case.base.basecase import BaseCase
from case.pages.mallpage import MallPage


class MallPageTest(BaseCase):
    def __init__(self, methodName='runTest'):
        super(MallPageTest, self).__init__(methodName)
        self.mallPage = MallPage(self)
        self.mini.app.navigate_to(route.mallpage_route)

    def test_01_mall_page_path(self):
        self.mallPage.check_mallpage_path()


if __name__ == '__main__':
    loader.run(module="mallpagetest", config="../config.json", generate_report=True)
