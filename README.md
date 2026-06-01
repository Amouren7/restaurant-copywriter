# 🍜 餐饮文案助手

> 面向餐饮老板的在线文案生成工具。点3下出5条文案，复制即用。

---

## 项目结构

```
restaurant-copywriter/
├── docs/                      ← 项目文档
│   ├── 01-项目计划书.md        ← 完整项目规划
│   ├── 02-执行时间表.md        ← 14天执行清单
│   ├── 03-产品需求文档.md      ← 产品设计PRD
│   ├── 04-技术架构文档.md      ← 技术方案
│   ├── 05-部署指南.md          ← 上线步骤（必读）
│   └── 06-小红书引流帖.md      ← 3篇引流帖
│
├── src/                       ← 源代码
│   ├── index.html             ← 前端页面（含CSS+JS）
│   ├── server.py              ← Flask后端
│   ├── prompts.py             ← 提示词模板库
│   └── requirements.txt       ← Python依赖
│
├── Procfile                   ← Railway部署配置
├── runtime.txt                ← Python版本
└── README.md                  ← 本文件
```

## 快速启动

**详见 [docs/05-部署指南.md](docs/05-部署指南.md)**

简要步骤：
1. 代码上传到GitHub
2. Railway连接GitHub仓库
3. 配置环境变量（DeepSeek API Key）
4. 自动生成域名，上线完成

## 本地开发

```bash
cd src
pip install -r requirements.txt
$env:DEEPSEEK_API_KEY="你的密钥"
$env:DEEPSEEK_BASE_URL="https://api.deepseek.com"
python server.py
# 打开 http://localhost:5000
```
