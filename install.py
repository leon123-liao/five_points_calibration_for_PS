import PyInstaller.__main__

# 定义打包参数（等同于命令行参数）
params = [
    'zlgcan_demo.py',       # 入口文件
    '--onefile',            # 打包成单个可执行文件
     '--windowed',           # 隐藏控制台（GUI程序适用）
    '--add-binary', './zlgcan.dll;.',
    '--add-binary', './kerneldlls/CANDevCore.dll;.',
    '--add-binary', './kerneldlls/CANDevice.dll;.',
    '--add-binary', './kerneldlls/CANDTU_NET.dll;.',
    '--add-binary', './kerneldlls/CANDTU_x64.dll;.',
    '--add-binary', './kerneldlls/CANET_TCP.dll;.',
    '--add-binary', './kerneldlls/CANFDCOM.dll;.',
    '--add-binary', './kerneldlls/CANFDNET.dll;.',
    '--add-binary', './kerneldlls/CANWIFI_TCP.dll;.',
    '--add-binary', './kerneldlls/CANWIFI_UDP.dll;.',
    '--add-binary', './kerneldlls/USBCAN.dll;.',
    '--add-binary', './kerneldlls/USBCANFD.dll;.',
    '--add-binary', './kerneldlls/USBCANFD800U.dll;.',
    '--add-binary', './kerneldlls/VirtualUSBCAN.dll;.',
    '--add-binary', './kerneldlls/ZlgCloud.dll;.',

    '--name=MyApp',         # 指定输出名称

]

# 调用 PyInstaller 执行打包
PyInstaller.__main__.run(params)