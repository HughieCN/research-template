# data/results

## 用途

存放由 Stata、Python 或其他分析程序直接生成的结果素材。

## 这里放什么

- 可被 LaTeX `\input` 引入的 `.tex` 结果片段；
- 图片型 PDF 文件；
- PNG 或其他分析图像；
- 后续排版需要使用的其他结果文件。

可以根据研究主题创建子目录，例如 `tables/`、`figures/`、`event_study/` 或 `robustness/`。

## 与 outputs/ 的关系

本目录保存分析程序产生的素材。完整的 LaTeX 包装器放在 [`outputs/`](../../outputs/)；包装器可以使用 `\input` 引入 TEX 片段，或使用 `\includegraphics` 引入 PDF、PNG 等图片素材。

## 版本管理

本目录中的内容默认提交到 Git。若某个文件过大、包含敏感信息或不适合共享，应在项目层面单独说明并配置排除规则。
