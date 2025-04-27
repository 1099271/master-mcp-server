# MasterFlow MCP Server

MasterFlow MCP Server 是一个基于 Model Context Protocol (MCP) 的服务器应用，为大型语言模型 (LLMs) 提供 MasterFlow API 工具和查询功能。

## 项目描述

该项目实现了一个 MCP 服务器，允许 LLMs 通过标准化的接口与 MasterFlow API 进行交互，主要功能包括：

- 提供笔记详情查询工具
- 支持通过笔记 ID 获取警报详情
- 使用标准化的 MCP 协议与 LLMs 通信

## 安装要求

- Python >= 3.12
- 依赖项请参见 pyproject.toml

## 快速开始

1. 克隆仓库

```bash
git clone <repository-url>
cd masterflow-mcp-server
```

2. 创建并激活虚拟环境

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate  # Windows
```

3. 安装依赖

```bash
pip install -e .
```

## 使用方法

### 直接运行服务器

```bash
python src/note_mcp_serve.py
```

### 作为库导入使用

```python
from src.note_mcp_serve import get_alert_details

# 使用 get_alert_details 函数获取笔记警报详情
note_details = await get_alert_details("your-note-id")
```

## 功能说明

### 获取笔记详情

通过笔记 ID 获取对应的笔记详细信息：

```python
await get_alert_details("your-note-id")
```

## 开发

本项目使用 FastMCP 框架构建，以提供标准化的工具接口给 LLM 模型使用。

## 许可证

[添加许可证信息]

## 作者

Ryan
