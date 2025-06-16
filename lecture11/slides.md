---
# You can also start simply with 'default'
theme: seriph
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

---

## 行動科学概論
 
# 社会科学におけるモデル入門


意見ダイナミクス 

### 呂沢宇

<div @click="$slidev.nav.next" class="mt-12 py-1" hover:bg="white op-10">
  Press Space for next page <carbon:arrow-right />
</div>

<div class="abs-br m-6 text-xl">

  <a href="https://github.com/lvzeyu/social_modeling_lecture" target="_blank" class="slidev-icon-btn">
    <carbon:logo-github />
  </a>
</div>

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
transition: slide-up
level: 2
---
# 振り返りとこれからの内容


<v-clicks depth="2">

- ABMとネットワークを組み合わせることによる意見ダイナミクスのシミュレーション
    - Majority Model
    - Voter Model
    - →　離散的意見を想定する意見ダイナミクスモデル　
- 連続的意見を想定する意見ダイナミクスモデル
    - 個人の意見は、さまざまな選択肢の中から極端なものからそうでないものまでなめらかに変化する状態がある。
       - 政治的立場を、非常に革新的($-1$)から非常に保守的($+1$)までの範囲でモデル化する
</v-clicks>

<style>
h1 {
  background-color: #3E1586;
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>


---
transition: slide-up
level: 2
---
# 連続的意見に関する意見ダイナミクスモデル

意見ダイナミクスシミュレーションの流れ

<v-clicks depth="2">

- 初期状態においてはネットワークの各ノードに無作為に意見が割り当てられる
- 意見の値は、特定なルールに従って更新されるにつれて変化する
- ある時点で、どの意見の最大変動も事前に規定された閾値より小さくなれば、システムは最終的に定常状態に到達し、シミュレーションを停止することができる
    - 典型的な定常状態が二極化か断片化である
</v-clicks>

<style>
h1 {
  background-color: #3E1586;
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>


---
transition: slide-up
level: 2
---
# 限定信頼モデル(Bounded-confidence model)

概要

<v-clicks depth="2">

- **基本設定**: あるトピックについての議論を行い、特にお互いの立場が近い場合には、相手の意見に影響を与える可能性がある
    - もし相手が正反対反対の意見を持っている場合、その相手を説得することは難しい

- **限定信頼の原理**：ある二つの意見は、その差が信頼限界または許容度と呼ばれる量より小さい場合にのみ。互い影響し合う。
    - あるノードとその隣接ノードを一つずつ選択する
    - もし両者の意見の差が信頼限界よりも小さければ、収束パラメータによって決定される相対量の分だけ、両者のお互いの方向に向かって「動く」
        - それ以外の場合には、意見は変化しない
</v-clicks>

<style>
h1 {
  background-color: #3E1586;
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>


---
transition: slide-up
level: 2
---
# 限定信頼モデル(Bounded-confidence model)

Deffuant-Weisbuch (DW) モデル

<v-clicks depth="2">

- ランダムに選ばれた2つのエージェント $i$ と $j$ の意見 $x_i(t)$ と $x_j(t)$ が、$t$ 時刻から $t+1$ 時刻へ更新される
  - もし $|x_i(t) - x_j(t)| < \epsilon$ であれば、意見は更新される
      - $$x_i(t+1) = x_i(t) + \mu (x_j(t) - x_i(t))$$
      - $$x_j(t+1) = x_j(t) + \mu (x_i(t) - x_j(t))$$
  - もし $|x_i(t) - x_j(t)| \ge \epsilon$ であれば、意見は変化しない
      - $$x_i(t+1) = x_i(t)$$
      - $$x_j(t+1) = x_j(t)$$
  - $\epsilon$ は信頼限界（許容度）
  - $\mu$ は収束パラメータ（妥協度）
</v-clicks>

<style>
h1 {
  background-color: #3E1586;
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>


---
transition: slide-up
level: 2
---
# 限定信頼モデル(Bounded-confidence model)

Deffuant-Weisbuch (DW) モデル

$$|x_i(t) - x_j(t)| < \epsilon$$

<v-clicks depth="2">

- $\epsilon$が、どの程度意見の異なる相手までなら、その意見を受け入れ、相互作用を通じて自分の意見を変化させるかを制御する
- $\epsilon$ が小さい場合: 自分とほとんど同じ意見を持つ相手としか相互作用し
    - 多数の非常に小さな意見のクラスターに分断する
- $\epsilon$ が大きい場合: 自分とかなり異なる意見を持つ相手でも、積極的に受け入れて相互作用する
    - 社会全体の意見は最終的に一つの意見に収束しやすい
    - (意見の範囲が$[0,1]である$)$\epsilon>0.5$の時、どのようなネットワークにおいても意見はならず$0.5$の周りに集中し、合意に達する
        - 最も離れた意見を持つエージェント同士ですら、最終的には相互作用の連鎖を通じてつながり、お互い影響を与え合うことができる

</v-clicks>


<style>
h1 {
  background-color: #3E1586;
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>




---
transition: slide-up
level: 2
---
# 限定信頼モデル(Bounded-confidence model)

Deffuant-Weisbuch (DW) モデル

$$x_i(t+1) = x_i(t) + \mu (x_j(t) - x_i(t))$$

<v-clicks depth="2">

- $\mu$ は意見変化の「速さ」と「度合い」を決定する
- $\mu=1$の時、相互作用した2つのエージェントの意見が完全に相手の意見に入れ替わる
    - モデルの挙動は非常に極端なものになる
- 通常、$\mu$ は $0 < \mu \le 0.5$ の範囲で設定される
    - $\mu$ が小さい場合 
        - 各エージェントは、相手の意見に対してわずかしか歩み寄りません
        - 意見の収束にはより多くの時間がかかる
    - $\mu$ が大きい場合
        - 各エージェントは、相手の意見に対して積極的に歩み寄り
        - $\mu = 0.5$ の場合は、相互作用した2つのエージェントの意見は完全に平均値に収束し、両者ともに中間的な立場を取る
</v-clicks>


<style>
h1 {
  background-color: #3E1586;
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>


---
transition: slide-up
level: 2
---
# 限定信頼モデル(Bounded-confidence model)

Hegselmann-Krause (HK) モデル


<v-clicks depth="2">

- 「自分と似た意見を持つグループの平均に合わせる」という行動をモデル化

- エージェント $i$ が相互作用の対象とするエージェントの集合 $N_i(t)$ を定義する
    - $$N_i(t) = \{ j \mid |x_i(t) - x_j(t)| < \epsilon \}$$
- エージェント $i$ の意見は、この集合内のエージェントの意見の平均に更新される
    - $$x_i(t+1) = \frac{1}{|N_i(t)|} \sum_{j \in N_i(t)} x_j(t)$$

- 各タイムステップで、全てのエージェントが同時に自分の意見を更新する
    - DWモデルはランダムにペアを選ぶ
</v-clicks>


<style>
h1 {
  background-color: #3E1586;
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>


---
transition: slide-up
level: 2
---
# 限定信頼モデル(Bounded-confidence model)

HKモデルとDWモデル


<v-clicks depth="2">

- 意見クラスターの形成
    - HKモデルには、より明確で、分離したクラスターに収束する
    - DWモデルでは、ランダムなペア選択と逐次的な更新のため、より小さな意見クラスターが形成される傾向がある
- 収束速度
    - HKモデルでは、全てのエージェントが同時に意見を更新するため、意見の収束は比較的速い
    - DWモデルでは、ンダムなペア選択と逐次的な更新のため、意見の収束はHKモデルよりも時間がかかる
</v-clicks>


<style>
h1 {
  background-color: #3E1586;
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>