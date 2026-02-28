# Quick Start Guide

Welcome to Westodyssey! This guide will help you get started with the AI collaboration framework inspired by Journey to the West.

## Installation

### Prerequisites
- Python 3.8 or higher
- Git
- OpenAI API key (or compatible LLM API)

### Step 1: Clone the Repository
```bash
git clone https://github.com/SynSwarm/WestOdyssey.git
cd WestOdyssey
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure API Key
Create a `.env` file in the project root:
```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

## Your First Mission

### Basic Usage
```python
from westodyssey import TangSeng

# Initialize the master (user proxy)
master = TangSeng()

# Assign a mission to the team
result = master.assign_mission(
    mission="Analyze trending AI projects on GitHub",
    context="Focus on projects related to multi-agent systems"
)

print(result)
```

### Understanding the Team Roles

Westodyssey organizes AI agents into four specialized roles:

#### 1. Wukong (悟空) - The Problem Solver
```python
# Wukong handles complex problem solving
wukong_result = master.wukong.solve("Write a Python script to scrape data")
```

#### 2. Bajie (八戒) - The Quality Auditor
```python
# Bajie reviews and audits all solutions
review_result = master.bajie.review(wukong_result)
```

#### 3. Wujing (沙僧) - The Deliverer
```python
# Wujing formats and delivers the final result
final_output = master.wujing.format(review_result)
```

#### 4. White Horse (白龙马) - The Memory
```python
# White Horse remembers all past missions
history = master.steed.recall("similar missions")
```

## Configuration

### Team Configuration
You can customize your team in `config/team_config.json`:

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

### Workflow Configuration
Configure the collaboration workflow in `config/workflow.yaml`:

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

## Examples

Check out the `examples/` directory for more comprehensive examples:

1. **Data Analysis**: `examples/data-analysis/`
2. **Code Review**: `examples/code-review/`
3. **Document Generation**: `examples/document-generation/`

## Next Steps

1. **Explore Documentation**: Read the full documentation for advanced features
2. **Join Community**: Participate in [GitHub Discussions](https://github.com/SynSwarm/WestOdyssey/discussions)
3. **Report Issues**: Help improve Westodyssey by reporting bugs
4. **Contribute**: Check out our [Contribution Guide](../CONTRIBUTING.md)

## Troubleshooting

### Common Issues

1. **API Key Issues**: Ensure your `.env` file contains a valid API key
2. **Dependency Issues**: Make sure all requirements are installed
3. **Permission Issues**: Check file permissions in the config directory

### Getting Help
- Check the [FAQ](../docs/faq.md)
- Join our [Discussions](https://github.com/SynSwarm/WestOdyssey/discussions)
- Open an [Issue](https://github.com/SynSwarm/WestOdyssey/issues)

---

**Remember**: Every complex task is a Digital Odyssey. Let your AI disciples work together to conquer it!