---
# You can also start simply with 'default'
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cover.sli.dev
# some information about your slides (markdown enabled)
title: 社会科学におけるモデル入門
info: |
  ## 行動科学概論
  社会科学におけるモデル入門

  担当者：呂沢宇
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


イントロダクション

### 呂沢宇

<div @click="$slidev.nav.next" class="mt-12 py-1" hover:bg="white op-10">
  スペースキーで次へ <carbon:arrow-right />
</div>

<div class="abs-br m-6 text-xl">

  <a href="https://github.com/lvzeyu/social_modeling_lecture" target="_blank" class="slidev-icon-btn">
    <carbon:logo-github />
  </a>
</div>

<style>
h1 {
  -webkit-text-fill-color: white;
  -moz-text-fill-color: white;
  color: white;
}
</style>

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
transition: fade-out
---

# 授業の概要

社会科学の観点からモデルとモデリングの基本的な概念および方法論について学ぶ

<v-clicks :depth="2">

- 📝 モデルとモデリングの考え方を把握する.
    - そもそも**モデル**ってなに?
    - モデリングで何かできるのか

- 例：ニュートンの運動方程式($F=ma$)は物体の運動を説明している 
    - 現実の複雑な運動を簡単な数学的関係に落とし込む
    - 条件を与えることで、未来の状態を予測できる

- 日常生活にも無意識のうちに「モデル」を使っている
    - 例：日常のルーティンをまとめるとき、すべての細かい行動を記録するのではなく、重要で典型的なものを抽象化して整理する
</v-clicks>

<br>
<br>


---
transition: fade-out
---

# 授業の概要

社会科学の観点からモデルとモデリングの基本的な概念および方法論について学ぶ

<v-clicks :depth="2">

- 🏙️ 社会科学における**社会シミュレーション**という手法の位置付け
    - 人間行動と社会シミュレーションとは?
        - Agent-Based Models(ABMs)を中心に紹介
    - 社会科学における社会シミュレーションの理論基盤
        - コールマン：ミクロ・マクロ リンク
    - シミュレーションモデルの表現と記述
    - シミュレーションの基本要素と構成
- 🧑‍💻 モデルを用いて社会現象や人間行動の分析を実装する能力を身につける.
    - ある社会現象を理解・解釈する際には適切なモデルを活用
    - NetLogoでモデルを実装するスキル

</v-clicks>
<br>
<br>

<!--
Here is another comment.
-->

---
transition: fade-out
---

# 授業の構成 

社会科学における典型なモデルを学ぶ

- **社会の自己組織化**
    - 個々の人々や集団が独立に行動することで、結果的に社会全体の秩序や構造が形成される
    - （人種による隔離を説明する）シェリングの住み分けモデル ([Schelling, 1971](https://www.suz.uzh.ch/dam/jcr:00000000-68cb-72db-ffff-ffffff8071db/04.02%7b_%7dschelling%7b_%7d71.pdf); [Erez Hatna & Benenson, 2012](https://www.jasss.org/15/1/6.html))

<div style="display: flex; justify-content: center;">
  <img src="./image/schelling.gif" width="300" />
</div>


<br>
<br>



---
transition: fade-out
---

# 授業の構成

社会科学における典型なモデルを学ぶ

- **協力行動（Cooperation）**
    - 囚人のジレンマ ([Axelrod, 1984](https://ee.stanford.edu/~hellman/Breakthrough/book/pdfs/axelrod.pdf))
    - **構造化された環境での協力（Cooperation in Structured Environments）**
        - 空間構造における協力行動の維持と変化

<div style="display: flex; justify-content: center;">
  <img src="./image/dilemma-prisoners-participants-game-theory-communication-strategy.png" width="250" />
</div>

---
transition: fade-out
---

# 授業の構成

社会科学における典型なモデルを学ぶ


- **社会における意見ダイナミックのモデリング**
    - Threshold model ([Granovetter, 1978](https://www.journals.uchicago.edu/doi/10.1086/226707); [Watts, 2002](https://www.pnas.org/doi/10.1073/pnas.082090499))
    - Voter Model
    - Bounded Confidence Model([Rainer & Krause, 2002](https://www.jasss.org/5/3/2.html))
    - 他に発展的なモデル（特にオンラインにおける意見分極化について）

<div style="display: flex; justify-content: center;">
  <img src="./image/opinion_dynamic.jpg" width="500" />
</div>

<br>
<br>


---
transition: fade-out
---

# 授業の構成 

社会科学における典型なモデルを学ぶ


- **ネットワークモデル**
    - ネットワークの基本概念
        - ネットワーク科学の詳細は、[Barabásiの本](https://www.kyoritsu-pub.co.jp/book/b10003149.html)に参照してほしい
    - Small Worlds Model ([Watts & Strogatz, 1998](https://www.nature.com/articles/30918); [Watts, 1999](https://www.journals.uchicago.edu/doi/10.1086/210318))
    - Scale-free Networks ([Albert-László Barabási & Albert, 1999](https://www.science.org/doi/full/10.1126/science.286.5439.509))

<div style="display: flex; justify-content: center;">
  <img src="./image/small_world.png" width="500" />
</div>


<br>
<br>

---
transition: fade-out
---

# 授業の構成

社会科学における典型なモデルを学ぶ


- **社会における伝播・感染現象**
    - SEIRモデル
    - SEIRモデルによる社会実装 ([Chang et al., 2020](https://www.nature.com/articles/s41586-020-2923-3))

<div style="display: flex; justify-content: center;">
  <img src="./image/Seir.jpg" width="500" />
</div>

<br>
<br>


---
transition: fade-out
---

# 授業の構成

NetLogoによるモデルの実装

<div class="grid grid-cols-2 gap-8">

<div>

<v-clicks>

- ABMの実装に特化したプログラミング言語・環境
- GUIでシミュレーションをリアルタイムに可視化できる
- 初心者でも直感的に扱いやすいシンプルな構文
- 豊富なサンプルモデルライブラリ（Models Library）を内蔵
- 授業で紹介する各モデルをNetLogoで実装・動作確認する
   - コードへの理解より、**モデルの振る舞いと概念の理解**を重視

</v-clicks>

</div>

<div class="flex items-center justify-center">
  <img src="./image/Netlogo.png" width="350" />
</div>

</div>

---
transition: fade-out
level: 2
---

# 授業の進め方

- 授業内容は進行状況による調整する可能性もある
- 授業の資料はオンラインで公開する
   - [本日の資料](https://lvzeyu.github.io/social_modeling_lecture/lecture1/)
   - リンクはGoogle Classroomでお知らせます
   - 資料のソースコードは[Github](https://github.com/lvzeyu/social_modeling_lecture)で公開されています
- 参考資料と参考文献は授業中適宜提示
- 授業で取り上げるモデルの一部について、実装コードを共有する


---
transition: fade-out
level: 2
---

# 成績評価

- **出席（50%)**
    - 授業中の議論に積極的に参加した場合、適宜加点する。
- **授業期間中の課題（25%)**
   - 授業内容の理解を確認するための課題を課す。
- **最終課題（25%): 社会モデリングをテーマとしての発表**
   - 発表10分+質疑応答5分　→ 受講者の人数によって適宜調整する
   - 以下のいずれかを選び、発表資料を作成すること。
       - 社会モデリングに関する論文の紹介：論文の内容を正しく理解し、そのモデルの構造や特徴を聴衆に分かりやすく伝えるよう工夫すること。
       - 既存の社会モデリング手法を基に、自分が興味を持つ対象についてモデリングの構想を発表すること
       - 可能であればモデルの実装と結果の再現が望ましい。
