# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import minium
# from case.base import loader
import subprocess
from case.base import loader
from subprocess import run


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def start_test_cmd():
    """
    不可用，启动了开发者工具，没有执行用例，没有日志
    :return:
    """
    subprocess.Popen("minitest -s suite.json -c config.json -g",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,)


def minium_init():
    mini = minium.Minium(conf={
        "project_path": "C:\\Users\\carbine_san\\Documents\\aixingzou\\dist",
        "dev_tool_path": "C:\\Program Files (x86)\\Tencent\\微信web开发者工具\\cli.bat",
        "debug_mode": "debug",
        "test_port": 9420,
        "platform": "ide",
        "app": "wx",
        "assert_capture": False,
        "request_timeout": 60,
        "enable_app_log": False,
        "remote_connect_timeout": 300,
        "auto_relaunch": True,
        "outputs": "outputs",
        "mock_native_modal": {

        }
    })
    # mini.connect_dev_tool()
    # mini.app.go_home()
    return mini


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    仅调试使用，本方法报告不能在H5报告中查看，实际测试请使用命令行
    """
    print_hi('here we go for the test!')
    # mini = minium_init()
    # start_test_cmd()
    # minium.WXMinium._dev_cli("minitest -s suite.json -c config.json -g")
    # (command="minitest -s suite.json -c config.json -g")
    loader.main(suite_path="suite.json", config="config.json", generate_report=False)
    # run(r"cli auto --project C:\Users\carbine_san\Documents\630zsh\dist --auto-port 9420")
    # runconfig = "minitest -s suite.json -c config.json -g"
    # run(runconfig, shell=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
