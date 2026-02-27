Westodyssey/
├── westodyssey/             # 核心源码包
│   ├── __init__.py
│   ├── core/                # 核心引擎 (对接 OpenClaw)
│   │   ├── engine.py
│   │   └── memory.py        # 白龙马节点
│   ├── agents/              # 角色定义包
│   │   ├── base.py
│   │   ├── wukong.py        # 悟空节点 (Solver)
│   │   ├── pigsy.py         # 八戒节点 (Critic)
│   │   ├── friar.py         # 沙僧节点 (Executor)
│   │   └── monk.py          # 唐僧节点 (Human-in-the-loop)
│   └── prompts/             # 存放每个角色的核心性格 System Prompt
├── examples/                # 给用户看的 Demo 脚本
│   └── simple_research.py   # 一个演示“悟空抓数据，八戒来挑刺”的测试脚本
├── .env.example             # 提供给用户的环境变量模板（不要填写真实 Key）
├── requirements.txt         # 依赖包列表
├── .gitignore
├── LICENSE
└── README.md
