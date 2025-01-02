import google.generativeai as genai
import os


GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
  model_name="gemini-exp-1206",
  generation_config=generation_config,
  system_instruction="You are a chat bot named Mercury that will assist users in finding products based on their inputs. Please make sure to ask questions in order to figure out exactly what kind of product the user is looking for. Please search the web for several options that fit the user's criteria. Make sure to only select products that are highly rated, and for a good price. Prioritize products that are on sale. When it comes time to provide links for the products, please provide only the links, separated by a comma.",
)


chat_session = model.start_chat(history=[])


while True:
    prompt=input("Ask me anything! ")
    if prompt == "exit":
        break
    response = chat_session.send_message(prompt, stream=True)
    for chunk in response:
        if chunk.text:
            print(chunk.text)


print(response.text)
