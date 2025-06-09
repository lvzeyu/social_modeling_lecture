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

- Agent based model(ABM)
    - 個々の自律的な「エージェント」が、ルールに従って行動し、他のエージェントや環境と相互作用することにより、マクロな現象を創発的に再現・分析するモデル
- ネットワークモデル
    - 現実世界の複雑な関係構造や相互作用をノード（点）とリンク（辺）に基づいて表現・分析する枠組み

</v-clicks>

<div style="margin-top: 5em;"></div>


<p v-click style="color: #3E1586; font-size: 1.5em; text-align: center;">
  ネットワークモデルとABMの組み合わせによる<br/><br/>複雑現象のシミュレーションと解析
</p>

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

# 振り返りとこれからの内容

ABMの要素

<div grid="~ cols-2 gap-4 items-start">

<div>

<v-clicks depth="2">

- エージェント (Agents)
- 相互作用 (Interactions)
- 環境 (Environment)
    - グリッドベース (Grid-based): 離散的なセル（マス目）で構成される空間
    - **ネットワーク (Network)**
        - ノードとリンクで構成される空間: エージェントがノード上に存在し、リンクを介して相互作用をする
        - ネットワークの構造がエージェントの振る舞いを制約する場合がある

</v-clicks>


</div>

<div class="flex justify-center">
  <img src="./image/abm_component.png" alt="ネットワーク図" width="350" />
</div>

</div>

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

# 振り返りとこれからの内容

ABMの要素

<div grid="~ cols-2 gap-4 items-start">

<div>

<v-clicks depth="2">

- **関係性の明示的表現**:物理的な位置関係だけでなく、抽象的な関係性をノード間のリンクとして直接的にモデル化できる
- **多様な構造**: 規則的なものから、ランダム、スモールワールド、スケールフリーといった現実世界によく見られる複雑な構造まで、様々な構造を表現できる
- **動的な変化の表現**:エージェントの行動変化に応じて、リンクが生成・削除される動的な環境として機能することは可能である

</v-clicks>


</div>

<div class="flex justify-center">
  <img src="./image/abm_env.png" alt="ネットワーク図" width="600" />
</div>

</div>

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

# 振り返りとこれからの内容

ネットワーク

<div class="flex justify-center">
  <img src="./image/network_types.png" alt="ネットワーク図" width="600" />
</div>

<v-clicks depth="2">

- ネットワークの構造は、ネットワークにおけるシミュレーションの過程と結果に大きな影響を与える

    - 構造的影響の特定:特定のネットワーク構造（例：ハブの有無、クラスタリングの度合い、平均経路長）が、シミュレーションで観察される現象 にどのように影響するかを明確
    - クリティカルな要素の特定: ある種のネットワーク構造では顕著に現れるが、別の構造ではそうでない現象を特定することで、その現象を引き起こすためにどのような構造的要素が必要なのかを明らかにする
    - 異なる状況下での性能評価

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

# 意見ダイナミクス

背景

<v-clicks depth="2">

- **意見ダイナミクス**に関するシミュレーション：社会における意見の形成と拡散を決定するプロセス
    - 意見形成メカニズムの解明
        - どのような要因（個人の信念、他者の影響、情報の質、ネットワーク構造など）が人々の意見形成に影響を与えるのか
    - 分極化・合意の条件の検証
        - 異なる意見を持つ人々がどのようにして対立を深めるのか、またその対立を緩和するためにはどのような介入が有効なのか
    - 政策介入の評価
        - 特定の情報が社会全体にどのような影響を与えるかを事前に評価する「What-if」シナリオ分析 

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

# 意見ダイナミクスのシミュレーション

意見ダイナミクスのシミュレーションの概要

<v-clicks depth="2">

- 初期状態として、ネットワークのノードに意見をランダムに割り当てる。
    - 基本的には、初期状態ではどちらの意見を持つ人はそれぞれ存在している（非合意の状態）

- 意見の更新ルールは、すべてのノードに対して繰り返し適用される。
    - 一回の反複で、すべてのノードに対してループを実行する
    - 通常、収束しやすいように、ノードはランダムな順序で非同期更新される
- 考えられる結果は2種類と考える
    - システムは定常状態に達し、どのノードもそれ以上意見を変更しなくなる。
        - すべてのノードが同じ意見を持つ合意
        - 一部のノードが一方の意見をもち、残りのノードがもう一方の意見を持つ分極化
    - システムは定常状態にいらず、一部のノードは意見を変え続ける
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

# 意見ダイナミクス

モデルの種類

- 連続的な意見

<div class="flex justify-center">
  <img src="./image/continuous.png" alt="ネットワーク図" width="400" />
</div>

<div grid="~ cols-2 gap-4 items-start">

<div>


- 離散的な意見　
    - 二値選択
        - 例：賛成／反対、はい／いいえ
    - 複数段階のリッカート尺度
        - 例：「まったくそう思わない」〜「非常にそう思う」までの5段階や7段階


</div>

<div class="flex justify-center">
  <img src="./image/discrete.png" alt="ネットワーク図" width="600" />
</div>

</div>


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

# 意見ダイナミクスのシミュレーション

