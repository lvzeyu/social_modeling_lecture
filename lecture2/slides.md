---
theme: neversink
layout: cover
color: indigo-light
transition: slide-left
---
 
# モデリングの概要


東北大学文学研究科
計算人文社会学

**呂沢宇**   

行動科学概論　_社会科学におけるモデル入門_ <a href="https://lvzeyu.github.io/https:/github.com/lvzeyu/social_modeling_lecture" class="ns-c-iconlink"><mdi-open-in-new /></a> 


<div @click="$slidev.nav.next" class="mt-12 py-1" hover:bg="white op-10">
  Press Space for next page <carbon:arrow-right />
</div>

<div class="abs-br m-6 text-xl">

  <a href="https://github.com/lvzeyu/social_modeling_lecture" target="_blank" class="slidev-icon-btn">
    <carbon:logo-github />
  </a>
</div>




---
transition: fade-out
---

# データ分析とモデル

人間の認知限界とデータ分析

- 人間は様々な情報を処理して世の中を理解・制御している
    - 対象となるものの振る舞いが複雑すぎると、直感的な理解や制御が及ばない場合がある

<v-click>

> 対象から情報(**データ**)を取得して、それを分析することによって、その対象がどのようなメカニズム・ルールで働いているのかを客観的に理解・制御しようとするのが**データ分析**である。

</v-click>

<div style="text-align: center;">
```mermaid {theme: 'neutral', scale: 1}
classDiagram
direction LR

class 対象 {
  生物現象
  物理現象
  社会現象
  人間行動
}

class データ {
  多次元
  複雑な構造
  データの不足
}

対象 --> データ : 観測
データ --> 対象 : メカニズムを推測

```
</div>

<p v-click style="color: #4F46E5; font-size: 1.5em; text-align: center;">
  データを眺める以上の分析が必要ならモデルの出番
</p>



---
class: flex justify-center items-center gap-20 px-40 text-xl
---

<div
  absolute text-6xl
  :class="$clicks < 1 ? 'text-black' : 'translate-y--18 scale-40 text-black/30'"
  transition duration-500 ease-in-out
>
  <span>モデルって何？</span>
</div>


<div flex flex-col items-center>
  <v-clicks>
    <div mt-12>
      <h1 flex flex-col items-center text="4xl!" style="text-align: center; line-height: 1.4;">
        <span style="color: #4F46E5;">なんか数式がいっぱいあって、<br />難しそうなもの</span>
      </h1>
    </div>
  </v-clicks>
</div>


---
layout: two-cols-title
transition: fade-out
level: 1
---

:: title ::
# モデルのタイプ

:: left ::
<div class="flex flex-col items-center">
  <div style="display: flex; justify-content: center;">
    <img src="./image/hinan2.gif" width="500" />
  </div>
  <p class="text-sm text-center mt-2">現実を再現するモデル</p>
</div>

:: right ::
<div class="flex flex-col items-center">
  <div style="display: flex; justify-content: center;">
    <img src="./image/Harmonic.png" width="250" />
  </div>
  <p class="text-sm text-center mt-2">物理現象のモデル</p>
</div>






---
transition: fade-out
---

# モデルの役割

なぜモデルなのか

<v-clicks depth="2">

- モデルとは、対象のデータの生成ルールを模擬したものである
    - 実際の分析対象では、自由に観測したり、内部条件を変えて操作したりすることは普通できません
- 同じような振る舞いをするモデルを作ってしまえば、様々な用途がある
  - 形式としては、数学やコンピュータープログラムなどの形式言語で書けるようなもの(==Formal Model==)と、言葉や図で表現するもの(==Informal Model==)がある
  - **モデルの目的**：考えを伝えたり理解したりするため

</v-clicks>


<div style="text-align: center;">
```mermaid {theme: 'neutral', scale: 1}
stateDiagram
    direction LR

    state 分析対象
    state データ
    state モデル

    分析対象 --> データ : 観測
    モデル --> データ : 生成
    データ --> モデル : メカニズムを推測
    モデル --> 分析対象: 真似する
```
</div>


<!--
Here is another comment.
-->

---
transition: fade-out
---

# Informal Model

人間は常にモデルの視点を用いて思考している

