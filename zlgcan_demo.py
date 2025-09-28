#  zlgcan_demo.py
#
#  ~~~~~~~~~~~~
#
#  ZLGCAN USBCANFD Demo
#
#  ~~~~~~~~~~~~
#
#  ------------------------------------------------------------------
#  Author : guochuangjian    
#  Last change: 17.01.2019
#
#  Language: Python 3.6
#  ------------------------------------------------------------------
#
import main_frame
import platform
from devDialog_frame import DevDialog
from xscope import RollingSineWave
from zlgcan import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import time
import json
import wx
import zlg_control

###############################################################################

###############################################################################

from main_frame import *
from zlg_control import *
class MainFrame(MyFrame):
    pass

    def m_button_save_offsetOnLeftDown(self, event ):
        if not self.m_textCtrl_25per_write.GetValue():
            per25 = 0
        else:
            per25 = int(self.m_textCtrl_25per_write.GetValue())

        if not self.m_textCtrl_50per_write.GetValue():
            per50 = 0
        else:
            per50 = int(self.m_textCtrl_50per_write.GetValue())

        if not self.m_textCtrl_75per_write.GetValue():
            per75 = 0
        else:
            per75 = int(self.m_textCtrl_75per_write.GetValue())

        if per25 > 1000 or per25 < -1000:
            per25 = 0
        if per50 > 1000 or per50 < -1000:
            per50 = 0
        if per75 > 1000 or per75 < -1000:
            per75 = 0
        zlgctl.EnterFactoryMode()
        time.sleep(0.2)
        zlgctl.WriteOffsetValue(per25, per50, per75)
        print("save")

    def m_button_closeOnLeftDown( self, event ):
        zlgctl.SetPosition(0x64)

    def m_button_25perOnLeftDown( self, event ):
        zlgctl.SetPosition(0x19)

    def m_button_50perOnLeftDown( self, event ):
        zlgctl.SetPosition(0x32)

    def m_button_75perOnLeftDown( self, event ):
        zlgctl.SetPosition(0x48)

    def m_button_100perOnLeftDown( self, event ):
        zlgctl.SetPosition(0)

    def m_button_debug_two_arm_upOnLeftDown( self, event ):
        zlgctl.EnterFactoryMode()
        zlgctl.EnterMotorContorlMode()
        zlgctl.MotorContorl_TwoArm_Up()
        # zlgctl.test()
    def m_button_debug_two_arm_upOnLeftUp(self, event):
        zlgctl.MotorContorl_Stop_All()
        print("stop")
    def m_button_debug_two_arm_downOnLeftDown( self, event ):
        zlgctl.EnterFactoryMode()
        zlgctl.EnterMotorContorlMode()
        zlgctl.MotorContorl_TwoArm_Down()

    def m_button_debug_two_arm_downOnLeftUp( self, event ):
        zlgctl.MotorContorl_Stop_All()
        print("stop")

    def m_button_debug_roller_upOnLeftDown( self, event ):
        zlgctl.EnterFactoryMode()
        zlgctl.EnterMotorContorlMode()
        zlgctl.MotorContorl_Roller_Up()

    def m_button_debug_roller_upOnLeftUp( self, event ):
        zlgctl.MotorContorl_Stop_All()
        print("stop")

    def m_button_debug_roller_downOnLeftDown( self, event ):
        zlgctl.EnterFactoryMode()
        zlgctl.EnterMotorContorlMode()
        zlgctl.MotorContorl_Roller_Down()

    def m_button_debug_roller_downOnLeftUp( self, event ):
        zlgctl.MotorContorl_Stop_All()
        print("stop")

    def m_button_debug_left_arm_upOnLeftDown( self, event ):
        zlgctl.EnterFactoryMode()
        zlgctl.EnterMotorContorlMode()
        zlgctl.MotorContorl_LeftArm_Up()

    def m_button_debug_left_arm_upOnLeftUp( self, event ):
        zlgctl.MotorContorl_Stop_All()
        print("stop")

    def m_button_debug_left_arm_downOnLeftDown( self, event ):
        zlgctl.EnterFactoryMode()
        zlgctl.EnterMotorContorlMode()
        zlgctl.MotorContorl_LeftArm_Down()

    def m_button_debug_left_arm_downOnLeftUp( self, event ):
        zlgctl.MotorContorl_Stop_All()
        print("stop")

    def m_button_debug_right_arm_upOnLeftDown( self, event ):
        zlgctl.EnterFactoryMode()
        zlgctl.EnterMotorContorlMode()
        zlgctl.MotorContorl_RightArm_Up()

    def m_button_debug_right_arm_upOnLeftUp( self, event ):
        zlgctl.MotorContorl_Stop_All()
        print("stop")

    def m_button_debug_right_arm_downOnLeftDown( self, event ):
        zlgctl.EnterFactoryMode()
        zlgctl.EnterMotorContorlMode()
        zlgctl.MotorContorl_RightArm_Down()

    def m_button_debug_right_arm_downOnLeftUp( self, event ):
        zlgctl.MotorContorl_Stop_All()
        print("stop")

    def m_button_upOnLeftDown( self, event ):
        zlgctl.EnterFactoryMode()
        zlgctl.EnterMotorContorlMode()
        zlgctl.MotorContorl_RightArm_Up()

    def m_button_upOnLeftUp( self, event ):
        zlgctl.MotorContorl_Stop_All()
        print("stop")

    def m_button_downOnLeftDown( self, event ):
        zlgctl.EnterFactoryMode()
        zlgctl.EnterMotorContorlMode()
        zlgctl.MotorContorl_RightArm_Down()

    def m_button_downOnLeftUp( self, event ):
        zlgctl.MotorContorl_Stop_All()
        print("stop")

    def MyFrameOnSetFocus( self, event ):
        zlgctl.EnterFactoryMode()
        print("setFocus")

    def MyFrameOnLeftDown(self, event):
        zlgctl.EnterFactoryMode()

    def m_button_stop_allOnLeftDown( self, event ):
        zlgctl.EnterFactoryMode()
        zlgctl.EnterMotorContorlMode()
        zlgctl.MotorContorl_Stop_All()
        event.Skip()
        print("stop all motors")

