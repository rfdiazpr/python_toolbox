# Copyright 2009-2010 Ram Rachum. No part of this program may be used, copied
# or distributed without explicit written permission from Ram Rachum.

'''
Defines the NodeMenu class.

See its documentation for more info.
'''

from itertools import izip

from garlicsim.general_misc.third_party.ordered_dict import OrderedDict
import wx

from garlicsim_wx.general_misc.cute_menu import CuteMenu


class ForkByCrunchingUsingMenu(CuteMenu):
    def __init__(self, frame):
        super(ForkByCrunchingUsingMenu, self).__init__()
        self.frame = frame
        self._build()
    
    def _build(self):
        
        frame = self.frame
        

        self.AppendSeparator()
        
        
        self.new_step_profile_button = self.Append(
            -1,
            '&New step profile...',
            ' Create a new step profile'
        )
        frame.Bind(wx.EVT_BUTTON, self.on_new_step_profile_button,
                   self.new_step_profile_button)
        
        
    def on_new_step_profile_button(self, event):
        raise NotImplementedError#tododoc
    

    def _get_step_profile_items(self):
        # Getting the existing menu items, while slicing out the separator and
        # "New step profile..." button:
        return list(self.GetMenuItems())[:-2]
    
        
    def _recalculate(self):
        gui_project = self.frame.gui_project
        if not gui_project:
            return
        step_profiles = gui_project.step_profiles
            
        items = self._get_step_profile_items()
        
        def find_item_of_step_profile(step_profile):
            matching_items = [item for item in items if
                              item.step_profile == step_profile]
            assert len(matching_items) in [0, 1]
            if matching_items:
                (matching_item,) = matching_items
                return matching_item
            else:
                return None
        
        step_profiles_to_items = OrderedDict(
            ((step_profile, find_item_of_step_profile(step_profile))
             for step_profile in step_profiles)
        )
        
        needed_items = filter(None, step_profiles_to_items.values())
        unneeded_items = [item for item in items if (item not in needed_items)]
        
        for item in items:
            self.RemoveItem(item)
            
        itemless_step_profiles = [
            step_profile for step_profile in step_profiles if
            (step_profiles_to_items[step_profile] is None)
        ]
        
        for itemless_step_profile in itemless_step_profiles:
            step_profile_text = itemless_step_profile.__repr__(
                short_form=True,
                root=gui_project.simpack,
                namespace=gui_project.namespace
            )
            new_item = wx.MenuItem(
                None,
                -1,
                step_profile_text,
                'Fork by crunching using %s' % step_profile_text
            )
            new_item.step_profile = step_profile
            step_profiles_to_items[itemless_step_profile] = new_item
            
        for i, item in enumerate(step_profiles_to_items.itervalues()):
            self.InsertItem(i, item)
                
        
        updated_items = self._get_step_profile_items()
        for item, step_profile in izip(updated_items, step_profiles):
            assert item.step_profile == step_profile
            
        
                
            
            
        
        
        
        
    