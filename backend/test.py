
import google.generativeai as genai
import config
def roleplay(query,role,desc,chatStr):
    genai.configure(api_key=config.apikeyGoogle)
    chatStr += f"Vivek: {query}\n {role}({desc}):"
    generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}
    safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
    convo = model.start_chat(history=[
])
    
    convo.send_message(chatStr)
    chatStr += convo.last.text + "\n"
    r = builtins.open(
        c.roleplay, "a"
    )
    r.write(f"Vivek:{query}\n" +role+":"+ convo.last.text + "\n")
    r.close()
    print(convo.last.text)
    return convo.last.text
roleplay()



def roleplayOld(query,role,desc,chatStr):
    openai.api_key = apikey
    chatStr += f"Vivek: {query}\n {role}({desc}):"
    client = OpenAI()
   
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct-0914",
        prompt=chatStr,
        temperature=1,
        max_tokens=1256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    chatStr += response.choices[0].text + "\n"
    r = builtins.open(
        c.roleplay, "a"
    )
    r.write(f"Vivek:{query}\n" +role+":"+ response.choices[0].text + "\n")
    r.close()
    return response.choices[0].text