# Copyright 2009-2010 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

from garlicsim.misc import GarlicSimException

from .step_types import (SimpleStep, StepGenerator, HistoryStep,
                         HistoryStepGenerator, InplaceStep,
                         InplaceStepGenerator)


def determine_step_type(step_function):
    assert callable(step_function)
    name = step_function.__name__
    if 'step' not in step:
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
    