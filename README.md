# 🔍 Frequency Analysis Tool

This project is a **Frequency Analysis Tool** written in Python.  
It performs **letter frequency analysis** and can **decrypt simple Caesar cipher messages** by estimating the most probable shift based on letter frequency.  
It supports both **French ** and **English ** alphabets.

The program includes a **graphical user interface (GUI)** using `Tkinter`, and displays **letter frequency histograms** using `Matplotlib`.

---

## Project Overview

This mini-project allows users to input a piece of text (which can be encrypted) and automatically:

1. **Performs frequency analysis** of the letters in the text.  
2. **Displays a bar chart** showing the frequency of each letter.  
3. **Estimates the Caesar cipher shift** by assuming that the most frequent letter corresponds to `'E'` (common in both French and English).  
4. **Decrypts the text** using the estimated shift value.  
5. **Displays the decrypted text** in a Tkinter window.

This project demonstrates how frequency analysis can be used to **break substitution ciphers**, such as the **Caesar cipher**, by comparing the statistical distribution of letters.

---

## Features

- Performs **letter frequency analysis** using Python’s `collections.Counter`
- Automatically **decrypts Caesar ciphers**
- Displays results as **bar charts** using `matplotlib`
- Provides a simple **graphical interface** using `tkinter`
- Works for **French** and **English** texts
- Includes predefined letter frequency distributions for:
  - French  
  - English  
  - Spanish (for comparison)

---

## Requirements

You need **Python 3.x** and the following library:

```bash
pip install matplotlib
