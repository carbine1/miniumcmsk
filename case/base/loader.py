from minium.framework import loader
import onetest

# def run(**kwargs):
    # loader.main(**kwargs)

g_case_list = []
FILENAME_SUMMARY = "summary.json"


def print_help():
    help_message = r""":param version:
    :param path:用例所在的文件夹，默认当前路径
    :param module:用例的包名或者文件名
    :param apk:show apk path which may you need to install before running test1 in android device
    :param case_name:test_开头的用例名
    :param generate_report:生成网页测试报告
    :param suite_path:测试计划文件
    :param config:配置文件名，配置项目参考配置文件
    :param sys_path_list:添加 module 的搜索路径
    :param show_accounts:查看开发者工具当前登录的多账号, 需要通过 9420 端口,以自动化模式打开开发者工具
    :param run_mode:选择以parallel(并行)或者fork(复刻)的方式运行用例
    :param only_native:Only init native driver
    :param test_connection:test1 connection between minium and ide
    :param test_port:test1 connection port, default: 9420
    :param task_limit_time:task max runtime, default: 0, unlimited
    :param just_test:just test1 loader, not run session
    :param is_check_env:check system environment for minitest"""
    print(help_message)


def main(version=False, path=None, module=None, apk=False, case_name=None, generate_report=False, suite_path=None,
         config=None, sys_path_list=None,
         show_accounts=None, run_mode="fork", only_native=False, test_connection=None, test_port="9420",
         task_limit_time=60, just_test=False, is_check_env=False):
    # bug: 在 fork 模式下Python 会出现 crash
    # crashed on child side of fork pre-exec
    # Invalid dylib load. Clients should not load the unversioned libcrypto dylib as it does not have a stable ABI.
    """

    :param version:
    :param path:用例所在的文件夹，默认当前路径
    :param module:用例的包名或者文件名
    :param apk:show apk path which may you need to install before running test1 in android device
    :param case_name:test_开头的用例名
    :param generate_report:生成网页测试报告
    :param suite_path:测试计划文件
    :param config:配置文件名，配置项目参考配置文件
    :param sys_path_list:添加 module 的搜索路径
    :param show_accounts:查看开发者工具当前登录的多账号, 需要通过 9420 端口,以自动化模式打开开发者工具
    :param run_mode:选择以parallel(并行)或者fork(复刻)的方式运行用例
    :param only_native:Only init native driver
    :param test_connection:test1 connection between minium and ide
    :param test_port:test1 connection port, default: 9420
    :param task_limit_time:task max runtime, default: 0, unlimited
    :param just_test:just test1 loader, not run session
    :param is_check_env:check system environment for minitest
    :return:
    """
    import multiprocessing

    multiprocessing.set_start_method("spawn")

    # only_native = parser_args.only_native
    # test_connection = parser_args.test_connection
    # test_port = parser_args.test_port
    # task_limit_time = int(parser_args.task_limit_time) or None
    # just_test = parser_args.just_test
    # is_check_env = parser_args.check_env

    if show_accounts:
        # 打印已登录的多账号
        print(loader.WXMinium().get_test_accounts())
        exit(0)

    if test_connection:
        # 测试ws链接是否正常
        loader.test_ws_connection(test_port)
        exit(0)

    if sys_path_list:
        # 添加 package 寻找路径到 sys.path
        for sys_path in sys_path_list:
            loader.logger.info("insert %s to sys.path", sys_path)
            loader.sys.path.insert(0, sys_path)

    if version:
        # 打印 minium 版本信息
        print(loader.build_version())
        exit(0)

    if apk:
        # 打印 android uiautomator 相关的 apk 包路径
        bin_root = loader.os.path.join(
            loader.os.path.dirname(loader.os.path.dirname(__file__)),
            "native",
            "lib",
            "at",
            "bin",
            "*apk",
        )
        print("please install apk:")
        for filename in loader.glob.glob(bin_root):
            print(f"adb install -r {filename}")
        exit(0)

    if path is None:
        # 用例目录路径
        loader.logger.debug("case directory path not specified, use current path")
        path = loader.os.getcwd()

    if not loader.os.path.exists(path) or not loader.os.path.isdir(path):
        loader.logger.error("case directory: %s not exists" % path)
        print_help()
        exit(0)

    loader.sys.path.insert(0, path)

    # 提前预加载默认配置，否则处理 suite 的时候logger 参数不生效
    loader.minitest.AssertBase.setUpConfig(default=True)

    # 处理 suite、case、module 参数
    suite = None
    if suite_path:
        tests, suite = loader.load_from_suite(path, suite_path)
        print(f"load {tests.countTestCases()} cases")
        print(
            f'import package {",".join(suite.success_pkg)} success, import package {",".join(suite.fail_pkg)} fail'
        )
    elif module is None:
        # raise RuntimeError("suite_path or pkg is necessary")
        loader.logger.error("suite_path or module_path is necessary at least one")
        print_help()
        exit(0)
    elif case_name is None:
        loader.load_from_module(module)
    else:
        loader.load_single_case(module, case_name)
    print("after load %s" % suite_path or module)
    for c in g_case_list:
        print(str(c))
    # 处理 config 参数
    if config and not loader.os.path.exists(config):
        # raise RuntimeError("config not exists:%s" % config)
        loader.logger.error("config not exists:%s" % config)
        print_help()
        exit(0)
    conf_list = loader.get_config(config)
    # 处理一下import error的问题
    if suite and suite.fail_pkg:
        for conf in conf_list:
            if conf.outputs:
                summary_path = loader.os.path.join(conf.outputs, FILENAME_SUMMARY)
                loader.update_summary(summary_path, {"import_error": suite.fail_pkg})

    if is_check_env:
        loader.check_env(conf_list)
        print("check env done")
        exit(0)

    # 输出版本信息
    print(loader.build_version())
    if just_test:
        exit(0)
    # 启动 session
    loader.run_session(conf_list, run_mode, only_native, generate_report, task_limit_time)
    exit(0)
