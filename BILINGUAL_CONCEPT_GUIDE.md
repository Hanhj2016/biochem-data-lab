# BioChem Data Lab Bilingual Concept Guide  
# BioChem Data Lab 双语概念导览

## Purpose / 用途

This guide summarizes the main notebooks, code recipes, and synthetic datasets in BioChem Data Lab. It is written for learners who may come from software, IT, data analysis, or general science backgrounds.

本导览总结 BioChem Data Lab 中主要 notebooks、code recipes 和合成数据集，面向具有软件、IT、数据分析或普通科学背景的学习者。

All datasets are synthetic and educational. They are not clinical, diagnostic, regulatory, drug-efficacy, patient, proprietary, or real experimental evidence.

所有数据均为合成教学数据，不是临床、诊断、监管、药效、病人、专有或真实实验结论证据。

---

## Quick Mental Model / 快速理解框架

| BioChem concept | Plain meaning | IT/software analogy | Daily-life analogy |
|---|---|---|---|
| Enzyme | Biological catalyst | Worker/service | Kitchen worker or machine |
| Substrate | Material an enzyme processes | Input/request/job | Raw ingredient |
| Enzyme activity | How fast/effectively enzyme works | Throughput | Items processed per minute |
| Control | Baseline condition | Default config | Original recipe |
| Treatment | Changed condition | Modified config | Recipe with one changed ingredient |
| Dose/concentration | Strength of treatment | Load/parameter value | Salt/coffee/cleaner amount |
| Response | Measured outcome | Health metric | Plant health or color intensity |
| Replicate | Repeated measurement | Repeated benchmark run | Measuring temperature several times |
| QC | Quality control | Log/environment check | Checking a scale before trusting weight |
| Outlier/review flag | Point worth checking | Suspicious benchmark run | One impossible body-weight reading |
| Standard curve | Calibration relationship | Sensor calibration model | Using known weights to calibrate a scale |
| Gene expression | Gene signal level | Module activity/log signal | Department activity level |
| PCA | Compress many features into 2D | Observability summary | Map made from many ratings |
| Heatmap | Color-coded matrix | Monitoring dashboard | Colored classroom score table |

---

## Core Cautions / 核心注意事项

English:
- Describe patterns cautiously: “is consistent with”, “appears lower”, “suggests a pattern”.
- Do not say synthetic data proves mechanism, treatment effect, diagnosis, or drug efficacy.
- Always check replicates, variability, missing values, and quality flags before interpreting.
- A graph is not a conclusion; it is a way to inspect evidence.

中文：
- 谨慎描述模式：可以说“与某种趋势一致”“看起来较低”“提示一种模式”。
- 不要说合成数据证明机制、治疗效果、诊断或药效。
- 解释前先检查重复测量、波动、缺失值和质量标记。
- 图形不是结论，而是帮助检查证据的工具。

---

## Notebook and Data Map / Notebook 与数据对应表

