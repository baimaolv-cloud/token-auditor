#!/usr/bin/env python3
"""
TOKEN 审计日志记录工具

用法:
  python log_token.py --task "qqbrowser-skill 修复" --type DEBUG --in 3200 --out 4100 --cached 153000
  python log_token.py --report                    # 生成当日 TOP3 报告
  python log_token.py --summary                   # 显示当日摘要
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# 日志目录
LOG_DIR = Path.home() / ".qclaw" / "workspace" / "logs" / "token-audit"
ARCHIVE_DIR = LOG_DIR / "archive"

def ensure_dirs():
    """确保日志目录存在"""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

def get_today_log() -> Path:
    """获取当日日志文件路径"""
    today = datetime.now().strftime("%Y-%m-%d")
    return LOG_DIR / f"{today}.jsonl"

def get_today_summary() -> Path:
    """获取当日摘要文件路径"""
    today = datetime.now().strftime("%Y-%m-%d")
    return LOG_DIR / f"{today}-summary.md"

def log_token(
    task_name: str,
    task_type: str,
    tokens_in: int,
    tokens_out: int,
    tokens_cached: int,
    cost_usd: float = 0.0,
    session_id: Optional[str] = None,
    details: Optional[dict] = None
):
    """记录 TOKEN 消耗"""
    ensure_dirs()
    
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "task_name": task_name,
        "task_type": task_type,
        "tokens_in": tokens_in,
        "tokens_out": tokens_out,
        "tokens_cached": tokens_cached,
        "tokens_total": tokens_in + tokens_out,
        "cost_usd": cost_usd,
        "session_id": session_id or "unknown",
        "details": details or {}
    }
    
    log_file = get_today_log()
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
    
    print(f"[OK] Logged: {task_name} ({log_entry['tokens_total']} TOKEN)")
    return log_entry

def generate_report():
    """生成当日 TOP3 报告"""
    ensure_dirs()
    
    log_file = get_today_log()
    if not log_file.exists():
        print("[WARN] 当日无 TOKEN 记录")
        return
    
    # 读取所有记录
    records = []
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    
    if not records:
        print("[WARN] 当日无 TOKEN 记录")
        return
    
    # 统计
    total_in = sum(r["tokens_in"] for r in records)
    total_out = sum(r["tokens_out"] for r in records)
    total_cached = sum(r["tokens_cached"] for r in records)
    total_cost = sum(r["cost_usd"] for r in records)
    
    # 按 task_name 分组统计
    task_stats = {}
    for r in records:
        name = r["task_name"]
        if name not in task_stats:
            task_stats[name] = {
                "count": 0,
                "tokens_in": 0,
                "tokens_out": 0,
                "tokens_cached": 0,
                "cost_usd": 0.0,
                "type": r["task_type"],
                "details": []
            }
        task_stats[name]["count"] += 1
        task_stats[name]["tokens_in"] += r["tokens_in"]
        task_stats[name]["tokens_out"] += r["tokens_out"]
        task_stats[name]["tokens_cached"] += r["tokens_cached"]
        task_stats[name]["cost_usd"] += r["cost_usd"]
        task_stats[name]["details"].append(r["details"])
    
    # 排序 TOP3
    top3 = sorted(
        task_stats.items(),
        key=lambda x: x[1]["tokens_in"] + x[1]["tokens_out"],
        reverse=True
    )[:3]
    
    # 生成报告
    today = datetime.now().strftime("%Y-%m-%d")
    report = f"""# TOKEN 审计日报 - {today}

## 总览

- **总消耗**：{total_in + total_out}K TOKEN ({total_in}K in + {total_out}K out)
- **缓存利用**：{total_cached}K TOKEN
- **预估成本**：${total_cost:.4f}
- **任务数量**：{len(task_stats)} 个

## TOP3 消耗任务
"""
    
    for i, (task_name, stats) in enumerate(top3, 1):
        total_tokens = stats["tokens_in"] + stats["tokens_out"]
        percentage = (total_tokens / (total_in + total_out) * 100) if (total_in + total_out) > 0 else 0
        
        report += f"""### {i}. {task_name}
- **消耗**：{total_tokens}K TOKEN ({percentage:.1f}%)
- **类型**：{stats["type"]}
- **次数**：{stats["count"]} 次
- **详情**：
"""
        
        # 汇总 details
        all_details = {}
        for d in stats["details"]:
            for k, v in d.items():
                if k not in all_details:
                    all_details[k] = 0
                all_details[k] += v if isinstance(v, (int, float)) else 1
        
        for k, v in all_details.items():
            report += f"  - {k}：{v} 次\n"
        
        report += "\n"
    
    report += f"""## 优化建议

_根据今日消耗情况，建议关注 TOP1 任务的 TOKEN 优化_

---

*生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M")}*
*累计任务：{len(records)} 条记录*
"""
    
    # 写入报告
    summary_file = get_today_summary()
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"[OK] Report generated: {summary_file}")
    print(report)

def show_summary():
    """显示当日摘要"""
    log_file = get_today_log()
    if not log_file.exists():
        print("[WARN] 当日无 TOKEN 记录")
        return
    
    records = []
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    
    if not records:
        print("[WARN] 当日无 TOKEN 记录")
        return
    
    total_in = sum(r["tokens_in"] for r in records)
    total_out = sum(r["tokens_out"] for r in records)
    total_cached = sum(r["tokens_cached"] for r in records)
    
    print(f"""
今日 TOKEN 消耗摘要 ==========================================
输入 TOKEN：{total_in}K
输出 TOKEN：{total_out}K
缓存 TOKEN：{total_cached}K
总消耗：{total_in + total_out}K
任务数量：{len(records)} 个
=============================================================
""")

def main():
    parser = argparse.ArgumentParser(description="TOKEN 审计工具")
    parser.add_argument("--task", help="任务名称")
    parser.add_argument("--type", default="UNKNOWN", help="任务类型 (DEBUG/CODE/REPORT/ROUTINE)")
    parser.add_argument("--in", dest="tokens_in", type=int, default=0, help="输入 TOKEN")
    parser.add_argument("--out", dest="tokens_out", type=int, default=0, help="输出 TOKEN")
    parser.add_argument("--cached", dest="tokens_cached", type=int, default=0, help="缓存 TOKEN")
    parser.add_argument("--cost", dest="cost_usd", type=float, default=0.0, help="成本 USD")
    parser.add_argument("--session", dest="session_id", help="会话 ID")
    parser.add_argument("--report", action="store_true", help="生成报告")
    parser.add_argument("--summary", action="store_true", help="显示摘要")
    
    args = parser.parse_args()
    
    if args.report:
        generate_report()
    elif args.summary:
        show_summary()
    elif args.task:
        log_token(
            task_name=args.task,
            task_type=args.type,
            tokens_in=args.tokens_in,
            tokens_out=args.tokens_out,
            tokens_cached=args.tokens_cached,
            cost_usd=args.cost_usd,
            session_id=args.session_id
        )
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
