# outputs

## 用途

存放供研究者阅读、检查和插入论文的最终排版源文件。

## 这里放什么

`outputs/` 根目录中的 `.tex` 文件是完整的 LaTeX 包装器。它们可以：

- 使用 `\input` 引入 `data/results/` 中的 TEX 结果片段；
- 使用 `\includegraphics` 引入图片型 PDF、PNG 等结果素材；
- 添加标题、注释、脚注和页面设置；
- 生成单页或多页 PDF。

## 编译产物

LaTeX 产生的 PDF、`.aux`、`.log` 等文件放在 `out/`。`out/` 中的内容可以重新生成，默认不提交到 Git。

## 与 data/results/ 的关系

`data/results/` 保存分析程序直接生成的结果素材；本目录保存如何把这些素材排版成完整结果的 LaTeX 文件。
