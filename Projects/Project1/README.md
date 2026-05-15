# 🧾 Interactive Personal Data Collector (Python)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Project-Beginner%20Friendly-green)
![Type](https://img.shields.io/badge/Project-Console%20App-orange)

---

## 🌟 Overview
The **Interactive Personal Data Collector** is a beginner-friendly Python console application that takes user input, processes it, and displays structured personal information.

It also demonstrates how Python handles **data types**, **memory addresses**, and **type conversion** in a simple and interactive way.

---

## ✨ Features
- 👤 Takes user details (Name, Age, Height, Favourite Number)
- 🧠 Displays data types using `type()`
- 🧮 Shows memory address using `id()`
- 🎂 Calculates approximate birth year
- 💬 Interactive terminal experience

---

## 💻 How It Works
1. Program welcomes the user
2. Takes input using `input()`
3. Converts data into proper types:
   - `str` → Name  
   - `int` → Age & Favourite Number  
   - `float` → Height  
4. Calculates birth year:
   ```python
   birthyear = 2026 - age