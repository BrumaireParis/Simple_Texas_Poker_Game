# 德州扑克单机版 / Texas Hold'em Single-Player

一个使用 Python + Tkinter 制作的单机德州扑克图形界面游戏。项目以可运行、易测试、规则相对完整为目标，适合作为桌面小游戏原型。

This is a single-player Texas Hold'em desktop game built with Python and Tkinter. It focuses on being playable, easy to inspect, and reasonably faithful to the core poker flow.

## 创作说明 / Creation Note

本程序为 AI 辅助创作项目：核心设计、代码实现、调试和文档整理均在人类指令与 AI 编程助手协作下完成。

This program was created with AI assistance. The design, implementation, debugging, and documentation were completed through collaboration between a human user and an AI coding assistant.

## 功能特色 / Features

- 主菜单：新游戏、排行榜、设置、退出游戏。
- 设置：支持主流分辨率、UI 缩放、全屏切换和语言切换。
- 多语言：中文、英语、德语、法语、西语、葡语、日语、韩语；首次启动默认跟随系统语言。
- 新游戏：可选择 AI 数量、AI 难度和分房，最多 6 人同桌（玩家 + 5 名 AI）。
- 分房：新手房、普通房、高倍房，不同房间拥有不同盲注和初始资金。
- 规则流程：庄位轮转、小盲/大盲、烧牌、翻牌/转牌/河牌、看牌、跟注、加注、弃牌、摊牌、all-in 分池结算。
- AI 行为：不同难度和隐藏游玩风格，高级 AI 会通过蒙特卡洛模拟估算胜率。
- 对局节奏：AI 会模拟思考时间；玩家行动有 30 秒倒计时。
- 牌桌表现：随机 AI 名字、虚拟头像、行动浮层、筹码堆图像和侧边栏行动记录。
- 复盘辅助：摊牌后，赢家最佳 5 张牌会以黄色边框高亮。
- 排行榜：按净收益优先排序，显示资金、胜局/手数、胜率和房间；空榜会显示虚拟挑战记录，首次保存真实成绩后自动替换。

English summary:

- Main menu with New Game, Leaderboard, Settings, and Exit.
- Common resolutions, UI scaling, fullscreen mode, and language selection.
- Eight UI languages: Chinese, English, German, French, Spanish, Portuguese, Japanese, and Korean.
- Up to 6 players at one table, including the human player.
- Multiple rooms with different blinds and buy-ins.
- Dealer rotation, blinds, burn cards, flop/turn/river, betting, showdown, all-in handling, and side pots.
- AI opponents with difficulty levels, randomized play styles, and Monte Carlo win-rate estimation on higher difficulty.
- Simulated AI thinking time and a 30-second player action timer.
- Avatars, action bubbles, chip visuals, scrollable action log, and highlighted winning five-card hands.
- Profit-first leaderboard with virtual challenge entries before the first real record.

## 运行方式 / How To Run

需要 Python 3。Tkinter 通常随 Python 一起安装。

Python 3 is required. Tkinter is usually included with standard Python installations.

```bash
python texas_holdem_gui.py
```

## 文件说明 / Files

- `texas_holdem_gui.py`：游戏主程序。
- `leaderboard.json`：排行榜存档。发行版默认为空数组，游戏会在空榜时显示虚拟挑战榜。
- `readme.md`：项目说明文档。

## 备注 / Notes

这是一个单机娱乐项目，不涉及真钱下注，也不提供联网多人功能。AI 行为用于模拟牌桌节奏和决策，并不代表真实扑克训练软件的强度。

This is a single-player entertainment project. It does not involve real-money gambling and does not include online multiplayer. The AI is designed for table feel and casual gameplay rather than professional poker training.
