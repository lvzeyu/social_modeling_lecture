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


ネットワークモデル

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

- ネットワークの基本概念
    - ノートとリンクによる複雑な対象を比較的に単純な構造で表現する
    - 次数、最短経路長、クラスター係数などの指標でネットワークの特徴を理解する
- ネットワークモデル
    - ネットワークの特徴がどのように現れるかについての直感や仮説を取り込んでモデルを構築し、そのモデルに従って構築されたネットワークと現実のネットワークを比較することで、何かモデルによって再現できて、何か再現出来ないにかを確認する
        - ネットワークモデルによって現実世界のネットワークがどのようなメカニズムで成り立っているのかについての知見を得ることができる
    - WSモデル: 適切なランダム性$p$を設定することで、短い最短経路長と大きいクラスター係数という二つ望ましい特徴を持つネットワークを生成することが可能である
    - **Barabasi-Albertモデル：スケールフリーな構造を再現するためのモデル**

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

# Power Laws

現実世界におけるPower Laws

Power Laws（べき乗則）とは、ある量の分布が「一部の巨大な値が稀に存在し、大多数は小さな値に集中する」という特性を持つことである
<div grid="~ cols-2 gap-4 items-start">

<div>

<div class="flex justify-center">
  <img src="./image/power_law_wealth.png" alt="ネットワーク図" width="800" />
</div>


</div>

<div class="flex justify-center">
  <img src="./image/power_law_university.png" alt="ネットワーク図" width="800" />
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

# Power Laws

現実世界におけるPower Laws

スケールフリーネットワーク(Scale-free Network)：ノードの次数分布（1つのノードが持つリンク数）がPower Lawsに従うネットワーク
<div grid="~ cols-2 gap-4 items-start">

<div>

<div class="flex justify-center">
  <img src="./image/power_transportation.png" alt="ネットワーク図" width="800" />
</div>


</div>

<div class="flex justify-center">
  <img src="./image/power_law_social_media.png" alt="ネットワーク図" width="800" />
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

# 次数分布に着目するネットワークモデル

Configuration Model

ある次数分布が与えられたとき、その次数分布と同じ次数分布を持つネットワークをどのように構築する❓

<div grid="~ cols-2 gap-4 items-start">

<div>

<v-clicks depth="2">

- Configuration Network
    - (a) 各ノードに対して、ノードの次数に対応する数のスタブを割り当てる
        - スタブとは、そのノードを端点とし、まだ接続されていないぶら下がったリンクのことである
    - スタブのペアをランダムに選択し、スタブ同士の結合によるノード間にリンクを引く
    - 全てのスタブがペアを作り、結合されるまでに手順を繰り返す

</v-clicks>


</div>

<div class="flex justify-center">
  <img src="./image/configuration_network.png" alt="ネットワーク図" width="350" />
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

# 次数分布に着目するネットワークモデル

Configuration Model

ある次数分布が与えられたとき、その次数分布と同じ次数分布を持つネットワークをどのように構築する❓

<div grid="~ cols-2 gap-4 items-start">

<div>

<v-clicks depth="2">

- 各ノードに接続されたスタブの数はそのノードの次数に等しいので、各ノードは最終的に望ましい次数を持つことになる
    - 二つのノード間に複数のリンクがあるネットワーク(c)まらは自己ループがあるネットワーク(d)を生成する可能性もあるので、場合による制御する必要がある

</v-clicks>


</div>

<div class="flex justify-center">
  <img src="./image/configuration_network.png" alt="ネットワーク図" width="350" />
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

# 次数分布に着目するネットワークモデル

既存モデルに対する考察


<v-clicks depth="2">

- 今までは基本的に静的ネットワークモデルであった
    - ネットワークの全てのノードは最初から存在し、それらのノード間のリンクを追加したり張り替えたりして、ネットワークを構築してきた
- 一方、現実のネットワークはノードやリンクが時間とともに現れたり消えたりすることが多いく、**動的**である
    - SNSに新しいユーザが増加し、全体的なネットワーク規模が成長する傾向がある
- 動的モデルでネットワークの成長をモデルする
    - 小さなネットワークを初期状態として考え、その後ノードが一人ずつ追加される
    - 追加されるノードは、モデルに特有の何らかのルールに基づいてネットワークを構築していく
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