<div class="grid grid-cols-3 gap-6 mt-10 items-start">
  <div class="flex flex-col items-center">
    <img src="./image/dare1.png" class="h-48 w-full object-contain rounded" />
  </div>
  <div class="flex flex-col items-center relative h-48">
    <img v-click="[1,2]" src="./image/Nidoran_black_white_bg.png" class="h-48 w-full object-contain rounded absolute inset-0" />
    <img v-click="2" src="./image/Nidoran.png" class="h-48 w-full object-contain rounded absolute inset-0" />
  </div>
  <div class="flex flex-col items-center relative h-48">
    <img v-click="[1,2]" src="./image/nidoran_female_black_white_bg.png" class="h-48 w-full object-contain rounded absolute inset-0" />
    <img v-click="2" src="./image/nidoran_female.png" class="h-48 w-full object-contain rounded absolute inset-0" />
  </div>
</div>


---
transition: fade-out
---

# Informal Model

人間は常にモデルの視点を用いて思考している

<div style="display: flex; justify-content: center;">
  <img src="./image/macdonald.png" class="h-100 object-contain rounded" />
</div>

---
transition: fade-out
---

# Informal Modelからモデルへの考察

<v-clicks depth="3">

- モデルとは、複雑な現実世界や抽象的な概念を、特定の目的のために**単純化・抽象化**し、分かりやすく構造化したもの
    - >「形状」で事物を区分する「モデル」
    - >「色」で事物を抽象化する「モデル」
- 人間の認知は 「直接現実を扱う」のではなく「表象」を扱う
    - 人間は現実をそのまま把握しているのではなく、常に何らかの「モデル」を通して世界を認識し、思考しているといえる
    - モデルとは、この「`分解された要素`」と「`その関係`」を記述したものでもある
- 同じ対象や現象であっても、目的や視点に応じて、異なるモデルを適用することが可能である

- 完全に正しいモデルは存在しない、あるのは、目的に応じて適切（あるいは最適）なモデルである

</v-clicks>


<v-clicks depth="3">

> All models are wrong, but some are useful. - George E. P. Box

</v-clicks>


---
layout: two-cols-title
transition: fade-out
---

:: title ::
# 科学におけるモデル

Formal Modelの概念と例

- Formal Model とは、現象を数式・論理・アルゴリズムなどの**形式言語**によって**明示的に**表現し、**検証可能**な形で構築されたモデルである

:: left ::
<div class="flex justify-center">
  <img src="./image/gravitation.png" class="h-60 object-contain rounded" />
</div>

:: right ::

- ニュートンの重力モデル
    - 明示的：変数が明確である
    - 分解（decomposition）：現象（落下・惑星運動）を質量、距離や力という要素に分解している
    - 関係の定式化
    - 検証可能：実験・観測で測定できる

---
transition: fade-out
---

# 科学におけるモデル

Formal Modelからの考察

<v-clicks depth="2">

- ニュートンの重力モデルは、惑星の公転軌道が円ではなく楕円であるという観測事実を踏まえ、それを説明する基盤の上に構築された
    - モデルは観測事実に基づく
- 「重さをもつ物体どうしが互いに引き合う」という発想それ自体は、ニュートン以前にも存在していた
   - それ以前にはそれを厳密に定式化し、予測や検証に耐える形で表現した `formal model` は存在しなかった
- ニュートンの重力モデルは重要な要素を抽出した抽象化である
   - 地球と太陽の関係に注目する一方で、天体の詳細な形状や材質、さらには当時まだ未知であった天体の影響などは基本的に扱っていない
- 地球上の落下現象や惑星の運動など他の現象にも同じモデルで説明できる
   - 未知の現象にも適用可能

</v-clicks>

---
transition: slide-up
level: 2
---

# モデルのタイプ

 どのようにモデルを作成するのか

<v-clicks depth="2">


- **具現化のアプローチ(Embodiment Approach)**
    - モデルには重要な構成要素が含まれ、できるだけ実際の現象を忠実に再現することを目的とする
    > 気象モデル: 天候を予測するための数値シミュレーションでは、大気の流れ、温度、湿度などの重要な変数を考慮し、風速や降水量の予測を行う    

