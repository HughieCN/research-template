# data/external

## 用途

存放本机使用的外部原始数据和人工维护输入。

## 版本管理

本目录只提交 README，其他内容一律不提交。原始大数据、受限访问数据、敏感数据和机器专用路径都留在本机。

## 与其他目录的关系

这里的输入可以由 `src/features/acquire/` 读取，再经过整理后写入 `data/processed/` 或 `data/ready/`。