| Topic | Notebook or recipe | Main dataset | Main learning goal |
|---|---|---|---|
| Enzyme activity | `01_Enzyme_Activity_Python.ipynb` | `data/enzyme_activity_sample.csv` | Compare control vs treatment means |
| t-test | `02_T_Test_Python.ipynb` | `data/enzyme_activity_sample.csv` | Test two-group mean difference |
| ANOVA | `03_ANOVA_Python.ipynb` | `data/anova_cell_viability_sample.csv` | Compare more than two groups |
| Dose-response | `04_Dose_Response_Python.ipynb` | `data/cell_viability_sample.csv` | Plot viability across concentrations |
| Gene expression | `05_Gene_Expression_Python.ipynb` | `data/gene_expression_toy.csv` | Calculate log2 fold change |
| Dose-response plot recipe | `code_recipes/python/06_dose_response_plot_python.py` | summarized dose-response data | Reusable Plotly function |
| IC50-style curve fitting | `07_Advanced_IC50_Curve_Fitting_Python.ipynb` | `data/dose_response_ic50_sample.csv` | Fit educational dose-response curves |
| Data QC/outliers | `08_Advanced_Data_QC_Outlier_Visualization_Python.ipynb` | `data/qc_outlier_sample.csv` | Review suspicious replicate values |
| PCA/heatmap | `09_Advanced_PCA_Heatmap_Gene_Expression_Python.ipynb` | `data/gene_expression_matrix_toy.csv` | Visualize gene expression patterns |
| Capstone | `10_Capstone_BioDose_Advanced_Challenge.ipynb` | drug-response scenario datasets | Combine ranking, QC, and cautious interpretation |
| Graphical showcase | `11_Graphical_Showcase_Python.ipynb` | multiple synthetic datasets | See many graph types in one place |
| AI bridge | `13_BioDose_AI_Bridge_Python.ipynb` | drug-response scenario datasets | Turn analysis into AI-safe summaries |
| Experimental design | `14_Experimental_Design_and_Replicates_Python.ipynb` | `data/enzyme_activity/enzyme_activity_three_groups.csv` | Understand controls and replicates |
| Enzyme kinetics | `15_Enzyme_Kinetics_Michaelis_Menten_Python.ipynb` | `data/enzyme_kinetics/*.csv` | Understand saturation, Km, Vmax |
| Bradford assay | `16_Standard_Curve_Bradford_Assay_Python.ipynb` | `data/standard_curves/bradford_standard_curve.csv` | Estimate unknown protein concentration |
| Plate QC | `17_Assay_QC_Plate_Layout_Python.ipynb` | `data/assay_qc/plate_layout_edge_effect.csv` | Detect spatial/edge effects |
| qPCR | `18_qPCR_Delta_Delta_Ct_Python.ipynb` | `data/qpcr/qpcr_delta_ct_sample.csv` | Calculate relative expression |
| Growth curve | `19_Growth_Curve_OD600_Python.ipynb` | `data/growth_curve/bacterial_growth_curve.csv` | Interpret OD600 over time |
| Sequence basics | `20_Sequence_Basics_GC_Content_Python.ipynb` | `data/sequences/synthetic_sequences.csv` | Summarize DNA strings |
| Sequence recipe | `code_recipes/python/16_sequence_basics_python.py` | `data/sequences/synthetic_sequences.csv` | Reusable sequence functions |
| AI summary review | `21_AI_LLM_Lab_Summary_Review_Python.ipynb` | `data/ai_literacy/ai_lab_summary_review_cases.csv` | Review AI-style summaries for overclaims |
| Career/academic tracks | `22_Career_Academic_Advancement_Tracks_Python.ipynb` | `data/career_scenarios/*.csv` | Practice role-based lab and portfolio scenarios |

---

## 1. Enzyme Activity, t-test, ANOVA, and Replicates  
## 1. 酶活性、t 检验、ANOVA 与重复测量

### English

Enzyme activity means how strongly or quickly an enzyme performs its reaction. In the simplest notebook, `control` is the baseline condition and `treatment` is a changed condition. The sample dataset shows control activity around 100 and treatment activity around 87.5, so the teaching pattern is lower activity in treatment.

The t-test notebook asks whether two group means are different relative to within-group variation. Its output, such as `t statistic: 9.029` and `p-value: 0.0001`, means the observed synthetic group difference is large compared with the small replicate variation. It does not prove mechanism.

The ANOVA notebook extends this idea to more than two groups: control, low dose, medium dose, and high dose. ANOVA asks whether at least one group mean differs, but it does not directly identify every pairwise difference.

The experimental design notebook adds a deeper question: are there enough replicates, is there a control group, and is variability visible? SD describes the spread of individual observations. SEM describes uncertainty around the estimated mean.

### 中文

酶活性表示酶工作得多快或多有效。最基础的 notebook 中，`control` 是 baseline 对照条件，`treatment` 是改变后的条件。示例数据中 control 平均约 100，treatment 平均约 87.5，所以教学模式是 treatment 组酶活性较低。

t-test notebook 问的是：两组均值的差异，相对于组内波动来说是否明显。例如 `t statistic: 9.029` 和 `p-value: 0.0001` 表示在合成数据中，两组差异相对于重复测量波动很大。但这不证明机制。

ANOVA notebook 把比较扩展到多组，例如 control、low dose、medium dose、high dose。ANOVA 问的是“是否至少有一组均值不同”，但不会直接告诉你每一对组之间具体如何不同。

实验设计 notebook 进一步强调：是否有对照组、重复数是否平衡、组内波动是否可见。SD 描述单个观测值的分散程度；SEM 描述均值估计的不确定性。

---

## 2. Dose-Response, IC50-style Fitting, QC, and BioDose AI Bridge  
## 2. 剂量-反应、IC50 风格拟合、质量检查与 BioDose AI Bridge

