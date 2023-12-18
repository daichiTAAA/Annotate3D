import dash
from dash import dcc, html
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

# 椅子のような形状の3D点群データを生成
# これは非常に単純化された例です
x = [0, 0, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
y = [0, 1, 1, 0, 0, 0, 1, 1, 0.5, 0.5, 0, 1, 0, 1, 0.5, 0.5]
z = [0, 0, 0, 0, 0, 0.5, 0.5, 1, 1, 1.5, 1.5, 1.5, 1, 1, 1, 0.5]

# Plotly Graph Objectsを使用して点群を作成
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode="markers")])

# Dashアプリの初期化
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# アプリのレイアウトの定義
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H1("椅子の形状を模した3D点群"))),
        dbc.Row(dbc.Col(dcc.Graph(figure=fig))),
    ]
)

# アプリの実行
if __name__ == "__main__":
    app.run_server(debug=True)
