init python:

    # Eventを終了させる関数
    # jlabelはjump先のラベル
    # jlabelを指定しない場合はreturnする場合と同じ場所に飛ぶ
    def event_end(jlabel=None):
        global enable_event
        if enable_event:
            renpy.error("there are no events to end")
        else:
            enable_event = True
            if jlabel == None:
                renpy.return_statement()
            else:
                renpy.pop_call()
                renpy.jump(jlabel)
    
    # 他のインタラクションを禁止してラベルを呼ぶ
    # Event終了後は必ずevent_end関数を呼ばなければならない
    # screenからセリフを呼び出したいときは必ずこれを使う
    class Event(Action):

        def __init__(self, calllabel_0, **kwargs):
            self.clabel = calllabel_0
            self.kwargs = kwargs
        
        def __call__(self):
            global enable_event
            if enable_event:
                enable_event = False
                renpy.call(self.clabel, **self.kwargs)
                enable_event = True