### English

Dose-response analysis asks how a measured response changes as concentration increases. In the synthetic cell viability datasets, higher concentration is associated with lower viability. This resembles a pressure-test curve: as load increases, system health decreases.

Plotting dose-response curves often uses a log-scale x-axis because concentrations span orders of magnitude. Tick labels such as `2` and `5` can represent intermediate log ticks like 0.02, 0.05, 0.2, or 0.5 depending on the decade.

IC50-style notebooks fit a curve to estimate where the response reaches a midpoint-like region. A lower educational IC50-style estimate means the curve drops earlier in this synthetic example. It is not drug potency evidence.

QC notebooks remind students that suspicious values should be reviewed, not automatically deleted. A red `review` point is a prompt to inspect raw data, replicate structure, or plate conditions.

The BioDose AI Bridge creates a structured markdown summary that AI can safely use for explanation. The AI relationship is not “AI decides the science”; it is “AI receives a cautious, structured summary and helps with wording, questions, and interpretation boundaries.”

### 中文

剂量-反应分析关注：随着浓度升高，测量结果如何变化。在合成 cell viability 数据中，浓度越高，细胞活力指标越低。它类似系统压力测试：负载越高，系统健康分数越低。

dose-response 图常用 log scale，因为浓度跨度可能跨越多个数量级。x 轴上反复出现的 `2` 和 `5` 常是对数坐标中的中间刻度，例如 0.02、0.05、0.2、0.5，具体取决于所在数量级。

IC50-style notebook 用曲线拟合估计 response 到达中间下降区域的大致浓度。较低的 educational IC50-style estimate 表示在这个合成例子中曲线更早下降，但它不是药效证据。

QC notebook 提醒学生：可疑值应该 review，而不是自动删除。红色 `review` 点表示需要检查原始数据、重复测量结构或 plate 条件。

BioDose AI Bridge 会生成结构化 markdown 摘要，让 AI 可以安全地辅助解释。它和 AI 的关系不是“AI 做科学结论”，而是“AI 基于谨慎、结构化的结果帮助改写、提问和提醒解释边界”。

---

## 3. Gene Expression, Heatmap, PCA, and qPCR  
## 3. 基因表达、热图、PCA 与 qPCR

### English

Gene expression means how strongly a gene signal appears under a condition. Fold change compares treatment mean to control mean. Log2 fold change makes increases and decreases easier to compare: +1 means about 2-fold higher, -1 means about half.

Heatmaps show many gene-by-sample values as colors. In gene-wise z-score heatmaps, each gene is scaled relative to its own average, so the color answers: is this gene high or low in this sample compared with its own typical level?

PCA plots in this project usually show samples, not genes. Genes are the features used to position samples. If control, low treatment, and high treatment samples separate on PC1, it suggests broad expression-pattern differences in the synthetic matrix.

qPCR uses Ct values. Lower Ct means the signal reached threshold earlier, usually indicating more starting material. Delta Ct normalizes target gene Ct to a housekeeping gene such as GAPDH. Delta-delta Ct compares treatment to control. `2^-ddCt` gives relative expression.

### 中文

基因表达表示某个基因在某个条件下的信号强弱。fold change 比较 treatment 平均值与 control 平均值。log2 fold change 让升高和降低更对称：+1 约等于 2 倍升高，-1 约等于降低到一半。

热图用颜色表示大量 gene-by-sample 数值。在 gene-wise z-score heatmap 中，每个基因相对于它自己的平均水平被标准化，因此颜色回答的是：这个基因在这个样本中相对自己平常水平是高还是低？

本项目中的 PCA 图通常显示 sample，而不是 gene。gene 是决定 sample 位置的特征。如果 control、low treatment、high treatment 在 PC1 上分开，说明这个合成矩阵中存在整体表达模式差异。

qPCR 使用 Ct 值。Ct 越低，表示信号越早达到阈值，通常代表起始信号越多。Delta Ct 用 GAPDH 等 housekeeping gene 对目标基因归一化。Delta-delta Ct 比较 treatment 与 control。`2^-ddCt` 得到相对表达量。

---

## 4. Plate QC and Spatial Effects  
## 4. 孔板质量检查与空间效应

### English

A 96-well plate is an 8 by 12 grid of wells, but plate QC ideas apply to other formats too. Each well is like one small experimental container. A heatmap helps reveal row, column, and edge patterns that a table may hide.

