"""
Dash apps for the demonstration of functionality

Copyright (c) 2018 Gibbs Consulting and others - see CONTRIBUTIONS.md

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# pylint: disable=no-member

import uuid
import random

from datetime import datetime

import pandas as pd

import dash
from dash import Dash
from dash import dcc, html
from dash.dependencies import MATCH, ALL

import plotly.graph_objs as go

import dpd_components as dpd

from dash.exceptions import PreventUpdate


# pylint: disable=too-many-arguments, unused-argument, unused-variable

app = Dash("SimpleExample")

app.layout = html.Div(
    [
        # Add a link to go back to Django
        html.A("Go to Django App", href="http://localhost:8000/polls/"),
        dcc.RadioItems(
            id="dropdown-color",
            options=[
                {"label": c, "value": c.lower()} for c in ["Red", "Green", "Blue"]
            ],
            value="red",
        ),
        html.Div(id="output-color"),
        dcc.RadioItems(
            id="dropdown-size",
            value="medium",
        ),
        html.Div(id="output-size"),
    ]
)


@app.callback(
    dash.dependencies.Output("output-color", "children"),
    [dash.dependencies.Input("dropdown-color", "value")],
)
def callback_color(dropdown_value):
    "Change output message"
    return "The selected color is %s." % dropdown_value


@app.callback(
    dash.dependencies.Output("output-size", "children"),
    [
        dash.dependencies.Input("dropdown-color", "value"),
        dash.dependencies.Input("dropdown-size", "value"),
    ],
)
def callback_size(dropdown_color, dropdown_size):
    "Change output message"
    return "The chosen T-shirt is a %s %s one." % (dropdown_size, dropdown_color)


a2 = Dash("Ex2", serve_locally=True)

a2.layout = html.Div(
    [
        dcc.RadioItems(
            id="dropdown-one",
            options=[
                {"label": i, "value": j}
                for i, j in [
                    ("O2", "Oxygen"),
                    ("N2", "Nitrogen"),
                    ("CO2", "Carbon Dioxide"),
                ]
            ],
            value="Oxygen",
        ),
        html.Div(id="output-one"),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
