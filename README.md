<div align="center">

# CodeAlpha: Python Development Tasks

[![GitHub Repo](https://img.shields.io/badge/GitHub-sharvan--m%2Fcodealpha__tasks-blue?logo=github)](https://github.com/sharvan-m/codealpha_tasks)
[![Language](https://img.shields.io/badge/Language-Python%203.x-blue?logo=python)](https://www.python.org/)
[![Internship](https://img.shields.io/badge/Internship-CodeAlpha%20Python-orange)](#-overview)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](#-license)

**A practical collection of Python projects developed for the CodeAlpha Python Development Internship, showcasing game development logic, financial tracking automation, and file-system manipulation.**

[Overview](#-overview) • [Task Breakdown](#-task-breakdown) • [Project Details](#-project-details) • [Repository Structure](#-repository-structure) • [Execution Guide](#-execution-guide)

</div>

---

## 📖 Overview

This repository contains clean, standalone Python utility applications engineered during the **CodeAlpha Python Development Internship**. Each script demonstrates fundamental programming paradigms using the Python standard library with zero external dependency requirements:

- **Interactive Control Flow & Game Loops (`p1.py`)**
- **Dictionary Data Structures & File I/O (`p2.py`)**
- **Operating System Automation & File Management (`p3.py`)**

---

## 📋 Task Breakdown

| Script | Project Title | Key Modules | Focus & Capabilities |
| :--- | :--- | :--- | :--- |
| **`p1.py`** | **Hangman Word Guessing Game** | `random` | Interactive word guessing game with attempt tracking and dynamic masking |
| **`p2.py`** | **Stock Portfolio Tracker** | Python Built-ins | Real-time portfolio valuation calculator with automated `portfolio.txt` report export |
| **`p3.py`** | **Automated File Organizer** | `os`, `shutil` | Directory creation and safe batch file movement between directories |

---

## 🛠️ Project Details

### 🎮 1. Hangman Word Guessing Game (`p1.py`)
A classic CLI-based word puzzle game. The computer picks a secret word, and the player attempts to guess it letter by letter within a limited number of allowed attempts.
- **Logic:**
  - Random secret word selection via `random.choice`.
  - Dynamic display showing revealed characters and remaining blanks (`_`).
  - Attempt counter (starts at 6 lives) decrementing on incorrect guesses.
- **Run:**
  ```bash
  python p1.py
  ```

---

### 📈 2. Stock Portfolio Tracker (`p2.py`)
A financial calculator that computes the aggregate monetary value of a user's stock holdings based on live stock prices.
- **Features:**
  - Configurable pricing dictionary (`AAPL`, `TSLA`, `GOOG`, `MSFT`).
  - Interactive user prompts for share quantities.
  - Automatically writes the calculated net worth to an output file (`portfolio.txt`).
- **Run:**
  ```bash
  python p2.py
  ```

---

### 📂 3. Automated File Transfer Utility (`p3.py`)
A system automation script that automates moving files from an ingestion directory to a designated target location.
- **Features:**
  - Verifies and automatically initializes the destination directory if missing using `os.makedirs`.
  - Iterates through source files and transfers them safely via `shutil.move`.
- **Run:**
  ```bash
  python p3.py
  ```

---

## 📂 Repository Structure

```text
codealpha_tasks/
├── p1.py              # Task 1: Hangman Word Guessing Game
├── p2.py              # Task 2: Stock Portfolio Investment Tracker
├── p3.py              # Task 3: Automated File Transfer Utility
├── .gitignore         # Build and output exclusions
└── README.md          # Comprehensive project documentation
```

---

## ⚡ Execution Guide

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/) installed. No third-party packages required — all projects use Python's built-in standard library (`random`, `os`, `shutil`).

### Clone and Run
```bash
git clone https://github.com/sharvan-m/codealpha_tasks.git
cd codealpha_tasks

# Run any task directly:
python p1.py
python p2.py
python p3.py
```

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).

*Developed as part of the CodeAlpha Python Development Internship by [Sharvan M](https://github.com/sharvan-m).*
