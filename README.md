# Harmonium Swarams Transposition Tool

A web app that allows users to **select a musical scale and swarams (notes)** and see the corresponding chord **transposed to a chosen scale**, with an interactive piano interface for visualizing the notes.  

This project demonstrates the full workflow of **identifying a problem, designing a solution, and implementing a working tool**.

---

## Features

- Interactive piano keyboard with **clickable keys** representing swarams.  
- Dropdown to select a **target scale** for transposition.  
- **Dynamic output** showing the transposed chord relative to the selected scale.  
- Styled front end for a **clean, user-friendly visualization**.  

---

## Problem

Musicians and learners often need to **transpose swarams (notes) between scales**, which can be tedious to calculate manually. There was no quick, visual way to do this interactively.  

---

## Solution

- Built an **interactive piano interface** to select swarams.  
- Developed a **Flask backend** that computes the transposed chord for any selected scale.  
- Created **dynamic front-end visualizations** to display the transposed notes in real time.  
- Applied **musical theory formulas** to accurately map swarams to notes and transpose them.  

This approach allows users to **see the chord relative to any scale immediately**, providing an intuitive, hands-on tool for learning and practice.  

---

## Skills Demonstrated

- Full-stack web development: **Python (Flask), HTML, CSS, JavaScript**.  
- Problem-solving: translating a **real-world domain problem into a working application**.  
- Integration: connecting front-end interaction with backend logic seamlessly.  
- Domain knowledge: applied **musical theory** to programming logic for accurate transposition.  

---

## How it Works

- The backend, built with **Python and Flask**, calculates the transposed chord for a given scale.  
- The front end uses **HTML, CSS, and JavaScript** to render the piano and display results dynamically.  
- Musical theory formulas are used to map swarams to notes and transpose them accurately.  
- The app **visualizes musical transposition**, allowing users to see how chords shift between scales in real time.

---

## Tech Stack

- Python (Flask)  
- HTML, CSS, JavaScript  
- Musical theory formulas for swaram transposition  

---

## Usage

1. Run the Flask app:  
```bash
python app.py
