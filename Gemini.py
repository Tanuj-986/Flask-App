from google import genai
import time

client = genai.Client(api_key="AIzaSyDuyfX_wGo8OZ8drQafnmQPROqBiwCQG1M")

t1 = time.time()


# Audio Prompt

myfile = client.files.upload(file='c:\\Users\\patil\\Downloads\\Recording.mp3')

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents=["Answer it", myfile]
)


# Text Prompt
# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="Explain how AI works",
# )

t2 = time.time()
print(response.text)

t3 = t2-t1
print(f"Response time: {t3}")
