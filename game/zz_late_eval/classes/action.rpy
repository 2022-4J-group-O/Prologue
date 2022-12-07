init python:
    # インタラクション的なことをしながらラベルを呼ぶ
    # callするラベルは必ずreturnされなければならない
    # screenからセリフを呼び出したいときは必ずこれを使う
    class FromSc(Action):

        def __init__(self, calllabel_0, jumplabel_0=None, **kwargs):
            self.clabel = calllabel_0
            self.jlabel = jumplabel_0
            self.kwargs = kwargs
        
        def __call__(self):
            renpy.call("say_about", calllabel_0=self.clabel, jumplabel_0=self.jlabel, **self.kwargs)
