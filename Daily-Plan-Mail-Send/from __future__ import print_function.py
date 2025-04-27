import os
import base64
import schedule
import time
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
from email.header import Header

# 学习计划字典，加入资源链接
learning_plan = {
    "Monday": {
        "task": "🔥 今天是 Python 学习日！掌握函数、类与对象！",
        "resources": [
            "📚 Python官方文档：[https://www.python.org/doc/](https://www.python.org/doc/)",
            "🎓 Python基础教程：[https://www.learnpython.org/](https://www.learnpython.org/)"
        ]
    },
    "Tuesday": {
        "task": "💡 今天我们一起入门量化交易！",
        "resources": [
            "📘 量化交易书籍推荐：[https://www.amazon.com/Quantitative-Trading-Strategies-Hands-Algorithmic/dp/1118482923](https://www.amazon.com/Quantitative-Trading-Strategies-Hands-Algorithmic/dp/1118482923)",
            "📊 量化交易教程：[https://www.quantstart.com/](https://www.quantstart.com/)"
        ]
    },
    "Wednesday": {
        "task": "📊 数据分析大挑战！今天我们学习 pandas 库！",
        "resources": [
            "📑 pandas官方文档：[https://pandas.pydata.org/pandas-docs/stable/](https://pandas.pydata.org/pandas-docs/stable/)",
            "🎥 Python数据分析教程：[https://www.datacamp.com/courses/pandas-foundations](https://www.datacamp.com/courses/pandas-foundations)"
        ]
    },
    "Thursday": {
        "task": "🚀 启程机器学习之旅！了解基本算法及应用。",
        "resources": [
            "🎓 机器学习入门：[https://www.coursera.org/learn/machine-learning](https://www.coursera.org/learn/machine-learning)",
            "📚 周志华《机器学习》：[http://www.machinelearning.org/](http://www.machinelearning.org/)"
        ]
    },
    "Friday": {
        "task": "📉 量化交易进阶！继续学习回测策略。",
        "resources": [
            "📖 回测策略资源：[https://www.backtrader.com/](https://www.backtrader.com/)",
            "🔧 回测框架教程：[https://www.quantconnect.com/](https://www.quantconnect.com/)"
        ]
    },
    "Saturday": {
        "task": "💻 编程练习日！来巩固我们这一周学到的知识。",
        "resources": [
            "🔐 LeetCode编程挑战：[https://leetcode.com/](https://leetcode.com/)",
            "💡 编程练习平台：[https://www.hackerrank.com/domains/tutorials/10-days-of-javascript](https://www.hackerrank.com/domains/tutorials/10-days-of-javascript)"
        ]
    },
    "Sunday": {
        "task": "📝 总结日！回顾这周的学习并整理笔记。",
        "resources": [
            "📘 如何做有效笔记：[https://medium.com/@mr_melocotton/how-to-take-notes-like-a-pro-7d5820c431db](https://medium.com/@mr_melocotton/how-to-take-notes-like-a-pro-7d5820c431db)"
        ]
    }
}

def create_message(sender, to, subject, body_text):
    """创建一封带有趣味性和HTML格式的邮件"""
    message = MIMEText(body_text, 'html', 'utf-8')  # 使用html格式以支持丰富内容
    message['to'] = to
    message['from'] = sender
    message['subject'] = Header(subject, 'utf-8')

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_email(to, subject, body_text):
    """通过 Gmail API 发送邮件"""
    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/gmail.send'])
    service = build('gmail', 'v1', credentials=creds)

    message = create_message(
        sender='你的Gmail地址@gmail.com',
        to=to,
        subject=subject,
        body_text=body_text
    )

    send_message = service.users().messages().send(userId="me", body=message).execute()
    print('✅ 邮件发送成功！Message Id:', send_message['id'])

def job():
    """每天定时发送当天的学习计划和资源链接"""
    import datetime
    today = datetime.datetime.now().strftime('%A')  # 获取今天星期几

    subject = f'🚀 今天的学习任务：{today}！'

    # 获取当天学习任务和资源
    task = learning_plan.get(today, {}).get("task", "今天没有学习任务，请更新学习计划。")
    resources = learning_plan.get(today, {}).get("resources", [])

    # 将任务和资源链接合并为邮件正文
    body_text = f"<h2>🎯 今天的任务：{task}</h2><ul>"
    for resource in resources:
        body_text += f"<li>🔗 <a href='{resource}'>{resource}</a></li>"
    body_text += "</ul><br><br><p>加油！💪 每天进步一点点！🚀</p>"

    to = '你的邮箱@gmail.com'  # 修改为你自己的邮箱
    send_email(to, subject, body_text)

# 每天定时发送学习计划（每天早上8点发送）
schedule.every().day.at("08:00").do(job)

# 持续运行脚本，等待执行任务
while True:
    schedule.run_pending()
    time.sleep(60)  # 每60秒检查一次任务是否该执行
