# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 765,416 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"25%"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer8.Add( self.m_staticText1, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"50%"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer8.Add( self.m_staticText2, 1, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"75%"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer8.Add( self.m_staticText3, 1, wx.ALIGN_LEFT|wx.ALL, 5 )


        bSizer7.Add( bSizer8, 0, wx.EXPAND, 50 )

        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button_save_offset = wx.Button( self, wx.ID_ANY, _(u"写入补偿"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button_save_offset, 0, wx.ALL, 5 )

        self.m_textCtrl_25per_write = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_textCtrl_25per_write, 1, wx.ALL, 5 )

        self.m_textCtrl_50per_write = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_textCtrl_50per_write, 1, wx.ALL, 5 )

        self.m_textCtrl_75per_write = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_textCtrl_75per_write, 1, wx.ALL, 5 )


        bSizer7.Add( bSizer1, 0, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button_get_offset = wx.Button( self, wx.ID_ANY, _(u"当前补偿"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button_get_offset, 0, wx.ALL, 5 )

        self.m_textCtrl_25per_get = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_textCtrl_25per_get, 1, wx.ALL, 5 )

        self.m_textCtrl_50per_get = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_textCtrl_50per_get, 1, wx.ALL, 5 )

        self.m_textCtrl_75per_get = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_textCtrl_75per_get, 1, wx.ALL, 5 )


        bSizer7.Add( bSizer11, 1, wx.EXPAND, 5 )


        bSizer3.Add( bSizer7, 1, wx.EXPAND, 5 )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer281 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_left_arm_angle = wx.StaticText( self, wx.ID_ANY, _(u"左支臂角度"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_left_arm_angle.Wrap( -1 )

        bSizer281.Add( self.m_staticText_left_arm_angle, 0, wx.ALL, 5 )

        self.m_textCtrl_left_arm_angle = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer281.Add( self.m_textCtrl_left_arm_angle, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer281, 1, wx.EXPAND, 5 )

        bSizer2811 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_right_arm_angle = wx.StaticText( self, wx.ID_ANY, _(u"右支臂角度"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_right_arm_angle.Wrap( -1 )

        bSizer2811.Add( self.m_staticText_right_arm_angle, 0, wx.ALL, 5 )

        self.m_textCtrl_right_arm_angle = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2811.Add( self.m_textCtrl_right_arm_angle, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer2811, 1, wx.EXPAND, 5 )

        bSizer2812 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_angle_difference = wx.StaticText( self, wx.ID_ANY, _(u"角度差"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_angle_difference.Wrap( -1 )

        bSizer2812.Add( self.m_staticText_angle_difference, 0, wx.ALL, 5 )

        self.m_textCtrl_angle_difference = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2812.Add( self.m_textCtrl_angle_difference, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer2812, 1, wx.EXPAND, 5 )

        bSizer2813 = wx.BoxSizer( wx.VERTICAL )

        self.m_button_up = wx.Button( self, wx.ID_ANY, _(u"补偿+"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2813.Add( self.m_button_up, 0, wx.ALL, 5 )

        self.m_button_down = wx.Button( self, wx.ID_ANY, _(u"补偿-"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2813.Add( self.m_button_down, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer2813, 1, wx.EXPAND, 5 )


        bSizer3.Add( bSizer14, 1, wx.EXPAND, 5 )

        bSizer71 = wx.BoxSizer( wx.VERTICAL )

        bSizer81 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer81.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        bSizer81.Add( self.m_staticText11, 0, wx.ALL, 5 )

        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, _(u"控制指令"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        bSizer81.Add( self.m_staticText21, 0, wx.ALL, 5 )

        self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )

        bSizer81.Add( self.m_staticText31, 1, wx.ALIGN_LEFT|wx.ALL, 5 )


        bSizer71.Add( bSizer81, 0, wx.EXPAND, 50 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, _(u"位置"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        bSizer12.Add( self.m_staticText16, 0, wx.ALL, 5 )

        self.m_button_close = wx.Button( self, wx.ID_ANY, _(u"关闭"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button_close, 0, wx.ALL, 5 )

        self.m_button_25per = wx.Button( self, wx.ID_ANY, _(u"25%"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button_25per, 0, wx.ALL, 5 )

        self.m_button_50per = wx.Button( self, wx.ID_ANY, _(u"50%"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button_50per, 0, wx.ALL, 5 )

        self.m_button_75per = wx.Button( self, wx.ID_ANY, _(u"75%"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button_75per, 0, wx.ALL, 5 )

        self.m_button_100per = wx.Button( self, wx.ID_ANY, _(u"打开"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button_100per, 0, wx.ALL, 5 )

        self.m_button_stop_all = wx.Button( self, wx.ID_ANY, _(u"停止"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button_stop_all, 0, wx.ALL, 5 )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer28 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, _(u"当前位置"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        bSizer28.Add( self.m_staticText17, 0, wx.ALL, 5 )

        self.m_textCtrl_current_pos = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer28.Add( self.m_textCtrl_current_pos, 0, wx.ALL, 5 )


        bSizer12.Add( bSizer28, 1, wx.EXPAND, 5 )


        bSizer71.Add( bSizer12, 0, wx.EXPAND, 5 )

        bSizerMotorControl = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText161 = wx.StaticText( self, wx.ID_ANY, _(u"单电机控制"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText161.Wrap( -1 )

        bSizerMotorControl.Add( self.m_staticText161, 0, wx.ALL, 5 )

        self.m_button_debug_two_arm_up = wx.Button( self, wx.ID_ANY, _(u"支臂同时升"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerMotorControl.Add( self.m_button_debug_two_arm_up, 0, wx.ALL, 5 )

        self.m_button_debug_two_arm_down = wx.Button( self, wx.ID_ANY, _(u"支臂同时降"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerMotorControl.Add( self.m_button_debug_two_arm_down, 0, wx.ALL, 5 )

        self.m_button_debug_roller_up = wx.Button( self, wx.ID_ANY, _(u"卷筒升"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerMotorControl.Add( self.m_button_debug_roller_up, 0, wx.ALL, 5 )

        self.m_button_debug_roller_down = wx.Button( self, wx.ID_ANY, _(u"卷筒降"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerMotorControl.Add( self.m_button_debug_roller_down, 0, wx.ALL, 5 )

        self.m_button_debug_left_arm_up = wx.Button( self, wx.ID_ANY, _(u"左支臂升"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerMotorControl.Add( self.m_button_debug_left_arm_up, 0, wx.ALL, 5 )

        self.m_button_debug_left_arm_down = wx.Button( self, wx.ID_ANY, _(u"左支臂降"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerMotorControl.Add( self.m_button_debug_left_arm_down, 0, wx.ALL, 5 )

        self.m_button_debug_right_arm_up = wx.Button( self, wx.ID_ANY, _(u"右支臂升"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerMotorControl.Add( self.m_button_debug_right_arm_up, 0, wx.ALL, 5 )

        self.m_button_debug_right_arm_down = wx.Button( self, wx.ID_ANY, _(u"右支臂降"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerMotorControl.Add( self.m_button_debug_right_arm_down, 0, wx.ALL, 5 )


        bSizer71.Add( bSizerMotorControl, 1, wx.EXPAND, 5 )


        bSizer3.Add( bSizer71, 2, wx.EXPAND, 5 )

        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer17.Add( ( 0, 0), 2, wx.EXPAND, 5 )


        bSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer18 = wx.BoxSizer( wx.VERTICAL )

        self.m_checkBoxMotorData = wx.CheckBox( self, wx.ID_ANY, _(u"电机实时数据"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.m_checkBoxMotorData, 1, wx.ALL, 5 )


        bSizer17.Add( bSizer18, 1, wx.EXPAND, 5 )

        bSizer19 = wx.BoxSizer( wx.VERTICAL )

        self.m_checkBox_calibrate = wx.CheckBox( self, wx.ID_ANY, _(u"工厂标定"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox_calibrate.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

        bSizer19.Add( self.m_checkBox_calibrate, 0, wx.ALL, 5 )

        self.m_buttonCalibrate = wx.Button( self, wx.ID_ANY, _(u"开始标定"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonCalibrate.Hide()

        bSizer19.Add( self.m_buttonCalibrate, 0, wx.ALL, 5 )


        bSizer17.Add( bSizer19, 1, wx.EXPAND, 5 )

        bSizer20 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_sw_ver = wx.StaticText( self, wx.ID_ANY, _(u"sw:0101-v1.0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_sw_ver.Wrap( -1 )

        self.m_staticText_sw_ver.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
        self.m_staticText_sw_ver.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

        bSizer20.Add( self.m_staticText_sw_ver, 0, wx.ALL, 5 )


        bSizer17.Add( bSizer20, 1, wx.EXPAND, 5 )


        bSizer3.Add( bSizer17, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.MyFrameOnClose )
        self.Bind( wx.EVT_LEFT_DOWN, self.MyFrameOnLeftDown )
        self.Bind( wx.EVT_SET_FOCUS, self.MyFrameOnSetFocus )
        self.m_button_save_offset.Bind( wx.EVT_LEFT_DOWN, self.m_button_save_offsetOnLeftDown )
        self.m_button_get_offset.Bind( wx.EVT_LEFT_DOWN, self.m_button_get_offsetOnLeftDown )
        self.m_button_up.Bind( wx.EVT_LEFT_DCLICK, self.m_button_upOnLeftDClick )
        self.m_button_up.Bind( wx.EVT_LEFT_DOWN, self.m_button_upOnLeftDown )
        self.m_button_up.Bind( wx.EVT_LEFT_UP, self.m_button_upOnLeftUp )
        self.m_button_down.Bind( wx.EVT_LEFT_DCLICK, self.m_button_downOnLeftDClick )
        self.m_button_down.Bind( wx.EVT_LEFT_DOWN, self.m_button_downOnLeftDown )
        self.m_button_down.Bind( wx.EVT_LEFT_UP, self.m_button_downOnLeftUp )
        self.m_button_close.Bind( wx.EVT_LEFT_DOWN, self.m_button_closeOnLeftDown )
        self.m_button_25per.Bind( wx.EVT_LEFT_DOWN, self.m_button_25perOnLeftDown )
        self.m_button_50per.Bind( wx.EVT_LEFT_DOWN, self.m_button_50perOnLeftDown )
        self.m_button_75per.Bind( wx.EVT_LEFT_DOWN, self.m_button_75perOnLeftDown )
        self.m_button_100per.Bind( wx.EVT_LEFT_DOWN, self.m_button_100perOnLeftDown )
        self.m_button_stop_all.Bind( wx.EVT_LEFT_DOWN, self.m_button_stop_allOnLeftDown )
        self.m_button_debug_two_arm_up.Bind( wx.EVT_LEFT_DCLICK, self.m_button_debug_two_arm_upOnLeftDClick )
        self.m_button_debug_two_arm_up.Bind( wx.EVT_LEFT_DOWN, self.m_button_debug_two_arm_upOnLeftDown )
        self.m_button_debug_two_arm_up.Bind( wx.EVT_LEFT_UP, self.m_button_debug_two_arm_upOnLeftUp )
        self.m_button_debug_two_arm_down.Bind( wx.EVT_LEFT_DCLICK, self.m_button_debug_two_arm_downOnLeftDClick )
        self.m_button_debug_two_arm_down.Bind( wx.EVT_LEFT_DOWN, self.m_button_debug_two_arm_downOnLeftDown )
        self.m_button_debug_two_arm_down.Bind( wx.EVT_LEFT_UP, self.m_button_debug_two_arm_downOnLeftUp )
        self.m_button_debug_roller_up.Bind( wx.EVT_LEFT_DCLICK, self.m_button_debug_roller_upOnLeftDClick )
        self.m_button_debug_roller_up.Bind( wx.EVT_LEFT_DOWN, self.m_button_debug_roller_upOnLeftDown )
        self.m_button_debug_roller_up.Bind( wx.EVT_LEFT_UP, self.m_button_debug_roller_upOnLeftUp )
        self.m_button_debug_roller_down.Bind( wx.EVT_LEFT_DCLICK, self.m_button_debug_roller_downOnLeftDClick )
        self.m_button_debug_roller_down.Bind( wx.EVT_LEFT_DOWN, self.m_button_debug_roller_downOnLeftDown )
        self.m_button_debug_roller_down.Bind( wx.EVT_LEFT_UP, self.m_button_debug_roller_downOnLeftUp )
        self.m_button_debug_left_arm_up.Bind( wx.EVT_LEFT_DCLICK, self.m_button_debug_left_arm_upOnLeftDClick )
        self.m_button_debug_left_arm_up.Bind( wx.EVT_LEFT_DOWN, self.m_button_debug_left_arm_upOnLeftDown )
        self.m_button_debug_left_arm_up.Bind( wx.EVT_LEFT_UP, self.m_button_debug_left_arm_upOnLeftUp )
        self.m_button_debug_left_arm_down.Bind( wx.EVT_LEFT_DCLICK, self.m_button_debug_left_arm_downOnLeftDClick )
        self.m_button_debug_left_arm_down.Bind( wx.EVT_LEFT_DOWN, self.m_button_debug_left_arm_downOnLeftDown )
        self.m_button_debug_left_arm_down.Bind( wx.EVT_LEFT_UP, self.m_button_debug_left_arm_downOnLeftUp )
        self.m_button_debug_right_arm_up.Bind( wx.EVT_LEFT_DCLICK, self.m_button_debug_right_arm_upOnLeftDClick )
        self.m_button_debug_right_arm_up.Bind( wx.EVT_LEFT_DOWN, self.m_button_debug_right_arm_upOnLeftDown )
        self.m_button_debug_right_arm_up.Bind( wx.EVT_LEFT_UP, self.m_button_debug_right_arm_upOnLeftUp )
        self.m_button_debug_right_arm_down.Bind( wx.EVT_LEFT_DCLICK, self.m_button_debug_right_arm_downOnLeftDClick )
        self.m_button_debug_right_arm_down.Bind( wx.EVT_LEFT_DOWN, self.m_button_debug_right_arm_downOnLeftDown )
        self.m_button_debug_right_arm_down.Bind( wx.EVT_LEFT_UP, self.m_button_debug_right_arm_downOnLeftUp )
        self.m_checkBoxMotorData.Bind( wx.EVT_CHECKBOX, self.m_checkBoxMotorDataOnCheckBox )
        self.m_checkBox_calibrate.Bind( wx.EVT_CHECKBOX, self.m_checkBox_calibrateOnCheckBox )
        self.m_checkBox_calibrate.Bind( wx.EVT_LEFT_DOWN, self.m_checkBox_calibrateOnLeftDown )
        self.m_buttonCalibrate.Bind( wx.EVT_LEFT_DOWN, self.m_buttonCalibrateOnLeftDown )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def MyFrameOnClose( self, event ):
        event.Skip()

    def MyFrameOnLeftDown( self, event ):
        event.Skip()

    def MyFrameOnSetFocus( self, event ):
        event.Skip()

    def m_button_save_offsetOnLeftDown( self, event ):
        event.Skip()

    def m_button_get_offsetOnLeftDown( self, event ):
        event.Skip()

    def m_button_upOnLeftDClick( self, event ):
        event.Skip()

    def m_button_upOnLeftDown( self, event ):
        event.Skip()

    def m_button_upOnLeftUp( self, event ):
        event.Skip()

    def m_button_downOnLeftDClick( self, event ):
        event.Skip()

    def m_button_downOnLeftDown( self, event ):
        event.Skip()

    def m_button_downOnLeftUp( self, event ):
        event.Skip()

    def m_button_closeOnLeftDown( self, event ):
        event.Skip()

    def m_button_25perOnLeftDown( self, event ):
        event.Skip()

    def m_button_50perOnLeftDown( self, event ):
        event.Skip()

    def m_button_75perOnLeftDown( self, event ):
        event.Skip()

    def m_button_100perOnLeftDown( self, event ):
        event.Skip()

    def m_button_stop_allOnLeftDown( self, event ):
        event.Skip()

    def m_button_debug_two_arm_upOnLeftDClick( self, event ):
        event.Skip()

    def m_button_debug_two_arm_upOnLeftDown( self, event ):
        event.Skip()

    def m_button_debug_two_arm_upOnLeftUp( self, event ):
        event.Skip()

    def m_button_debug_two_arm_downOnLeftDClick( self, event ):
        event.Skip()

    def m_button_debug_two_arm_downOnLeftDown( self, event ):
        event.Skip()

    def m_button_debug_two_arm_downOnLeftUp( self, event ):
        event.Skip()

    def m_button_debug_roller_upOnLeftDClick( self, event ):
        event.Skip()

    def m_button_debug_roller_upOnLeftDown( self, event ):
        event.Skip()

    def m_button_debug_roller_upOnLeftUp( self, event ):
        event.Skip()

    def m_button_debug_roller_downOnLeftDClick( self, event ):
        event.Skip()

    def m_button_debug_roller_downOnLeftDown( self, event ):
        event.Skip()

    def m_button_debug_roller_downOnLeftUp( self, event ):
        event.Skip()

    def m_button_debug_left_arm_upOnLeftDClick( self, event ):
        event.Skip()

    def m_button_debug_left_arm_upOnLeftDown( self, event ):
        event.Skip()

    def m_button_debug_left_arm_upOnLeftUp( self, event ):
        event.Skip()

    def m_button_debug_left_arm_downOnLeftDClick( self, event ):
        event.Skip()

    def m_button_debug_left_arm_downOnLeftDown( self, event ):
        event.Skip()

    def m_button_debug_left_arm_downOnLeftUp( self, event ):
        event.Skip()

    def m_button_debug_right_arm_upOnLeftDClick( self, event ):
        event.Skip()

    def m_button_debug_right_arm_upOnLeftDown( self, event ):
        event.Skip()

    def m_button_debug_right_arm_upOnLeftUp( self, event ):
        event.Skip()

    def m_button_debug_right_arm_downOnLeftDClick( self, event ):
        event.Skip()

    def m_button_debug_right_arm_downOnLeftDown( self, event ):
        event.Skip()

    def m_button_debug_right_arm_downOnLeftUp( self, event ):
        event.Skip()

    def m_checkBoxMotorDataOnCheckBox( self, event ):
        event.Skip()

    def m_checkBox_calibrateOnCheckBox( self, event ):
        event.Skip()

    def m_checkBox_calibrateOnLeftDown( self, event ):
        event.Skip()

    def m_buttonCalibrateOnLeftDown( self, event ):
        event.Skip()