Edge wells are the outer wells: row A, row H, column 1, and column 12. Edge effects can happen because evaporation, temperature, or incubation conditions differ at the plate boundary.

The plate QC notebook compares edge and non-edge wells. In the synthetic data, edge wells tend to have lower viability. That means treatment interpretation should be cautious if treatment placement overlaps with edge positions.

### 中文

96-well plate 是 8 x 12 的孔板，但 plate QC 的思想也适用于其他孔板格式。每个 well 都像一个小实验容器。Heatmap 能显示表格中不容易发现的行、列和边缘模式。

Edge wells 是最外圈孔：A 行、H 行、1 列、12 列。边缘效应可能来自蒸发、温度、孵育条件等位置差异。

Plate QC notebook 比较 edge wells 与 non-edge wells。在合成数据中，edge wells 的 viability 倾向较低。因此如果 treatment 大多放在边缘位置，就要谨慎解释 treatment effect。

---

## 5. Michaelis-Menten Enzyme Kinetics  
## 5. Michaelis-Menten 酶动力学

### English

Michaelis-Menten-style enzyme kinetics asks how initial velocity changes as substrate concentration increases. At low substrate, velocity rises quickly. At high substrate, velocity begins to level off because enzymes become saturated.

The model is:

```text
velocity = (Vmax * substrate) / (Km + substrate)
```

`Vmax` is the maximum-like velocity. `Km` is the substrate concentration where the velocity reaches about half of Vmax. In this project, these are educational estimates from synthetic data.

Clean and noisy datasets can show the same saturation pattern. The noisy data may still fit similarly, but larger error bars mean less confidence in exact parameters.

### 中文

Michaelis-Menten 风格酶动力学关注：底物浓度增加时，初始反应速度如何变化。低底物浓度时，速度快速上升；高底物浓度时，速度逐渐变平，因为酶接近饱和。

模型为：

```text
velocity = (Vmax * substrate) / (Km + substrate)
```

`Vmax` 是类似最大速度的参数。`Km` 是速度达到约一半 Vmax 时的底物浓度。本项目中的这些参数都是合成数据的教学估计。

Clean 和 noisy 数据都可能显示相同的饱和模式。Noisy 数据的拟合结果可能接近 clean 数据，但误差线更大表示对精确参数的信心更低。

---

## 6. Bradford-style Standard Curve  
## 6. Bradford 风格标准曲线

### English

A Bradford-style assay estimates protein concentration from absorbance at 595 nm. Standards with known concentrations are used to fit a calibration line. Unknown sample absorbance values are converted back into concentration estimates.

A linear fit may look excellent, for example with high `r_squared`, but estimates are safest inside the tested standard range. If an unknown is above the highest standard, it is extrapolated and should be reviewed. A real workflow might dilute and re-run the sample.

### 中文

Bradford 风格实验通过 595 nm 吸光度估计蛋白浓度。已知浓度的 standards 用来拟合校准线。未知样本的 absorbance 再通过这条线反推浓度。

即使线性拟合很好，例如 `r_squared` 很高，估计值也最好落在标准曲线范围内。如果未知样本高于最高 standard，就是外推，需要 review。真实实验中通常会稀释后重新测定。

---

## 7. Growth Curves and OD600  
## 7. 生长曲线与 OD600

### English

OD600 measures optical density at 600 nm and is often used as an indirect indicator of microbial culture density. Higher OD600 usually means a cloudier culture.

Growth curves often include lag phase, log phase, and stationary phase. The growth notebook estimates a log-phase rate from a selected time window, such as 2 to 6 hours. In the synthetic data, StrainA has a higher estimated rate and shorter doubling time than StrainB in that window.

### 中文

OD600 是 600 nm 下的光密度，常用作微生物培养密度的间接指标。OD600 越高，培养液通常越浑浊。

生长曲线常包括 lag phase、log phase 和 stationary phase。Growth notebook 从特定时间窗口估计 log-phase rate，例如 2 到 6 小时。在合成数据中，StrainA 在该窗口内估计增长率更高、倍增时间更短。

---

## 8. Sequence Basics: GC Content, Motifs, Reverse Complement  
## 8. 序列基础：GC 含量、motif、反向互补

### English

