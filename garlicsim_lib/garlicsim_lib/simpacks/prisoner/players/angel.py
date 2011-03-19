# Copyright 2009-2011 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

'''
This module defines the `Angel` player type.

See its documentation for more information.
'''

from ..base_player import BasePlayer


class Angel(BasePlayer):
    
    color = 'White'
    
    def make_move(self, round):
        return True
