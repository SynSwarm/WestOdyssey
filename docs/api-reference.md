# API Reference

This document provides detailed API reference for Westodyssey framework.

## Core Classes

### TangSeng Class
The main orchestrator class that represents the human user (Tang Sanzang).

```python
from westodyssey import TangSeng

# Initialize TangSeng
master = TangSeng(
    config_path="config/team_config.json",
    workflow_path="config/workflow.yaml"
)
```

#### Constructor Parameters
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `config_path` | str | Path to team configuration file | `"config/team_config.json"` |
| `workflow_path` | str | Path to workflow configuration file | `"config/workflow.yaml"` |
| `api_key` | str | OpenAI API key (optional) | `None` (reads from .env) |
| `verbose` | bool | Enable verbose logging | `False` |

#### Methods

##### `assign_mission(mission, context=None)`
Assign a mission to the team.

```python
result = master.assign_mission(
    mission="Analyze trending AI projects",
    context="Focus on multi-agent systems"
)
```

**Parameters:**
- `mission` (str): The main mission/task description
- `context` (str, optional): Additional context or constraints

**Returns:**
- `dict`: Mission result with status and output

##### `get_team_status()`
Get current status of all team members.

```python
status = master.get_team_status()
```

**Returns:**
- `dict`: Team status information

##### `reset_team()`
Reset the team to initial state.

```python
master.reset_team()
```

### Wukong Class
The core problem solver (Sun Wukong).

```python
from westodyssey.agents import Wukong

wukong = Wukong(
    model="gpt-4",
    temperature=0.7,
    tools=["browser", "code_interpreter"]
)
```

#### Constructor Parameters
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `model` | str | LLM model to use | `"gpt-4"` |
| `temperature` | float | Creativity level (0.0-1.0) | `0.7` |
| `tools` | list | Available tools | `["browser", "code_interpreter"]` |
| `max_tokens` | int | Maximum tokens per response | `4000` |

#### Methods

##### `solve(problem, context=None)`
Solve a complex problem.

```python
solution = wukong.solve(
    problem="Write a web scraper for GitHub trends",
    context="Use Python and BeautifulSoup"
)
```

##### `generate_code(language, task)`
Generate code for a specific task.

```python
code = wukong.generate_code(
    language="python",
    task="Data analysis with pandas"
)
```

##### `research(topic, sources=5)`
Research a topic and gather information.

```python
research_result = wukong.research(
    topic="AI agent frameworks",
    sources=5
)
```

### Bajie Class
The quality auditor (Zhu Bajie).

```python
from westodyssey.agents import Bajie

bajie = Bajie(
    model="claude-3-sonnet",
    strictness="high"
)
```

#### Constructor Parameters
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `model` | str | LLM model to use | `"claude-3-sonnet"` |
| `strictness` | str | Review strictness level | `"high"` |
| `max_review_cycles` | int | Maximum review cycles | `3` |

#### Methods

##### `review(solution, criteria=None)`
Review a solution for quality and safety.

```python
review_result = bajie.review(
    solution=wukong_solution,
    criteria=["security", "efficiency", "best_practices"]
)
```

##### `audit_code(code, language="python")`
Perform code audit.

```python
audit_result = bajie.audit_code(
    code=python_code,
    language="python"
)
```

##### `validate_output(output, format_spec)`
Validate output format.

```python
validation_result = bajie.validate_output(
    output=data_output,
    format_spec={"type": "markdown", "sections": ["introduction", "analysis"]}
)
```

### Wujing Class
The data deliverer (Sha Wujing).

```python
from westodyssey.agents import Wujing

wujing = Wujing(
    model="gpt-3.5-turbo",
    temperature=0.0
)
```

#### Constructor Parameters
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `model` | str | LLM model to use | `"gpt-3.5-turbo"` |
| `temperature` | float | Strictness level | `0.0` |

#### Methods

##### `format(data, format_type="markdown")`
Format data into specified format.

