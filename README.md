# 🎯 Number Guessing Game Using Python & Tkinter

## 📌 Project Overview

Number Guessing Game is a GUI-based Python project developed using the Tkinter library. In this game, the computer randomly generates a secret number according to the selected difficulty level, and the player has to guess that number within a limited number of attempts and within a specific time limit.

The project is designed to improve problem-solving skills and demonstrate the use of Python GUI programming concepts such as event handling, functions, conditional statements, timers, exception handling, and random number generation.

---

# ✨ Features

### 1. Graphical User Interface (GUI)
- Developed using Python Tkinter.
- User-friendly interface with buttons, labels, and input fields.

### 2. Difficulty Levels
The game provides three difficulty levels:

| Difficulty | Number Range | Maximum Attempts |
| Easy       | 1 – 50       | 10 Attempts      |
| Medium     | 1 – 100      | 7 Attempts       |
| Hard       | 1 – 500      | 5 Attempts       |

---

### 3. Random Number Generation
A secret number is generated using Python's `random` module.

Example:

```python
number = random.randint(1,100)
```

---

### 4. Guess Validation

The game checks whether the entered number is:

- Too Low
- Too High
- Correct

---

### 5. Limited Attempts

The player has a fixed number of attempts according to the selected difficulty level.

---

### 6. Countdown Timer

- The player gets 30 seconds to guess the number.
- Timer automatically decreases every second.
- If time reaches zero, the game ends.

---

### 7. Hint System

The Hint button tells whether the secret number is:

- Even Number
- Odd Number

---

### 8. Best Score Feature

The game stores the minimum number of attempts used to win.

---

### 9. Play Again Feature

Allows the player to restart the game without closing the application.

---

# 🛠 Technologies Used

| Technology    | Purpose                   |
| Python 3      | Programming Language      |
| Tkinter       | GUI Development           |
| Random Module | Random Number Generation  |
| MessageBox    | Popup Messages            |

---

# 📚 Python Concepts Used

## 1. Functions

```python
def start_game():
def guess():
def countdown():
def hint():
```

Used to divide the program into reusable blocks.

---

## 2. Variables

Examples:

```python
number
attempts
max_attempts
time_left
best_score
```

---

## 3. Global Variables

```python
global number, attempts, max_attempts, time_left
```

Used to access variables inside functions.

---

## 4. Conditional Statements

```python
if
elif
else
```

Used for checking user guesses.

---

## 5. Loops

Timer repeatedly executes using:

```python
root.after()
```

---

## 6. Exception Handling

```python
try:
except:
```

Prevents the program from crashing when invalid input is entered.

---

## 7. Event Driven Programming

Buttons trigger functions when clicked.

Example:

```python
command=guess
command=hint
```

---

## 8. String Formatting

```python
f"Attempts Left : {left}"
```

---

## 9. Operators Used

### Arithmetic Operators

```python
+
-
%
+=
-=
```

### Comparison Operators

```python
<
>
==
```

---

## 10. GUI Widgets Used

### Label
Displays text.

### Entry
Takes user input.

### Button
Performs actions.

### OptionMenu
Used for selecting difficulty.

### MessageBox
Displays popup messages.

---

# 📂 Project Structure

```text
Number-Guessing-Game/
│
├── guessing_game.py
├── README.md
└── screenshots/
```

---

# 🚀 Installation Steps

### Step 1
Install Python.

Download:

https://www.python.org/downloads/

### Step 2
Clone Repository:

```bash
Git clone 
```

### Step 3

Open project folder.

### Step 4

Run:

```bash
python guessing_game.py
```

---

# 🎮 How To Play

### Step 1
Run the program.

### Step 2
Select difficulty level.

### Step 3
Enter your guess.

### Step 4
Click **Guess**.

### Step 5

Game displays:

- Too Low
- Too High
- Correct

### Step 6

Use Hint button if needed.

### Step 7

Win before:

- Attempts finish
OR
- Timer reaches zero.

### Step 8

Press **Play Again** to restart.

---

# 📸 Screenshots

Add project screenshots here.

Example:

---

# 🧠 Algorithm

### Step 1:
Start program.

### Step 2:
Select difficulty.

### Step 3:
Generate random number.

### Step 4:
Initialize:

- attempts = 0
- timer = 30

### Step 5:
Take user input.

### Step 6:

Check:

- Too Low
- Too High
- Correct

### Step 7:

If correct:

Display Winner.

Else:

Continue until attempts or timer end.

### Step 8:

Restart using Play Again.


# 📖 Learning Outcomes

Through this project, the following concepts were learned:

✅ Python GUI Programming

✅ Functions and Modular Programming

✅ Random Number Generation

✅ Event Handling

✅ Exception Handling

✅ Timers in Tkinter

✅ User Input Validation

✅ Game Development Basics

---

# 👨‍💻 Author

**Name:** Alok Singh

**Course:** Bachelor of Computer Applications (BCA)

**University:** Mahatma Gandhi Kashi Vidyapith (MGKVP)

**Project:** Number Guessing Game Using Python Tkinter

---

# 📄 License

This project is developed for educational purposes.
    
