# 🌌 Aurora-Plan 学习与邮件自动化系统

> 一个融合提示工程、AI 学习与实战演练的学习自动化系统，支持每日任务、邮件提醒与项目扩展。

## 📌 项目目标

本项目旨在帮助学习者通过系统化方式掌握软件工程、提示工程与人工智能相关知识，逐步构建实际可用的自动化工具，并在过程中强化编程实践能力。

- 📧 Gmail API 邮件提醒
- 🧠 提示工程学习 JSON 模板
- 🔄 自动化脚本执行任务
- 💡 结合实战项目进行阶段性总结与功能扩展

## 🗂️ 目录结构说明

```bash
Aurora-Plan/
├── config/                    # 配置文件，如 Gmail API 授权
│   ├── credentials.json
│   └── token.json
├── data/                      # 学习计划数据文件（每日任务、总结）
│   └── learning_plan.json
├── email_templates/          # HTML 富格式邮件模板
│   ├── day_1.html
│   └── week_summary_1.html
├── scripts/                  # 执行任务的主脚本（发送邮件、加载计划）
│   ├── send_daily_email.py
│   └── utils.py
├── notes/                    # 提示工程相关笔记（可拓展为 Markdown）
│   └── prompting_notes.md
├── .gitignore
├── README.md
└── requirements.txt
```

## 🚀 快速开始

### 1. 克隆仓库并安装依赖

```bash
git clone https://github.com/your-username/Aurora-Plan.git
cd Aurora-Plan
pip install -r requirements.txt
```

### 2. 配置 Gmail API

将你从 [Google Cloud Console](https://console.cloud.google.com/) 下载的 `credentials.json` 和授权生成的 `token.json` 放入 `config/` 目录。

### 3. 运行每日任务邮件发送

```bash
python scripts/send_daily_email.py
```

程序将读取 `data/learning_plan.json` 中的当天任务内容，并调用 Gmail API 发送邮件。

## ✨ 核心功能

- 每日学习内容任务 + 邮件提醒
- 支持 HTML 富格式邮件
- 提示工程相关提示词记录与实践
- 每 7 天自动生成阶段总结邮件
- 可拓展的目录结构（支持笔记、脚本、模型接口等）

## 📚 推荐学习方式

> 每天 1～2 小时，坚持输出 + 实战演练，结合 Aurora-Plan 实际开发过程完成提示工程的学习与复现。

1. 每天完成学习计划 JSON 中的任务；
2. 阅读邮件内容中 HTML 模板里的提示与鼓励；
3. 在 `notes/` 目录记录今日笔记、反思与反馈；
4. 逐步拓展项目功能，例如：
   - 增加发送 Slack 通知
   - 增加日历集成
   - 自动整理每周总结到 Notion 或 Obsidian

## 🔒 安全建议

- `credentials.json` 和 `token.json` 不应提交到公共仓库。
- `.gitignore` 已自动排除上述文件。

## 🤝 协作与贡献

欢迎任何建议与贡献，后续将支持更多脚本模块和自动化调度能力。

---

_🪐 Aurora-Plan，点亮学习与创作的未来之旅。_
