# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['zlgcan_demo.py'],
    pathex=[],
    binaries=[('./zlgcan.dll', '.'), ('./kerneldlls/CANDevCore.dll', '.'), ('./kerneldlls/CANDevice.dll', '.'), ('./kerneldlls/CANDTU_NET.dll', '.'), ('./kerneldlls/CANDTU_x64.dll', '.'), ('./kerneldlls/CANET_TCP.dll', '.'), ('./kerneldlls/CANFDCOM.dll', '.'), ('./kerneldlls/CANFDNET.dll', '.'), ('./kerneldlls/CANWIFI_TCP.dll', '.'), ('./kerneldlls/CANWIFI_UDP.dll', '.'), ('./kerneldlls/USBCAN.dll', '.'), ('./kerneldlls/USBCANFD.dll', '.'), ('./kerneldlls/USBCANFD800U.dll', '.'), ('./kerneldlls/VirtualUSBCAN.dll', '.'), ('./kerneldlls/ZlgCloud.dll', '.')],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='MyApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
