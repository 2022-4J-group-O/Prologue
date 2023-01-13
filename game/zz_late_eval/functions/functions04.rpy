init python:
    # サンプル画像を作成する関数
    # name: サンプル画像の名前 x, y: サンプル画像のサイズ col: サンプル画像の色
    def SampleImage(name, x, y, col="#0000ff", **properties):
        return Composite((x, y),  (0, 0), Solid(col), (0, 0), Text(name), **properties)