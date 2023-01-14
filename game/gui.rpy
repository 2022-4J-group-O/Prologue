################################################################################
## 初期化
################################################################################

## このファイルは GUI をカスタマイズする基本的なオプションを記載しています。次の
## init offset ステートメントにより、このファイルの init 文は他のファイルの init
## 文よりも先に実行されます。
init offset = -2

## まず最初に gui.init を実行して、スタイルを扱いやすい初期値にリセットし、ゲー
## ムの横幅と縦幅を設定します。
init python:
    gui.init(1920, 1080)



################################################################################
## GUI 設定変数
################################################################################


## カラー #########################################################################
##
## インターフェースのテキストのカラー。

## アクセントカラー。タイトル・ラベル・ハイライトされたテキスト・ボタンの背景・
## スライダーのつまみ等、インターフェイスの様々な場所で使います。
define gui.accent_color = '#0099cc'

## selected（選択中）でも hover（フォーカス中）でもない状態のテキストボタンのカ
## ラー。
define gui.idle_color = '#888888'

## スモールカラー。クイックメニューなどの、明るさを調節する必要のある小さなテキ
## ストボタンに使います。
define gui.idle_small_color = '#aaaaaa'

## hover（フォーカス中）のテキストボタンのカラー。また、バーの充足部分（左側）や
## スライダーのつまみ等の画像を再生成するときにも使われます。
define gui.hover_color = '#66c1e0'

## selected（選択中）のテキストボタンのカラー。ボタンが現在のスクリーンであった
## り、環境設定の値と一致したりすると、ボタンは選択中になります。
define gui.selected_color = '#ffffff'

## insensitive (選択不可能）なテキストボタンのカラー。
define gui.insensitive_color = '#8888887f'

## バーの非充足部分（右側）やスライダーの背景部分のカラー。バーやスライダーのカ
## ラーは直接使われず、 GUI を変更・更新した場合の画像生成に使われます。
define gui.muted_color = '#003d51'
define gui.hover_muted_color = '#005b7a'

## text_color は台詞や選択肢のテキストのカラーです。interface_text_color はヒス
## トリーやヘルプなどそれ以外のテキストのカラーです。
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## フォントとフォントサイズ ################################################################

## ゲーム内の台詞や選択肢に使われるフォント。
define gui.text_font = "fonts/ZenMaruGothic-Regular.ttf"

## キャラクターの名前に使われるフォント。
define gui.name_text_font = gui.text_font

## ゲームメニューなどのインターフェースに使われるテキストのフォント。
define gui.interface_text_font = "fonts/Kaisotai-Next-UP-B.ttf"

## 一般的な台詞のテキストサイズ。
define gui.text_size = 33

## キャラクターの名前のテキストサイズ。
define gui.name_text_size = 45

## インターフェースのテキストサイズ。
define gui.interface_text_size = 33

## インターフェースのラベル（見出し）のテキストサイズ。
define gui.label_text_size = 36

## notify（通知）スクリーンのテキストサイズ。
define gui.notify_text_size = 24

## ゲームタイトルのテキストサイズ。
define gui.title_text_size = 75


## メインメニューとゲームメニュー #############################################################

## メインメニューとゲームメニューの背景画像。メインメニューはゲーム起動時に最初
## に表示されるメニュー、ゲームメニューはゲーム中右クリックで呼び出せるメニュー
## です。画像を変えたい場合は gui ディレクトリーにある該当の画像を入れ替えてくだ
## さい。
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## ダイアローグ（台詞） ##################################################################
##
## 以下の変数は、一度に表示される台詞とキャラクターの名前を、どのようにスクリー
## ンに表示するか制御します。

## 台詞を表示するテキストボックスの高さ。テキストボックスの画像を変えたい場合は
## gui/textbox.png の画像を入れ替えます。
define gui.textbox_height = 278

## 画面に対する、テキストボックスの垂直方向の位置。 0.0 は上端、0.5 は中央、 1.0
## は下端になります。
define gui.textbox_yalign = 1.0


## テキストボックスに対する、キャラクター名の位置。左上からのピクセル数で指定す
## るか 0.0 から 1.0 までの小数で指定します。 0.5 は中央に表示。
define gui.name_xpos = 360
define gui.name_ypos = 0

## キャラクター名の文字揃え。 0.0 は左揃え、0.5 は中央揃え、 1.0 は右揃えになり
## ます。0.0 以外にした場合、キャラクター名の位置の調整も必要になります。
define gui.name_xalign = 0.0

## キャラクター名を表示するネームボックスのサイズ。None にすると、自動的に決定さ
## れます。画像を変えたい場合は gui/textbox.png の画像を入れ替えます（デフォルト
## 画像は透明なので表示されません）。
define gui.namebox_width = None
define gui.namebox_height = None

