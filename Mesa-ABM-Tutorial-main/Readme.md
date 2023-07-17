# Sugarscape Constant Growback Model with Traders
此为[英文版教程](https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial)的汉化版，
## 总结

This is Epstein & Axtell's Sugarscape model with Traders, a detailed description is in Chapter four of
*Growing Artificial Societies: Social Science from the Bottom Up.* (1996).
代码大致分为几个部分:资源类、交易主体类、模型类，然后是数据分析。

### 运行

任何笔记本电脑都可以通过谷歌Colab在其各自的会话运行,或下载并运行在您的本地机器，但需要[Jupyter]([https://www.codecademy.com/article/setting-up-jupyter-notebook)  

### 模型: 

模型类充当一个管理器，它实例化主体、场景、调度程序和数据收集器，并管理主体间的相互作用和排序。

### 主体: 

- **糖**: 糖(主体)以每个时间步骤一个单位的速度生长，可被贸易主体收获和交易。糖在整个场景中不均匀分布，糖山在空间的左上角和右下角。
- **香料**: 香料(主体)以每小时一个单位的速度生长，可被贸易主体收获和交易。香料在整个场景中不均匀分布，香料山在空间的右上方和左下方。
- **交易商**:交易商代理商具有以下属性:(1)糖代谢，(2)香料代谢，(3)视野， (4)初始糖禀赋， (5)初始香料禀赋。他们在这片土地上游走,收割糖和香料并其他代理商进行交易。如果糖或香料用完，它们就会从模型中移除。

交易员代理根据规则**M**游走场地:
- 在视野允许的范围内，向四个主要方格方向眺望，找出没有被占据的地点。
- 考虑仅未占据的位置，使用Cobb-Douglas函数找出能产生最大福利的最近位置。
- 移动到新位置
- 收集该地点上所有的资源(糖和香料)
 (Epstein和Axtell, 1996，第99页)

交易者根据规则**T**进行交易:
- 交易主体和潜在交易伙伴计算他们的边际替代率(MRS)，如果他们是相等的，结束。
- 交换资源，香料从边际替代率（MRS）较高的代理流向MRS较低的代理，糖则反向流动。
- 价格（p）是通过取代理人的MRS的几何平均数来计算的。
- 如果 p > 1，那么p单位的香料将被交换为1单位的糖；如果 p < 1，那么1单位的香料将被交换为1/p单位的糖。
- 交易发生的条件是：（a）它能使双方代理人更好（增加MRS）；并且（b）不会导致代理人的MRS相互交叉，否则就*结束*。
- 这个过程将一直重复，直到满足*结束*条件。
（Epstein和Axtell，1996，第105页）

该模型演示了几个Mesa的概念和特性：
 - 多网格
 - 多种类型的代理（交易者、糖、香料）
 - 当代理死亡时，动态地从网格和日程表中移除代理
 - 在模型和主体级别收集数据
 - 批处理运行器（即参数扫描）

### 额外资源

此代码通常与[Mesa-Example仓库](https://github.com/projectmesa/mesa-examples)中的sugarscape_g1mt文件夹中的代码相匹配。