---
name: token-auditor
version: 1.0.0
description: TOKEN 消耗审计工具。用于统计当日 TOKEN 消耗 TOP3 任务，生成审计报告。每日结束时自动生成日报，支持手动查询。
author: XiaoXia
keywords: TOKEN, 审计, 成本, 统计, 报告, TOP3
---

# TOKEN 消耗审计 Skill

## 触发条件
- 用户询问"TOKEN 消耗"、"成本统计"、"审计报告"
- 每日结束时（22:00-23:00）自动检查是否需要生成日报
- 用户要求查看"TOP3 任务"、"消耗排行"

## 核心功能

### 1. 任务 TOKEN 记录
每次完成重要任务后，记录 TOKEN 消耗，格式如下：

```json
{
  "timestamp": "2026-03-29T22:16:00+08:00",
  "task_name": "qqbrowser-skill 修复",
  "task_type": "DEBUG",
  "tokens_in": 3200,
  "tokens_out": 4100,
  "tokens_cached": 153000,
  "cost_usd": 0.0000,
  "session_id": "session-1774792539993",
  "details": {
    "commands_executed": 15,
    "files_read": 8,
    "browser_outputs": 2,
    "errors": 3
  }
}
```

### 2. 日志文件结构
```
workspace/logs/token-audit/
├── 2026-03-29.jsonl          # 当日详细记录
├── 2026-03-29-summary.md     # 当日 TOP3 报告
└── archive/                  # 历史归档
    └── 2026-03/
        ├── 2026-03-28.jsonl
        └── 2026-03-28-summary.md
```

### 3. 审计报告格式（Markdown）
```markdown
# TOKEN 审计日报 - 2026-03-29

## 总览
- **总消耗**：7.3K TOKEN (3.2K in + 4.1K out)
- **缓存利用**：153K TOKEN (98% hit)
- **预估成本**：$0.0000
- **任务数量**：3 个

## TOP3 消耗任务
### 1. qqbrowser-skill 修复
- **消耗**：5.2K TOKEN (71%)
- **类型**：DEBUG
- **详情**：
  - 命令执行：15 次
  - 文件读取：8 次
  - 浏览器输出：2 次（最大消耗源）
- **优化建议**：使用 `browser_get_info --type title` 替代 `browser_snapshot`

### 2. TOKEN 消耗分析报告
- **消耗**：1.5K TOKEN (21%)
- **类型**：REPORT
- **详情**：
  - 对话轮次：3 次
  - 报告生成：1 次
- **优化建议**：精简报告内容，避免重复分析

### 3. 日常问候与状态检查
- **消耗**：0.6K TOKEN (8%)
- **类型**：ROUTINE
- **详情**：
  - 系统检查：3 次
  - 问候消息：1 次
- **优化建议**：无必要优化

## 优化建议
### 今日发现的问题
1. 浏览器命令输出过大（消耗 50K TOKEN）
2. 对话历史未清理（累积 7 条消息）
3. 工作流文件冗长（26K TOKEN）

### 明日改进计划
1. 启用 browser 命令轻量模式
2. 对话超过 5 条消息时自动总结
3. 精简 AGENTS.md 至 3K TOKEN

## 趋势对比
| 日期       | 消耗   | 任务数 | TOP1        | 趋势     |
|------------|--------|--------|-------------|----------|
| 2026-03-28 | 6.8K   | 2      | 代码分析    | ⬇️       |
| 2026-03-29 | 7.3K   | 3      | DEBUG       | ⬆️       |

---

*生成时间：2026-03-29 22:16*  
*累计消耗：2664.9万 TOKEN*  
```

## 使用方法

当用户询问 TOKEN 消耗情况时：
1. 检查 `workspace/logs/token-audit/` 目录下的当日日志
2. 统计当日所有任务的 TOKEN 消耗
3. 找出 TOP3 消耗任务
4. 生成审计报告，包含：
   - 总消耗统计
   - TOP3 任务详情
   - 优化建议
   - 趋势对比

## 任务类型分类
- **DEBUG**: 调试、修复问题
- **REPORT**: 生成报告、分析
- **ROUTINE**: 日常问候、状态检查
- **DEV**: 开发新功能
- **RESEARCH**: 研究、调研
