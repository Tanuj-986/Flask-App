from secret import *

def brain(prompt):  

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": (prompt),
            }
        ],
        stream=False,
        model="llama-3.3-70b-versatile",
    )
    
    response = chat_completion.choices[0].message.content

    print(response)
    return response







