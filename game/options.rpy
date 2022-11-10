## このファイルはゲームをカスタマイズする基本的なオプションを記載しています。
##
## 二つの'#'で始まる行はコメントなのでアンコメント（#を消してコメントをコードに
## 戻すこと）してはいけません。一つの'#'で始まる行はコメントアウト（#を加えてコ
## ードをコメント化し、実行できなくすること）されたコードで、必要に応じてアンコ
## メントできます。


## 基本 ##########################################################################

## 人の目で読み取れるゲーム名。ゲーム名はデフォルトのウィンドウタイトルに使われ
## る他、インターフェースやエラーリポートにも表示されます。
##
## _() で囲まれた文字列は翻訳時に生成されるファイルに記載されます。

define config.name = _("Prologue")


## 上で定義したタイトルをメインメニュースクリーン（ゲーム起動後、最初に表示され
## るスクリーン）に表示するかどうか決めます。False にすると表示しません。

define gui.show_name = True


## ゲームのバージョン。

define config.version = "1.0"


## About（バージョン情報）スクリーンに表示されるテキスト。トリプルクオートの間に
## テキストを入力します。段落の間には空行を挿入して下さい。

define gui.about = _p("""
""")


## 実行ファイルやビルドされた配布物のディレクトリー名に使われる、ゲームの簡易
## 名。簡易名は ASCII 文字（半角英数字）のみで構成され、スペース・コロン・セミコ
## ロンなどを含んでは行けません。

define build.name = "Prologue"


## サウンドと音楽 #####################################################################

## これらの3つの変数は、特に、どのミキサーがデフォルトでプレーヤーに表示されるか
## を制御します。これらのいずれかをFalseに設定すると、適切なミキサーが非表示にな
## ります。

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## サウンドやボイスの設定画面で、ユーザーがテストサウンドを再生可能にする場合、
## 以下の行をアンコメントしてサンプルサウンドを指定します。

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## 次の行をアンコメントしてオーディオファイルを指定すると、メインメニューで再生
## されます。このファイルは、停止するか他の音楽が再生されない限りゲーム中で流れ
## 続けます。

# define config.main_menu_music = "main-menu-theme.ogg"


## トランジション #####################################################################
##
## 以下の変数は、メニュー切り替えなどのイベントに対するトランジションを設定しま
## す。各変数にはトランジションを指定します。トランジションを使わない場合は None
## に設定します。

## ゲームメニュー（ゲーム中、右クリックで表示されるメニュー）を開いたり閉じたり
## する時のトランジション。

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## ゲームメニューのスクリーンを切り替える時のトランジション。

define config.intra_transition = dissolve


## ゲームデータをロードした後に使われるトランジション。

define config.after_load_transition = None


## ゲーム終了後、メインメニューに戻る時のトランジション。

define config.end_game_transition = None


## メインメニューからゲームを開始する時のトランジションは、ここでは設定できませ
## ん。代わりに、ゲーム開始後の最初のシーンで with ステートメントを使ってくださ
## い。


## テキストウィンドウの管理 ################################################################
##
## 次の変数は、台詞を表示するテキストウィンドウの挙動を制御します。"show" であれ
## ば常に表示、"hide" であれば台詞が表示されているときにのみ表示します。"auto"
## であれば scene ステートメントの直前に非表示にして、say ステートメントの直前に
## 再表示します。
##
## ゲーム開始後でも "window show"、"window hide"、"window auto" ステートメントで
## 変更することができます。

define config.window = "auto"


## テキストウィンドウを表示したり、非表示にしたりする時のトランジション。

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## 環境設定のデフォルト ##################################################################

## デフォルトの文字表示速度。数字は一秒に表示する文字数で、デフォルト値の 0 は無
## 限（一瞬で表示）を意味します。

default preferences.text_cps = 0

default preferences.slow_cps = 5
## デフォルトのオート待ち時間。0 から 30 までの数字を取り、数字が大きいほど待ち
## 時間が長くなります。

default preferences.afm_time = 15


## セーブディレクトリー ##################################################################
##
## プラットフォームごとの Ren'Py がゲームのセーブデータを作成する場所を制御しま
## す。セーブファイルは以下の場所に作成されます：
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## この値は一般的に変更するべきではありません。もし変更する場合、式や変数ではな
## く文字列で直接指定しなければなりません。

define config.save_directory = "Prologue-1665662419"


## アイコン ########################################################################
##
## タスクバーやダックに表示されるアイコン。

define config.window_icon = "gui/window_icon.png"


## ビルド設定 #######################################################################
##
## このセクションは、プロジェクトを配布物にビルドするときの挙動を制御します。

init python:

    ## 以下の機能はファイルパターン（ワイルドカード等で複数ファイルを指定する文
    ## 字列）を利用します。ファイルパターンは、大文字小文字を区別せず、ベースデ
    ## ィレクトリーからの相対パスを参照します（最初の / は無視します）。複数のパ
    ## ターンが一致した場合、先に定義した方が優先されます。
    ##
    ## パターンは以下の記号を使用します：
    ##
    ## / はディレクトリーのセパレーターです。
    ##
    ## * はディレクトリーセパレーターを除く、すべての文字に一致します。
    ##
    ## ** はディレクトリーセパレーターを含む、すべての文字に一致します。
    ##
    ## 例えば、"*.txt" はベースディレクトリーにある全ての txt ファイルに一致し、
    ## "game/**.ogg" はゲームディレクトリー及びそのサブディレクトリーにある全て
    ## の ogg ファイルに一致し、"**.psd" はプロジェクトのあらゆる psd ファイルに
    ## 一致します。

    ## classify（分類）を None に設定したファイルは配布物から除外されます。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## アーカイブ（書庫化・暗号化）したいファイルは 'archive'（または任意の文字
    ## 列）に分類します。

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## documentation（ドキュメント）に指定したパターンと一致するファイルは mac
    ## 用アプリのビルドで複製され、app と zip のどちらにも含まれるようになりま
    ## す。

    build.documentation('*.html')
    build.documentation('*.txt')


## 拡張をダウンロードしたり、アプリ内課金を行う場合には、Google Play ライセンス
## キーが必要です。キーは Google Play developer console の "Services & APIs" に
## あります。

# define build.google_play_key = "..."


## itch.io project に関連付けられたユーザー名とプロジェクト名。二つの名前はスラ
## ッシュで分けてください。

# define build.itch_project = "renpytom/test-project"


## ここから追加プロパティー #########################################################10

## defineで定義したフィールドはreadonly

# プレーヤーが主に操作をするディレクトリー
define user_directory = "game_data"

# 読み込むファイルのlist
define objects = ['red', 'blue', 'green', 'Book', 'Door', 'Key']

# 現在いるroom
default current_room = 'default'

# 内部変数
default say_interact = False