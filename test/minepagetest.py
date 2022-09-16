import minium

from case.base import loader
from case.base.basecase import BaseCase
from case.pages.minepage import MinePage


class MinePageTest(minium.MiniTest):

    def __init__(self, methodName='runTest'):
        super(MinePageTest, self).__init__(methodName)
        self.minepage = MinePage(self)

    def test_01_check_minepage_path(self):
        self.minepage.check_mine_page_path()

    def test_02_minepage_element(self):
        self.minepage.check_mine_page_base_element()


if __name__ == '__main__':
    loader.main(module="minepagetest", config="../config.json", generate_report=True)
