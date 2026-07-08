# 🔥 DSA Streak Tracker

A simple command-line tool that helps you track your daily DSA/LeetCode
practice, maintain a streak, and stay motivated — built with pure Python,
no external libraries required.

## 🚀 Why I built this

I committed to solving at least 1 DSA problem a day. Instead of tracking
it in a notes app, I built this tool to log my practice, see my streak,
and stay accountable — while practicing real Python (file handling, JSON,
functions, and clean CLI design).

## ✨ Features

- Log how many problems you solved each day + the topic/pattern practiced
- Automatically calculates your **current streak**
- Tracks your **best streak ever**
- Shows total problems solved and days logged
- View your last 10 days of practice history
- Motivational messages that scale with your streak length

## 🛠️ Built With

- Python 3 (standard library only — `json`, `os`, `datetime`)

## ⚙️ How to Run

```bash
git clone https://github.com/singhsakshi8322-gif/dsa-streak-tracker.git
cd dsa-streak-tracker
python streak_tracker.py
```

No installation needed — just Python 3 installed on your machine.

## 📸 Example

```
🔥 Current streak     : 4 day(s)
🏆 Best streak so far : 4 day(s)
✅ Total problems     : 11
📅 Days logged        : 4
Solid streak! You're building a real habit. 🚀
```

## 📚 What I Learned

- Working with JSON files for persistent local storage
- Handling dates and calculating consecutive-day streaks
- Structuring a clean, menu-driven CLI application
- Writing functions with single, clear responsibilities

## 🔮 Possible Future Improvements

- Add topic-wise stats (e.g. how many DP vs graph problems solved)
- Export progress as a chart using matplotlib
- Add weekly/monthly summary view