# 次数分布に着目するネットワークモデル

既存モデルに対する考察


<div grid="~ cols-2 gap-4 items-start">

<div>

<div class="flex justify-center">
  <img src="./image/power_transportation.png" alt="ネットワーク図" width="800" />
</div>


</div>

<v-clicks depth="2">

- ハブ(hub): ネットワーク内で次数degreeが極めて高いノード
    - ハブはネットワーク構造の中で非常に重要な役割を果たし、情報や影響の伝播において中心的な存在になる
- Configurationではハブを持つように事前に設定することでハブを生成自体は可能であるが、どの過程を経てハブが発生するのか説明できない　
    - 接続先ののノードがランダムに選ばれるからである
</v-clicks>　

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

# Barabasi-Albertモデル

モデルの発想


<div grid="~ cols-2 gap-4 items-start">

<div>

<div class="flex justify-center">
  <img src="./image/matthew.png" alt="ネットワーク図" width="800" />
</div>


</div>

<v-clicks depth="2">

- ハブがどのように生成されるのか❓
  - マタイ効果:「金持ちはより金持ちに、貧乏人はより貧乏に」
      - 学術:有名な研究者の論文は、内容にかかわらず引用されやすくなる
      - SNS:フォロワーの多い人の投稿は拡散されやすく、さらにフォロワーが増える
  - **優先的選択**：ノードが新たなリンクを形成する際、既に多くのリンク（高次数）を持つノードに接続しやすい
</v-clicks>　

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

# Barabasi-Albertモデル

モデルの構造


<div grid="~ cols-2 gap-4 items-start">

<div>

<v-clicks depth="2">

- （最初に \( m_0 \) 個のノードを用意し、それらの間を完全に接続する完全ネットワークからスタートする）
- 各ステップにおいて新しいノードを1つ追加し、既存のノードの中から選んでリンクを張る
- 新しいノードは、既存ノードの次数に比例した確率で接続先を選ぶ
    - $P(i) = \frac{k_i}{\sum_j k_j}$
- ステップを繰り返して、ネットワークのノード数を目的のサイズまで増やす

</v-clicks>


</div>

<div class="flex justify-center">
  <img src="./image/BA.png" alt="ネットワーク図" width="800" />
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

# Barabasi-Albertモデル

モデルの考察


<div grid="~ cols-2 gap-4 items-start">

<div>

<v-clicks depth="2">

- 最初は全てのノードの次数は等しく
- 新しいノードやリンクが追加されることにつれて、ノードの次数は大きくなっていく
  - 新たに追加されたノードは、優先的選択に基づいて既存ノードにリンクを張りる
  - 既に多くのリンクを持つノードがさらにリンクを獲得する確率が高く、次数は非対称に拡大していく
  - 結果として、ノードごとに大きな次数の格差が生まれ、一部のノードがハブ化していく
</v-clicks>


</div>

<div class="flex justify-center">
  <img src="./image/BA_results.png" alt="ネットワーク図" width="800" />
</div>

</div>

<p v-click style="color: #3E1586; font-size: 1em; text-align: center;">
  多くの現実のネットワークの成長時には、優先的選択のメカニズムが働いていることが確認された
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

# Barabasi-Albertモデル

モデルの拡張


<v-clicks depth="2">

- BAモデルの問題点：あるノードに隣接ノードが全くない場合はどうするのか
    - ノードの次数はゼロなので、リンクを獲得する確率もゼロで、そのノードはリンクを持つことはない
        - そのため、完全グラフからスタートすることが多い
        - 「理想」な完全グラフではなくでも機能すべきことは望ましい
- 魅力モデル（Attractiveness Model）：リンクの接続確率は次数と魅力度の和に比例することに変更する
    - $\Pi_i = \frac{k_i + A_i}{\sum_j (k_j + A_j)}$
    - **新規ノードも注目されうる**：魅力度$A_i$により、開始直後でもリンクを得られる
    - 才能、ブランド、知名度など現実世界における影響をもつ要素をモデルに反映できる
        - $A_i$の設計方法による多様なバリエーション
</v-clicks>　

<p v-click style="color: #3E1586; font-size: 1em; text-align: center;">
  BAモデルの限界を克服するために、要素を導入したモデルが提案されている
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