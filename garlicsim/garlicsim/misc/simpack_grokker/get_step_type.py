# Copyright 2009-2010 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

import types

from garlicsim.general_misc.third_party import decorator

from garlicsim.misc import GarlicSimException

from .step_types import (SimpleStep, StepGenerator, HistoryStep,
                         HistoryStepGenerator, InplaceStep,
                         InplaceStepGenerator)


def get_step_type(step_function):
    step_type_attribute = getattr(step_function, 'step_type', None)
    if step_type_attribute:
        return step_type_attribute
    else:
        step_type = _get_step_type(step_function)
        actual_function = \
            (step_function if isinstance(step_function, types.FunctionType)
             else step_function.im_func)
        actual_function.step_type = step_type
        return step_type


def _get_step_type(step_function):
    assert callable(step_function)
    name = step_function.__name__
    if 'step' not in name:
        raise GarlicSimException("%s is not a step function-- It doesn't have "
                                 "the word 'step' in it." % step_function) #tododoc: test this
    if 'inplace_step_generator' in name:
        return InplaceStepGenerator
    elif 'inplace_step' in name:
        return InplaceStep
    elif 'history_step_generator' in name:
        return HistoryStepGenerator
    elif 'step_generator' in name:
        return StepGenerator
    elif 'history_step' in name:
        return HistoryStep
    else:
        assert 'step' in name
        return SimpleStep
    