DNA sequences can be treated as strings made of A, T, G, and C. Sequence basics notebooks calculate length, GC content, motif counts, and reverse complements.

GC content is:

```text
(G count + C count) / sequence length * 100%
```

G-C pairs are usually more stable than A-T pairs, but GC content alone does not prove function.

A motif is a short sequence pattern such as `ATG`. Finding `ATG` is useful practice, but a short motif does not automatically prove biological meaning. Reverse complement uses base-pair rules A/T and G/C and reverses orientation.

### 中文

DNA 序列可以看成由 A、T、G、C 组成的字符串。序列基础 notebooks 会计算长度、GC content、motif 次数和 reverse complement。

GC content 公式是：

```text
(G 的数量 + C 的数量) / 序列长度 * 100%
```

G-C 配对通常比 A-T 更稳定，但 GC content 本身不能证明功能。

motif 是短序列模式，例如 `ATG`。找到 `ATG` 是有用练习，但短 motif 不会自动证明生物学意义。Reverse complement 根据 A/T、G/C 配对规则生成互补链并反转方向。

---


## 9. AI/LLM Review and Career/Academic Advancement  
## 9. AI/LLM 审阅与职业/学术发展

### English

The AI/LLM review notebook teaches students to treat AI-written scientific text as a draft, not as evidence. The task is to compare an AI-style sentence with the actual dataset or figure, then revise overclaims into cautious scientific wording.

Notebook 22 turns career and academic preparation into code and datasets. Students practice role-style scenarios such as QC analyst plate review, research assistant replicate review, assay-development day variability, qPCR replicate checks, sequence triage, and AI figure-caption review.

For software or IT learners, this is like reviewing generated documentation against logs, tests, and monitoring output. A polished paragraph is not enough; it must trace back to real evidence.

A strong student artifact is usually one figure or table, one cautious result paragraph, one limitation, one next-step idea, and one short reflection.

### 中文

AI/LLM review notebook 教学生把 AI 写出的科学文字当作草稿，而不是证据。任务是把 AI-style 句子与真实表格或图形对应检查，再把过度结论改写成谨慎的科学表达。

Notebook 22 把职业和学术准备落实到代码和数据集中。学生会练习类似 QC analyst 的孔板 review、research assistant 的重复测量 review、assay development 的跨天波动检查、qPCR 重复 Ct 检查、序列 triage，以及 AI 图注 overclaim review。

对软件或 IT 背景学习者来说，这类似检查自动生成文档是否真的对应 logs、tests 和 monitoring output。文字流畅不代表可信，必须能追溯到证据。

一个强的学生作品通常包括：一个图或表、一段谨慎结果解释、一个 limitation、一个 next-step idea，以及一个简短 reflection。

---

## Suggested Student Workflow / 建议学习流程

English:
1. Start with the dataset preview and understand each column.
2. Identify the biological question and the measured response.
3. Check controls and replicates before interpreting means.
4. Use plots to inspect patterns, not to overstate conclusions.
5. Report uncertainty, QC notes, and limitations.
6. Translate numeric observations into cautious scientific language.

中文：
1. 先看 dataset preview，理解每一列。
2. 明确生物化学问题和测量指标。
3. 在解释均值前检查 control 和 replicate。
4. 用图形检查模式，但不要过度结论化。
5. 报告不确定性、QC notes 和 limitations。
6. 把数字观察转化为谨慎的科学语言。

---

## Example Cautious Sentences / 谨慎表达示例

English:
- “In this synthetic dataset, treatment samples show lower mean enzyme activity than controls.”
- “The pattern is consistent with a dose-response-style decrease in viability.”
- “Review flags suggest that replicate-level values should be checked before interpretation.”
- “The fitted parameter is an educational estimate and should not be treated as a real biological constant.”

中文：
- “在这个合成数据集中，treatment 样本的平均酶活性低于 control。”
- “该模式与剂量-反应风格的 viability 下降一致。”
- “Review flags 提示在解释前应检查重复测量值。”
- “拟合参数是教学估计，不应视为真实生物常数。”

---

## Final Reminder / 最后提醒

This repository teaches data reasoning in biochemistry contexts. The central skill is not only running code, but learning how to connect data, graphs, uncertainty, QC, and cautious interpretation.

本项目训练的是生物化学场景下的数据推理能力。核心技能不只是运行代码，而是学会把数据、图形、不确定性、质量检查和谨慎解释连接起来。
