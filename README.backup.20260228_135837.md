# 🌀 Westodyssey (OpenClaw之西游记) 
**Every complex task is a Digital Odyssey.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Powered by OpenClaw](https://img.shields.io/badge/Engine-OpenClaw-blue)](https://github.com/OpenClaw/OpenClaw)
[![Website](https://img.shields.io/badge/Official-Westodyssey.com-gold)](https://westodyssey.com)

> **“敢问路在何方？路在分布式执行与角色化纠偏之中。”**

**Westodyssey** 是一个基于 [OpenClaw](https://github.com/OpenClaw/OpenClaw) 核心引擎二次开发的增强型多智能体（Multi-Agent）协作框架。我们通过引入极具东方哲学色彩的**“西游协作模型（The Pilgrimage Protocol）”**，彻底重构了 AI Agent 的工作流，解决了传统框架中**协同难、黑盒化、易失控**的致命痛点。

---

## 🎯 为什么需要 Westodyssey？

目前的 Agent 框架往往过于抽象，单一 Agent 容易产生幻觉（Hallucination），而多 Agent 协作又容易陷入死循环。

Westodyssey 不卷底层模型参数，而是**卷人机协作的直觉**：
1. **降维认知：** 任何非技术人员都能秒懂“八戒负责给悟空的代码挑刺”。
2. **拒绝黑盒：** 将冷冰冰的 Terminal Log 转化为具有角色性格的“对抗辩论流”。
3. **人类兜底：** 确立了用户（唐僧）的最高决策权，Agent 跑偏时一键念咒纠回。

---

## 🎭 核心架构：取经团队 (The Squad)

在 Westodyssey 中，每一个智能体都被赋予了极其克制且明确的系统边界：

### 🐒 Wukong (The Lead Solver / 首席攻坚手)
* **能力：** 最高权限的工具调用者（浏览器控制、代码沙盒、API 搜索）。
* **职责：** 负责拆解最复杂的任务并暴力输出解决方案。他是能力的上限，但也最容易“上头”。

### 🐷 Pigsy (The Critic / 首席风控与审计官)
* **能力：** 交叉验证、鲁棒性测试、Red Teaming（红蓝对抗）。
* **底层逻辑：**
  * *“懒惰”即优化：* 嫌悟空的代码太复杂，强制要求寻找更低 Token 消耗的降级方案。
  * *“胆小”即安全：* 拦截可能导致死循环或被封 IP 的高风险操作。
  * *“碎碎念”即反思：* 悟空的代码如果不经过八戒的 `Review_Pass`，绝不允许进入下一环节。

### 🐢 Friar (The Executor / 首席执行官)
* **能力：** 0 Temperature，极致稳定。
* **职责：** 承接经过确认的方案，进行数据清洗、Markdown 格式化、本地文件 I/O 等“脏活累活”。

### 👳‍♂️ The Monk (The Orchestrator / 用户与决策者)
* **能力：** `Human-in-the-loop` 协议。
* **职责：** 把握最终方向。不需要懂代码，只需要在关键节点按下“同意”或下达“紧箍咒（纠偏指令）”。

### 🐎 The Steed (The Memory Layer / 记忆与基础设施)
* **能力：** RAG (Retrieval-Augmented Generation)、向量数据库。
* **职责：** 默默承载所有的对话上下文与私有知识库，确保团队走得再远也不忘初衷。

---

## 🛠 核心机制：紧箍咒协议 (The Tight-Fillet Protocol)

Westodyssey 不相信完全的“Auto”。我们设计了优雅的降级与求助机制：
1. **自动驾驶：** 悟空执行 ➡️ 八戒审计 ➡️ 沙僧落地。
2. **风险挂起：** 当八戒连续 3 次打回悟空的方案，或系统检测到 Token 消耗异常。
3. **呼叫唐僧：** 系统强制暂停，弹出控制台请求用户介入。用户只需输入一句自然语言（如：“八戒说得对，悟空你换个思路，用官方 API 试试”），即可重置 Agent 状态。

---

## 🚀 快速开始 (Quick Start)

### 1. 安装
```bash
git clone [https://github.com/YourName/Westodyssey.git](https://github.com/YourName/Westodyssey.git)
cd Westodyssey
pip install -r requirements.txt
```

### 2. 组建团队并开启奥德赛
用极其优雅的代码定义你的取经之旅：
```bash
from westodyssey import Pilgrimage
from westodyssey.agents import Wukong, Pigsy, Friar, Monk

# 1. 配置角色 (可混搭不同厂商的大模型)
team = Pilgrimage(
    solver=Wukong(model="gpt-4o", tools=["browser", "code_interpreter"]),
    critic=Pigsy(model="claude-3-5-sonnet", strictness="high"),
    executor=Friar(model="deepseek-chat"),
    orchestrator=Monk(human_in_the_loop=True) # 开启唐僧兜底模式
)

# 2. 发布宏愿 (下达任务)
task = "帮我抓取 GitHub 上排名前 5 的 AI Agent 框架，对比它们的底层逻辑，并生成一份带图表的 Markdown 分析报告。"

# 3. 踏上旅程
team.dispatch(task)
```

## 📅 路线图 (Roadmap)
 * [x] Phase 1: 确立 Westodyssey 核心概念与专属域名 Westodyssey.com
 * [ ] Phase 2: 发布开源的 Agent System Prompts 性格配置文件库。
 * [ ] Phase 3: 推出 Westodyssey Dashboard，让多智能体协作过程可视化（取经路线图 UI）。
 * [ ] Phase 4: 上线商业化 SaaS 平台，支持企业级私有化“取经团队”部署。

## 🤝 参与共建 (Join the Journey)
无论你是能写核心底层逻辑的“悟空”，还是擅长发现 Bug 的“八戒”，亦或是热爱写文档的“沙僧”，Westodyssey 社区都欢迎你的加入！
 * 🌍 官网: Westodyssey.com (建设中)
 * 🐛 Issues: 欢迎提交你遇到的任何“妖怪”。
“每一场复杂的计算，都是一段波澜壮阔的数字奥德赛。” 立即 ⭐ Star 本项目，和我们一起西行！

