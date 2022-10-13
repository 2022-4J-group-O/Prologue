################################################################################
## 初期化
################################################################################

init offset = -1


################################################################################
## スタイル
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## ゲーム内のスクリーン
################################################################################


## Say（発話）スクリーン ################################################################
##
## Say スクリーンはプレイヤーにダイアローグ（台詞）を表示するのに使います。who、
## what の二つのパラメーターをとり、who は発話しているキャラクターの名前、what
## は表示されるテキストを意味します。（キャラクターの名前がない場合 who は None
## になります）
##
## このスクリーンは、テキストを表示するために "what" のＩＤを持つ text
## displayable を必ず作成しなければなりません。また、スタイルのプロパティを適用
## するために、ＩＤ "who" とＩＤ "window" を持つ text displayable も作成するとい
## いでしょう。
##
## https://ja.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## サイドイメージ（テキストボックス横に表示するイメージ）があれば、テキスト
    ## の上に表示します。ただし variant（画面のタイプ）が phone の場合は、スペー
    ## スが足りないので表示しません。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## namebox を Character オブジェクトから使えるスタイルの接頭辞として追加します。
## （例：namebox_background)
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input（入力）スクリーン ##############################################################
##
## renpy.input を表示するのに使うスクリーンです。prompt のパラメーターは、プロン
## プト（入力ボックスの隣に表示されるテキスト）を表示するのに使います。
##
## このスクリーンは input のパラメーター を受け付けるために "input" をＩＤに持つ
## input displayable を作成する必要があります。
##
## https://ja.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice（選択）スクリーン #############################################################
##
## このスクリーンは、ゲーム内の選択肢を表示する menu ステートメントに使います。
## items のパラメーターは caption（選択肢のテキスト）と action（クリック時の実行
## 内容）を要素に持つオブジェクトのリスト（配列）です。
##
## https://ja.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu（クイックメニュー）スクリーン ###################################################
##
## クイックメニューはゲーム中に常時表示されるスクリーンで、ゲーム外の機能に素早
## くアクセスすることができます。

screen quick_menu():

    ## 他のスクリーンの上に表示する。
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("ロールバック") action Rollback()
            textbutton _("ヒストリー") action ShowMenu('history')
            textbutton _("スキップ") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("オート") action Preference("auto-forward", "toggle")
            textbutton _("セーブ") action ShowMenu('save')
            textbutton _("Q.セーブ") action QuickSave()
            textbutton _("Q.ロード") action QuickLoad()
            textbutton _("設定") action ShowMenu('preferences')


## 次のコードは、プレイヤーが明示的にインターフェースを隠さない限り quick_menu
## スクリーンが常にゲーム中に表示されるようにしています。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## メインメニュースクリーンとゲームメニュースクリーン
################################################################################

## Navigation（ナビゲーション）スクリーン ####################################################
##
## このスクリーンはメインメニューとゲームメニューに表示され、各メニュー間を移動
## したり、ゲームをスタートしたりする機能を提供しています。

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("スタート") action Start()

        else:

            textbutton _("ヒストリー") action ShowMenu("history")

            textbutton _("セーブ") action ShowMenu("save")

        textbutton _("ロード") action ShowMenu("load")

        textbutton _("環境設定") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("リプレイ終了") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("メインメニュー") action MainMenu()

        textbutton _("バージョン情報") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## モバイルデバイスにはヘルプは不要であるか不適切です。
            textbutton _("ヘルプ") action ShowMenu("help")

        if renpy.variant("pc"):

            ## 終了ボタンはiOSでは使用できません。また、AndroidやWebでは必要あり
            ## ません。
            textbutton _("終了") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu（メインメニュー）スクリーン #####################################################
