# Aurora Plan - Daily Learning System

## 项目简介

Aurora Plan 是一个基于 GitHub 和 Google Cloud Gmail API 构建的个人学习日程自动化发送系统。
通过本系统，可以每天接收定制化学习计划邮件，结合提示工程练习与项目实操，逐步掌握软件工程与人工智能应用开发能力。

## 功能特色

- 自动从 GitHub 拉取学习计划 JSON 文件
- 使用 Google Cloud Gmail API 自动发送学习内容邮件
- 每天最多学习 2 小时，注重效率与持续性
- 结合提示工程训练，提高与 AI 的交互能力
- 结合实际项目（Daily Plan系统）逐步实操扩展

## 技术栈

- GitHub (存储学习资源与项目代码)
- Google Cloud Console (Gmail API)
- Python (发送邮件与自动化脚本)
- JSON (存储学习计划)
- Visual Studio Code (开发环境)

## 快速开始

1. 配置 Google Cloud Console 项目并启用 Gmail API

2. 下载 `credentials.json` 与 `token.json` 到本地

3. 克隆本项目到本地：

   ```bash
   git clone https://github.com/你的用户名/daily-learning-plan-chatgpt.git
   ```

4. 安装必要的 Python 库：

   ```bash
   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```

5. 运行发送邮件脚本（示例）：

   ```bash
   python send_daily_plan.py
   ```

## 文件结构

```
/Daily-Plan-Mail-Send
    ├── credentials.json
    ├── token.json
    ├── send_daily_plan.py
/learning-plan
    ├── aurora_plan.json
README.md
```

## 后续扩展

- 增加提示工程练习模块
- 整合到 Web 界面（可选）
- 支持多模板、多计划发送
- 提供每日学习数据统计与分析

## 致谢

感谢自己在成长路上的坚持！🌟
