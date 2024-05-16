import pytest
import pandas.testing as pdt
import us_vis
import pandas as pd


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 3, 5], [2, 4, 6]]),
        ({'Coord': [1, 2], 'US10': [3, 4], '': [5, 6]}, ['US10']),
    ])
def test_col_names(test,expected):
    pdt.assert_frame_equal(us_vis.vis.col_names(test), expected)


def test_col_names_string():
    with pytest.raises(TypeError):
        error_expected = us_vis.vis.col_names([['Hello', 'world'],
                                               ['Hello', 'world']])


@pytest.mark.parametrize(
    "test, expected",
    [
        ({'Coord': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'US10': [3, 4, 5, 5, 2, 3, 4, 1, 3, 4]}),
        ({'Coord': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'US10': [2, 3, 4, 4, 1, 2, 3, 0, 2, 3]}),
    ])
def test_sub_min(test,expected):
    pdt.assert_frame_equal(us_vis.vis.sub_min(test), expected)


def test_sub_min_string():
    with pytest.raises(TypeError):
        error_expected = us_vis.vis.sub_min([['Hello', 'world'],
                                            ['Hello', 'world']])


def test_odd_col():
    assert us_vis.vis.odd_col() == "You might need to recalculate "
    assert us_vis.vis.odd_col("5") == "You might need to recalculate 5"


@pytest.mark.parametrize(
    "test, expected",
    [
        ([{'Coord':[1.95, 2.0, 2.05, 2.1, 2.15, 2.2, 2.25, 2.3, 2.35, 2.4, 2.45, 2.5, 2.55, 2.6, 2.65, 2.7, 2.75, 2.8, 2.85, 2.9, 2.95, 3.0, 3.05, 3.1, 3.15, 3.2, 3.25], 'US50':[None, 0.00, 1.92, 3.90, 6.44, 10.02, 14.56, 19.89, 25.95, 32.59, 39.78, 46.62, 53.85, 60.97, 66.88, 73.31, 76.81, 78.80, 78.76, 78.52, 77.82, 76.97, 76.44, 76.04, 75.72, 75.18, 75.34], 'US70':[None, -19.37, -18.44, -15.32, -10.68, -4.90, 1.44, 7.39, 13.08, 18.10, 22.73, 25.97, 29.35, 27.10, 24.18, 21.14, 18.33, 15.69, 13.30, 6.09, 4.89, 4.02, 2.97, 1.86, 1.42, 0.00, 0.24]}], ["US50", "US70"]), (['US50']),
    ])
def test_odd_values(test,expected):
    pdt.assert_frame_equal(us_vis.vis.odd_col(pd.Dataframe(test)), expected)


def test_odd_string():
    assert us_vis.vis.odd_col() == "You might need to recalculate "


@pytest.mark.parametrize(
    "test, expected",
    [
        (['US10', 'US20', 'US30', 'US40', 'US50', 'US60'], "1 2 3 4"),
        (['US50', 'US60']),
        (['US10', 'US20', 'US30', 'US40', 'US50', 'US60'], "0 0 0"),
        (['US10', 'US20', 'US30', 'US40', 'US50', 'US60'])
    ])
def test_del_col(test,expected):
    pdt.assert_frame_equal(us_vis.vis.col_names(test), expected)