```python
formatted = wujing.format(
    data=raw_data,
    format_type="markdown"
)
```

##### `clean_data(data, rules=None)`
Clean and normalize data.

```python
cleaned = wujing.clean_data(
    data=raw_dataset,
    rules=["remove_duplicates", "normalize_dates"]
)
```

##### `deliver(output, destination)`
Deliver output to destination.

```python
delivery_result = wujing.deliver(
    output=final_output,
    destination="file://output/report.md"
)
```

### Steed Class
The memory system (White Dragon Horse).

```python
from westodyssey.agents import Steed

steed = Steed(
    vector_db_path="memory_database",
    embedding_model="text-embedding-3-small"
)
```

#### Constructor Parameters
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `vector_db_path` | str | Path to vector database | `"memory_database"` |
| `embedding_model` | str | Embedding model to use | `"text-embedding-3-small"` |

#### Methods

##### `record(event, metadata=None)`
Record an event to memory.

```python
steed.record(
    event="mission_completed",
    metadata={"mission_id": "123", "duration": "1.5h"}
)
```

##### `recall(query, limit=5)`
Recall similar memories.

```python
memories = steed.recall(
    query="data analysis mission",
    limit=5
)
```

##### `get_context(mission_id)`
Get context for a specific mission.

```python
context = steed.get_context(mission_id="123")
```

## Workflow API

### Pilgrimage Workflow
The main workflow orchestrator.

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

#### Methods

##### `dispatch(mission, context=None)`
Dispatch a mission through the full workflow.

```python
result = workflow.dispatch(
    mission="Analyze AI trends",
    context="Latest developments in 2024"
)
```

##### `get_progress(mission_id)`
Get progress of a specific mission.

```python
progress = workflow.get_progress(mission_id="123")
```

##### `pause_mission(mission_id)`
Pause a mission for human review.

```python
workflow.pause_mission(mission_id="123")
```

## Configuration API

### Team Configuration
Team configuration structure:

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

### Workflow Configuration
Workflow configuration structure:

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

## Utility Functions

### `load_config(config_path)`
Load configuration from file.

```python
from westodyssey.utils import load_config

config = load_config("config/team_config.json")
```

### `save_config(config, config_path)`
Save configuration to file.

```python
from westodyssey.utils import save_config

save_config(team_config, "config/team_config.json")
```

### `validate_config(config)`
Validate configuration structure.

```python
from westodyssey.utils import validate_config

is_valid = validate_config(team_config)
```

## Error Handling

### Custom Exceptions

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
    print(f"Mission timed out: {e}")
except ReviewCycleExceededError as e:
    print(f"Too many review cycles: {e}")
```

### Error Recovery

```python
from westodyssey.recovery import retry_with_backoff

@retry_with_backoff(max_retries=3)
def execute_mission(mission):
    return workflow.dispatch(mission)
```

## Examples

### Basic Usage
```python
from westodyssey import TangSeng

# Initialize
master = TangSeng()

# Execute mission
result = master.assign_mission(
    mission="Create a market analysis report",
    context="Focus on AI agent market in 2024"
)

print(result["output"])
```

### Advanced Configuration
```python
from westodyssey.workflow import Pilgrimage
from westodyssey.agents import Wukong, Bajie, Wujing, Steed

# Create custom team
wukong = Wukong(model="gpt-4o", tools=["all"])
bajie = Bajie(model="claude-3-5-sonnet", strictness="extreme")
wujing = Wujing(model="gpt-4", temperature=0.0)
steed = Steed(embedding_model="text-embedding-3-large")

# Create workflow
workflow = Pilgrimage(
    wukong=wukong,
    bajie=bajie,
    wujing=wujing,
    steed=steed,
    human_in_the_loop=False  # Full automation
)

# Execute
result = workflow.dispatch("Complex data analysis task")
```

---

**Note**: This API reference is continuously updated. Check the [GitHub repository](https://github.com/SynSwarm/WestOdyssey) for the latest version.