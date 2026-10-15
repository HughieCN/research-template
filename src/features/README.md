# src/features

## 用途

存放从原始或外部数据构造研究数据的代码。

## 目录结构

- `acquire/`：获取或读取外部数据。
- `curate/`：清洗、筛选、合并和整理数据。
- `engineer/`：构造特征、指标和分析变量。

## 与其他目录的关系

这里的代码读取 `data/external/` 或 `configs/local.yaml` 中登记的本机数据位置，把结果写入 `data/processed/` 和 `data/ready/`。分析逻辑属于 [`src/research/`](../research/)。