## ネームボックスのボーダーのサイズ。左、上、右、下の順で指定します。ボックスの
## サイズは、その中に表示されるキャラクター名のサイズから更にボーダー分拡張した
## サイズになります。
define gui.namebox_borders = Borders(5, 5, 5, 5)

## True に設定すると、ネームボックスの背景画像をスケーリングではなくタイリングで
## 表示します。
define gui.namebox_tile = False


## テキストボックスに対する、台詞の位置。左上からのピクセル数で指定するか 0.0 か
## ら 1.0 までの小数で指定します。 0.5 だと中央に表示。
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## 台詞の最大ピクセル幅。このピクセル幅以上の台詞は折り返して表示されます。
define gui.dialogue_width = 1116

## 台詞の文字揃え。 0.0 は左揃え、0.5 は中央揃え、 1.0 は右揃えになります。0.0
## 以外にした場合、台詞の位置の調整も必要になります。
define gui.dialogue_text_xalign = 0.0


## ボタン #########################################################################
##
## 以下の変数は、ボタンをどのように表示するか制御します。画像を変えたい場合は
## gui/button ディレクトリーにある各 background.png の画像を入れ替えます（デフォ
## ルト画像は透明なので表示されません）。ボタンの状態に合わせて画像を変えたい場
## 合は、ファイル名に idle_、hover_、selected_、selected_hover_ の接頭辞を付けま
## す。

## ボタンの縦幅と横幅。None にすると自動的に計算されます。
define gui.button_width = None
define gui.button_height = None

## ボタンのボーダーのサイズ。左、上、右、下の順で指定します。ボタンのサイズは、
## その中のテキストやオブジェクトのサイズから更にボーダー分拡張したサイズになり
## ます。
define gui.button_borders = Borders(6, 6, 6, 6)

## True に設定すると、ボタンの背景画像をスケーリングではなくタイリングで表示しま
## す。
define gui.button_tile = False

## ボタンのテキストに使用するフォント。
define gui.button_text_font = gui.interface_text_font

## ボタンのテキストのサイズ。
define gui.button_text_size = gui.interface_text_size

## 状態別のボタンのテキストのカラー。idle は選択可能、hover はフォーカス中、
## selected は選択中、insensitive は選択不可能な状態です。
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## ボタンのフレームに対する、テキストの文字揃え。 0.0 は左揃え、0.5 は中央揃え、
## 1.0 は右揃えになります。
define gui.button_text_xalign = 0.0


## 以下の変数は、様々なボタンの種類ごとにボタンの基本設定を上書きします。詳細は
## gui ドキュメンテーションを参考にしてください。
##
## デフォルトのインターフェースには、radio、check、confirm、page、quick、
## navigation、choice、slot、test、help、nvl のボタンが用意されています。radio
## と check は環境設定の各項目のボタン（デフォルトでは同じ画像）。confirm は確認
## 画面の選択肢、page は セーブ・ロード画面のページ切り替え、quick はクイックメ
## ニュー、 navigation はゲームメニューのメニュー切り替えに使うボタンです。

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## 上記以外にも、接頭辞と接尾辞を適切に組み合わせた変数名を追加すれば、様々なカ
## スタマイズが可能になります。例えば、次の行をアンコメントすると navigation（メ
## ニュー切り替え）ボタンの横幅を指定することができます。

# define gui.navigation_button_width = 250


## Choice（選択）ボタン ###############################################################
##
## Choice ボタンは、ゲーム内の選択肢に使うボタンです。

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"


## File Slot（ファイルスロット）ボタン ######################################################
##
## File slot は特別なボタンで、セーブデータのサムネイル画像と詳細情報を含んでい
## ます。他のボタンと同じように gui/button ディレクトリーにある slot_ の接頭辞が
## 付いた背景画像を使います。

## File slot ボタンの設定。
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## File slot に使われるサムネイル画像の横幅と縦幅。
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## １ページあたりの File slot の列数（cols）と行数（rows）。
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## 配置と間隔 #######################################################################
##
## 以下の変数は、インターフェースの様々な要素の位置と間隔を制御します。

## 画面左端からの navigation（メニュー切り替え）ボタンの位置。
define gui.navigation_xpos = 60

## 画面上端からの skip indicator（スキップ表示）スクリーンの位置。
define gui.skip_ypos = 15

## 画面上端からの notify（通知）スクリーンの位置。
define gui.notify_ypos = 68

## ゲーム中の choice（選択）ボタンの間隔。
define gui.choice_spacing = 33

## メインメニューやゲームメニューの navigation（メニュー切り替え）ボタンの間隔。
define gui.navigation_spacing = 6

## 環境設定の各項目の間隔。
define gui.pref_spacing = 15