- **アナロジーアプローチ(Analogy Approach)**
    - 現実のシステムを抽象化し、別のよく理解されたシステムとの類似性を活用することで、モデリングを行う
  > 例：情報の拡散は病気のようにモデリングできる；生物の進化論を制度や文化の進化に応用する

</v-clicks>


---
layout: two-cols-title
transition: slide-up
level: 2
---

:: title ::
# モデルのタイプ

具現化のアプローチ

:: left ::

- 現象の再現性と説明力の向上を目指し、現実問題への応用に直結する志向

- **例: 避難行動モデル**
  - 災害発生時避難行動をモデル化することで、誰が、いつ、どこへ、どのルートで避難するのかを予測
  - 防災行動計画の立案を支援する

:: right ::
<div class="flex flex-col items-center">
  <v-switch>
    <template #1>
      <img src="./image/information_2-6.jpg" alt="Image 1" class="h-64" />
    </template>
    <template #2>
      <img src="./image/uc22-031_verification_1.jpg" alt="Image 2" class="h-64" />
    </template>
    <template #3>
      <img src="./image/uc22-031_achievements_3.jpg" alt="Image 3" class="h-64" />
    </template>
    <template #4>
      <img src="./image/uc22-031_verification_2.png" alt="Image 4" class="h-64" />
    </template>
  </v-switch>
</div>





---
transition: slide-up
level: 2
---

# モデルのタイプ

アナロジーアプローチ

<v-clicks depth="3">


- 特定の対象を**直接的にモデル化することは難しい**場合、**すでに理解されている別のシステム**と類似点を見出し、それを活用してモデリングを行う

> 問題：牛の革の量を推定するために、牛の体表面積を求めなさい

- **扱いにくい問題**：牛は複雑な形状をしており、体の各部位ごとの曲率や凹凸が存在するため、正確な体表面積の計算が難しい
- **既に理解しているシステム**：球体の表面積は公式で簡単に計算できる
- 牛全体をひとつの球体とみなす
    - 牛の代表的な寸法（例えば、体長や幅）から「平均的な半径$r$」を定める
- 球体の表面積公式で牛全体の革面積の近似値とする
- 切断ロスや余裕部分、部分的な重なりなどを考慮し、後に補正係数を適用する

</v-clicks>


---
transition: slide-up
level: 2
margin: tight
---

# アナロジーアプローチ

簡単なモデルでも色々な問題に応用できる：囚人のジレンマを例として

- 囚人のジレンマモデル
    - **ゲーム理論**における有名な非協力ゲーム
    - 2人の囚人が**協力**するか**裏切る**かを選択する状況

|  | **囚人Bが協力** | **囚人Bが裏切る** |
|---|---|---|
| **囚人Aが協力** | (−1, −1) | (−3, 0) |
| **囚人Aが裏切る** | (0, −3) | (−2, −2) |

<v-clicks depth="3">
 

- **協力**: 2人とも1年間の懲役
- **裏切り**: 裏切った方は釈放、裏切られた方は3年間の懲役
- **相互裏切り**: 2人とも2年間の懲役

</v-clicks>


---
transition: slide-up
level: 2
margin: tight
---

# アナロジーアプローチ

簡単なモデルでも色々な問題に応用できる：囚人のジレンマを例として

|  | 囚人Bが協力 | 囚人Bが裏切る |
|---|---|---|
| **囚人Aが協力** | (−1, −1) | (−3, 0) |
| **囚人Aが裏切る** | (0, −3) | (−2, −2) |

<v-clicks depth="3">

- 各囚人は**個別の最適戦略**として「`裏切る`」選択をする
  - もし囚人Bが協力すると考えるなら、囚人Aは「`裏切る`」ことで0年の懲役となり有利
  - もし囚人Bが裏切ると考えるなら、囚人Aが「`協力`」すると3年、裏切ると2年の懲役となるため「`裏切る`」方が有利
  - どちらのケースでも「`裏切る`」方が懲役が短くなるため、囚人Aは合理的に「`裏切る`」を選択
  - 囚人Bも同様に考えるため、結果として両者が「`裏切る`」を選び、(−2, −2) となる
