---
# You can also start simply with 'default'
theme: neversink
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cover.sli.dev
# some information about your slides (markdown enabled)
title: Welcome to Slidev
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# apply unocss classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
contextMenu: false
hideNavigation: true
shortcut:
  toc: false
layout: cover
color: light

---

# NetLogo入門

東北大学文学研究科
計算人文社会学

**呂沢宇**   

行動科学概論　_社会科学におけるモデル入門_ <a href="https://lvzeyu.github.io/https:/github.com/lvzeyu/social_modeling_lecture" class="ns-c-iconlink"><mdi-open-in-new /></a>  



---
layout: two-cols-title
columns: is-7
---

::title::
# シミュレーションモデルを実装するツール

プログラミングベースのツール

::left::

- Python、Juliaなどのプログラミング言語を用いてシミュレーションモデルを実装することができる
    - 高い柔軟性と拡張性
- モデリングとシミュレーションの実装に支援するライブラリも多くある
    - ライブラリは、自分で毎回ゼロからすべてを実装するのではなく、あらかじめ用意された機能を呼び出して利用できる仕組みである。これにより、開発を効率化し、複雑な処理も比較的容易に実装できる
    - [Mesa](https://github.com/projectmesa/mesa)

::right::

```python {1|3-10|12-18|all}
from mesa import Agent, Model

class MoneyAgent(Agent):
    def __init__(self, model):
        super().__init__(model)
        self.wealth = 1

    def step(self):
        if self.wealth > 0:
            other = self.random.choice(
                list(self.model.agents))
            other.wealth += 1
            self.wealth -= 1

class MoneyModel(Model):
    def __init__(self, N):
        super().__init__()
        for _ in range(N):
            MoneyAgent(self)

    def step(self):
        self.agents.shuffle_do("step")
```


---
layout: two-cols-title
---

::title::
# シミュレーションモデルを実装するツール

グラフィックツール

::left::

- インタフェースで操作しながらモデルを構築・実行するツール
    - 直感的に扱いやすく
    - 実装の自由度や拡張性は、プログラミングベースのツールより制限される
- [Agent Sheets](http://www.agentsheets.com/)
- [VisualBots](https://github.com/nyje/visual-bots)
- [Repast Simphony](https://repast.github.io/repast_simphony.html)

::right::
 
<img src="./image/graphic_tool.png" class="h-64 mx-auto" />

<style scoped>
.two-cols-header {
  row-gap: 0.5rem !important;
}
</style>


---
class: flex justify-center items-center gap-20 px-40 text-xl
---

<div
  absolute text-3xl
  :class="$clicks < 1 ? 'text-black' : 'translate-y--18 scale-40 text-black/30'"
  transition duration-500 ease-in-out
>
  <span>コードを少し書きながらビジュアルも使えるツールでもある?</span>
</div>


<div flex flex-col items-center>
  <v-clicks>
    <div mt-12>
      <h1 flex flex-col items-center text="4xl!" style="text-align: center; line-height: 1.4;">
        <a href="https://ccl.northwestern.edu/netlogo/" target="_blank" rel="noopener noreferrer" class="flex items-center gap-3 no-underline">
          <img src="./image/netlogo_logo.png" class="h-10 w-auto" alt="NetLogo logo" />
          <span style="color: #000000;">NetLogo</span>
        </a>
      </h1>
    </div>
  </v-clicks>
</div>




---
transition: fade-out
---

# NetLogoの画面

<div class="flex justify-center">
  <img src="./image/netlogo_general.png" class="h-100 w-auto" alt="NetLogo logo" />
</div>

---

# インターフェース画面

<img src="./image/netlogo-interface.png" class="h-96 mx-auto" />

---
transition: fade-out
---

# NetLogoの動作の仕組み

<div class="grid grid-cols-2 gap-8 mt-8 items-center">
  <div class="flex justify-center">
    <img src="./image/netlogo_procedure.png" class="h-60 object-contain rounded" />
  </div>

  <div>

  - インターフェース画面でボタンを押すことによって、プログラムが実行される
      - `setup` と`go` の2 つのボタンを作成することが規範的な作り方である
          - `setup` で初期化
          - `go` で実行
  - `go procedure` の中から別の`procedure`を呼び出して、より複雑な処理などを行うことになる
      - `ask`文を使って、エージェントに命令するという形式でプログラミングを行う設定を使うことは多い

  </div>
</div>


---

# NetLogoで構築されるモデルの基本要素

<div class="flex justify-center">
  <img src="./image/netlogo_component.png" class="h-80 w-auto" alt="NetLogo logo" />
</div>

- **patch** がグリッド状に敷き詰められ，その上を **turtle** が動く
- **link** は turtle 同士をつなぐもの（有向リンクと無向リンクがある）
- **observer** は turtle, patch, link に命令を出すことができる


---
class: flex justify-center items-center gap-20 px-40 text-xl
---

<div
  absolute text-3xl
  :class="$clicks < 1 ? 'text-black' : 'translate-y--18 scale-60 text-black/30'"
  transition duration-500 ease-in-out
>
  <span>これからNetLogoの文法を説明する</span>
</div>
<div flex flex-col items-center>
  <div
    mt-12
    :class="$clicks < 1 ? 'opacity-0' : $clicks < 2 ? 'opacity-100' : 'translate-y--8 scale-60 opacity-30'"
    transition duration-500 ease-in-out
  >
    <h1 flex flex-col items-center text="4xl!" style="text-align: center; line-height: 1.4;">
      <span style="color: #000000;">一度にすべてを覚えるのは難しい....</span>
    </h1>
  </div>
  <v-click at="2">
    <div mt-6 text-center text-2xl text-gray-600>
      <span>💡 まずは聞き流し、その後は実践を通して理解していく</span>
    </div>
  </v-click>
</div>

---
layout: iframe-left
title: iframe Left Layout
url: https://www.netlogoweb.org/launch#https://www.netlogoweb.org/assets/modelslib/Sample%20Models/Social%20Science/Prisoner's%20Dilemma/Prisoner's%20Dilemma%20Basic.nlogox
scale: 0.5
class: my-cool-content-on-the-right
---


```ts {|1|8-10|13,21-29|15-17|3-19,22-29}{maxHeight:'500px'}
globals [partner-is-silent?]

to setup
  clear-all
  ;;Build the jail cell
  ask patches with [ count neighbors != 8 ] [
    set pcolor gray]

  ;;make the face visible
  create-turtles 1 [set color gray set size 30 set shape "face"]
  ;; set up the prisoner's dilemma
  ifelse partner-silence-known? [
    set partner-is-silent? partner-silent?
  ]
  [
    ;;if partner silence is not known, choose randomly whether or not he is silent.
    ifelse random 2 = 0
    [ set partner-is-silent? true ]
    [ set partner-is-silent? false ]
  ]
end

;;play the game, changing the face depending on the outcome.
to answer
  setup  ;;clears variables away so that setup doesn't need to be pressed every time.

  ;;next the four possible combinations of choices are dealt with.
  ;;the result corresponds to the tables in the interface and Info tabs.
  ;;first check to see if your partner was silent.
  ifelse partner-is-silent? [
      ;;now go through your two possible choices
      ifelse you-silent? [
      ask turtles [set shape "face silent"]
      user-message "You and your partner both remain silent.  You are sentenced to one year imprisonment."
    ] [
      ask turtles [set shape "face devious"]
      user-message "You confess and your partner remains silent. You go free."
    ]
  ]
  ;;your partner confessed.
  [
    ;;again go through your two possible choices
    ifelse you-silent? [
      ask turtles [set shape "face sucker" ]
      user-message "You remain silent, but your partner confesses.  You are sentenced to five years imprisonment."
    ] [
      ask turtles [set shape "face rational"]
      user-message "You and you partner both confess.  You are sentenced to three years imprisonment."
    ]
  ]
end
```


---
transition: fade-out
layout: two-cols-title
---

::title::
# Netlogoの基本文法

変数の代入と演算

::left::

<v-click at="1">

**`set` コマンドで変数に値を代入する**

- `x = 10` のような書き方はできない
- 変数の型（数値・文字列など）を宣言する必要はない
- 文字列は `"..."` で囲む

</v-click>

<v-click at="2">

**四則演算**

- `+ - * /` の前後に**半角スペース**が必要
- 論理演算子：`and`，`or`，`not`

</v-click>

::right::

```text {|1-3|5-8|10-13}
; 変数の代入
set x 10
set y "hogehoge"

; 四則演算
set x 10 + 5
set y 12 * 2 / 4 - 3
set z 10 mod 3

; 論理演算子
if (x > 5 and x < 20) [ ... ]
if (x < 0 or x > 100) [ ... ]
if (not (x = 0)) [ ... ]
```

</br>

<Admonition title="Info" color="teal-light" width="400px">
<span style="font-size: 1.3em;">`;` で始まる行は**コメント**です。NetLogoはその行を無視します。</span>
</Admonition>


---
transition: fade-out
layout: two-cols-title
---

::title::
# 変数の種類

変数の目的による使い分け

::left::

<v-click at="1">

**グローバル変数**（`globals`）
- モデル全体で共有される変数
- どのエージェント・手続きからでも参照・更新できる

</v-click>

<v-click at="2">

**エージェント変数**
- 各エージェントがそれぞれ独立した値を持つ

</v-click>

<v-click at="3">

**ローカル変数**（`let`）
- 特定な処理範囲内だけで有効な一時的な変数

</v-click>

::right::

```text {1|1,6|2-3,8,11|16}
globals [total-count]
turtles-own [energy]
patches-own [fertility]

to setup
  set total-count 100
  create-turtles total-count [
    set energy 50
  ]
  ask patches [
    set fertility random 10
  ]
end

to go
  let avg-energy mean [energy] of turtles
  ask turtles [
    set energy energy - 1
  ]
end
```



---
transition: fade-out
layout: two-cols-title
---

::title::
# Netlogoの基本文法

リストの操作

::left::

<v-click at="1">

**リストの作成**

- `(list ...)` でリストを作成
- インデックスアクセス（`x[0]`）は**不可**

</v-click>

<v-click at="2">

**要素の取り出し**

- `item (番号) (リスト)` で指定した位置の要素を取得

</v-click>

<v-click at="3">

**要素の置き換え**

- `replace-item (番号) (リスト) (値)` で指定位置の要素を更新

</v-click>

::right::

```text {|1-3|5-7|9-11}
; リストの作成
set y (list 1 2 3)
; => [1 2 3]

; 要素の取り出し
let first-item item 0 y
; => 1

; 要素の置き換え
set y replace-item 0 y 99
; => [99 2 3]
```


---
transition: fade-out
layout: two-cols-title
---

::title::
# ask 文

エージェントへの命令を定義する

::left::

<v-click at="1">

**turtle への命令**
- `turtles` — 現在存在する全ての turtle
- `turtle (番号)` — 指定した ID の turtle のみ

</v-click>

<v-click at="2">

**patch への命令**
- `patches` — 全ての patch
- `patch (x) (y)` — 指定した座標の patch のみ

</v-click>

<v-click at="3">

**link への命令**
- `links` — 全ての link
- `link (n1) (n2)` — 指定した2つの turtle 間の link のみ

</v-click>



::right::

```text {|1-6|8-12|14-19}
; turtle への命令
ask turtles [
  fd 1                   ; 1歩前進
  set color red          ; 色を赤に変更
]
ask turtle 4 [ rt 90 ]  ; id=4 の turtle のみ右折

; patch への命令
ask patches [
  set pcolor scale-color green fertility 0 10
                         ; fertility の値で緑の濃淡を設定
]
ask patch 0 0 [ set pcolor white ]  ; 原点の patch のみ白

; link への命令
ask links [
  set color gray         ; 全 link をグレーに
  set thickness 0.5      ; 太さを設定
]
ask link 0 1 [ set color red ]  ; turtle 0-1 間の link のみ赤
```


---
layout: two-cols-title
---

::title::
# 制御構文

::left::

<v-click at="1">

**if 文**

条件が真のときだけブロックを実行する

</v-click>

<v-click at="2">

**ifelse 文**

条件が真のときと偽のときで異なるブロックを実行する

</v-click>

<v-click at="3">

**while 文**

条件が真の場合、ブロックを繰り返し実行する

</v-click>

<Admonition title="ブロック [ ] とは" color="teal-light" width="400px">

`[ ]` で囲まれた部分が**ブロック**です。条件が成立したときに実行する命令をまとめて記述します。

</Admonition>

::right::


```text {|1-5|7-13|15-20}
ask turtles [
  if xcor > 0 [
    set color red
  ]
]

ask patches [
  ifelse pxcor > 0 [
    set pcolor blue
  ][
    set pcolor red
  ]
]

ask turtle 0 [
  while [any? other turtles-here][
    right random 360
    fd 1
  ]
]
```

---
layout: two-cols-title
---

::title::
# 制御構文

::left::

<v-click at="1">

**repeat 文**

指定した回数だけブロックを繰り返し実行する

</v-click>

<v-click at="2">

**foreach 文**

リストの各要素に対してブロックを順番に実行する

</v-click>

<v-click at="3">

**loop 文**

`stop` が呼ばれるまで無限にブロックを繰り返す

</v-click>




::right::

```text {|1-3|5-12|14-22}
ask turtle 0 [
  repeat 10 [fd 1]
]

set tlist (list turtle 0 turtle 1)
foreach tlist [
  x -> ask x [
    right random 360
    fd 1
  ]
]

loop [
  ask turtle 0 [
    if any? other turtles-here [
      right random 360
      fd 1
      stop
    ]
  ]
]
```

---
layout: two-cols-title
---

::title::
# procedureについて


> 他のプログラミング言語の「関数」に相当
::left::

<v-click at="1">

**`to`〜`end`：通常の procedure**

- 名前をつけた命令のまとまり
- `to 名前` で定義し、名前を書くだけで呼び出す

</v-click>

<v-click at="2">

**`to-report`〜`end`：戻り値がある procedure**

- 計算結果を返したいときに使う
- `report` で値を返す

</v-click>

<v-click at="3">

**引数をとる procedure**

- 名前の後ろに `[ 引数名 ]` を書く

</v-click>

::right::

```text {|1-7|9-14|16-20}
; 通常の procedure
to move-turtle
  right random 360
  fd 1
end

ask turtles [ move-turtle ]

; 戻り値がある procedure
to-report double [ x ]
  report x * 2
end

set y double 5  ; y = 10

; 引数をとる procedure
to color-turtle [ c ]
  set color c
end

ask turtles [ color-turtle red ]
```

---
layout: two-cols-title
---

::title::
# Netlogoで囚人的ジレンマモデルの実装

::left::

<v-click at="1">

- **変数の定義**

</v-click>

<v-click at="2">

- **エージェントの設定**
  - `create-turtles` でエージェントを生成・初期化

</v-click>

<v-click at="3">

- **手続きの定義**
  - `to`〜`end` で処理をまとめた手続きを定義
  - `setup` で初期化，`answer` でゲームを実行

</v-click>

<v-click at="4">

- **演算・論理演算子**

</v-click>

<v-click at="5">

- **制御構文**
  - `ifelse` で条件分岐し，パートナーの行動・自分の選択に応じて結果を切り替える

</v-click>

::right::

```ts {|1,13,18,19|6-7,10,33,36,44,47|3-21,24-51|6,17|12-19,29-51}{maxHeight:'550px'}
globals [partner-is-silent?]

to setup
  clear-all
  ;;Build the jail cell
  ask patches with [ count neighbors != 8 ] [
    set pcolor gray]

  ;;make the face visible
  create-turtles 1 [set color gray set size 30 set shape "face"]
  ;; set up the prisoner's dilemma
  ifelse partner-silence-known? [
    set partner-is-silent? partner-silent?
  ]
  [
    ;;if partner silence is not known, choose randomly whether or not he is silent.
    ifelse random 2 = 0
    [ set partner-is-silent? true ]
    [ set partner-is-silent? false ]
  ]
end

;;play the game, changing the face depending on the outcome.
to answer
  setup  ;;clears variables away so that setup doesn't need to be pressed every time.

  ;;next the four possible combinations of choices are dealt with.
  ;;the result corresponds to the tables in the interface and Info tabs.
  ;;first check to see if your partner was silent.
  ifelse partner-is-silent? [
      ;;now go through your two possible choices
      ifelse you-silent? [
      ask turtles [set shape "face silent"]
      user-message "You and your partner both remain silent.  You are sentenced to one year imprisonment."
    ] [
      ask turtles [set shape "face devious"]
      user-message "You confess and your partner remains silent. You go free."
    ]
  ]
  ;;your partner confessed.
  [
    ;;again go through your two possible choices
    ifelse you-silent? [
      ask turtles [set shape "face sucker" ]
      user-message "You remain silent, but your partner confesses.  You are sentenced to five years imprisonment."
    ] [
      ask turtles [set shape "face rational"]
      user-message "You and you partner both confess.  You are sentenced to three years imprisonment."
    ]
  ]
end
```


---

# よく使う命令

**エージェントの生成**

| 命令 | 説明 |
|------|------|
| `create-turtles (数値)` | 指定数の turtle を作成 |
| `hatch` | turtle から新しい turtle を生み出す（親の変数値を受け継ぐ） |

**乱数**

| 命令 | 説明 |
|------|------|
| `random (数値)` | 0 以上・指定値未満の整数をランダムに返す |
| `random-float (数値)` | 0 以上・指定値未満のランダムな浮動小数点数を返す |



---

# よく使う命令


**エージェント集合の操作**

| 命令 | 説明 |
|------|------|
| `any?` | エージェント集合が空でなければ `true` を返す |
| `with` | 条件を満たすエージェントだけを返す |
| `of` | エージェントが持つ変数の値を返す：`[pcolor] of patch 3 5` |
| `one-of` | エージェント集合からランダムに1つ返す |
| `max-one-of` | 変数が最大のエージェントを1つ返す |
| `min-one-of` | 変数が最小のエージェントを1つ返す |
| `other` | 自分自身を除いたエージェント集合を返す |


---

# よく使う命令

**patchに対する操作**

| 命令 | 説明 |
|------|------|
| `neighbors4` | ノイマン近傍の4つの patch を返す |
| `neighbors` | ムーア近傍の8つの patch を返す |
| `in-radius (数値)` | 指定距離以下にある patch（または turtle）の集合を返す |
| `patch-here` | turtle がいる patch を返す |
| `patch-at (dx) (dy)` | 対象の turtle から見て相対座標 (dx, dy) の位置にある patch を返す |


---

# インターフェース画面での変数の設定（スライダー）

<div class="p-4 border-2 border-dashed border-gray-400 rounded bg-gray-50 text-gray-500 text-sm text-center mb-4">
  【画像プレースホルダー】スライドB.15 — スライダーの作成方法とダイアログボックスのスクリーンショット
</div>

- 上部の「ボタン」→「スライダー」を選択し，好きな場所でクリックして作成
- グローバル変数名・最小値・最大値などを入力して設定
- ソースコードを編集せずに，シミュレーション実行時に変数を変更できる
- チューザー（chooser）やインプットボックスも同様に作成可能

---

# グラフの描画

<div class="p-4 border-2 border-dashed border-gray-400 rounded bg-gray-50 text-gray-500 text-sm text-center mb-4">
  【画像プレースホルダー】スライドB.16 — グラフの作成ダイアログとリアルタイムグラフの例のスクリーンショット
</div>

**作成の仕方**
1. 「プロット」を選択し，インターフェース画面に配置
2. ダイアログでグラフの名前・軸のラベルを入力
3. **プロットペン**：何の値をプロットするかのコマンドを記述（例：`plot count turtles`）
4. OK を押す

実行すればリアルタイムにグラフが表示される

---

# コマンドセンター

<div class="p-4 border-2 border-dashed border-gray-400 rounded bg-gray-50 text-gray-500 text-sm text-center mb-4">
  【画像プレースホルダー】スライドB.17 — コマンドセンターのスクリーンショット
</div>

- インターフェース画面の**下部**にある入力欄
- コマンドを直接入力して，エージェントに命令を送ることができる

```text
ask patches [set pcolor green]
```

全ての patch を緑色に変更できる（シミュレーション実行中でも可能）

- `observer>` の部分をクリックすれば，`patches` / `turtles` / `links` を選択可能
- turtle を右クリック → `inspect turtle (番号)` でも個別のコマンドセンターが利用可能

---
layout: center
class: text-center
---

# まとめ

1. ABMのためのソフトウェアツール
2. NetLogoとは
3. NetLogoの基本構成（画面・動作の仕組み）
4. NetLogo世界の基本要素（turtle・patch・link・observer）
5. 変数の定義と代入
6. ask 文とエージェント集合
7. 基本的な構文（if / ifelse / while / repeat / foreach）
8. procedure の定義
9. よく使う命令
10. インターフェースの活用（スライダー・グラフ・コマンドセンター）


<style>
.toc { display: none !important; }
</style>