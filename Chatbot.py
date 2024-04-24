import openai
import gradio as gr #interface
openai.api_key="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"

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()
def chat_gpt(prompt):
    result=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]

    )
    return result.choices[0].message.content.strip()
if __name__== "__main__":
    while True:
        user_input = input("You:  ")
        if user_input.lower() in ["quit", "exit" , "bye"]:
            break

        result=chat_gpt(user_input)
        print("chatbot:",result)

