# API 参考文档

本文档提供Westodyssey框架的详细API参考。

## 核心类

### TangSeng 类
代表人类用户（唐僧）的主要协调器类。

```python
from westodyssey import TangSeng

# 初始化TangSeng
master = TangSeng(
    config_path="config/team_config.json",
    workflow_path="config/workflow.yaml"
)
```

#### 构造函数参数
| 参数 | 类型 | 描述 | 默认值 |
|------|------|------|--------|
| `config_path` | str | 团队配置文件路径 | `"config/team_config.json"` |
| `workflow_path` | str | 工作流配置文件路径 | `"config/workflow.yaml"` |
| `api_key` | str | OpenAI API密钥（可选） | `None`（从.env读取） |
| `verbose` | bool | 启用详细日志 | `False` |

#### 方法

##### `assign_mission(mission, context=None)`
向团队分配任务。

```python
result = master.assign_mission(
    mission="分析热门AI项目",
    context="重点关注多智能体系统"
)
```

**参数:**
- `mission` (str): 主要任务描述
- `context` (str, 可选): 额外上下文或约束条件

**返回:**
- `dict`: 包含状态和输出的任务结果

##### `get_team_status()`
获取所有团队成员的当前状态。

```python
status = master.get_team_status()
```

**返回:**
- `dict`: 团队状态信息

##### `reset_team()`
将团队重置到初始状态。

```python
master.reset_team()
```

### Wukong 类
核心问题解决者（孙悟空）。

```python
from westodyssey.agents import Wukong

wukong = Wukong(
    model="gpt-4",
    temperature=0.7,
    tools=["browser", "code_interpreter"]
)
```

#### 构造函数参数
| 参数 | 类型 | 描述 | 默认值 |
|------|------|------|--------|
| `model` | str | 使用的LLM模型 | `"gpt-4"` |
| `temperature` | float | 创意水平 (0.0-1.0) | `0.7` |
| `tools` | list | 可用工具 | `["browser", "code_interpreter"]` |
| `max_tokens` | int | 每次响应的最大token数 | `4000` |

#### 方法

##### `solve(problem, context=None)`
解决复杂问题。

```python
solution = wukong.solve(
    problem="编写GitHub趋势的网络爬虫",
    context="使用Python和BeautifulSoup"
)
```

##### `generate_code(language, task)`
为特定任务生成代码。

```python
code = wukong.generate_code(
    language="python",
    task="使用pandas进行数据分析"
)
```

##### `research(topic, sources=5)`
研究主题并收集信息。

```python
research_result = wukong.research(
    topic="AI智能体框架",
    sources=5
)
```

### Bajie 类
质量审计官（猪八戒）。

```python
from westodyssey.agents import Bajie

bajie = Bajie(
    model="claude-3-sonnet",
    strictness="high"
)
```

#### 构造函数参数
| 参数 | 类型 | 描述 | 默认值 |
|------|------|------|--------|
| `model` | str | 使用的LLM模型 | `"claude-3-sonnet"` |
| `strictness` | str | 审查严格程度等级 | `"high"` |
| `max_review_cycles` | int | 最大审查循环次数 | `3` |

#### 方法

##### `review(solution, criteria=None)`
审查解决方案的质量和安全性。

```python
review_result = bajie.review(
    solution=wukong_solution,
    criteria=["security", "efficiency", "best_practices"]
)
```

##### `audit_code(code, language="python")`
执行代码审计。

```python
audit_result = bajie.audit_code(
    code=python_code,
    language="python"
)
```

##### `validate_output(output, format_spec)`
验证输出格式。

```python
validation_result = bajie.validate_output(
    output=data_output,
    format_spec={"type": "markdown", "sections": ["introduction", "analysis"]}
)
```

### Wujing 类
数据交付者（沙僧）。

```python
from westodyssey.agents import Wujing

wujing = Wujing(
    model="gpt-3.5-turbo",
    temperature=0.0
)
```

#### 构造函数参数
| 参数 | 类型 | 描述 | 默认值 |
|------|------|------|--------|
| `model` | str | 使用的LLM模型 | `"gpt-3.5-turbo"` |
| `temperature` | float | 严格程度水平 | `0.0` |

#### 方法

##### `format(data, format_type="markdown")`
将数据格式化为指定格式。

```python
formatted = wujing.format(
    data=raw_data,
    format_type="markdown"
)
```

##### `clean_data(data, rules=None)`
清理和规范化数据。

```python
cleaned = wujing.clean_data(
    data=raw_dataset,
    rules=["remove_duplicates", "normalize_dates"]
)
```

##### `deliver(output, destination)`
将输出交付到目标位置。

```python
delivery_result = wujing.deliver(
    output=final_output,
    destination="file://output/report.md"
)
```