##########解决鼠标左健双击后焦点无法更新的BUG########################
    def m_button_upOnLeftDClick( self, event ):
        pass

    def m_button_downOnLeftDClick( self, event ):
        pass

    def m_button_debug_two_arm_upOnLeftDClick( self, event ):
        pass

    def m_button_debug_two_arm_downOnLeftDClick( self, event ):
        pass

    def m_button_debug_roller_upOnLeftDClick( self, event ):
        pass

    def m_button_debug_roller_downOnLeftDClick( self, event ):
        pass

    def m_button_debug_left_arm_upOnLeftDClick( self, event ):
        pass

    def m_button_debug_left_arm_downOnLeftDClick( self, event ):
        pass

    def m_button_debug_right_arm_upOnLeftDClick( self, event ):
        pass

    def m_button_debug_right_arm_downOnLeftDClick( self, event ):
        pass

    def MyFrameOnClose( self, event ):
        zlgctl.ZlgReset()
        event.Skip()

    def m_checkBoxMotorDataOnCheckBox( self, event ):
        is_checked = self.m_checkBoxMotorData.GetValue()
        if is_checked:
            print("checked!")
            rolling_wave.start()
        else:
            print("unchecked!")
            # rolling_wave.stop()
        event.Skip()

    def m_checkBox_calibrateOnCheckBox( self, event ):
        is_checked = self.m_checkBox_calibrate.GetValue()
        if is_checked:
            print("checked!")
            self.m_buttonCalibrate.Show()
            self.GetSizer().Layout() if self.GetSizer() else None
        else:
            self.m_buttonCalibrate.Hide()
            self.GetSizer().Layout() if self.GetSizer() else None
        event.Skip()

    def m_buttonCalibrateOnLeftDown( self, event ):
        zlgctl.EnterFactoryMode()
        time.sleep(0.1)
        zlgctl.Calibrate()
        event.Skip()

class MyDialog(DevDialog):
    pass

    def m_button_closeOnLeftDown( self, event ):
        event.Skip()
        sys.exit()

if __name__ == "__main__":
    print("Python3 版本:", sys.version)
    print(platform.architecture())
    app = wx.App()
    win = MainFrame(None)
    zlgctl = ZLG_Control(win)

    rolling_wave = RollingSineWave(
        data_points=9000,
        window_size=1000,
        update_interval=50,
        # line_color='r'
    )

    if zlgctl._dev_handle == 0:
        dialog = MyDialog(None)
        dialog.Show()
    else:
        zlgctl.ZlgInit()
        zlgctl.EnterFactoryMode()
        zlgctl.start_receive_thread(rolling_wave._update_data)
        win.Show()


    app.MainLoop()

