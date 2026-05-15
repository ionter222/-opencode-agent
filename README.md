# 🎲 OpenCode DM Agent — D&D 5E 地下城主智能体

> 在 [OpenCode](https://opencode.ai) 中用 AI DM 开团！一个像人类 DM 一样带团的智能体。

![DM Agent](https://img.shields.io/badge/OpenCode-DM%20Agent-FF5733?style=flat-square)

## ⚠️ 重要说明

本仓库**不包含**版权受限的 D&D 内容。以下目录需要**你自己准备**：

| 目录 | 内容 | 来源 |
|------|------|------|
| `规则/` | D&D 5E 规则书（PHB、DMG、MM 等） | D&D Beyond / 官方购买 |
| `模组/` | 冒险模组 PDF | D&D Beyond / 官方购买 |
| `世界观/` | 战役设定资料 | 官方设定集 / 自行收集 |
| `opencode.json` | API Key 配置 | 参考下方配置说明自行填写 |

项目提供了目录结构和 `.gitignore` 占位，你把文件放进去即可。

## ✨ 功能特性

- **真正的 DM 体验** — 叙事生动、判罚公平、世界一致，像一个有经验的人类 DM
- **规则驱动** — 严格遵循 D&D 5E 规则书，可灵活添加村规
- **角色卡管理** — 自动跟踪和更新 PC/NPC 角色数据
- **模组支持** — 按照模组剧本推进冒险
- **真实骰子** — 集成骰子程序，所有检定真实投骰
- **NPC 队友系统** — 为队伍自动生成完整角色卡的 NPC 同伴
- **在线查证** — 不确定的规则联网搜索，绝不臆想
- **存档系统** — 保存/读取战役进度

## 🚀 快速开始

### 1. 安装 OpenCode

确保已安装 [OpenCode](https://opencode.ai/download)。

### 2. 克隆/创建项目

```bash
# 创建你的 TRPG 战役目录
mkdir my-campaign
cd my-campaign

# 复制本项目的 .opencode/ 和 dice.py 到你的目录
```

### 3. 目录结构

```
my-campaign/
├── .opencode/
│   └── agents/
│       └── dm.md              # DM 智能体配置文件 ← 核心
├── 规则/                       # ⚠️ 自备 D&D 5E 规则书
├── 角色卡/                     # 你的角色数据
│   ├── 玩家1.md
│   └── NPC-队友.md
├── 模组/                       # ⚠️ 自备冒险模组
├── 世界观/                     # ⚠️ 自备战役设定
├── dice.py                     # 骰子程序
├── opencode.json               # ⚠️ 自配 API Key
└── save_*.json                 # 战役存档
```

### 4. 配置 API Key

复制 `opencode.json.example` 为 `opencode.json`，填入你的 API Key：

```bash
cp opencode.json.example opencode.json
```

```json
{
  "provider": {
    "deepseek": {
      "options": {
        "apiKey": "env:YOUR_API_KEY_HERE"
      }
    }
  }
}
```

或者使用环境变量（推荐）：
```bash
export DEEPSEEK_API_KEY="sk-你的key"
```

支持的提供商：DeepSeek、Anthropic、OpenAI、Google、Groq 等。

### 5. 开团！

在终端中运行：

```bash
# 进入战役目录
cd my-campaign

# 启动 OpenCode
opencode

# 切换到 DM 智能体（Tab 键切换 或 /agent 命令）
# 或 @dm 在对话中召唤
```

## 🎯 用法

### 直接开团

```
/dm 我想玩凡戴尔的失落矿坑，创建 3 级角色开团
```

### 辅助人类 DM

```
/dm 帮我生成一个随机遭遇表，玩家等级 3，地点在森林
```

### 创建 NPC

```
/dm 队伍需要个治疗职业，创建一个精灵牧师 NPC
```

### 战斗辅助

```
/dm 帮我计算这场战斗的经验值：2个哥布林首领 + 4个普通哥布林，5个3级玩家
```

## ⚙️ 智能体提示词

核心提示词位于 `.opencode/agents/dm.md`，包含以下指令模块：

| 模块 | 说明 |
|------|------|
| 核心身份 | DM 角色定位与风格 |
| 工作守则 | 十大核心操作规范 |
| 规则执行 | 规则书引用与村规管理 |
| 角色卡管理 | 自动更新触发条件 |
| 骰子检定 | dice.py 集成规范 |
| 在线查证 | 搜索边界与来源要求 |
| 玩家自主权 | Agency 保护原则 |
| NPC 队友 | 创建与操作规范 |
| 战斗管理 | 先攻/行动/描述 |
| 叙事风格 | 语言与氛围指导 |
| 存档管理 | 状态保存格式 |

## 🎲 dice.py

```bash
python dice.py d20        # 投一个 d20
python dice.py 2d6+3      # 投 2d6 加 3
python dice.py d20+5      # 带加值
python dice.py 3d8        # 投 3 个 d8
```

支持的骰子：`d3` `d4` `d6` `d8` `d10` `d12` `d20` `d100`

## 🧩 自定义与扩展

### 修改提示词

编辑 `.opencode/agents/dm.md`，可以：

- 调整 DM 的风格调性（更严肃/更搞笑）
- 添加自定义房规
- 修改 NPC 创建规则
- 调整战斗描述风格

### 添加自定义工具

在 `.opencode/tools/` 中添加 MCP 工具，例如：

- 地图生成器
- 随机宝藏表
- 名字生成器

### 战役存档

每个重要节点后 DM 会自动存档到 `save_<日期>.json`，可手动恢复：

```
/dm 读取上次存档
```

## 📦 作为依赖安装

如果你想把 DM Agent 作为一个独立的 opencode 插件使用：

```bash
# 在你的战役项目中
git clone https://github.com/yourname/opencode-dm-agent .opencode/dm
# 然后在 opencode.json 中引用
```

## 📋 推荐模型

| 模型 | 适用性 | 原因 |
|------|--------|------|
| Claude Sonnet 4 | ⭐⭐⭐⭐⭐ | 叙事能力强，角色扮演出色 |
| DeepSeek V3 | ⭐⭐⭐⭐ | 性价比高，中文支持好 |
| GPT-4o | ⭐⭐⭐⭐ | 规则理解准确 |
| Gemini 2.5 Pro | ⭐⭐⭐⭐ | 上下文窗口大，适合长团 |

## 📄 开源协议

MIT License — 自由使用、修改、分发。

---

**Made with 🎲 for D&D players and OpenCode community**