- もし**協力**していれば (−1, −1) の方が良かったのに(`社会的最適`)、達成できない

</v-clicks>




---
transition: slide-up
level: 2
---

# アナロジーアプローチ

<v-clicks depth="3">

簡単なモデルでも色々な問題に応用できる：囚人のジレンマを例として

- 囚人のジレンマでは、個々の合理的選択が全体として非効率な結果を招くことを説明できる
    - 色々な社会現象を囚人のジレンマのように表現し、アナロジーアプローチで分析することができる

- 企業間の価格競争
    - 競合する企業同士が価格を下げることで市場シェアを拡大しようとする場合、双方が値下げを行うと利益が減少
    - 一方のみが値下げすると、その企業が市場シェアを獲得できる
    - 両社ともに値下げを選択し、結果として双方の利益が減少する

- 環境問題における国際協力
- 日用品の買い占め

</v-clicks>

<!--
各国が環境保護のために協力することが望ましいものの、各国は自国の経済成長を優先し、環境対策を怠る可能性があります。全ての国が協力すれば環境改善が期待できますが、一部の国が協力を怠ると、全体の環境対策が効果を失うことになります。
災害時などにおいて、個人が必要以上に物資を買い占めると、他の人々が必要な物資を入手できなくなります。全員が冷静に行動すれば物資は行き渡りますが、他者が買い占めることを恐れて自らも買い占めに走ると、結果として全体の物資不足が深刻化します。
-->


---
transition: slide-up
level: 2
---

# アナロジーアプローチ

アナロジーアプローチの観点からのモデリングの注意点

<v-clicks depth="3">


- 異なる社会現象でも共通のメカニズムで考えられる
- 典型的なモデルでは多様な社会現象の説明に活用できる
    - 典型的なモデルの本質的な考え方を把握
  - モデルの転移可能性を常に意識する
- 対象や文脈に応じて拡張する必要性
  - 例: 繰り返しゲームへの拡張
    - 国家間の協力や企業間競争の分析には、単発の意思決定だけでなく、繰り返しの対話がある状況（長期的な競争・協力関係）に拡張する

</v-clicks>

---
transition: fade-out
level: 2
---

# モデリングの二つの原理

<v-clicks depth="3">


- KIDS原理：Keep It Descriptive, Stupid

    - 現実世界の複雑さを忠実にモデル化することを優先する
    - 目的：実際の社会現象のリアリティと妥当性を確保する

-  KISS原理：Keep It Simple, Stupid
    - できるだけ単純なモデルを構築する
    - 目的：モデルの理解しやすさ、透明性、汎用性を高める
       - 「分析志向」のシミュレーションでは重視される
       - 関連する学術領域の理論との比較と接合が容易となる

</v-clicks>


<p v-click style="color: #4F46E5; font-size: 1.5em; text-align: center;">
  KISSとKIDSは対立概念ではなく補完的な関係にある
</p>




---
transition: fade-out
level: 1
---

# モデリングの目的

推論

<v-clicks depth="3">

- **推論**とは、現実世界の現象や仕組みを抽象化して、数理的・形式的なモデルを用いて未知の情報を**導き出す**ことを意味する。
    - 対象物の特徴や構造を明確にする
    - モデル内の要素がどのように相互作用し、どのようにまとまることを記述(定義)する
    - どのような条件からどのような結果を生み出されるのか、それはなぜなのかを導き出す。

- 形式論理による推論は、正確な関係を導き出せることだけでなく、ときには直感に反するような予想外の関係を見つけ出すこともできる

- 論理は主張が正しくなる条件を明らかにする
  - 同じ問題に対して相反する論述は、どちらも正しそうに見える場合もある
   - モデルは前提を設けた上で定理を証明する
      - 相反する予測結果や説明が出てきたりするのは、前提が異なるため

</v-clicks>


---
transition: fade-out
level: 2
---

# モデリングの目的

理解

<v-clicks depth="3">

**理解**: 経験的な現象に(検証可能な)説明を与える

- モデルは経験的現象に明快で論理的説明を与える
    - モデル構造から説明する方法では、モデルを作るときに仮定して良いと思われる経験事実・観測事実からボトムアップ的に論理を構成する

