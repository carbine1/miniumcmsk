# import minium.miniprogram.base_driver.minium_log
import time

import minium

from case.base import loader, route


# logger = logging.getLogger("minium")
class MallPageTest(minium.MiniTest):
    # def __init__(self, methodName='runTest'):
    #     super(MallPageTest, self).__init__(methodName)
    #     self.mallPage = MallPage(self)
    #     # self.mallPage.go_mallpage()
    #     self.app.switch_tab(route.mallpage_route)

    def setUp(self) -> None:
        self.logger.info("======= setup function: %s=========" % self._testMethodName)
        # self.app.switch_tab(route.mallpage_route)
        # relaunch不限tab，优于switch_tab和navigate_to方法
        self.app.relaunch(route.mallpage_route)

    def test_01_mall_page_path(self):
        # self.app.switch_tab(route.mallpage_route)
        # self.app.relaunch("/pkgMine/pages/myHouse/manageOccupant/index", params={"houseCode":"056a44f8-73bf-4974-9bca-1bcf2abe4e09","roomType":"NORMAL_HOUSE","__key_":"16655405549815"})
        # time.sleep(30)
        self.assertEqual(self.app.current_page.path, route.mallpage_route)


if __name__ == '__main__':

    loader.main(module="mallpagetest", config="../config.json", generate_report=True)
