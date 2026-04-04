# Changelog

所有 notable 变更都会记录在此文件。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)。
版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。

## [1.0.1] - 2026-04-04

### Fixed
- 修复 Python 脚本中的中文编码问题（文件原本为 GBK 乱码，已修正为 UTF-8）
- 移除 Windows 控制台不兼容的 emoji 字符，避免 `UnicodeEncodeError`
- 修复 `package.json` 中的中文描述编码问题

### Changed
- 优化控制台输出格式，使用纯文本符号替代 emoji

## [1.0.0] - 2026-03-31

### Added
- 初始版本发布
- TOKEN 消耗记录功能
- 当日 TOP3 消耗任务统计
- Markdown 格式审计报告生成
- 支持任务类型分类（DEBUG/CODE/REPORT/ROUTINE）
