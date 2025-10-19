# WhatsApp Chat Auto-Responder Bot using OpenAI & PyAutoGUI

This Python project is an automated chatbot that reads WhatsApp messages from the screen, determines if a message is from a specific sender, generates an AI-based reply using OpenAI's GPT model, and sends the reply automatically using PyAutoGUI.

---

## 💡 Features

- Reads WhatsApp messages directly from the screen
- Detects if the last message is from a specified sender
- Uses OpenAI (GPT-3.5-turbo) to generate intelligent, motherly responses
- Pastes and sends replies automatically
- Supports Hindi-English bilingual conversation
- Designed for automation via GUI-based interactions

---

## 🔧 Requirements

- Python 3.7+
- OpenAI API Key
- WhatsApp Web or Desktop App (with predictable layout)
- Proper screen coordinates for your resolution
- Use your own coordinates for proper fuctionality of this code

---

## 📦 Libraries Used

- `pyautogui` - For automating mouse and keyboard actions
- `time` - To manage delays
- `pyperclip` - To manage clipboard operations
- `openai` - To access GPT API

Install with:

```bash
pip install pyautogui pyperclip openai

python program.py
