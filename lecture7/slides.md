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


ネットワークの概要

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
