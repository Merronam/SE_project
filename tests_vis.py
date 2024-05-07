import pytest
import pandas.testing as pdt
import tools.vis
import matplotlib.testing

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 3, 5], [2, 4, 6]]),
        ({'Coord': [1, 2], 'US10': [3, 4], '':[5, 6]}, ['US10']),
    ])

def test_col_names():
    pdt.assert_frame_equal(tools.vis.col_names(test), expected)

def test_col_names_string():
    with pytest.raises(TypeError):
        error_expected = tools.vis.col_names([['Hello', 'world'], ['Hello', 'world']])

@pytest.mark.parametrize(
    "test, expected",
    [
        ({'Coord': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'US10': [3, 4, 5, 5, 2, 3, 4, 1, 3, 4]}),
        ({'Coord': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'US10': [2, 3, 4, 4, 1, 2, 3, 0, 2, 3]}),
    ])

def test_sub_min():
    pdt.assert_frame_equal(tools.vis.sub_min(test), expected)

def test_sub_min_string():
    with pytest.raises(TypeError):
        error_expected = tools.vis.sub_min([['Hello', 'world'], ['Hello', 'world']])

data, ws = pd.DataFrame({'Coord': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'US10': [3, 4, 5, 5, 2, 3, 4, 1, 3, 4], 'US20': [2, 3, 4, 4, 1, 2, 3, 0, 2, 3]}), ['US10', 'US20']
tools.vis.vis_save(data,ws,"results")

def test_vis_fun():
    matplotlib.testing.compare.compare_images("results.png", "expected.png", 0.001)
