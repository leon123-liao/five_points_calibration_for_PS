import time

import wx

from zlgcan import *
import numpy as np

MAX_RCV_NUM = 10


class ZLG_Control():
    def __init__(self, win):
        super(ZLG_Control, self).__init__()
        self.win = win
        self.zcan = ZCAN()
        self._dev_handle = self.zcan.OpenDevice(ZCAN_USBCANFD_200U, 0, 0)
        print("dev_handle:" + str(self._dev_handle))

    def ZlgInit(self):
        self.info = self.zcan.GetDeviceInf(self._dev_handle)
        print("Device Information:\n%s" % (self.info))
        # Start CAN
        self.chn_handle = canfd_start(self.zcan, self._dev_handle, 0)
        print("channel handle:%d." % (self.chn_handle))

    def ZlgReset(self):
        # Close CAN
        ret = self.zcan.ResetCAN(self.chn_handle)
        if ret == 1:
            print("ResetCAN success! ")
        # Close Device
        ret = self.zcan.CloseDevice(self._dev_handle)
        if ret == 1:
            print("CloseDevice success! ")

    def MsgReadThreadFunc(self, callback):
        # Receive Messages
        list_data = [0, 0, 0, 0, 0, 0]
        counter = 0
        while True:
            counter += 1
            time.sleep(0.05)
            rcv_num = self.zcan.GetReceiveNum(self.chn_handle, ZCAN_TYPE_CAN)
            rcv_canfd_num = self.zcan.GetReceiveNum(self.chn_handle, ZCAN_TYPE_CANFD)
            if rcv_num:
                rcv_msg, rcv_num = self.zcan.Receive(self.chn_handle, rcv_num)
                for i in range(rcv_num):
                    # if rcv_msg[i].frame.can_id != 0x3c6:
                    #     print("timestamps:%6fs,type:CAN, %s ,id:%s, dlc:%d, eff:%d, rtr:%d, data:%s" % (
                    #         rcv_msg[i].timestamp / 1000000, "tx",
                    #         hex(rcv_msg[i].frame.can_id), rcv_msg[i].frame.can_dlc,
                    #         rcv_msg[i].frame.eff, rcv_msg[i].frame.rtr,
                    #         ''.join(hex(rcv_msg[i].frame.data[j]) + ' ' for j in range(rcv_msg[i].frame.can_dlc))))
                    if rcv_msg[i].frame.can_id == 0x3c6:
                        # self.win.m_textCtrl_current_pos.SetValue(str(rcv_msg[i].frame.data[0]))
                        try:
                            if self.win.m_textCtrl_current_pos:
                                self.win.m_textCtrl_current_pos.SetValue(str(rcv_msg[i].frame.data[0]))
                        except RuntimeError as e:
                            print("窗口已被销毁:", e)
                    if rcv_msg[i].frame.can_id == 0x5fd:
                        per25 = rcv_msg[i].frame.data[0] << 8 | rcv_msg[i].frame.data[1]
                        per50 = rcv_msg[i].frame.data[2] << 8 | rcv_msg[i].frame.data[3]
                        per75 = rcv_msg[i].frame.data[4] << 8 | rcv_msg[i].frame.data[5]

                        arr = np.array([per25, per50, per75], dtype=np.uint16)
                        arr_int16 = arr.astype(np.int16)
                        # self.win.m_textCtrl_25per_get.SetValue(str(arr_int16[0]))
                        # self.win.m_textCtrl_50per_get.SetValue(str(arr_int16[1]))
                        # self.win.m_textCtrl_75per_get.SetValue(str(arr_int16[2]))
                        try:
                            if self.win.m_textCtrl_25per_get:
                                self.win.m_textCtrl_25per_get.SetValue(str(arr_int16[0]))
                            if self.win.m_textCtrl_50per_get:
                                self.win.m_textCtrl_50per_get.SetValue(str(arr_int16[1]))
                            if self.win.m_textCtrl_75per_get:
                                self.win.m_textCtrl_75per_get.SetValue(str(arr_int16[2]))
                        except RuntimeError as e:
                            print("窗口已被销毁:", e)

                    if rcv_msg[i].frame.can_id == 0x5f9:
                        left_angle = rcv_msg[i].frame.data[0] << 8 | rcv_msg[i].frame.data[1]
                        right_angle = rcv_msg[i].frame.data[2] << 8 | rcv_msg[i].frame.data[3]

                        try:
                            if self.win.m_textCtrl_right_arm_angle:
                                self.win.m_textCtrl_right_arm_angle.SetValue(str(right_angle))
                            if self.win.m_textCtrl_left_arm_angle:
                                self.win.m_textCtrl_left_arm_angle.SetValue(str(left_angle))
                            if self.win.m_textCtrl_angle_difference:
                                self.win.m_textCtrl_angle_difference.SetValue(str(left_angle - right_angle))
                        except RuntimeError as e:
                            print("窗口已被销毁:", e)
                    if rcv_msg[i].frame.can_id == 0x5fa:
                        left_arm_power = (rcv_msg[i].frame.data[0] << 8 | rcv_msg[i].frame.data[1]) / 10
                        right_arm_power = (rcv_msg[i].frame.data[2] << 8 | rcv_msg[i].frame.data[3]) / 10
                        roll_power = (rcv_msg[i].frame.data[4] << 8 | rcv_msg[i].frame.data[5]) / 10
                        # list_power = [left_arm_power, right_arm_power, roll_power]
                        list_data[0] = left_arm_power
                        list_data[1] = right_arm_power
                        list_data[2] = roll_power
                        callback(list_data)

                    if rcv_msg[i].frame.can_id == 0x5fb:
                        left_arm_speed = (rcv_msg[i].frame.data[0] << 8 | rcv_msg[i].frame.data[1])
                        right_arm_speed = (rcv_msg[i].frame.data[2] << 8 | rcv_msg[i].frame.data[3])
                        roll_speed = (rcv_msg[i].frame.data[4] << 8 | rcv_msg[i].frame.data[5])
                        list_data[3] = left_arm_speed / 1000
                        list_data[4] = right_arm_speed / 1000
                        list_data[5] = roll_speed / 1000
                        callback(list_data)

                    if rcv_msg[i].frame.can_id == 0x5F7:
                        if rcv_msg[i].frame.data[0] == 0x01 or rcv_msg[i].frame.data[0] == 0x02 or \
                                rcv_msg[i].frame.data[0] == 0x03 or rcv_msg[i].frame.data[0] == 0x04 or \
                                rcv_msg[i].frame.data[0] == 0x05 or \
                                rcv_msg[i].frame.data[0] == 0x06:
                            try:
                                if self.win.m_checkBox_calibrate:
                                    if counter % 30 > 10 and counter % 30 <= 20:
                                        self.win.m_checkBox_calibrate.SetLabel("标定中.")
                                    elif counter % 30 > 20 and counter % 30 <= 30:
                                        self.win.m_checkBox_calibrate.SetLabel("标定中..")
                                    else:
                                        self.win.m_checkBox_calibrate.SetLabel("标定中...")
                            except RuntimeError as e:
                                print("窗口已被销毁:", e)
                        if rcv_msg[i].frame.data[1] == 0xAA:
                            try:
                                if self.win.m_checkBox_calibrate:
                                    if counter % 30 > 10 and counter % 30 <= 20:
                                        self.win.m_checkBox_calibrate.SetLabel("标定成功！")
                            except RuntimeError as e:
                                print("窗口已被销毁:", e)
                        if rcv_msg[i].frame.data[1] == 0xFF:
                            try:
                                if self.win.m_checkBox_calibrate:
                                    if counter % 30 > 10 and counter % 30 <= 20:
                                        self.win.m_checkBox_calibrate.SetLabel("标定失败！")
                            except RuntimeError as e:
                                print("窗口已被销毁:", e)

                    if rcv_msg[i].frame.can_id == 0x3c7:
                        month = rcv_msg[i].frame.data[3]
                        date = rcv_msg[i].frame.data[4]
                        if month <= 9:
                            str_month = "0"+f"{month:x}"
                        else:
                            str_month = f"{month:x}"
                        if date <= 9:
                            str_date = "0"+f"{date:x}"
                        else:
                            str_date = f"{date:x}"
                        ver_major = rcv_msg[i].frame.data[5] >> 4
                        ver_min = rcv_msg[i].frame.data[5] & 0x0F
                        sw_version = "sw:" + str_month + str_date + "-V" + f"{ver_major:x}" + "." + f"{ver_min:x}"
                        try:
                            if self.win.m_staticText_sw_ver:
                                self.win.m_staticText_sw_ver.SetForegroundColour(wx.RED)
                                self.win.m_staticText_sw_ver.SetLabel(sw_version)
                        except RuntimeError as e:
                            print("窗口已被销毁:", e)


    def start_receive_thread(self, callback):
        self._terminated = False
        self._read_thread = threading.Thread(None, target=self.MsgReadThreadFunc, args=(callback,), name="WorkerThread")
        self._read_thread.start()
        # self.MsgReadThreadFunc()

    def ExitMotorContorlMode(self):
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x3cc
            msgs[i].frame.can_dlc = 8
            for j in range(msgs[i].frame.can_dlc):
                msgs[i].frame.data[j] = 0
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)

    def SetPosition(self, pos):
        self.ExitMotorContorlMode()
        time.sleep(0.1)
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x3c5
            msgs[i].frame.can_dlc = 8
            for j in range(msgs[i].frame.can_dlc):
                msgs[i].frame.data[j] = 0
            msgs[i].frame.data[0] = pos
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)
        print("Tranmit Num: %d." % ret)

    def EnterFactoryMode(self):
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x5F2
            msgs[i].frame.can_dlc = 8
            msgs[i].frame.data[0] = 0x01
            msgs[i].frame.data[1] = 0x58
            msgs[i].frame.data[2] = 0x58
            msgs[i].frame.data[3] = 0x58
            msgs[i].frame.data[4] = 0x47
            msgs[i].frame.data[5] = 0x49
            msgs[i].frame.data[6] = 0x4d
            msgs[i].frame.data[7] = 0x49
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)

    def EnterMotorContorlMode(self):
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x3cc
            msgs[i].frame.can_dlc = 8
            for j in range(msgs[i].frame.can_dlc):
                msgs[i].frame.data[j] = 0
            msgs[i].frame.data[0] = 0x9F
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)

    def MotorContorl_Stop_All(self):
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x5F8
            msgs[i].frame.can_dlc = 8
            for j in range(msgs[i].frame.can_dlc):
                msgs[i].frame.data[j] = 0
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)

    def MotorContorl_TwoArm_Up(self):
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x5F8
            msgs[i].frame.can_dlc = 8
            for j in range(msgs[i].frame.can_dlc):
                msgs[i].frame.data[j] = 0
            msgs[i].frame.data[0] = 0x01
            msgs[i].frame.data[1] = 0x01
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)

    def MotorContorl_TwoArm_Down(self):
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x5F8
            msgs[i].frame.can_dlc = 8
            for j in range(msgs[i].frame.can_dlc):
                msgs[i].frame.data[j] = 0
            msgs[i].frame.data[0] = 0x02
            msgs[i].frame.data[1] = 0x02
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)

    def MotorContorl_LeftArm_Down(self):
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x5F8
            msgs[i].frame.can_dlc = 8
            for j in range(msgs[i].frame.can_dlc):
                msgs[i].frame.data[j] = 0
            msgs[i].frame.data[0] = 0x02
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)

    def MotorContorl_RightArm_Down(self):
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x5F8
            msgs[i].frame.can_dlc = 8
            for j in range(msgs[i].frame.can_dlc):
                msgs[i].frame.data[j] = 0
            msgs[i].frame.data[1] = 0x02
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)

    def MotorContorl_LeftArm_Up(self):
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x5F8
            msgs[i].frame.can_dlc = 8
            for j in range(msgs[i].frame.can_dlc):
                msgs[i].frame.data[j] = 0
            msgs[i].frame.data[0] = 0x01
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)

    def MotorContorl_RightArm_Up(self):
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x5F8
            msgs[i].frame.can_dlc = 8
            for j in range(msgs[i].frame.can_dlc):
                msgs[i].frame.data[j] = 0
            msgs[i].frame.data[1] = 0x01
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)

    def MotorContorl_Roller_Down(self):
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x5F8
            msgs[i].frame.can_dlc = 8
            for j in range(msgs[i].frame.can_dlc):
                msgs[i].frame.data[j] = 0
            msgs[i].frame.data[2] = 0x02
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)

    def MotorContorl_Roller_Up(self):
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x5F8
            msgs[i].frame.can_dlc = 8
            for j in range(msgs[i].frame.can_dlc):
                msgs[i].frame.data[j] = 0
            msgs[i].frame.data[2] = 0x01
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)

    def WriteOffsetValue(self, per25, per50, per75):
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x5FC
            msgs[i].frame.can_dlc = 8
            for j in range(msgs[i].frame.can_dlc):
                msgs[i].frame.data[j] = 0
            msgs[i].frame.data[0] = (per25 >> 8) & 0xFF
            msgs[i].frame.data[1] = per25 & 0xFF
            msgs[i].frame.data[2] = (per50 >> 8) & 0xFF
            msgs[i].frame.data[3] = per50 & 0xFF
            msgs[i].frame.data[4] = (per75 >> 8) & 0xFF
            msgs[i].frame.data[5] = per75 & 0xFF
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)

    def test(self):
        transmit_num = 3
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        msgs[0].transmit_type = 0  # 0-正常发送，2-自发自收
        msgs[0].frame.eff = 0  # 0-标准帧，1-扩展帧
        msgs[0].frame.rtr = 0  # 0-数据帧，1-远程帧
        msgs[0].frame.can_id = 0x5F2
        msgs[0].frame.can_dlc = 8
        msgs[0].frame.data[0] = 0x01
        msgs[0].frame.data[1] = 0x58
        msgs[0].frame.data[2] = 0x58
        msgs[0].frame.data[3] = 0x58
        msgs[0].frame.data[4] = 0x47
        msgs[0].frame.data[5] = 0x49
        msgs[0].frame.data[6] = 0x4d
        msgs[0].frame.data[7] = 0x49

        msgs[1].transmit_type = 0  # 0-正常发送，2-自发自收
        msgs[1].frame.eff = 0  # 0-标准帧，1-扩展帧
        msgs[1].frame.rtr = 0  # 0-数据帧，1-远程帧
        msgs[1].frame.can_id = 0x3cc
        msgs[1].frame.can_dlc = 8
        for j in range(msgs[1].frame.can_dlc):
            msgs[1].frame.data[j] = 0
        msgs[1].frame.data[0] = 0x9F

        msgs[2].transmit_type = 0  # 0-正常发送，2-自发自收
        msgs[2].frame.eff = 0  # 0-标准帧，1-扩展帧
        msgs[2].frame.rtr = 0  # 0-数据帧，1-远程帧
        msgs[2].frame.can_id = 0x5f8
        msgs[2].frame.can_dlc = 8
        for j in range(msgs[2].frame.can_dlc):
            msgs[2].frame.data[j] = 0
        msgs[2].frame.data[0] = 0x01
        msgs[2].frame.data[1] = 0x01
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)

    def Calibrate(self):
        transmit_num = 1
        msgs = (ZCAN_Transmit_Data * transmit_num)()
        for i in range(transmit_num):
            msgs[i].transmit_type = 0  # 0-正常发送，2-自发自收
            msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
            msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
            msgs[i].frame.can_id = 0x3cc
            msgs[i].frame.can_dlc = 8
            for j in range(msgs[i].frame.can_dlc):
                msgs[i].frame.data[j] = 0
            msgs[i].frame.data[0] = 0x7F
        ret = self.zcan.Transmit(self.chn_handle, msgs, transmit_num)