- モデルは、直感と一致する結果も反直感的な結果もともに説明できる

<div class=" bg-gray-200 p-4 rounded">
需要と価格の関係モデル：需要が増えると価格が上がる

- 商品需要が上昇すると、短期的に価格も上昇する
- 長期的に見れば、需要の増加は価格を低下させることもある: 需要の増加は、大量生産の効果のため価格の低下を引き起こす
</div>

</v-clicks>


---
transition: fade-out
level: 2
---

# モデリングの考察

モデルによる予測と探索

<v-clicks depth="3">

- モデルは、個別の事象も全体的傾向も予測できる
- モデルの予測と説明には密接な関係がある
    - 説明が予測を補強する
    - 予測が説明を検証する
    - 説明なしで予測できる場合もある
        - 深層学習モデル

- モデルは直感や可能性を探るために使われる
    - モデルを通じて、まだ観測されていないパターンや動作の可能性を探る
  - モデルのパラメータに、あえて現実の状況とは異なる値を入れて、対象の振る舞いをシミュレートする

</v-clicks>

<!--
仮想的に現実とは異なるパラメータ（例えば、道路の容量を意図的に小さく設定する、特定の時間帯の交通量を極端に増加させる）を与えることで、渋滞がどのように発生し、どのように拡大するかを観察できます。これにより、モデルの挙動や実際の交通状況に対する理解が深まります。
-->



---
transition: fade-out
level: 2
---

# モデリングの例

自然渋滞の問題

<v-clicks depth="3">

- モデルがデータを説明できるということは、モデルを作るときに仮定したモデル構造が正しかった可能性が高い

- 自然渋滞：高速道路では、事故でもないのに自然に渋滞が発生する
    - なぜ自然渋滞が発生するのか?


<div class="grid grid-cols-2 gap-4 mt-8">
  <img src="./image/traffic1.jpg" class="w-full rounded shadow" />
  <img src="./image/traffic2.jpg" class="w-full rounded shadow" />
</div>

> <p v-click>濃い黒色のクルマは、自分の前にスペースがなかったために、1秒前の時点から動けなかったクルマを表している。</p>

> <p v-click>道路上のクルマの数が増えて密度が高くなると、動けないクルマが出てくる。つまり、渋滞が発生することになる。</p>


</v-clicks>

---
transition: fade-out
level: 2
---

# モデリングの例

自然渋滞のモデリング

<v-clicks depth="3">

> 車間が詰まってくるほど遅い速度に調整

> 車間距離が十分に長ければ一定の最高速度に調整

- それぞれの車の動き（加速度）を方程式で表してみる(モデル化)
  - 最適速度モデル：ドライバーが車間距離に応じてアクセル・ブレーキ(車の加速度)を操作する様子を数式で定義する

$$
\frac{dv_i}{dt} = a \left( V(h_i) - v_i \right)
$$

- $v_i$ : 車両 $i$ の速度
- $h_i = x_{i-1} - x_i$ : 前方車両 $i-1$ との車間距離
- $x_i$ : 車両 $i$ の位置
- $V(h)$ : 最適速度関数（ここで、$h_i$に応じて何らかの形で車両が取りたい速度を決めると思ってよい）
- $a$ : 速度調整の応答係数（運転者の反応速度に関係）

</v-clicks>


---
transition: fade-out
level: 2
---

# モデリングの考察

モデルによる推論と説明

<v-clicks depth="3">

