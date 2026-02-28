# 快速开始指南

欢迎使用OpenClaw之西游记！本指南将帮助您快速开始使用这个基于《西游记》启发的AI协作框架。

## 安装

### 前置要求
- Python 3.8 或更高版本
- Git
- OpenAI API密钥（或其他兼容的LLM API）

### 步骤1：克隆仓库
```bash
git clone https://github.com/SynSwarm/WestOdyssey.git
cd WestOdyssey
```

### 步骤2：安装依赖
```bash
pip install -r requirements.txt
```

### 步骤3：配置API密钥
在项目根目录创建`.env`文件：
```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

## 您的第一个任务

### 基础使用
```python
from westodyssey import TangSeng

# 初始化唐僧（用户代理）
master = TangSeng()

# 向团队下达任务
result = master.assign_mission(
    mission="分析GitHub上热门的AI项目",
    context="重点关注多智能体系统相关的项目"
)

print(result)
```

### 理解团队角色

Westodyssey将AI智能体组织成四个专业角色：

#### 1. 悟空 - 问题解决者
```python
# 悟空处理复杂问题解决
wukong_result = master.wukong.solve("编写一个Python脚本抓取数据")
```

#### 2. 八戒 - 质量审计官
```python
# 八戒审查和审计所有解决方案
review_result = master.bajie.review(wukong_result)
```

#### 3. 沙僧 - 交付者
```python
# 沙僧格式化并交付最终结果
final_output = master.wujing.format(review_result)
```

#### 4. 白龙马 - 记忆库
```python
# 白龙马记住所有过去的任务
history = master.steed.recall("类似的任务")
```

## 配置

### 团队配置
您可以在`config/team_config.json`中自定义团队：

```json
{
  "wukong": {
    "model": "gpt-4",
    "temperature": 0.7,
    "tools": ["browser", "code_interpreter"]
  },
  "bajie": {
    "model": "claude-3-sonnet",
    "strictness": "high"
  },
  "wujing": {
    "model": "gpt-3.5-turbo",
    "temperature": 0.0
  }
}
```

### 工作流配置
在`config/workflow.yaml`中配置协作工作流：

```yaml
workflow:
  steps:
    - load_context: true
    - solve_problem: true
    - review_solution: true
    - format_output: true
    - record_memory: true
  
  constraints:
    max_review_cycles: 3
    require_human_approval: true
```

## 示例

查看`examples/`目录获取更多完整示例：

1. **数据分析**: `examples/data-analysis/`
2. **代码审查**: `examples/code-review/`
3. **文档生成**: `examples/document-generation/`

## 下一步

1. **探索文档**: 阅读完整文档了解高级功能
2. **加入社区**: 参与[GitHub Discussions](https://github.com/SynSwarm/WestOdyssey/discussions)
3. **报告问题**: 通过报告bug帮助改进Westodyssey
4. **贡献代码**: 查看我们的[贡献指南](../CONTRIBUTING.md)

## 故障排除

### 常见问题

1. **API密钥问题**: 确保`.env`文件包含有效的API密钥
2. **依赖问题**: 确保所有需求都已安装
3. **权限问题**: 检查config目录的文件权限

### 获取帮助
- 查看[常见问题](../docs/faq.md)
- 加入我们的[讨论区](https://github.com/SynSwarm/WestOdyssey/discussions)
- 提交[问题报告](https://github.com/SynSwarm/WestOdyssey/issues)

---

**记住**: 每一个复杂任务都是一场数字奥德赛。让您的AI徒弟们协同工作，征服它！