## 環境設定の各項目にある、各ボタンの間隔。
define gui.pref_button_spacing = 0

## セーブ・ロード画面の file page（ページ切り替え）ボタンの間隔。
define gui.page_spacing = 0

## セーブ・ロード画面の file slot（ファイルスロット）ボタン間隔。
define gui.slot_spacing = 15

## メインメニューのテキストの文字揃え。
define gui.main_menu_text_xalign = 1.0


## フレーム ########################################################################
##
## 以下の変数は、インターフェースのコンポーネントを収納するフレームを制御しま
## す。フレームは、ウィンドウやオーバーレイが用意されていない場面で使われます。

## 一般的なフレーム。デフォルトのインターフェースでは未使用です。画像は gui/
## frame.png。
define gui.frame_borders = Borders(6, 6, 6, 6)

## confirm（確認）スクリーンに使用するフレーム。画像は gui/overlay/confirm.png。
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## skip indicator（スキップ表示）スクリーンに使用するフレーム。画像は gui/
## skip.png。
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## notify（通知）スクリーンに使用するフレーム。画像は gui/notify.png。
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## True に設定すると、フレームの背景画像をスケーリングではなくタイリングで表示し
## ます。
define gui.frame_tile = False


## バー・スクロールバー・スライダー ############################################################
##
## 以下の変数は、バー・スライダー・スクロールバーの外見を制御します。
##
## デフォルトの GUI はスライダーと垂直スクロールバーだけを使用します。他のバーは
## 開発者が追加したスクリーンでのみ使われます。

## バー・スクロールバー・スライダーの各々の太さ（水平バーでは縦幅、垂直バーでは
## 横幅）。
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## True に設定すると、バーの背景をスケーリングではなくタイリングで表示します。
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## 水平バーのボーダー。画像はそれぞれ、 gui/bar/left.png 及び right.png、gui/
## slider/horizontal_**.png、gui/scrollbar/horizontal_**.png。
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## 垂直バーのボーダー。画像はそれぞれ、gui/bar/bottom.png 及び top.png、gui/
## slider/vertical_**.png、gui/scrollbar/vartical_**.png。
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## スクロール不可能なスクロールバーをどう扱うか。 "hide" なら非表示、None なら表
## 示します。
define gui.unscrollable = "hide"


## ヒストリー #######################################################################
##
## History（履歴）スクリーンは、プレイヤーが見終わった台詞を表示します。

## ヒストリーのエントリー（１台詞）を最大いくつまで保持するか。
define config.history_length = 250

## History スクリーンにおける、エントリーの高さ。None にすると可変になりますが、
## パフォーマンスが低下します。
define gui.history_height = 210

## キャラクター名の縦座標・横座標・横幅・文字揃え。
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## 台詞の縦座標・横座標・横幅・文字揃え。
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## NVL モード #####################################################################
##
## NVL（ノベル）スクリーンは、 NVL モード（全画面方式）のキャラクターの台詞を表
## 示するスクリーンです。

## NVL モードに使用する背景のボーダー。画像は gui/nvl.png。
define gui.nvl_borders = Borders(0, 15, 0, 30)

## NVL モードにおける、一度に表示されるエントリー（１台詞）の最大数。この値以上
## のエントリーを表示しようとすると、一番古いエントリーが取り除かれます。
define gui.nvl_list_length = 6

## NVL モードにおける、エントリー（１台詞）の高さ。None にすると可変になります。
define gui.nvl_height = 173

## NVL モードにおいて、gui.nvl_height を None に設定した場合の各エントリーの間
## 隔。また、台詞と選択肢との間隔にも使われます。
define gui.nvl_spacing = 15

## キャラクター名の縦座標・横座標・横幅・文字揃え。
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## 台詞の縦座標・横座標・横幅・文字揃え。
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## nvl_thought（モノローグ）の縦座標・横座標・横幅・文字揃え。
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## NVL モードにおける、選択肢の横座標と文字揃え。
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0

## 多言語対応 #######################################################################

## 次の変数は改行・禁則処理を制御します。デフォルトの値が推奨です。他の値は
## https://www.renpy.org/doc/html/style_properties.html#style-property-language
## を参照してください。

define gui.language = 'japanese-normal'


################################################################################
## モバイルデバイス
################################################################################

init python:

    ## タブレットやスマートフォンでタッチしやすいように、 quick ボタンのサイズを
    ## 大きくします。
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## スマートフォンで見やすいように、GUI の各要素のサイズと間隔を変更します。
    @gui.variant
    def small():

        ## フォントサイズ。
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## テキストボックスの位置を調整。
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## 様々なサイズとスペーシングを変更。
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## ファイルスロットの配置。
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL モード。
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
