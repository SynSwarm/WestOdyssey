# 配置指南

本文档解释如何根据您的特定需求配置Westodyssey。

## 目录
1. [快速配置](#快速配置)
2. [团队配置](#团队配置)
3. [工作流配置](#工作流配置)
4. [模型配置](#模型配置)
5. [工具配置](#工具配置)
6. [内存配置](#内存配置)
7. [环境变量](#环境变量)
8. [最佳实践](#最佳实践)

## 快速配置

### 最小配置
在项目根目录创建`.env`文件：

```bash
# .env
OPENAI_API_KEY=your_openai_api_key_here
```

创建基本配置文件：

```bash
# config/team_config.json
{
  "wukong": {
    "model": "gpt-4"
  },
  "bajie": {
    "model": "claude-3-sonnet"
  },
  "wujing": {
    "model": "gpt-3.5-turbo"
  }
}

# config/workflow.yaml
workflow:
  steps:
    - load_context: true
    - solve_problem: true
    - review_solution: true
    - format_output: true
```

### 快速启动脚本
```python
# quick_start.py
from westodyssey import TangSeng
import os

# 从环境变量加载API密钥
os.environ["OPENAI_API_KEY"] = "your_key_here"

# 使用默认配置初始化
master = TangSeng()

# 准备使用！
```

## 团队配置

### Wukong配置
核心问题解决者配置：

```json
{
  "wukong": {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 4000,
    "tools": ["browser", "code_interpreter", "web_search", "file_system"],
    "timeout_seconds": 300,
    "retry_attempts": 3,
    "system_prompt": "你是孙悟空，齐天大圣。你是最强大的问题解决者...",
    "capabilities": {
      "code_generation": true,
      "data_analysis": true,
      "research": true,
      "planning": true
    }
  }
}
```

### Bajie配置
质量审计官配置：

```json
{
  "bajie": {
    "model": "claude-3-sonnet",
    "strictness": "high",
    "max_review_cycles": 3,
    "review_criteria": [
      "security",
      "efficiency", 
      "best_practices",
      "readability",
      "maintainability"
    ],
    "risk_threshold": 0.7,
    "system_prompt": "你是猪八戒，质量审计官。你极其挑剔...",
    "validation_rules": {
      "code_quality": ["pylint", "black"],
      "security_checks": ["bandit", "safety"],
      "performance_checks": true
    }
  }
}
```

### Wujing配置
数据交付者配置：

```json
{
  "wujing": {
    "model": "gpt-3.5-turbo",
    "temperature": 0.0,
    "output_formats": ["markdown", "json", "csv", "html"],
    "formatting_rules": {
      "markdown": {
        "headers": true,
        "tables": true,
        "code_blocks": true
      },
      "json": {
        "indent": 2,
        "sort_keys": true
      }
    },
    "quality_checks": ["syntax", "structure", "completeness"],
    "system_prompt": "你是沙僧，数据交付者。你严谨且精确..."
  }
}
```

### Steed配置
内存系统配置：

```json
{
  "steed": {
    "embedding_model": "text-embedding-3-small",
    "vector_db_path": "memory_database",
    "chunk_size": 1000,
    "chunk_overlap": 200,
    "retrieval_top_k": 5,
    "similarity_threshold": 0.7,
    "memory_retention_days": 30,
    "backup_enabled": true,
    "backup_path": "backups/memory",
    "system_prompt": "你是白龙马，内存系统..."
  }
}
```

## 工作流配置

### 基础工作流
```yaml
# config/workflow.yaml
workflow:
  name: "标准取经流程"
  version: "1.0"
  
  steps:
    - name: "load_context"
      enabled: true
      timeout: 60
      
    - name: "solve_problem"
      enabled: true
      timeout: 300
      
    - name: "review_solution"
      enabled: true
      timeout: 180
      
    - name: "format_output"
      enabled: true
      timeout: 120
      
    - name: "record_memory"
      enabled: true
      timeout: 30

  constraints:
    max_total_time: 1200
    max_review_cycles: 3
    require_human_approval: true
    human_approval_timeout: 3600
    
  notifications:
    enabled: true
    channels: ["console", "file"]
    levels: ["error", "warning", "info"]
    
  monitoring:
    enabled: true
    metrics: ["execution_time", "token_usage", "success_rate"]
    logging_level: "INFO"
```

### 高级工作流
```yaml
workflow:
  name: "高级分析工作流"
  
  phases:
    - phase: "发现阶段"
      steps: ["research", "data_gathering", "initial_analysis"]
      parallel: false
      
    - phase: "解决方案开发"
      steps: ["design", "implementation", "testing"]
      parallel: true
      max_parallel: 2
      
    - phase: "质量保证"
      steps: ["code_review", "security_audit", "performance_test"]
      parallel: false
      
    - phase: "交付阶段"
      steps: ["formatting", "documentation", "deployment"]
      parallel: true

  fallback_strategies:
    - condition: "timeout_exceeded"
      action: "notify_human"
      
    - condition: "quality_below_threshold"
      action: "retry_with_different_approach"
      
    - condition: "resource_exhausted"
      action: "pause_and_wait"

  optimization:
    token_optimization: true
    parallel_execution: true
    cache_enabled: true
    compression_enabled: true
```

## 模型配置

### OpenAI模型
```json
{
  "openai_models": {
    "gpt-4": {
      "max_tokens": 8192,
      "cost_per_1k_tokens": 0.03,
      "capabilities": ["reasoning", "coding", "analysis"]
    },
    "gpt-4-turbo": {
      "max_tokens": 128000,
      "cost_per_1k_tokens": 0.01,
      "capabilities": ["long_context", "multimodal"]
    },
    "gpt-3.5-turbo": {
      "max_tokens": 16385,
      "cost_per_1k_tokens": 0.001,
      "capabilities": ["fast", "efficient"]
    }
  }
}
```

### Anthropic模型
```json
{
  "anthropic_models": {
    "claude-3-5-sonnet": {
      "max_tokens": 200000,
      "capabilities": ["analysis", "writing", "reasoning"]
    },
    "claude-3-opus": {
      "max_tokens": 200000,
      "capabilities": ["complex_reasoning", "strategy"]
    }
  }
}
```

### 模型选择策略
```yaml
model_selection:
  strategy: "cost_aware"
  
  rules:
    - condition: "task_complexity == 'high'"
      model: "gpt-4"
      
    - condition: "task_length > 10000"
      model: "gpt-4-turbo"
      
    - condition: "task_type == 'formatting'"
      model: "gpt-3.5-turbo"
      
    - condition: "review_required == true"
      model: "claude-3-sonnet"
      
  fallback:
    primary: "gpt-4"
    secondary: "gpt-3.5-turbo"
    emergency: "local_llm"
```

## 工具配置

### 可用工具
```json
{
  "tools": {
    "browser": {
      "enabled": true,
      "timeout": 30,
      "headless": true,
      "allowed_domains": ["github.com", "docs.python.org", "stackoverflow.com"]
    },
    
    "code_interpreter": {
      "enabled": true,
      "languages": ["python", "javascript", "bash"],
      "timeout": 60,
      "sandbox": true,
      "memory_limit": "512MB"
    },
    
    "web_search": {
      "enabled": true,
      "provider": "brave",
      "api_key_env": "BRAVE_API_KEY",
      "results_limit": 10,
      "safe_search": true
    },
    
    "file_system": {
      "enabled": true,
      "allowed_paths": ["./data", "./output", "./logs"],
      "read_only": false,
      "backup_enabled": true
    },
    
    "api_client": {
      "enabled": true,
      "apis": {
        "github": {
          "token_env": "GITHUB_TOKEN",
          "rate_limit": 10
        },
        "openweather": {
          "api_key_env": "WEATHER_API_KEY"
        }
      }
    }
  }
}
```

### 工具权限系统
```yaml
tool_permissions:
  wukong:
    - browser: "full"
    - code_interpreter: "full"
    - web_search: "full"
    - file_system: "write"
    - api_client: "read_write"
    
  bajie:
    - browser: "read_only"
    - code_interpreter: "read_only"
    - file_system: "read_only"
    - api_client: "read_only"
    
  wujing:
    - file_system: "write"
    - code_interpreter: "execute_only"
    
  steed:
    - file_system: "read_write"
```

## 内存配置

### 向量数据库
```yaml
memory:
  vector_db:
    type: "chromadb"
    path: "./memory_database"
    collection_name: "mission_memories"
    
  embedding:
    model: "text-embedding-3-small"
    dimension: 1536
    batch_size: 100
    
  retrieval:
    strategy: "hybrid"
    similarity_threshold: 0.7
    top_k: 5
    rerank: true
    
  storage:
    retention_days: 30
    compression: true
    backup_frequency: "daily"
    
  indexing:
    chunk_size: 1000
    chunk_overlap: 200
    metadata_fields: ["mission_id", "timestamp", "agent", "tags"]
```

### 内存优化
```json
{
  "memory_optimization": {
    "deduplication": true,
    "compression": true,
    "pruning": {
      "enabled": true,
      "strategy": "lru",
      "max_items": 10000,
      "min_similarity": 0.9
    },
    "caching": {
      "enabled": true,
      "ttl_seconds": 3600,
      "max_size_mb": 100
    }
  }
}
```

## 环境变量

### 必需变量
```bash
# .env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
BRAVE_API_KEY=...
GITHUB_TOKEN=...
```

### 可选变量
```bash
# 可选配置
WESTODYSSEY_LOG_LEVEL=INFO
WESTODYSSEY_CACHE_DIR=./cache
WESTODYSSEY_MAX_TOKENS=1000000
WESTODYSSEY_TIMEOUT=3600
WESTODYSSEY_DATA_DIR=./data
```

### Docker环境
```dockerfile
# Docker环境变量
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
ENV WESTODYSSEY_LOG_LEVEL=INFO
ENV PYTHONPATH=/app
```

## 最佳实践

### 配置管理
1. **使用环境变量**存储敏感信息
2. **版本控制**配置文件
3. **验证配置**在部署前
4. **使用模板**处理通用配置
5. **详细记录**所有选项

### 性能优化
```yaml
performance:
  token_optimization: true
  parallel_processing: true
  caching:
    enabled: true
    ttl: 3600
  compression:
    enabled: true
    level: "medium"
```

### 安全最佳实践
```yaml
security:
  api_keys:
    storage: "environment"
    rotation: "monthly"
    
  permissions:
    principle: "least_privilege"
    audit_logging: true
    
  data_protection:
    encryption: true
    sanitization: true
    retention_policy: "30_days"
```

### 监控配置
```yaml
monitoring:
  metrics:
    - name: "execution_time"
      aggregation: "average"
      threshold: 300
      
    - name: "token_usage"
      aggregation: "sum"
      alert_threshold: 1000000
      
    - name: "success_rate"
      aggregation: "percentage"
      target: 0.95
      
  alerts:
    - condition: "success_rate < 0.9"
      action: "notify_team"
      
    - condition: "execution_time > 600"
      action: "investigate"
```

### 配置文件示例

#### 完整示例
```bash
# project_root/
#   .env
#   config/
#     team_config.json
#     workflow.yaml
#   data/
#   logs/
#   memory_database/
```

#### 生产环境配置
```json
{
  "environment": "production",
  "team": {
    "wukong": {
      "model": "gpt-4",
      "temperature": 0.3,
      "tools": ["code_interpreter", "api_client"],
      "timeout": 600
    }
  },
  "workflow": {
    "require_human_approval": true,
    "max_review_cycles": 3,
    "monitoring": {
      "enabled": true,
      "alerting": true
    }
  },
  "security": {
    "audit_logging": true,
    "data_encryption": true
  }
}
```

---

**下一步:**
1. 使用`westodyssey validate-config`测试您的配置
2. 从最小配置开始，根据需要扩展
3. 监控性能并进行相应调整
4. 定期审查配置以寻找优化机会