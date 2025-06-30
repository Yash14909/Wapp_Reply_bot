import pyautogui   #tracks the cursor position
import time
import pyperclip   #collects content from the clipboard (Ex-Whatsapp) 
import openai  # Correct import for OpenAI API

# ✅ Set your API key here
openai.api_key = "***"
  # Add your API key

# ✅ Function to check last message sender
def is_last_message_from_sender(chat_text, sender_name="YASHVARDHAN REDDY"):
    try:
        messages = chat_text.strip().split("/2024")[-1]
        return sender_name in messages
    except:
        return False

# ✅ Click into the chat window (adjust coordinates as needed)
pyautogui.click(1639, 1412)
time.sleep(2)

while True:
    # ✅ Select and copy the chat content
    pyautogui.moveTo(1026, 244)
    pyautogui.dragTo(1131, 1321, duration=1.0, button='left')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(1994, 281)

    # ✅ Get copied chat content
    chat_history = pyperclip.paste()
    print(chat_history)

    # ✅ Check if the last message was from the sender
    if is_last_message_from_sender(chat_history):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a person named Xyz who speaks Hindi as well as English. "
                        "He's from India and is a coder. You analyze the chat history and respond like Maa. "
                        "Output should be only the next chat response as plain text."
                    )
                },
                {"role": "user", "content": chat_history}
            ]
        )

        response = completion.choices[0].message.content.strip()
        pyperclip.copy(response)

        # ✅ Paste the AI response into the message box and send
        pyautogui.click(1808, 1328)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.press('enter')

    # ✅ Add delay or break if needed to avoid infinite fast loop
    time.sleep(5)
