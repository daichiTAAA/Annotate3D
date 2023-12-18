import dash
from dash import dcc, html
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import numpy as np
from plyfile import PlyData
import pandas as pd

ply_file_path = "/Users/noda/Annotate3D/data/EngineBlock.ply"


# PLYファイルを読み込む関数
def read_ply(filename):
    plydata = PlyData.read(filename)
    vertex = plydata["vertex"]
    df_vertices = pd.DataFrame({"x": vertex["x"], "y": vertex["y"], "z": vertex["z"]})

    face_indices = None
    if "face" in plydata:
        # PLYファイルの構造に合わせてフィールド名を調整
        face_field_name = "vertex_indices"  # 例えば 'vertex_index' などに変更する場合があります
        if face_field_name in plydata["face"].data.dtype.names:
            faces = plydata["face"].data[face_field_name]
            face_indices = np.concatenate(
                [np.array(face).reshape(-1, 3) for face in faces]
            )

    return df_vertices, face_indices


# PLYファイルの読み込み
ply_vertices, ply_faces = read_ply(ply_file_path)

# Plotlyの散布図で点群を表示
scatter = go.Scatter3d(
    x=ply_vertices["x"],
    y=ply_vertices["y"],
    z=ply_vertices["z"],
    mode="markers",
    marker=dict(size=2),
)

# PlotlyのMeshでサーフェースを表示
mesh = None
if ply_faces is not None:
    mesh = go.Mesh3d(
        x=ply_vertices["x"],
        y=ply_vertices["y"],
        z=ply_vertices["z"],
        i=ply_faces[:, 0],
        j=ply_faces[:, 1],
        k=ply_faces[:, 2],
        opacity=0.5,
    )

fig = go.Figure(data=[scatter, mesh] if mesh else [scatter])

# Dashアプリの初期化
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# アプリのレイアウトの定義
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H1("PLYファイルの3D点群とサーフェース表示"))),
        dbc.Row(
            dbc.Col(
                dcc.Graph(figure=fig, style={"height": "100vh"}),
                width="12",
                style={"margin": "auto"},
            )
        ),
    ]
)

# アプリの実行
if __name__ == "__main__":
    app.run_server(debug=True)
