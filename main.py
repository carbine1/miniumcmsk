# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import minium
from case.base import loader
from subprocess import run



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def minium_init():
    mini = minium.Minium({
  "project_path": "C:\\Users\\carbine_san\\Documents\\630zsh\\dist",
  "dev_tool_path": "C:\\Program Files (x86)\\Tencent\\微信web开发者工具\\cli.bat",
  "debug_mode": "debug",
  "test_port": 9420,
  "platform": "ide",
  "app": "wx",
  "assert_capture": False,
  "request_timeout": 60,
  "remote_connect_timeout": 300,
  "auto_relaunch": True,
  "outputs": "outputs"
})
    mini.connect_dev_tool()
    mini.app.go_home()
    return mini


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # mini =minium_init()
    # loader.main(suite_path="suite.json", config="config.json", generate_report=True)
    # run(r"cli auto --project C:\Users\carbine_san\Documents\630zsh\dist --auto-port 9420")
    runconfig = "minitest -s suite.json -c config.json -g"
    run(runconfig, shell=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
