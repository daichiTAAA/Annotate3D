"""3D CADモデルの点群データへの変換
  * .step形式の3D CADモデルを.plyまたは.obj形式の点群データへ変換する
  * FreeCADをインストールし、FreeCADのpython APIを使用する"""

import FreeCAD
import ImportGui

# STEPファイルのパス
step_file = "path/to/your/file.step"

# FreeCADドキュメントを作成
doc = FreeCAD.newDocument()

# STEPファイルをインポート
ImportGui.insert(step_file, doc.Name)

# OBJファイルとしてエクスポート
obj_file = "path/to/your/output.obj"
__objs__ = []
for obj in FreeCAD.ActiveDocument.Objects:
    if obj.TypeId[:4] != "Mesh":
        __objs__.append(obj)
ImportGui.export(__objs__, obj_file)
