import pytest
import pandas.testing as pdt
import us_vis
import matplotlib.testing
import pandas as pd

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 3, 5], [2, 4, 6]]),
        ({'Coord': [1, 2], 'US10': [3, 4], '':[5, 6]}, ['US10']),
    ])

def test_col_names():
    pdt.assert_frame_equal(us_vis.vis.col_names(test), expected)

def test_col_names_string():
    with pytest.raises(TypeError):
        error_expected = us_vis.vis.col_names([['Hello', 'world'], ['Hello', 'world']])

@pytest.mark.parametrize(
    "test, expected",
    [
        ({'Coord': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'US10': [3, 4, 5, 5, 2, 3, 4, 1, 3, 4]}),
        ({'Coord': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'US10': [2, 3, 4, 4, 1, 2, 3, 0, 2, 3]}),
    ])

def test_sub_min():
    pdt.assert_frame_equal(us_vis.vis.sub_min(test), expected)

def test_sub_min_string():
    with pytest.raises(TypeError):
        error_expected = us_vis.vis.sub_min([['Hello', 'world'], ['Hello', 'world']])

data, ws = pd.DataFrame({'Coord': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'US10': [3, 4, 5, 5, 2, 3, 4, 1, 3, 4], 'US20': [2, 3, 4, 4, 1, 2, 3, 0, 2, 3]}), ['US10', 'US20']
us_vis.vis.vis_save(data,ws,"results")

def test_vis_fun():
    matplotlib.testing.compare.compare_images("results.png", "expected.png", 0.001)

def test_odd_col():
    assert us_vis.vis.odd_col() == "You might need to recalculate "
    assert us_vis.vis.odd_col("5") == "You might need to recalculate 5"
