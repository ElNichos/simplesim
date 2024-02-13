from simtypes.electric_elements_types.electric_branch import *


# TODO Complete this later
# class TestElementModeData:
#     pass

def test_cyclic_frequency():
    cyclic_frequency = 2 * 50 * 3.14
    assert get_cyclic_frequency(50).__round__(2) == cyclic_frequency.__round__(2)



