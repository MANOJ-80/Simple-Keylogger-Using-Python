# Simple Keylogger in Python
[![Python Version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## What is a Keylogger?

A keylogger is a type of surveillance software that records every keystroke made on a computer's keyboard. It can capture user inputs including passwords, messages, and other sensitive information. Keyloggers can be used for legitimate purposes, such as monitoring employee activity, but they can also be misused for malicious intent, such as stealing personal information.

![Keylogger Example](keyboard.jpg)

## Purpose of This Project

This project, **Simple Keylogger in Python**, is designed for educational purposes only. It demonstrates how keyloggers function and the mechanisms behind keystroke logging. Understanding these concepts is crucial for cybersecurity awareness and defense strategies.

### Warning:
**DO NOT use this keylogger on any real or sensitive data.** This code is for educational purposes only and should only be run in a controlled environment, such as a personal computer or a virtual machine, where it cannot cause harm. Misuse of this code could result in data loss or legal consequences.

## Features

- **Keystroke Logging**: Records keystrokes along with timestamps.
- **Automatic File Saving**: Saves the logged keystrokes to a text file at specified intervals.
- **ESC Key Functionality**: Stops logging when the ESC key is pressed.

## Files Included

- `keylogger.py`: The main script that captures and logs keystrokes.

## How It Works

### Logging Process:
1. The script listens for key presses in the background.
2. When a key is pressed, it records the keystroke along with a timestamp.
3. The captured keystrokes are saved to a text file (`keylogger.txt`) at regular intervals.
4. The logging process continues until the user presses the ESC key, which stops the listener.

## Requirements

To run this project, you need the following:

- **Python 3.x**
- **pynput library** (install via pip):
  ```bash
  pip install pynput
  ```
## How to Run
1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the keylogger script
   ```bash
   python3 keylogger.py
   ```
   - This will start logging keystrokes until the ESC key is pressed.
## Conclusion
This project serves as a learning tool to understand the mechanics of keyloggers. It highlights the importance of cybersecurity practices, such as being aware of software that records user inputs. Always remember to respect privacy and legal boundaries when dealing with such technologies.

**Disclaimer**: The author is not responsible for any misuse or damage caused by the use of this code. Use at your own risk.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

   
  
