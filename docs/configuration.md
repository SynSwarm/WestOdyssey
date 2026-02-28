# Configuration Guide

This guide explains how to configure Westodyssey for your specific needs.

## Table of Contents
1. [Quick Configuration](#quick-configuration)
2. [Team Configuration](#team-configuration)
3. [Workflow Configuration](#workflow-configuration)
4. [Model Configuration](#model-configuration)
5. [Tool Configuration](#tool-configuration)
6. [Memory Configuration](#memory-configuration)
7. [Environment Variables](#environment-variables)
8. [Best Practices](#best-practices)

## Quick Configuration

### Minimal Configuration
Create a `.env` file in your project root:

```bash
# .env
OPENAI_API_KEY=your_openai_api_key_here
```

Create basic configuration files:

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

### Quick Start Script
```python
# quick_start.py
from westodyssey import TangSeng
import os

# Load API key from environment
os.environ["OPENAI_API_KEY"] = "your_key_here"

# Initialize with default config
master = TangSeng()

# Ready to use!
```

## Team Configuration

### Wukong Configuration
The core problem solver configuration:

```json
{
  "wukong": {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 4000,
    "tools": ["browser", "code_interpreter", "web_search", "file_system"],
    "timeout_seconds": 300,
    "retry_attempts": 3,
    "system_prompt": "You are Sun Wukong, the Monkey King. You are the most capable problem solver...",
    "capabilities": {
      "code_generation": true,
      "data_analysis": true,
      "research": true,
      "planning": true
    }
  }
}
```

### Bajie Configuration
The quality auditor configuration:

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
    "system_prompt": "You are Zhu Bajie, the quality auditor. You are extremely挑剔...",
    "validation_rules": {
      "code_quality": ["pylint", "black"],
      "security_checks": ["bandit", "safety"],
      "performance_checks": true
    }
  }
}
```

### Wujing Configuration
The data deliverer configuration:

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
    "system_prompt": "You are Sha Wujing, the data deliverer. You are严谨 and precise..."
  }
}
```

### Steed Configuration
The memory system configuration:

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
    "system_prompt": "You are the White Dragon Horse, the memory system..."
  }
}
```

## Workflow Configuration

### Basic Workflow
```yaml
# config/workflow.yaml
workflow:
  name: "Standard Pilgrimage"
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

### Advanced Workflow
```yaml
workflow:
  name: "Advanced Analysis Workflow"
  
  phases:
    - phase: "Discovery"
      steps: ["research", "data_gathering", "initial_analysis"]
      parallel: false
      
    - phase: "Solution Development"
      steps: ["design", "implementation", "testing"]
      parallel: true
      max_parallel: 2
      
    - phase: "Quality Assurance"
      steps: ["code_review", "security_audit", "performance_test"]
      parallel: false
      
    - phase: "Delivery"
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

## Model Configuration

### OpenAI Models
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

### Anthropic Models
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

### Model Selection Strategy
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

## Tool Configuration

### Available Tools
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

### Tool Permission System
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

## Memory Configuration

### Vector Database
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

### Memory Optimization
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

## Environment Variables

### Required Variables
```bash
# .env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
BRAVE_API_KEY=...
GITHUB_TOKEN=...
```

### Optional Variables
```bash
# Optional configuration
WESTODYSSEY_LOG_LEVEL=INFO
WESTODYSSEY_CACHE_DIR=./cache
WESTODYSSEY_MAX_TOKENS=1000000
WESTODYSSEY_TIMEOUT=3600
WESTODYSSEY_DATA_DIR=./data
```

### Docker Environment
```dockerfile
# Docker environment variables
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
ENV WESTODYSSEY_LOG_LEVEL=INFO
ENV PYTHONPATH=/app
```

## Best Practices

### Configuration Management
1. **Use Environment Variables** for secrets
2. **Version Control** configuration files
3. **Validate Configurations** before deployment
4. **Use Templates** for common configurations
5. **Document All Options** thoroughly

### Performance Optimization
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

### Security Best Practices
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

### Monitoring Configuration
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

### Example Configuration Files

#### Complete Example
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

#### Production Configuration
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

**Next Steps:**
1. Test your configuration with `westodyssey validate-config`
2. Start with minimal configuration and expand as needed
3. Monitor performance and adjust accordingly
4. Review configuration regularly for optimization opportunities