from config import *
import openai
openai.api_key=OPENAI_KEY
textfile=input("Enter text file name you want to save this to. Press Enter for automatic generation\n")
text=input("Enter the text\n")
action=input("What do you want to do with this text?\nType 1 for grammer check\nType 2 for making an email\nType 3 for translating to a different language\n")
match(action):
    case "1":
        prompt=f"Improve grammer in this text and give only final text in output\n{text}"
    case "2":
        prompt=f"Make this email professional and give only final text in output\n{text}"
    case "3":
        lang=input("What language you want the text to translate in?\n")
        prompt=f"Change the text to {lang} and give the final result in output\n{text}"
        
        
response=openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=1,
    max_tokens=2560,
    frequency_penalty=0,
    top_p=1
)


print(f"The grammatically corrected sentence is: {response.choices[0].message.content}")
if(len(textfile)==0):
    textfile=text[0:12]
    
with open(f"Outputs/{textfile}.txt","w") as f:
    f.write(response.choices[0].message.content)