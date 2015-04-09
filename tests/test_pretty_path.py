import pytest
from collections import Counter
from which_plates.main import which_plates
from preety_path import preet_path


@pytest.mark.webtest
def test_pretty_path():
    plates   = Counter({45:2, 35:2, 25:2, 15:2, 10:2, 5:2, 2.5: 2})
    goal     = 100
    percents = (.20, .40, .60, .80, 1)
    path = which_plates(goal, plates, percents)
    path = preety_path(path)
    assert path[0] == [5, 10, 5]

