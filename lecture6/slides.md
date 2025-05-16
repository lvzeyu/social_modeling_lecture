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


Opinion Dynamics: Granovetter's threshold model

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

# 背景

More Is Different (量が多いことは質の違いを生む)

<v-clicks depth="2">


- 「More Is Different」は１９７２年にAndersonがScience誌に発表した[エッセイ](https://solid-mater.com/entry/more)のタイトルである。

> P. W. Anderson．１９７７年のノーベル物理学賞受賞者にして、最も創造性の高い物理学者と呼ばれるなど、二十世紀を象徴する理論物理学者である

- 還元主義(Reductionist)という考え方
    - この世界の全てはある基本法則に基づいて決められている
        - 物理学の基本的な粒子(素粒子)を理解すれば、物理、化学や生物学全ての現象が自動的に理解可能になる

- 還元主義に対する批判
    - スケールの違いによる本質的な違い: 「量的な差異（More）」は単なる量の増加ではなく、「質的な差異（Different）」をもたらす
    - 創発（Emergence）の重要性: 個々の要素の単純な相互作用が、より高次のレベルで「質的に新しい現象」を生み出すことがあり、それらは要素の性質から直接的に予測・説明できない
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

<!--
物理学者フィリップ・W・アンダーソンが1972年に発表した有名なエッセイ「More Is Different（多ければ異なる）」を紹介します。
このエッセイの背景：20世紀中頃、科学界では素粒子物理学がもっとも「偉い」学問と見なされていました。
電子、クォーク、ニュートリノといった「究極の基本構成要素」を探求するこの分野は、「万物の根源に迫る学問」として注目を集め、潤沢な研究資金と強い発言力を持っていました。
その一方で、化学や生物学、そしてアンダーソンが専門とした**物性物理学（固体物理）**は、
「素粒子物理から派生した二流の応用分野」とみなされる風潮すらありました。

- 還元主義: たとえば、素粒子（電子やクォークなど）の性質を完全に理解できれば、物理現象だけでなく、化学反応や生命現象、さらには人間の意識や社会現象さえも、原理的にはすべて説明できるとする立場です。
- 素粒子がわかればすべてがわかる」という還元主義的思考に対し、深い違和感を抱くようになります
- 「世界は階層的に構造化されており、それぞれの階層に固有の法則がある。
よって、下位レベルの法則を知っているだけでは、上位レベルの現象は説明できない。」
- 彼の主張の核心は、「数が増えれば、単に量が増えるだけではなく、新たな質が生まれる」ということです。これは、「More（多く）」であることが、「Different（異なる）」性質を生む、という意味です。
- 具体的には、個々の構成要素は単純であっても、それらが多数集まり、相互に影響を与え合うと、予測不能な性質や構造が生まれることがあります。これを**創発（Emergence）**と呼びます。
- このように、「More Is Different」は、複雑さや創発といった視点の重要性を、物理学内部から提起した画期的な論考でした
-->

---
transition: slide-up
level: 2
---

# 背景

Complexity Science (複雑系科学)

<div grid="~ cols-2 gap-4">
<div>

<v-clicks depth="2">

- 自然や社会の様々な現象や構造には，多数の分散した構成要素の相互作用によって継続的に発展する「複雑系」としての性質がある
    - 多数の小さな要素とそれを含む大きな要素の関係に現れる「**創発**」
    - 系の時間的発展の中に現れる「**自己組織化**」
    - 現象の数理モデル・計算モデルを創り計算機内で動かして理解する「**構成的手法**」を用いて，複雑系を理解する
        - 要素間の相互作用がシステムの挙動を決めるため、個々の要素だけを見ても全体の挙動を完全には予測できない
</v-clicks>


</div>

<div>

<div style="display: flex; justify-content: center;">
  <img src="./image/nature2.png" width="600" />
</div>

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


<!--
- 多数の要素（エージェント）が互いに影響を及ぼし合いながら、全体として予測困難で多様なふるまいを示すシステムを呼ばれます
- 複雑系科学とは、このような複雑系を対象として、**創発（emergence）・適応（adaptation）・自己組織化（self-organization）**などの現象を理論的・計算的に解明しようとする学際的な研究分野

-->

---
transition: slide-up
level: 2
---

# 背景

複雑系としての人間社会


<v-clicks depth="2">

- 社会科学が対象とする複雑現象には非線形な相互作用が存在し，系全体として創発的な振舞いを示す
- Interaction-induced collective behavior: 相互作用の強さやパターンによって、個々の行動の単純な総和とは異なる「集団レベルの現象」が創発する
    - 自然渋滞モデル；個々の車の小さなブレーキや速度調整が積み重なることで、渋滞パターンが発生する
    - Schelling's model: 個々のエージェントのわずかな非寛容さが相互作用を繰り返すうちに、都市やコミュニティ全体の大規模なセグリゲーションを生む。
- Diversity-induced collective behavior: 個々人の属性や性質の「ばらつき（多様性）」が存在することで、全体としてのマクロな挙動が創発される
    - **Granovetter's threshold model**: 個々人の属性（意見や閾値）の差による、社会運動や流行が発生しやすくなる現象を説明
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

<!--
- 社会は、単に個人の行動の総和ではなく、人々の間にある相互作用と多様性によって、想定外の集団的なふるまいが創発します。

- 相互作用によって生まれる集団的な振る舞い
    - 各個人は「少しだけ異なる隣人を避けたい」という控えめな選好しか持っていません。しかし、この選好が繰り返し作用すると、都市全体が人種・属性ごとに完全に分断されてしまうような極端な状態が出現します。
- 人々の「違い」＝多様性そのものが、創発的な社会現象の鍵になるケースです

-->

---
transition: slide-up
level: 2
---

# Threshold model

単純な意思決定から見る集団的行動

<div grid="~ cols-2 gap-4">
<div>

<v-clicks depth="3">

デモや抗議運動などに参加することを例で考えなさい
- 個人が単純な二値的（binary）的な意思決定を行う：「デモに参加する」／「デモに参加しない」
    - 社会的影響（Social Influence）：個人の態度や行動が、他者からの影響によって変化する（説得、同調、服従など）
- 各個人の持つ「閾値（threshold）」という概念が導入される
    - 「自分以外に何人以上の人がデモに参加していれば、自分も参加する」という基準

</v-clicks>

</div>

<div>

<div style="display: flex; justify-content: center;">
  <img src="./image/demo.png" width="600" />
</div>

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

<!--
Threshold modelでは色々な伝播的現象を説明するためのモデルですが、ここではデモや抗議運動を例を考えなさい

このモデルでは、各人が「参加する」か「参加しない」か、**二値的（binary）**な意思決定を行います。

しかしその判断は、必ずしも個人の内面だけで完結しません。
- 社会的影響（Social Influence）:他の人が何をしているか、どれだけの人が参加しているかという情報が、私たちの意思決定に大きな影響を与えます。これは「説得」「同調」「服従」など、社会心理学でよく知られた現象です。

- 「閾値（threshold）」という考え方です。これは、「自分以外に何人以上がデモに参加していれば、自分も参加する」という個人の基準を意味します。
    - 閾値が0の人：誰も参加していなくても、自分は行動する。
    - 閾値が3の人：少なくとも3人が先に行動しないと、自分は動かない。
    - 閾値が99の人：多数の行動を見ない限り、自分は決して参加しない。
-->

---
transition: slide-up
level: 2
---

# Threshold model

Diversity-induced collective behavior



<v-clicks depth="3">

- 研究関心：人々の選好（＝閾値）の分布が集団行動にどのように影響する
    -  個々人の選好を知っていても、直接的には集団全体の振る舞いを予測できないはず
        - 一人ひとりの選好を単純に合計するではなく、他者の行動との相互作用を通じて非線形的に影響している
    - 「代表的な平均的個人（mean member）」の特性だけではなく、集団内の異質性（heterogeneity）や多様性（diversity）がどのように全体の行動に影響を与えるかを把握する

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

<!--
Granovetterの問題設定は、「人々がどのような**閾値（threshold）**を持っているか＝行動選好の分布」によって、集団全体のふるまいがどう変わるのか？という問いです。
- 個々の選好がわかっていても、それを単純に足し合わせても全体のふるまいは予測できないという点です。
- それは、人々の意思決定が他者の行動に依存しており、相互に影響を与え合うからです。つまり、ここには**非線形性（non-linearity）**が存在します。
    -「私が参加するかどうか」は、「他の誰が先に動くか」によって変わる
    - 一人ひとりの行動は単純でも、その相互作用が予測困難な全体像を生み出す
    - これは、まさに複雑系の特徴です。
- このモデルから得られるもう一つの重要な教訓は、「平均的な個人（mean member）」という考え方だけでは不十分だという点です。
-->


---
transition: slide-up
level: 2
---

# Threshold model

モデルの仮定


<v-clicks depth="3">

集団行動への参加決定は、コストと利得という二つの要素によって決められる

- 参加に伴うコスト
    - デモへの参加による逮捕・拘束のリスク
    - 時間や経済的なコスト

- 参加に伴う利得
    - デモ成功による制度的変化

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

<!--
これまでの説明では、各個人が「何人以上が行動したら自分も行動するか」という**閾値（threshold）**を持つという前提を紹介しました。
では、その閾値はどのように決まるのか？あるいは、閾値という設定はなぜ合理であるといえますかを考えてみたいと思います
ここで重要になるのが、**コストと利得（benefit）**という考え方です。
人が集団行動（例：デモや抗議運動）に参加するかどうかを判断する際、多くの場合、
¥
- 参加したときに得られる利得（ベネフィット） と
- 参加に伴うコスト（負担やリスク）
この2つを比較しています。

- 参加に伴うコスト
    - 集団行動に参加することには、さまざまなリスクや負担があります。
    - 身体的リスク：デモへの参加で逮捕されたり拘束されたりする可能性
    - 時間的・経済的コスト：仕事や家庭の時間を犠牲にする必要があるかもしれません
    - このようなコストが高いと、人々の閾値は高くなりやすい（＝より多くの他者が先に動かないと、自分は行動しない）と考えられます。
- 参加に伴う利得（ベネフィット）
    - 一方で、行動に参加することで得られる価値や成果もあります。
    - 自分が信じる目的の達成（制度改革、社会的正義の実現）
    - デモが成功することで政治的な変化が起こる
    - あるいは、自分が「声を上げた」という満足感や他者からの評価も利得の一部と考えられます
    - 利得が大きいと、たとえコストがあっても参加しやすくなり、閾値が低くなることが多いです。


-->

---
transition: slide-up
level: 2
---

# Threshold model

モデルの仮定

<div grid="~ cols-2 gap-4">
  <!-- 左側のテキスト部分 -->
  <div>
    <v-clicks>
      <ul>
        <li><strong>Net benefit = 利得（Benefit）− コスト（Cost）</strong></li>
        <li>個人が集団行動に参加するかどうかは、Net benefit によって決まる。
          <ul>
            <li><code>Net benefit &gt; 0</code> の場合、個人は行動に参加する。</li>
            <li><code>Net benefit ≤ 0</code> の場合、個人は行動に参加しない。</li>
          </ul>
        </li>
      </ul>
    </v-clicks>
  </div>

  <!-- 右側の画像部分 -->
  <div style="display: flex; justify-content: center; align-items: center;">
    <img src="./image/Benefit.png" width="600" />
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

<!--
■ 横軸：集団内の参加者の割合（Proportion of group participating in the riot）
- 0%〜100%の範囲で、暴動やデモなどの行動に実際に参加している人の割合を示しています。

■ 縦軸：純利益（Net benefit）
- 参加による利得からコストを差し引いた値です。
- 0より上なら「参加することの方が得」、下なら「損になる」状態。

■ 横軸：集団内の参加者の割合（Proportion of group participating in the riot）
0%〜100%の範囲で、暴動やデモなどの行動に実際に参加している人の割合を示しています。

■ 縦軸：純利益（Net benefit）
参加による利得からコストを差し引いた値です。

0より上なら「参加することの方が得」、下なら「損になる」状態。
-->

---
transition: slide-up
level: 2
---

# Threshold model

モデルの動き

<div grid="~ cols-2 gap-4">
<div>

<v-clicks depth="3">

- エージェント数：100人  
- 閾値（threshold）は 0〜99 の一様分布（整数）  
- 最初のエージェントが行動を開始し、それをトリガーに次々と参加  
- 各ステップで1人ずつ行動に参加し、最終的に全員が参加する  

</v-clicks>

</div>

<div>

<div style="display: flex; justify-content: center;">
  <img src="./image/Riot1.svg" width="600" />
</div>

</div>

</div>

カスケード(cascade): 階段状に水が流れ落ちていく滝のように、ある個人または少数の個体の行動や選択の影響が連鎖的に他者へと広がっていく現象


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

# Threshold model

モデルの動き

<div grid="~ cols-2 gap-4">
<div>

<v-clicks depth="3">

- 基本設定はバージョン1と同じ  
- ただし、閾値が $1$ と $3$ のエージェントが $2$ に変更された  
- 最初のエージェントは行動を開始するが、他の誰も続かず終了  
    - 一部のエージェントの閾値が少し高くといった小さい変更だけで、連鎖がが途中で止まってしまった
</v-clicks>


</div>

<div>

<div style="display: flex; justify-content: center;">
  <img src="./image/Riot2.svg" width="600" />
</div>

</div>

</div>

<v-clicks depth="3">

- カスケードを生み出すには、十分な数の低閾値エージェントが必要
    - 行動が広がるか否かは、平均的な傾向ではなく、「どこに低閾値の人がいるか（分布の構造）」に強く依存する　→　マイクロな条件の重要性
</v-clicks>


<!--
まず、バージョン1の設定を思い出してください：

閾値が低い人（たとえば 0, 1, 2…）から順番に影響を受けて行動し、全体にカスケードが広がる

ところが今回は、ほんの少し設定を変えただけです。

閾値1と3のエージェントを、それぞれ閾値2に変更
→ すると、最初の行動者だけが動き、他の誰も続かない

このように、たった2人の閾値の変更が、全体の結果を大きく左右するのです。

カスケードが進むには、「次に行動する人がいる条件」を満たさなければなりません。
もしその「つなぎ役」がいなくなれば、連鎖が途中で止まってしまうのです。

この現象は、次のように整理できます：

カスケードには、「低閾値の人が連続して配置されている」ことが必要

一人でもその鎖が切れると、行動はそれ以上拡大しない

この話から得られる重要な教訓は：

行動が広がるかどうかは、「平均的な傾向」ではなく、「閾値分布の具体的な構造」によって決まる

つまり、

いくら平均閾値が低くても、途中に高い壁（高閾値の人）がいれば行動は止まる

一方で、少数でも閾値0〜1のような人が適切な位置にいれば、大きな変化を引き起こせる

これはまさに、マイクロな条件の違いがマクロな結果を左右するという、複雑系の典型的特徴です。

-->

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

# Threshold model

閾値の分布

<div grid="~ cols-2 gap-4">
<div>

<v-clicks depth="3">

- $r(t)$ は時点 $t$ におけるアクティブなエージェント数
    - 例えば、デモに参加している人の数
     - $r(0)$：初期の「先導者（instigator）」の数

- $F(x)$ は閾値の累積分布関数を表す
  $$
  F(x) = P(\Theta_i < x)
  $$
    - 潜在的参加者を表す


- シミュレーションの均衡状態：
  $$
  r_e = F(r_e)
  $$  

</v-clicks>

</div>

<div>

<div style="display: flex; justify-content: center;">
  <img src="./image/CDF.png" width="600" />
</div>

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

<!--

集団内における各人の閾値の分布が、社会運動などの行動の広がり（カスケード）にどう影響するかを動的に示したものです。

- 横軸: 行動に参加している人の割合（例: デモに参加している人の割合）
- 縦軸（y軸）: 閾値がx以下の人の割合、つまり「今の参加率で参加する人の割合」→ その割合を見て「自分も行動に参加しよう」と判断する人の割合（つまり潜在的参加者）
- 曲線：累積分布関数F(x)は、各値x 以下の閾値を持つ人の割合を表します。
- F(x)が急激に上昇する箇所では、「ちょっと参加者が増えるだけで参加したがる人が一気に増える」
    - 初期の参加者（インスティゲーター）の役割が非常に重要
- 参加率と実際に参加する人の割合が一致する点が均衡点になります
    - この点では、参加する人の割合と、行動しようとする人の割合が一致しています。

1. **初期状態：**
   - 参加者の割合を \( r(t) \) とする。

2. **次の参加者の決定：**
   - このとき参加する人の割合は、累積分布関数によって決まり、
     \[
     r(t+1) = F(r(t))
     \]
   - つまり、閾値が \( r(t) \) 以下の人（= 今の参加状況を見て参加する人）の割合。

3. **同様に次の時点でも：**
   - 次の時点では、
     \[
     r(t+2) = F(r(t+1))
     \]
   - というように、**参加率は繰り返し関数 \( F \) によって更新されていく**。

4. **図上の動き：**
   - グラフ上ではこの繰り返しが「階段状の矢印」として視覚化される。
   - 縦に \( F(r(t)) \)、横に \( r(t+1) \) と移動する動きが続く。

5. **最終的に収束：**
   - この反復は、45度線 \( F(x) = x \) と累積分布関数 \( F(x) \) の交点、
     \[
     r_e = F(r_e)
     \]
   - に収束する。これが **均衡点（equilibrium point）** である。

この点では、参加率 = 閾値以下の人の割合、が一致しているため、これ以上広がらず、カスケードが止まります。

安定点が0に近ければ → 動きが起こらずに終了

安定点が高い位置にあれば → 行動が集団全体に波及
-->


---
transition: slide-up
level: 2
---

# Threshold model

閾値の分布

<div grid="~ cols-2 gap-4">
<div>

<v-clicks depth="3">

- 仮定：閾値は平均 $\mu$、標準偏差 $\sigma$ の正規分布に従う 
    - エージェント数は常に100人、$\mu = 25$ で設定される
- $r_e$：平衡時のアクティブなエージェント数  



</v-clicks>

</div>

<div>

<div style="display: flex; justify-content: center;">
  <img src="./image/STD.png" width="600" />
</div>

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

# Threshold model

閾値の分布

<div grid="~ cols-2 gap-4">
<div>

<v-clicks depth="3">


- 臨界値より小さいの際には、ほとんどの人が「25人くらいが行動しないと、自分は動かない」と思って、閾値が非常に低い人がほとんど存在しなくなるるため、誰も続かない
    - 標準偏差が小さいため、「5人でも行動する」「10人でも行動する」という極端に閾値の低い人がほぼ存在しない
    - 集団があまりに均質すぎると、誰も最初にリスクをとらず、変化が起きない



</v-clicks>

</div>

<div>

<div style="display: flex; justify-content: center;">
  <img src="./image/s1.svg" width="300" />
</div>

<div style="display: flex; justify-content: center;">
  <img src="./image/s10.svg" width="300" />
</div>

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

<!--
ここでは、具体的なモデル設定に基づいて、閾値モデルの動きをシミュレーション的に理解していきます。
このように、平均閾値 
多様性の程度 、そして初期の行動者の存在が、
最終的にどれだけの人が参加するかを決定します。

-->


---
transition: slide-up
level: 2
---

# Threshold model

閾値の分布

<div grid="~ cols-2 gap-4">
<div>

<v-clicks depth="3">


- 臨界値に近いの場合、閾値分布がちょうどよい多様性を持つため、少数のインスティゲーターの行動が、低い閾値を持つエージェントを引き込み、次々と参加者が増えていくことで、カスケードが発生する

- 臨界値に等しいの場合は、社会全体に行動が拡大し、100人全員が最終的に行動に参加



</v-clicks>

</div>

<div>

<div style="display: flex; justify-content: center;">
  <img src="./image/s12.svg" width="300" />
</div>

<div style="display: flex; justify-content: center;">
  <img src="./image/s13.svg" width="300" />
</div>

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

# Threshold model

閾値の分布

<div grid="~ cols-2 gap-4">
<div>

<v-clicks depth="3">


- 臨界値より大きいの場合、閾値のばらつきが大きくなりすぎる。
    - 非常に低い閾値の人（たとえば「2人でも行動する」）と非常に高い閾値の人（たとえば「90人以上が行動しないと自分は動かない」）が混在

- 初期の参加者は一部の人を動かすが、それが途中で途切れやすい

</v-clicks>

</div>

<div>

<div style="display: flex; justify-content: center;">
  <img src="./image/s60.svg" width="600" />
</div>

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

# Threshold model

閾値の分布

<div grid="~ cols-2 gap-4">
<div>

<v-clicks depth="3">


- 多様性の重要性:適度な多様性があることで、集合的行動が広がる
    - 平均閾値が同じでも、分布が違えば集団行動は全く異なる

- 転換点の特定
    - 特定な臨界値を境に、劇的な変化が起こりうる

- [Demo](https://rf.mokslasplius.lt/granovetters-threshold-model/)
</v-clicks>

</div>

<div>

<div style="display: flex; justify-content: center;">
  <img src="./image/STD.png" width="600" />
</div>

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

# Threshold model

閾値モデルの拡張

- Granovetter（1978）の閾値モデルでは、「各個人は、他の全員の行動を見て、それに応じて自分の行動を決める」という完全情報・完全接続の社会を想定している

- 局所ネットワークにおける閾値モデルの適用
    - 各個人は、社会全体の行動率ではなく、自分の「局所的な近隣（近くの人々）」の中での行動率に応じて行動する([Centola & Macy 2007](https://www.journals.uchicago.edu/doi/10.1086/521848);[Siegel 2009](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-5907.2008.00361.x);[Watts 2002](https://www.pnas.org/doi/10.1073/pnas.082090499))
    


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

# Threshold model

閾値モデルの拡張

- エージェントの観察範囲は、ネットワーク構造によって決まる ([Siegel 2009](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-5907.2008.00361.x))


<div style="display: flex; justify-content: center;">
  <img src="./image/network_threshold.png" width="500" />
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

# Threshold model

閾値モデルの拡張

- 局所ネットワークの（同質性）特徴は、集合的行動の結果を大きく左右する([Mustafa Yavaş & Gönenç Yücel 2014](https://journals.sagepub.com/doi/10.1177/0894439313512464))


<div grid="~ cols-2 gap-4">
<div>

<div style="display: flex; justify-content: center;">
  <img src="./image/network_example.png" width="300" />
</div>
</div>

<div>

<div style="display: flex; justify-content: center;">
  <img src="./image/network_result.png" width="600" />
</div>

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

# Threshold model

閾値モデルの応用

- 閾値モデルは、様々のコンテイション(contagion)に関する社会現象の説明に用いられている
    - 社会運動・抗議行動
    - 技術革新・製品普及　([Valente 1996](https://www.sciencedirect.com/science/article/pii/0378873395002561))
    - 政策受容([GILARDI & WASSERFALLEN, 2019](https://ejpr.onlinelibrary.wiley.com/doi/full/10.1111/1475-6765.12326))
    - 誤情報の伝播([Törnberg, 2018](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0203958))



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


<!--
1. 社会運動・抗議行動
誰かがデモに参加したことで、他の人も勇気づけられ、次々と参加が広がっていく

このような行動のカスケードが、制度変革や社会変動につながる

閾値モデルは、なぜ同じ不満を持つ社会で行動が起きる時と起きない時があるのかを説明する

2. 技術革新・製品普及（Valente 1996）
新しい技術や製品の利用も、「他の人が使っているなら自分も使う」という社会的影響を受ける

Valenteの研究では、医療現場における新技術の導入について、社会的ネットワーク内での閾値の違いが普及スピードに影響することを示した
→ 閾値の低い「先導者」が普及を駆動する

3. 政策の受容・拡散（Gilardi & Wasserfallen, 2019）
ある国や地域で新しい政策（例：同性婚、環境規制など）が採用されると、近隣や同盟国が影響を受けて導入に向かう

このような政策の連鎖的採用も、閾値モデルで説明可能

特に、**国レベルでも「他国の導入状況を見て自国が判断する」**という構造がある

4. 誤情報・陰謀論の拡散（Törnberg 2018）
SNS上での誤情報の拡散も、「どれだけ多くの人が信じて共有しているか」が個人の行動に影響を与える

閾値モデルは、なぜ一見根拠のない情報が急速に拡散するのか、あるいはなぜ一部では拡散せず終わるのかを説明する

特に、ネットワーク構造と閾値の相互作用によって拡散パターンが大きく異なることが示されている

■ なぜ閾値モデルは汎用的なのか？
どの現象も、「他者の行動を参照して自分の行動を決定する」という点で共通している

閾値モデルは、この社会的影響の構造を単純かつ強力に表現できる枠組み

このモデルを理解することは、複雑で予測困難な社会現象をより構造的・動的に捉えるための強力なツールとなるのです。
-->



---
transition: slide-up
level: 2
---

# Threshold model

閾値モデルの応用

- **閾値モデルは転換点（tipping point）の重要性を示した**；一定の割合以上の少数派が存在すれば、一見安定しているように見える社会的規範でもコンテイションを通じて覆される可能性がある
    - 性別役割に対する社会的期待
    - ゴミ分類という規範の受容
    - 禁煙活動
    - 流行語の普及



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

<!--
閾値モデルは、**「社会的変化はゆっくりではなく、ある瞬間に突然起こる」**という現象を説明できる重要な枠組みです。

転換点（tipping point） とは、ある臨界的な人数や割合を超えたときに、社会全体の行動や規範が一気に変わるという現象です。

閾値モデルでは、人々の行動が**「他人の行動数」や「割合」によって決まる**ため、少数派でも一定割合を超えると一斉に拡散する可能性がある。


性別役割に対する社会的期待

伝統的な性別役割（女性は家事、男性は仕事）が支配的だった社会でも、一定数の人が違う行動を取り始めると、次第にそれが「新しい当たり前」になる。

ゴミ分類・リサイクルの規範

もともとは一部の意識の高い人だけがやっていたリサイクルが、ある時点を境に社会全体で常識化する。
→ 自治体のルールや周囲の目が「他人の行動」として影響を与える

禁煙活動

最初は少数派の活動だった禁煙運動が、ある時点から急速に職場や公共空間のルールとして広がった

一部の人の声や行動が連鎖的に変化を促進

流行語・スラングの普及

一部の若者やインフルエンサーが使い始めた言葉が、転換点を超えることで一気に社会に浸透

最初は「変わった人たちの言葉」→ その後「一般的な言い回し」に

閾値モデルは、緩やかな変化ではなく、突発的・急激な社会的転換のメカニズムを説明する

一見安定しているように見える社会的規範も、一定割合を超えると一気に覆される

この視点は、社会運動、文化変容、行動変化キャンペーンなど、実践的な応用にもつながる

-->



---
transition: slide-up
level: 2
---

# Threshold model

閾値モデルの応用

[Centola et al., (2018)](https://www.science.org/doi/full/10.1126/science.aas8827): 転換点（tipping point）という示唆に基づく実証研究
- 問題関心：社会的規範の転換がどの時点で起こるかを実験で再現・検証しよう

- 実験設計
    - 参加者グループに写真を提示
        - ある人物の写真を見せて、その人物の「名前」を決めてもらう
        - 複数ラウンドを通して話し合いを行い、グループ内で共通の名前（=社会的合意）を形成させる
    - 異なる意見を持つ「confederates」を投入
        - 合意が形成されたあと、一貫して「違う名前」を主張するconfederatesをグループに加える
    - インセンティブは「協調すること」のみ
        - お金や正解の有無はなく、できるだけ他人と同じ名前を答えることが望ましいというルールだけが与えられる(社会的影響の要因)



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

# Threshold model

閾値モデルの応用


<div grid="~ cols-2 gap-4">
<div>

- 協力者の割合が10～20%程度では、影響は限定的で、多数派の意見は維持される傾向
- 協力者（少数派）の割合が約25%に達すると、それまで形成されていた多数派の合意が崩れ始める
    - 最終的には少数派が提示した新しい名前が、グループ全体の新たな合意になる

- 「粘り強い少数派からの変化」は閾値モデルによる提示する理論的な示唆だけでなく実験でも実証可能であると示した
</div>

<div>

<div style="display: flex; justify-content: center;">
  <img src="./image/Centola1.jpeg" width="250" />
</div>

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