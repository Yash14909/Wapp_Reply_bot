from openai import OpenAI
client = OpenAI (               #OpenAI here is creating an instance importing a class
    api_key="***",
)
command='''
19/06/2025, 10:03 AM - Yash: Hey bro, what's up?
19/06/2025, 10:04 AM - Aman: Yo! Just chilling. You?
19/06/2025, 10:04 AM - Yash: Same here 😄. Did you finish the Data science project?
19/06/2025, 10:05 AM - Aman: Almost! Just need to clean up the code. You?
19/06/2025, 10:05 AM - Yash: Done and dusted! Submitted it last night.
19/06/2025, 10:06 AM - Aman: Damn! You’re on fire 🔥
19/06/2025, 10:06 AM - Yash: Haha thanks 😎. Wanna meet in the evening?
19/06/2025, 10:07 AM - Aman: Sure, 5 PM at the café?
19/06/2025, 10:07 AM - Yash: Perfect. Don’t be late this time 😜
19/06/2025, 10:08 AM - Aman: Lol ok baba, I'll be there before you 😂
19/06/2025, 10:08 AM - Yash: Let’s see 😏
19/06/2025, 10:09 AM - Aman: Btw, did you check out that new series on Netflix?
19/06/2025, 10:09 AM - Yash: "Code Breakers"? Yeah! It’s epic!
19/06/2025, 10:10 AM - Aman: Brooo, that twist in episode 3 🤯
19/06/2025, 10:10 AM - Yash: IKR! Let’s talk about it when we meet.
19/06/2025, 10:11 AM - Aman: Deal! See ya 😎
19/06/2025, 10:11 AM - Yash: Peace ✌️

'''
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
       {"role":"system", "content":"you are a person named Yash  speaks hindi as well as english, He's from India and is a coder. You analyze the chat history and respond like Yash  "}, 
       {"role":"user","content":text}
    ]
)
print(completion.choices[0].message.content)