- 自然渋滞のモデリングに従って、仮想的な車たちを動かしてみることができる[(demo)](https://kaityo256.github.io/ov_model/)
    - 結果的には、モデルの中でも自然に渋滞が発生
  - モデルで仮定した数理構造(車の速度の変化を表したもの)から、対象としている現象を再現することができる
    - このモデルをさらに分析すると、「渋滞が発生する時には、車の速度の変動が後ろの車に伝わっていくにつれて拡大する」という論理的な説明や、渋滞が発生する混雑条件などが明らかになる

</v-clicks>

<div style="display: flex; justify-content: center;">
  <img src="./image/velocity_example.png" width="500" />
</div>  



---
transition: fade-out
level: 2
---

# モデリングの考察

モデルによる推論と説明

<v-clicks depth="3">

- **推論**: モデルで仮定した数理構造(車の速度の変化を表したもの)から対象としている現象を再現することができる
    - モデルを用いると、どのような車間距離や交通密度のもとで渋滞が自発的に発生するかを推論できる
        - 「なぜ原因がないのに渋滞が発生するのか？」という問いに対する因果的理解を提供する
    - 「モデルは自明なことを言い直しているだけ」?
        - モデルの推論が、「条件$A$が満たされれば結果$B$が伴う」というように、**条件付き**の形を取っている

- **説明**: 個々のドライバーがわずかにブレーキを踏むことが、後続車に波及して渋滞を生むメカニズムで説明できる
    - 渋滞を「個人レベルの行動の連鎖が集団的な非直感的なパターンを生む現象」として説明できる
    - 直感的には、事故や信号の故障など明確な外的原因によって渋滞が発生すると想定される(はず)
    - ミクロ（ドライバーの行動）からマクロ（交通流の集団挙動）への因果構造

</v-clicks>


---
transition: fade-out
level: 2
---

# モデリングの考察

モデルによる予測と探索

<v-clicks depth="3">

- モデルを用いると、現時点での交通密度が一定のしきい値を超えた場合、渋滞がどの地点でどのように発生・波及するかをシミュレーションで予測できる
- 異なる車種や運転手と反応速度の違いを仮定してモデルを動かすと、意外な渋滞パターンや緩和戦略が発見される
    - 「現実では試すことが難しい条件」を仮想的に試す思考実験の道具としてモデルを使う
    -  自動運転車が数台入るだけで渋滞波が大幅に減少する可能性がモデルから示唆されている（[Stern et al., 2018](https://www.sciencedirect.com/science/article/pii/S0968090X18301517)）

</v-clicks>

<!--
仮想的に現実とは異なるパラメータ（例えば、道路の容量を意図的に小さく設定する、特定の時間帯の交通量を極端に増加させる）を与えることで、渋滞がどのように発生し、どのように拡大するかを観察できます。これにより、モデルの挙動や実際の交通状況に対する理解が深まります。
-->




---
transition: fade-out
level: 1
---

# まとめ

モデルの軸

基本的に、モデルは二つの軸で整理することができる

<v-clicks depth="3">


- 目的：「分析」ー「設計」
  - 「分析志向」:ある現象に対して、その現象が生じるメカニズムを明らかにし、新たな理論を構築しようとする
    - 「設計志向」:ある現象に対して、ある介入を実施したりシステムに導入することで状態がどのように変わりうるのかを予測する

- 対象: 「具体」ー「抽象」
    - 「具体的志向」:特定の社会現象(例えば対象のデータが現実的に収集できるレベル)を対象にする
  - 「抽象的志向」:観察される現象一般を統一的に扱おうとする

</v-clicks>

<p v-click style="color: #3E1586; font-size: 1.5em; text-align: center;">
  モデルは極にのみ存在するものではない
</p>




---
transition: fade-out
level: 2
---

# まとめ

<v-clicks depth="3">

注意: 説明力があるモデル $\neq$ 真のモデル 

- 現象が説明されたとしても、そのモデルを構成するすべての要素が正しいとは言えません
    - モデルの構成には、現実の単純化・理想化が含まれており、説明力があっても一部の前提が現実から乖離している可能性がある
        - モデルの定義に不適切な要素が含まれると、結果の解釈のしやすさやモデルの妥当性に悪い影響を与える
    - モデル構造から説明する方法では、モデルを作るときに仮定して良いと思われる経験事実・観測事実からボトムアップ的に論理を構成する
        - どのような仮定を置くのかに注意する必要がある
        - 単純化しすぎていないか
        - 他の解釈可能性を排除していないか

</v-clicks>


---
transition: fade-out
level: 2
---

# まとめ

モデルの思考に慣れるように

<v-clicks depth="3">

- 抽象化：本質的な要素を抜き出す
- 前提を明示する: 「何を仮定するか」によって、モデルの構造も結果も変わることを意識する
- 因果を構造でとらえる: 結果から逆に構造を推測したり、「なぜそうなるのか」を関係で捉える

</v-clicks>


