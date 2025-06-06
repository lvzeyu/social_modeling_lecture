# 課題１
1000個のノードと約3000個のリンクからなるランダムネットワークをつくたいとする。この結果が得られるリンクの生成確率pを求めよ。

ランダムネットワーク（Erdős–Rényiモデル）において、リンクの期待数は以下で表されます：

$$
期待リンク数 = p \cdot \binom{N}{2} = p \cdot \frac{N(N - 1)}{2}
$$

与えられた条件：$N = 1000,\quad \text{リンク数} = 3000$を代入して$p$を求めます：

$$
3000 = p \cdot \frac{1000 \cdot 999}{2}
\Rightarrow p = \frac{3000 \cdot 2}{1000 \cdot 999}
= \frac{6000}{999000}
\approx 0.00601
$$

# 課題2

ランダムネットワークが社会的ネットワークのモデルとして不適切な原因を以下のうちから選び、その理由を説明しなさい。

a. ランダムネットワークは典型的に連結していない
b.ランダムネットワークは平均最短経路が短い
c.ランダムネットワーク内のノードは非常に異なる次数を持つ
d.ランダムネットワークはクラスター係数が低い

✅ d.クラスター係数が低い

- 社会的ネットワークの重要な特徴の一つに、「友人の友人は、自分も友人である可能性が高い」という傾向があります。これは高いクラスター係数として現れます。つまり、ネットワーク内に友人関係の密集したグループ（クラスター）が多く存在します。

- 一方、ランダムネットワーク（Erdős-Rényiモデル）では、ノード間のリンクは完全にランダムに決定されます。そのため、あるノードの2つの隣接ノード同士がリンクで結ばれている確率は、ネットワーク全体のリンク生成確率$p$と同じになり、非常に低くなります。

- この結果、ランダムネットワークのクラスター係数は、同じ規模の現実の社会的ネットワークに比べて著しく低くなり、現実の社会構造をうまく表現できないため、モデルとして不適切とされます。

3.WSモデルは、ランダムネットワークには見られない現実世界のネットワークのどの性質を捉えるのに有効か？

WSモデル（Watts-Strogatzモデル）は、現実世界の多くのネットワークが持つ**「スモールワールド性（Small-world property）」**を捉えるのに有効です。

スモールワールド性とは、以下の2つの性質を併せ持つことを指します。

- 短い平均最短経路 (Short average path length): ネットワーク内の任意の2つのノード間を、驚くほど少ないステップで到達できる。（ランダムネットワークもこの性質を持つ）
- 高いクラスタリング (High clustering coefficient): あるノードの隣人同士もまた隣人である確率が高い。（レギュラーネットワークの特徴）

WSモデルは、規則的なネットワーク（高いクラスタリング）から始めて、ごく少数のリンクをランダムにつなぎ変えることで、高いクラスタリングを維持したまま、平均最短経路を劇的に短くできることを示しました。