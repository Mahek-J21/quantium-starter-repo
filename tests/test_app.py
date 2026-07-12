import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dash.testing.application_runners import import_app


def test_header(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    header = dash_duo.find_element("#header")
    assert header.text == "Pink Morsel Sales Dashboard"


def test_graph_exists(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_exists(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-filter")
    assert radio is not None