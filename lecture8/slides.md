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

# 社会ネットワーク

社会ネットワークの特徴

| Name                             | Nodes   | Links    | Average Degree | Maximum Degree | Heterogeneity |
|----------------------------------|---------|----------|----------------|----------------|----------------|
| IMDB movies and actors           | 563,443 | 921,160  | 3.269754       | 800            | 5.406334       |
| IMDB actors costar               | 252,999 | 1,015,187| 8.025225       | 456            | 4.570261       |
| Twitter US politics              | 18,470  | 48,365   | 2.618571       | 204            | 8.298196       |
| Enron Email                      | 87,273  | 321,918  | 3.688632       | 1,338          | 17.436859      |
| Enron Executive Email            | 143     | 623      | 8.713287       | 42             | 1.482948       |



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

# 社会ネットワーク

社会ネットワークの特徴

様々の社会ネットワークにはいくつかの共通した性質がある
<v-clicks depth="2">

- 経路が短い
    - あるノードから他のノードへ数ステップで移動できる
- クラスタ係数が高い
    - 閉じた三角型の関係が多い
- ノードやリンクの変数（次数やリンクの重みなど）の分布が不均一になっている

> ネットワークの特徴がどのように現れるかについての直感や仮説を取り込んでモデルを構築し、そのモデルに従って構築されたネットワークと現実のネットワークを比較することで、何かモデルによって再現できて、何か再現出来ないにかを確認する

→ **ネットワークモデル**によって現実世界のネットワークがどのようなメカニズムで成り立っているのかについての知見を得ることができる
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

# ランダムネットワーク

ランダムネットワークの概要

孤立したノードが多数あり、そこにリンクを張ることによってネットワークを構築することを考えよう

<v-clicks depth="2">

- [ランダムに1つずつリンクを追加していくとどうなる？](https://www.networkpages.nl/CustomMedia/Animations/RandomGraph/ERRG/AddoneEdgepATime.html)
   - 接続されるのノードベアの数が増える
   - 接続された部分ネットワークが形成される
   - ある時点で、どのノードからどのノードへもリンクをたどっていくことができるようなネットワークになる

- 比較的に小規模な部分ネットワークのみで構成されるネットワークから、ほとんどすべてのノードを含む巨大ネットワークに成長し、変化は徐々に起こる

→ **ネットワークモデル**によって現実世界のネットワークがどのようなメカニズムで成り立っているのかについての知見を得ることができる
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

# ランダムネットワーク

Erdos-Renyi (ER)モデル

Erdos-Renyi (ER)モデルは、ノード数$N$とリンク生成確率$p$の二つのパラメータを持つモデルである。$G(N, p)$

- ノード数：$N$ 個のノードがある。
- リンク生成確率：各ノードのペアに対して、確率 $p$ でリンクを生成。
- 各エッジの有無は独立に決定される。

<v-clicks depth="2">

- あるリンク生成確率$p$のランダムネットワークを構築することは、偏ったコインを繰り返し投げて、表が何回出るか数えることと類似している
    - 偏ったコインが確率$p$で表を出すとすると、$t$回投げて表が出る回数の期待値は$pt$である
    - 表が出る回数の期待値は、偏ったコインを一回投げた時に表が出る確率とコインを投げた回数に比例している

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

# ランダムネットワーク

リンク数


<v-clicks depth="2">


- ランダムネットワークにおけるリンク数の期待値は、リンク生成確率$p$とノードペアの数に比例する
    - リンクが存在しうるペアの数　$\binom{N}{2}=\frac{N(N-1)}{2}$
- ランダムネットワークのリンク数の期待値：$<L>=\frac{pN(N-1)}{2}$
- ネットワークの平均次数は、リンク数の２倍をノード数で割った値
    - ランダムネットワークの平均次数の期待値: $<k>=p(N-1)$

</v-clicks>


<p v-click style="color: #3E1586; font-size: 1.5em; text-align: center;">
  ランダムネットワークモデルが現実世界のネットワークに当てはまるには、リンク生成確率pを小さく設定する必要がある
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

# ランダムネットワーク

次数分布

<v-clicks depth="2">


- ランダムネットワークの次数分布
    - あるノードが$k$個の隣接ノードを持つ確率について考えよう

- コインの問題と等価である：表が確率$p$で出る偏ったコインで合計$N-1$回を投げるとき
    - $k$回表が出る確率は二項分布に従う：$P(k; N-1, p) = \binom{N-1}{k} \cdot p^k \cdot (1 - p)^{N - 1 - k}$
        - $N - 1$: 試行回数（コインを投げる回数）
        - $k$: 表が出る回数
        - $p$: 表が出る確率
        - $\binom{N-1}{k}$: 表が $k$ 回出る並び方の数（組合せ）$\frac{(N-1)!}{k! \cdot (N-1 - k)!}$ 
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

# ランダムネットワーク

次数分布

<div grid="~ cols-2 gap-4 items-start">

<div>

<v-clicks>

- (a)ランダムネットワークにおける次数の確率分布は、平均次数$<k>$付近に高いビークをもち、どの両側で急速に減衰するベル型の曲線になる
- 多くの現実ネットワークはかなり異なる分布になる
    - (b)世界の航空網ネットワーク
    - (c)現実ネットワークとンダムネットワークとの比較
</v-clicks>

<p v-click style="color: #3E1586; font-size: 1.5em; text-align: center;">
  不整合性を解決するためには、より洗練されたネットワークモデルが必要となる
</p>


</div>

<div class="flex justify-center">
  <img src="./image/rn_degree.png" alt="ネットワーク図" width="800" />
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

# ランダムネットワーク

クラスター係数


<v-clicks>

- クラスタ係数は、あるノード $i$ における隣接ノード同士の接続の程度を示す指標である
- あるノードの隣接ノード同士がつながっている確率は、共通の隣接ノードがあるかどうかに依存せず、どのペアでも同じであるため$p$とあなる
    - 個々のノードの局部的なクラスターは多少ずれることはあるが、全てのノードの平均値は$p$でよく近似できる

- ランダムネットワークで現実のネットワークのような疎なネットワークを記述する場合、$p$を非常に小さいの値になる
    - このようなランダムネットワークのクラスター係数は非常に小さい
    - 現実のネットワークでは高いクラスタ係数をもつことは多い
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