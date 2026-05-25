; 各エージェントは「参加の閾値」を持ち、
; 周囲の参加者割合が閾値を超えると自分も参加する
; エージェント固有の変数定義
; threshold: イベントに参加するために必要な周囲の参加者割合（0〜100）
; riot?: 現在イベントに参加しているかどうかのフラグ
turtles-own [threshold riot?]

to setup
  ca
  set-default-shape turtles "circle"
  ; 最小閾値が最大閾値より大きい場合はエラーを表示して停止
  if max-threshold < min-threshold [
    print "min-threshold should be smaller than max-threshold"
    stop
  ]
  create-agents
  reset-ticks
end

to go
  ; 前ステップの参加者数を記録（収束判定のため）
  let prev-rioting count turtles with [riot? = true]
  ask turtles [
    ; 隣接エージェントのうちイベント参加者の割合を計算（%）
    let prop-rioting 100 * count link-neighbors with [riot? = true] / count link-neighbors
    ; 割合が自身の閾値以上になればイベントに参加する
    if prop-rioting >= threshold [
      set riot? true
      set color red  ; 参加者は赤色で表示
    ]
  ]
  ; 新しい参加者がいなければ収束とみなして停止（tick不進行）
  if count turtles with [riot? = true] = prev-rioting [stop]
  tick
end

to create-agents

  ; 閾値のパーセント値をエージェント数に対する絶対値に変換
  let min-threshold-n min-threshold * number-of-agents / 100
  let max-threshold-n max-threshold * number-of-agents / 100
  let mean-threshold-n mean-threshold * number-of-agents / 100
  let sd-threshold-n sd-threshold * number-of-agents / 100

  crt number-of-agents [
    set riot? false       ; 初期状態：イベント不参加
    set color blue        ; 非参加者は青色で表示
    ; 閾値分布の設定：一様分布または正規分布から閾値を割り当てる
    if threshold-distribution = "uniform" [set threshold (min-threshold + random (max-threshold - min-threshold))]
    if threshold-distribution = "normal" [set threshold round (random-normal mean-threshold sd-threshold)]
    ; 閾値を0〜100の範囲に制限する
    if threshold < 0 [set threshold 0]
    if threshold > 100 [set threshold 100]
  ]

  ;layout-circle (sort turtles) (max-pxcor - 1)
  arrange-turtles  ; エージェントを円形に配置

  ; ランダムネットワーク：各エージェントがランダムに number-of-links 本のリンクを持つ
  if network = "random" [
    ask turtles [create-links-with n-of number-of-links other turtles with [link-with myself = nobody]]
  ]

  ; スモールワールドネットワーク（Watts-Strogatz モデル）
  if network = "small-world" [
    let max-who 1 + max [who] of turtles
    let sorted sort ([who] of turtles)
    ; まず隣接エージェントと規則的にリンクを張る
    foreach sorted[ [?1] ->
      ask turtle ?1 [
        let i 1
        repeat number-of-links [
          create-link-with turtle ((?1 + i) mod max-who)
          set i i + 1
        ]
      ]
    ]
    ; rewire-prop の割合でリンクをランダムに再配線する
    repeat round (rewire-prop * number-of-agents) [
      ask one-of turtles [
        ask one-of my-links [die]
        create-link-with one-of other turtles with [link-with myself = nobody]
      ]
    ]
  ]

  ; 完全連結ネットワーク：全エージェント間にリンクを張る
  if network = "fully connected" [
    ask turtles [create-links-with other turtles with [link-with myself = nobody]]
  ]

end

; エージェントを円形に等間隔で配置する（layout-circle の代替実装）
to arrange-turtles
  let the-turtles sort [who] of turtles
  let angle 360 / number-of-agents  ; エージェント間の角度間隔
  let dist max-pxcor - 1            ; 円の半径
  let i 0
  foreach the-turtles [ [?1] ->
    ask turtle ?1 [
      ; 極座標から直交座標へ変換して配置
      setxy (dist * cos (angle * i)) (dist * sin (angle * i))
    ]
    set i i + 1
  ]
end

; BehaviorSpace用レポーター：参加者の最終割合（%）を返す
to-report final-proportion
  report 100 * count turtles with [riot? = true] / count turtles
end