### Steed 类
记忆系统（白龙马）。

```python
from westodyssey.agents import Steed

steed = Steed(
    vector_db_path="memory_database",
    embedding_model="text-embedding-3-small"
)
```

#### 构造函数参数
| 参数 | 类型 | 描述 | 默认值 |
|------|------|------|--------|
| `vector_db_path` | str | 向量数据库路径 | `"memory_database"` |
| `embedding_model` | str | 使用的嵌入模型 | `"text-embedding-3-small"` |

#### 方法

##### `record(event, metadata=None)`
将事件记录到记忆中。

```python
steed.record(
    event="mission_completed",
    metadata={"mission_id": "123", "duration": "1.5h"}
)
```

##### `recall(query, limit=5)`
回忆相似记忆。

```python
memories = steed.recall(
    query="data analysis mission",
    limit=5
)
```

##### `get_context(mission_id)`
获取特定任务的上下文。

```python
context = steed.get_context(mission_id="123")
```

## 工作流 API

### Pilgrimage 工作流
主要工作流协调器。

```python
from westodyssey.workflow import Pilgrimage

workflow = Pilgrimage(
    wukong=wukong,
    bajie=bajie, 
    wujing=wujing,
    steed=steed,
    human_in_the_loop=True
)
```

#### 方法

##### `dispatch(mission, context=None)`
通过完整工作流调度任务。

```python
result = workflow.dispatch(
    mission="分析AI趋势",
    context="2024年的最新发展"
)
```

##### `get_progress(mission_id)`
获取特定任务的进度。

```python
progress = workflow.get_progress(mission_id="123")
```

##### `pause_mission(mission_id)`
暂停任务进行人工审查。

```python
workflow.pause_mission(mission_id="123")
```

## 配置 API

### 团队配置
团队配置结构：

```python
team_config = {
    "wukong": {
        "model": "gpt-4",
        "temperature": 0.7,
        "tools": ["browser", "code_interpreter", "web_search"]
    },
    "bajie": {
        "model": "claude-3-sonnet", 
        "strictness": "high",
        "max_review_cycles": 3
    },
    "wujing": {
        "model": "gpt-3.5-turbo",
        "temperature": 0.0
    },
    "steed": {
        "embedding_model": "text-embedding-3-small",
        "vector_db_path": "memory_database"
    }
}
```

### 工作流配置
工作流配置结构：

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
    timeout_minutes: 30
  
  notifications:
    on_pause: true
    on_completion: true
    on_error: true
```

## 实用函数

### `load_config(config_path)`
从文件加载配置。

```python
from westodyssey.utils import load_config

config = load_config("config/team_config.json")
```

### `save_config(config, config_path)`
将配置保存到文件。

```python
from westodyssey.utils import save_config

save_config(team_config, "config/team_config.json")
```

### `validate_config(config)`
验证配置结构。

```python
from westodyssey.utils import validate_config

is_valid = validate_config(team_config)
```

## 错误处理

### 自定义异常

```python
from westodyssey.exceptions import (
    MissionTimeoutError,
    ReviewCycleExceededError,
    FormatValidationError,
    MemoryRetrievalError
)

try:
    result = workflow.dispatch(mission)
except MissionTimeoutError as e:
    print(f"任务超时: {e}")
except ReviewCycleExceededError as e:
    print(f"审查循环次数过多: {e}")
```

### 错误恢复

```python
from westodyssey.recovery import retry_with_backoff

@retry_with_backoff(max_retries=3)
def execute_mission(mission):
    return workflow.dispatch(mission)
```

## 示例

### 基础使用
```python
from westodyssey import TangSeng

# 初始化
master = TangSeng()

# 执行任务
result = master.assign_mission(
    mission="创建市场分析报告",
    context="重点关注2024年AI智能体市场"
)

print(result["output"])
```

### 高级配置
```python
from westodyssey.workflow import Pilgrimage
from westodyssey.agents import Wukong, Bajie, Wujing, Steed

# 创建自定义团队
wukong = Wukong(model="gpt-4o", tools=["all"])
bajie = Bajie(model="claude-3-5-sonnet", strictness="extreme")
wujing = Wujing(model="gpt-4", temperature=0.0)
steed = Steed(embedding_model="text-embedding-3-large")

# 创建工作流
workflow = Pilgrimage(
    wukong=wukong,
    bajie=bajie,
    wujing=wujing,
    steed=steed,
    human_in_the_loop=False  # 全自动化
)

# 执行
result = workflow.dispatch("复杂数据分析任务")
```

---

**注意**: 此API参考文档会持续更新。请查看[GitHub仓库](https://github.com/SynSwarm/WestOdyssey)获取最新版本。