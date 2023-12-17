from django.shortcuts import render
from django_plotly_dash import DjangoDash
import dash_core_components as dcc
import dash_html_components as html


# ここでDashアプリケーションを定義
def create_dash_application():
    app = DjangoDash("SimpleExample")  # Dashアプリの名前

    app.layout = html.Div(
        [
            html.H1("Plotly DashとDjangoの統合"),
            dcc.Graph(
                id="example-graph",
                figure={
                    "data": [
                        {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "SF"},
                        {
                            "x": [1, 2, 3],
                            "y": [2, 5, 3],
                            "type": "bar",
                            "name": "Montréal",
                        },
                    ],
                    "layout": {"title": "Dashデータ可視化"},
                },
            ),
        ]
    )
    return app


# DjangoビューでDashアプリケーションを初期化
create_dash_application()
