# Copyright 2009-2011 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

'''
This module defines the `SimpackInfoPanel` class.

See its documentation for more information.
'''

import wx

from garlicsim_wx.widgets.general_misc.cute_panel import CutePanel

from .name_display import NameDisplay
from .technical_details_bar import TechnicalDetailsBar
from .description_display import DescriptionDisplay
from .tags_display import TagsDisplay


class SimpackInfoPanel(CutePanel):
    def __init__(self, simpack_selection_dialog):
        self.simpack_selection_dialog = simpack_selection_dialog
        CutePanel.__init__(self, simpack_selection_dialog)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.name_display = NameDisplay(self)
        self.sizer.Add(self.name_display,
                       proportion=0,
                       flag=(wx.ALIGN_LEFT | wx.BOTTOM),
                       border=2)
        
        self.technical_details_bar = TechnicalDetailsBar(self)
        self.sizer.Add(self.technical_details_bar,
                       proportion=0,
                       flag=(wx.ALIGN_RIGHT | wx.BOTTOM),
                       border=2)
        
        self.small_h_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.small_h_sizer,
                       proportion=1,
                       flag=(wx.EXPAND))
        
        self.smaller_v_sizer = wx.BoxSizer(wx.VERTICAL)
        self.small_h_sizer.Add(self.smaller_v_sizer,
                               proportion=3,
                               flag=(wx.EXPAND))
        
        self.description_display = DescriptionDisplay(self)
        self.smaller_v_sizer.Add(self.description_display,
                                 proportion=1,
                                 flag=(wx.EXPAND | wx.RIGHT),
                                 border=2)

        self.tags_display = TagsDisplay(self)
        self.smaller_v_sizer.Add(self.tags_display,
                                 proportion=0,
                                 flag=(wx.EXPAND | wx.RIGHT),
                                 border=2)
        
        
        self.SetSizer(self.sizer)
        self.Layout()
        
        self.simpack_selection_dialog.\
                      simpack_metadata_changed_emitter.add_output(self.refresh)
         
        
    def refresh(self):
        self.name_display.refresh()
        self.technical_details_bar.refresh()
        self.description_display.refresh()
        self.tags_display.refresh()
        self.Layout()