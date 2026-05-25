globals [
  percent-similar  ; 各turtleの隣人のうち、同じ色の割合（平均）
  percent-unhappy  ; 不満を持つturtleの割合
]

turtles-own [
  happy?           ; 同じ色の隣人が %-similar-wanted 以上いれば true
  similar-nearby   ; 隣接パッチにいる同じ色のturtleの数
  other-nearby     ; 隣接パッチにいる異なる色のturtleの数
  total-nearby     ; 隣接パッチにいるturtleの総数
]

to setup
  clear-all
  ; 各パッチにランダムでturtleを配置する
  ask patches [
    ; すべてのパッチを白（空き地）で初期化する
    set pcolor white
    ; 0〜99 の乱数が density 未満なら、そのパッチにturtleを1体生成する
    ; density = 70 なら約70%のパッチが占有される
    if random 100 < density [
      sprout 1 [
        ; 青（105）またはオレンジ（27）をランダムに割り当て、2グループを表現する
        set color one-of [105 27]
        set size 1
      ]
    ]
  ]
  ; 初期配置に基づいて各turtleの満足度と隣人カウントを計算する
  update-turtles
  ; percent-similar と percent-unhappy の初期値を算出する
  update-globals
  ; ティックカウンターを0にリセットしてシミュレーション開始に備える
  reset-ticks
end

; 1ステップ進める：全turtleが満足したらシミュレーションを停止する
to go
  ; 全turtleが happy? = true になったら終了（収束条件）
  if all? turtles [ happy? ] [ stop ]
  ; 不満なturtleを空きパッチへ移動させる
  move-unhappy-turtles
  ; 移動後、各turtleの満足度と隣人カウントを再計算する
  update-turtles
  ; 集計指標（percent-similar, percent-unhappy）を更新する
  update-globals
  tick
end

; 不満なturtleを別の場所へ移動させる
to move-unhappy-turtles
  ; happy? = false のturtleだけを対象に find-new-spot を実行する
  ; 満足しているturtleはその場にとどまる
  ask turtles with [ not happy? ]
    [ find-new-spot ]
end

; 空きパッチが見つかるまでランダムに移動する
to find-new-spot
  rt random-float 360  ; rt（right turn）: 0〜360度のランダムな方向に向きを変える
  fd random-float 10   ; fd（forward）: 0〜10パッチ分ランダムに前進する
  if any? other turtles-here [ find-new-spot ] ; 他のturtleがいれば再試行
  move-to patch-here  ; パッチの中央に移動
end

to update-turtles
  ask turtles [
    ; neighbors は周囲8パッチを指す組み込み変数
    ; myself で「この ask を実行しているturtle自身」の色を参照する
    set similar-nearby count (turtles-on neighbors) with [ color = [ color ] of myself ]
    set other-nearby count (turtles-on neighbors) with [ color != [ color ] of myself ]
    ; 隣接turtleの総数（空きパッチは含まない）
    set total-nearby similar-nearby + other-nearby
    ; 同色の割合が %-similar-wanted 以上なら満足（happy? = true）
    ; 例: %-similar-wanted = 30 のとき、隣人の30%以上が同色なら満足
    set happy? similar-nearby >= (%-similar-wanted * total-nearby / 100)
    ; "old" モード: デフォルト形状で表示
    if visualization = "old" [ set shape "default" set size 1.3 ]
    ; "square-x" モード: 満足なturtleは四角、不満なturtleはXで表示
    if visualization = "square-x" [
      ifelse happy? [ set shape "square" ] [ set shape "X" ]
    ]
  ]
end

to update-globals
  ; 全turtleの similar-nearby を合計（モデル全体の同色隣人数）
  let similar-neighbors sum [ similar-nearby ] of turtles
  ; 全turtleの total-nearby を合計（モデル全体の隣人数）
  let total-neighbors sum [ total-nearby ] of turtles
  ; 同色隣人の割合をパーセントで算出（グラフ表示用グローバル変数に格納）
  set percent-similar (similar-neighbors / total-neighbors) * 100
  ; 不満なturtleの割合をパーセントで算出
  set percent-unhappy (count turtles with [ not happy? ]) / (count turtles) * 100
end

