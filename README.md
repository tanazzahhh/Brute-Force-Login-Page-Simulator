# Brute Force Login Simulator 

This project simulates a brute-force attack on a simple login form using Python and Selenium. It is meant for **educational purposes only** to demonstrate how weak passwords can be guessed from a wordlist.

---

## What This Project Does

- Tries multiple passwords from a list (`wordlist.txt`)
- Automates the process using Selenium
- Shows how quickly a weak password can be cracked

---

## Files in This Project

- `login.html` — A basic login form (runs locally)
- `wordlist.txt` — A list of passwords to try
- `brute_force.py` — Python script that runs the brute-force attack

---

## How to Use It

### Step 1: Install Requirements

Make sure you have Python installed. Then run this in your terminal:

```bash
pip install selenium
```

---

### Step 2: Set Things Up

- Save all the files (HTML, TXT, and Python) in the **same folder**.
- Open the `login.html` file in your browser to see the form.
- Make sure your Chrome browser is installed.
- If needed, [Download ChromeDriver](https://sites.google.com/chromium.org/driver/) and make sure it's in your system PATH.

*(If it already works for you, you can skip the download.)*

---

### Step 3: Run the Brute Force Script

In the terminal, go to the folder where your files are saved and run:

```bash
python brute_force.py
```

It will:
- Open your local login page
- Try each password from the wordlist
- Stop when the correct password is found

---

## Disclaimer

This project is for **learning purposes only**. Do not use it on real websites or without permission.

---

## Author

**Tanazzah Shaikh**  
Cybersecurity Student & Enthusiast