意見ダイナミクスのシミュレーションの指標

<v-clicks depth="2">

- 平均的意見：ノード全体の意見の平均
    - 平均的意見はダイナミクスを通じて変化していく、各反複の後にその値を確認する
    - システムが定常状態に達した場合、平均値はある値に収束する
- 離脱確率:ネットワークにおいて意見$1$で合意に達する頻度を、初期設定における意見$1$を持つノードの割合の関数として推定する
    - シミュレーションを複数回実行し、各実行の終わりに、システムが「意見1での合意状態」に達したかどうかを判定する
    - 各初期意見1比率において、意見1で合意に達したシミュレーション実行の回数を、その初期意見1比率での総実行回数で割ることで、離脱確率を算出する
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

# 意見ダイナミクスの発想

Ising model

<div grid="~ cols-2 gap-4 items-start">

<div>

<v-clicks depth="2">

- イジングモデル (Ising model) は、統計力学において、特に磁性体の性質を記述するモデル
    - 隣接スピン間の相互作用: 隣り合ったスピンは、同じ向きを向こうとするとエネルギー的に安定し、異なる向きを向くとエネルギー的に不安定になるという相互作用を持つ

- スピンを個々の人や集団、その相互作用が社会全体の振る舞いを決定するという発想で意見ダイナミクスをモデル化
    - 各個人は、自身の周囲の意見や外部からの情報（=外部磁場）を考慮し、自身の意見を修正する
</v-clicks>

</div>
<div class="flex flex-col items-center">
  <img src="./image/ising_model.png" alt="ネットワーク図" width="400" />
  <p class="mt-2 text-sm text-gray-600 text-center leading-snug">
      格子状に並んだスピンと呼ばれる要素から構成される。<br/>
      各スピンは、上向き (+1) または下向き (-1) のどちらか2つの状態しか取らない
    </p>
</div>

</div>



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

# 多数派モデル(Majority model)


概要

<div grid="~ cols-2 gap-4 items-start">

<div>

<v-clicks depth="2">

- 個人（エージェント）の意見が、局所的なグループにおける多数派の意見に従って更新される
    - 各エージェント $i$ は二値意見（例：$+1$ or $-1$）を持つ
    - 毎ステップ、ネットワーク上隣接するノードの意見を確認
    - 多数派意見（$+1$ または $-1$）を採用する
       - 同数の場合は、ランダムでどちらの意見を採用する
</v-clicks>

</div>
<div class="flex flex-col items-center">
  <img src="./image/majority.png" alt="ネットワーク図" width="400" />
  <p class="mt-2 text-sm text-gray-600 text-center leading-snug">
      大きなノード（更新対象）は、現在「意見1（赤）」を持っている。<br/>
      このノードの5つの隣接ノードにおける、3つのノードは「意見1（赤）」、つのノードは「意見0（青）」であるため、<br/>
      意見を変更せずにそのまま 「意見1（赤）」を保持する
    </p>
</div>

</div>

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

# 多数派モデル(Majority model)


意見ダイナミクスの考察

<v-clicks depth="2">

- 格子構造では合意に達しやすい
    - エージェントは局所的（近傍）にしか相互作用しないため、同じ意見が拡大しやすい
- 多くのネットワーク構造において、多数派ルールに基づく意見ダイナミクスは、単一の意見への合意に至るのではなく、異なる意見が長期的に共存する定常状態に収束する
    - 非局所的リンクの存在 
        - スケールフリーや小世界ネットワークでは、遠く離れたノード間にもリンクがあるため、局所的な意見が一貫して拡張できなくなる 
        - 意見の「境界」が簡単に乱され、一方向的に収束する過程が阻害される
    - ノード次数の非均質性
        - 極端に多くのリンクを持つハブノードが存在し、意見拡散に大きな影響力を持つ
        - 複数のハブが異なる意見を持っているとき、それぞれの周辺で安定した意見ドメインが形成され、意見の統一が阻害される
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

# Voter Model

概要

<div grid="~ cols-2 gap-4 items-start">

<div>

- 個人（エージェント）はランダムに選ばれた隣接ノードの意見を採用する
    - 各エージェント $i$ は二値意見（例：$+1$ or $-1$）を持つ
    - 毎ステップ、エージェントが、ランダムに選択された隣接エージェントの意見を採用する

</div>

<div class="flex justify-center">
  <img src="./image/voter.png" alt="ネットワーク図" width="600" />
</div>

</div>




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

# Voter Model

意見ダイナミクスの考察

<div>

- ネットワークにおける、Voterモデルの唯一の定常状態は合意である
    - 十分に長い時間が経過すると、すべてのエージェントが同じ意見（すべて +1 あるいはすべて −1）を持つ状態に必ず到達する
    - 多数派の意見の拡大と少数派の消滅
        - ある意見が多数派である場合、その意見を持つエージェントが隣接するエージェントを模倣させる機会が多くになり、多数派の意見はさらに多くのエージェントに伝播し、拡大していく
        - 少数派の意見を持つエージェントは、周囲に多数派の意見を持つエージェントが多い状況に置かれやすく、自身の意見を変える可能性が高い

</div>





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