##
## Ren'Py が起動した時に表示されるメインメニューを表示するスクリーンです。
##
## https://ja.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## 次のコードは、同じタグを持つ他のメニュースクリーンが表示された時にスクリ
    ## ーンを置換します。
    tag menu

    add gui.main_menu_background

    ## 次の空のフレームは gui/overlay/main_menu.png を表示してメインメニューを暗
    ## くしています。
    frame:
        style "main_menu_frame"

    ## use ステートメントは、他のスクリーンを現在のスクリーンの内に表示するのに
    ## 使います。メインメニューの実際のコンテンツは navigation（ナビゲーション）
    ## スクリーンです。
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu（ゲームメニュー）スクリーン #####################################################
##
## このスクリーンは、様々なゲームメニューの基本的な共通構造をレイアウトします。
## 各ゲームメニュースクリーンによって呼び出され、背景・現在のスクリーンタイト
## ル・ナビゲーションを表示します。
##
## scroll パラメーターは None 、"viewport" 、"vpgrid" のいずれかをとります。呼び
## 出し親のスクリーンのコンテンツは、このスクリーンの中の transclude の部分に配
## 置されます。

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 次のフレームはナビゲーションを表示するスペースを空けています。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("戻る"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About（バージョン情報）スクリーン #########################################################
##
## このスクリーンは、本ゲームと Ren'Py に関するコピーライトとクレジットを表示し
## ます。
##
## このスクリーンは特別なことをしていません。そのためカスタムスクリーン作成の例
## として利用していきます。

screen about():

    tag menu

    ## 次の use ステートメントは game_menu（ゲームメニュー）スクリーンをこのスク
    ## リーンの内に表示しています。use 文の子（内包されたオブジェクト）の vbox
    ## は game_menu スクリーンの中の viewport に配置されます。
    use game_menu(_("バージョン情報"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about は、通常 options.rpy で設定します。
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://ja.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save（セーブ・ロード）スクリーン #################################################
##
## 以下のスクリーンは、プレイヤーがゲームデータをセーブ・ロードできるようにしま
## す。どちらも構造はほとんど等しいため、第三の file_slots（ファイルスロット）ス
## クリーンで実装しています。
##
## https://ja.renpy.org/doc/html/screen_special.html#save https://ja.renpy.org/
## doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("セーブ"))


screen load():

    tag menu

    use file_slots(_("ロード"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("ページ {}"), auto=_("オートセーブ"), quick=_("クイックセーブ"))

    use game_menu(title):

        fixed:

            ## 次の文は、ページ名の input のイベントがより後に定義したボタンより
            ## も優先されるように、重なり順を反転しています。
            order_reverse True

            ## ページ名。クリックすると編集できるように、ボタンとして表示してい
            ## ます。
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## ファイルスロットを配置するグリッド。
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%Y年%m月%d日(%a) %H時%M分"), empty=_("空のスロット")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## 他のページにアクセスするボタン。
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) は１から９までの数字を生成します。
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences（環境設定）スクリーン ######################################################
##
## Preferences スクリーンは、各プレイヤーがゲームを自分に合う環境にカスタマイズ
## できるようにします。
##
## https://ja.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("環境設定"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("ディスプレイ")
                        textbutton _("ウィンドウ") action Preference("display", "window")
                        textbutton _("フルスクリーン") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("スキップ")
                    textbutton _("未読テキストもスキップ") action Preference("skip", "toggle")
                    textbutton _("選択肢後もスキップ継続") action Preference("after choices", "toggle")
                    textbutton _("トランジションをスキップ") action InvertSelected(Preference("transitions", "toggle"))

                ## この場所に "radio_pref" または "check_pref" をスタイルに持つ
                ## vbox を追加して、開発者が定義した環境設定を増やすことができま
                ## す。

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("文字表示速度")

                    bar value Preference("text speed")

                    label _("オート待ち時間")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("音楽の音量")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("効果音の音量")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("テスト") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("ボイスの音量")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("テスト") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("全てミュート"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History（履歴）スクリーン ############################################################
##
## このスクリーンは、ダイアローグヒストリー（台詞の履歴）を表示します。このスク
## リーンに特別なものはありませんが、_history_list に保存されたダイアローグヒス
## トリーにアクセスする必要があります。
##
## https://ja.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## データが大きくなりすぎる可能性があるため、このスクリーンを予測しないよう
    ## にしています。
    predict False

    use game_menu(_("ヒストリー"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## 次の文は history_height が None の場合でもレイアウトが正しく
                ## なるようにしています。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## キャラクター名のカラーが設定されている場合、その情報
                        ## を獲得して色付けします。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("ヒストリーはありません。")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help（ヘルプ）スクリーン ##############################################################
##
## キーやマウスの割り当てに関する情報を表示するスクリーン。実際のヘルプは他のス
## クリーン（keyboard_help、mouse_help、gamepad_help）を使います。

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("ヘルプ"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("キーボード") action SetScreenVariable("device", "keyboard")
                textbutton _("マウス") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("ゲームパッド") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("台詞を読み進める。またはボタンを選択する。")

    hbox:
        label _("Space")
        text _("台詞を読み進める。ただしボタンは選択しない。")

    hbox:
        label _("方向キー")
        text _("インターフェースを移動する。")

    hbox:
        label _("Escape")
        text _("ゲームメニューを開く。")

    hbox:
        label _("Ctrl")
        text _("押し続けている間スキップする。")

    hbox:
        label _("Tab")
        text _("スキップモードに切り替える。")

    hbox:
        label _("Page Up")
        text _("前の台詞に戻る。")

    hbox:
        label _("Page Down")
        text _("ロールバック中、次の台詞に進む。")

    hbox:
        label "H"
        text _("インターフェースを隠す。")

    hbox:
        label "S"
        text _("スクリーンショットを撮る。")

    hbox:
        label "V"
        text _("{a=https://ja.renpy.org/l/voicing}セルフボイシング{/a}を有効化する。")

    hbox:
        label "Shift+A"
        text _("アクセス性メニューを開きます。")


screen mouse_help():

    hbox:
        label _("左クリック")
        text _("台詞を読み進める。またはボタンを選択する。")

    hbox:
        label _("中クリック")
        text _("インターフェースを隠す。")

    hbox:
        label _("右クリック")
        text _("ゲームメニューを開く。")

    hbox:
        label _("マウスホイール上回転\n画面サイドをタッチ")
        text _("前の台詞に戻る。")

    hbox:
        label _("マウスホイール下回転")
        text _("ロールバック中、次の台詞に進む。")


screen gamepad_help():

    hbox:
        label _("Ｒトリガー\nＡ／下ボタン")
        text _("台詞を読み進める。またはボタンを選択する。")

    hbox:
        label _("Ｌトリガー\nＬボタン")
        text _("前の台詞に戻る。")

    hbox:
        label _("Ｒボタン")
        text _("ロールバック中、次の台詞に進む。")


    hbox:
        label _("方向パッド\n左右スティック")
        text _("インターフェースを移動する。")

    hbox:
        label _("スタート、ガイド")
        text _("ゲームメニューを開く。")

    hbox:
        label _("Ｙ／上ボタン")
        text _("インターフェースを隠す。")

    textbutton _("キャリブレート") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## 付加的なスクリーン
################################################################################


## Confirm（確認）スクリーン ############################################################
##
## Confirm スクリーンは、 Ren'Py がプレイヤーに「はい・いいえ」で答える質問をす
## る時に使います。
##
## https://ja.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 次の文は、このスクリーンが表示されている間、他のスクリーンの反応を無視す
    ## るようにしています。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("はい") action yes_action
                textbutton _("いいえ") action no_action

    ## 右クリックで「いいえ」と答える。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator（スキップ表示）スクリーン #################################################
##
## Skip_indicator スクリーンは、スキップ中であることを表示するスクリーンです。
##
## https://ja.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("スキップ中")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 矢印を次から次へと点滅させる transform（変換）。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 小さな黒い矢印型のグリフが入ったフォントが必要になります。
    font "DejaVuSans.ttf"


## Notify（通知）スクリーン #############################################################
##
## Notify スクリーンは、プレイヤーに短いメッセージを表示するのに使います。（例え
## ばクイックセーブをしたり、スクリーンショットを撮った時。）
##
## https://ja.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL（ノベル）スクリーン ###############################################################
##
## このスクリーンは NVL モード（全画面方式）の台詞と選択肢を表示します。
##
## https://ja.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## gui.nvl_height が設定されていれば vpgrid で等間隔に表示、そうでなけれ
        ## ば vbox で可変的に表示します。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 指定されれば選択肢を表示します。config.narrator_menuがTrueだと、メニ
        ## ューは正常に表示されないでしょう。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 次の文は一度に表示される NVL モードのエントリー（１台詞）の最大数を制御しま
## す。
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## モバイル用の別設定
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## マウスが使用できないので、ボタンが大きくて数が少ないクイックメニューに置き換
## えて、タッチしやすいようにしています。
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("ロールバック") action Rollback()
            textbutton _("スキップ") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("オート") action Preference("auto-forward", "toggle")
            textbutton _("メニュー") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
