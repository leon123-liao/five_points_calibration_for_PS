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
## Class DevDialog
###########################################################################

class DevDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"警告！"), pos = wx.DefaultPosition, size = wx.Size( 800,137 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

        bSizer17 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_toast = wx.StaticText( self, wx.ID_ANY, _(u"CAN设备连接失败，请确保ZCanPro软件没有打开，软后尝试重新插拔设备！"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_toast.Wrap( -1 )

        bSizer17.Add( self.m_staticText_toast, 0, wx.ALL, 5 )

        self.m_button_close = wx.Button( self, wx.ID_ANY, _(u"点击关闭"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_button_close, 0, wx.ALL, 5 )


        self.SetSizer( bSizer17 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button_close.Bind( wx.EVT_LEFT_DOWN, self.m_button_closeOnLeftDown )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def m_button_closeOnLeftDown( self, event ):
        event.Skip()


