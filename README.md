# 研究项目模板

Research Template for Data-Driven Projects

这是一个通用的研究项目模板，用于组织数据、分析代码、研究文档和可复现结果。它适合实证研究、数据分析和需要多人协作的研究项目。

本模板不是一个需要安装后发布的 Python package。它提供的是一个清晰的项目结构，以及 Python、uv、测试和代码检查的基础配置。

## 如何阅读一个使用本模板的项目

不需要安装 Python，也可以先从以下位置开始：

- 研究问题和设计：[`docs/design/`](docs/design/)
- 数据来源和变量定义：[`docs/data/`](docs/data/)
- 文献笔记：[`docs/literature/`](docs/literature/)
- 分析结果素材：[`data/results/`](data/results/)
- 排版后的研究结果：[`outputs/`](outputs/)

## 如何使用本模板

### 通过 GitHub 创建新项目

本仓库已经设置为 GitHub Template Repository：

1. 点击 `Use this template`。
2. 输入新项目的仓库名称。
3. 创建新仓库并 clone 到本地。
4. 修改新项目的 README 标题和项目简介。
5. 修改 `pyproject.toml` 中的项目名称和描述。

### 下载后在本地使用

也可以下载 ZIP，解压并修改文件夹名称，然后在新项目目录中初始化 Git。使用模板后，应至少修改：

- `README.md` 的标题和项目简介；
- `pyproject.toml` 中的 `name` 和 `description`；
- 与具体项目有关的 `AGENTS.md` 内容；
- 不适用于新项目的示例配置和说明。

## 目录结构

```text
.agents/      项目级 Agent Skills；供编程 agent 读取的技能说明。
configs/      本机配置模板；真实本机配置不会提交。
data/         外部输入、处理中间数据、分析就绪数据和结果素材。
docs/         数据说明、研究设计和文献笔记。
outputs/      完整的 LaTeX 包装器；编译产物位于 outputs/out/。
scripts/      探索性或一次性脚本。
src/          需要复用和测试的研究代码。
tests/        用于检查可复用代码的测试。
```

## 研究结果的基本流程

分析程序可以将结果素材写入 `data/results/`，例如可被 LaTeX 复用的 `.tex` 片段、图片型 PDF 或 PNG 文件。

完整的 LaTeX 包装器放在 `outputs/` 根目录中，可以使用 `\input` 引入 `.tex` 片段，或使用 `\includegraphics` 引入图片素材。LaTeX 编译产生的 PDF、`.aux` 和 `.log` 等文件放在 `outputs/out/`，该目录默认不提交到 Git。

## 环境与运行

模板使用 Python 3.12 和 uv 管理环境：

```powershell
uv sync
```

`uv sync` 只负责准备项目环境，不代表已经运行了研究流程。它会把 `.venv` 精确对齐到 `uv.lock`：添加分析依赖请使用 `uv add pandas`，直接 `pip install` 进 `.venv` 的包会在下一次 `uv sync` 时被移除。实际项目应在有可运行代码后，在本 README 或相关脚本中补充具体运行顺序。

常用检查命令：

```powershell
uv run pytest
uv run ruff check .
```

## 版本管理和数据边界

默认提交：

- 研究文档和设计记录；
- 源代码、脚本和测试；
- `data/results/` 中的结果素材；
- `outputs/` 根目录中的 LaTeX 包装器。

默认不提交：

- 原始数据、受限访问数据和本机专用数据；
- 本地配置、凭据和密钥；
- Python 环境、缓存和日志；
- `outputs/out/` 中可以重新生成的编译产物。

私有数据不应因为仓库是私有的就直接提交；公开模板尤其不能包含个人路径、账号信息或真实研究数据。

确实需要提交某个被忽略的小型文件时，用 `git add -f <路径>` 显式加入，并在 `docs/data/` 说明理由。`data/results/` 默认提交，但单个文件超过约 1 MB 时（高分辨率图像、大型表格片段）应先确认它是否真的需要进入 Git。

## 参与项目

共同作者可以先阅读 `docs/` 和 `outputs/`，不需要理解全部代码。需要运行或修改分析时，再根据项目 README 和相关目录中的说明准备环境。
