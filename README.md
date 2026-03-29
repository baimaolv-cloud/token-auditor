# token-auditor

**TOKEN 娑堣€楀璁″伐鍏?* - 缁熻褰撴棩 TOKEN 娑堣€?TOP3 浠诲姟锛岀敓鎴愬璁℃姤鍛娿€?
## 鍔熻兘鐗规€?
- 鉁?璁板綍姣忎釜浠诲姟鐨?TOKEN 娑堣€楋紙杈撳叆/杈撳嚭/缂撳瓨锛?- 鉁?鑷姩鐢熸垚姣忔棩 TOP3 娑堣€楁姤鍛?- 鉁?鏀寔浠诲姟鍒嗙被锛圖EBUG/REPORT/ROUTINE锛?- 鉁?鎻愪緵浼樺寲寤鸿
- 鉁?瓒嬪娍瀵规瘮鍒嗘瀽

## 瀹夎

```bash
# 浠?SkillHub 瀹夎
skillhub install token-auditor

# 鎴栦粠 GitHub 瀹夎
git clone https://github.com/baimaolv-cloud/token-auditor.git
```

## 浣跨敤鏂规硶

### 1. 璁板綍浠诲姟娑堣€?
```bash
python scripts/log_token.py \
  --task "qqbrowser-skill 淇" \
  --type DEBUG \
  --in 3200 \
  --out 4100 \
  --cached 153000
```

### 2. 鐢熸垚鏃ユ姤

```bash
python scripts/log_token.py --report
```

### 3. 鏌ョ湅鎽樿

```bash
python scripts/log_token.py --summary
```

## 瀹¤鎶ュ憡绀轰緥

```markdown
# TOKEN 瀹¤鏃ユ姤 - 2026-03-29

## 馃搳 鎬昏

- **鎬绘秷鑰?*锛?2.6K TOKEN (4.7K in + 7.9K out)
- **缂撳瓨鍒╃敤**锛?33K TOKEN
- **浠诲姟鏁伴噺**锛? 涓?
## 馃敐 TOP3 娑堣€椾换鍔?
### 1锔忊儯 qqbrowser-skill 淇
- **娑堣€?*锛?.3K TOKEN (58%)
- **绫诲瀷**锛欴EBUG
- **鍏抽敭鍙戠幇**锛氭祻瑙堝櫒鍛戒护杈撳嚭鏄渶澶ф秷鑰楁簮

### 2锔忊儯 TOKEN 娑堣€楀垎鏋愭姤鍛?- **娑堣€?*锛?.0K TOKEN (32%)
- **绫诲瀷**锛歊EPORT

### 3锔忊儯 鏃ュ父闂€欎笌鐘舵€佹鏌?- **娑堣€?*锛?.3K TOKEN (10%)
- **绫诲瀷**锛歊OUTINE
```

## 鏃ュ織缁撴瀯

```
workspace/logs/token-audit/
鈹溾攢鈹€ 2026-03-29.jsonl         # 璇︾粏璁板綍
鈹溾攢鈹€ 2026-03-29-summary.md    # TOP3 鎶ュ憡
鈹斺攢鈹€ archive/                 # 鍘嗗彶褰掓。
```

## 鍏抽敭鍙戠幇

鏍规嵁瀹為檯浣跨敤锛?*娴忚鍣ㄨ緭鍑烘槸鏈€澶?TOKEN 娑堣€楁簮**锛?
- `browser_snapshot` 鍗曟杩斿洖 4000+ 琛屽唴瀹?- 绾︽秷鑰?50K TOKEN锛堝崰涓婁笅鏂囩殑 32%锛?- **浼樺寲寤鸿**锛氱敤 `browser_get_info --type title` 鏇夸唬

## 浼樺寲鏁堟灉

| 浼樺寲椤?| 褰撳墠 | 浼樺寲鍚?| 鑺傜渷 |
|--------|------|--------|------|
| 娴忚鍣ㄨ緭鍑?| 50K | 5K | 90% |
| 瀵硅瘽鍘嗗彶 | 62K | 12K | 80% |
| 绯荤粺涓婁笅鏂?| 26K | 8K | 70% |

## 鐗堟湰鍘嗗彶

- **v1.0** (2026-03-29) - 鍒濆鐗堟湰
  - 鏀寔 TOKEN 璁板綍
  - 鏀寔 TOP3 鎶ュ憡鐢熸垚
  - 鏀寔浠诲姟鍒嗙被

## 浣滆€?
XiaoXia (灏忚櫨) 馃

## 璁稿彲璇?
MIT License
