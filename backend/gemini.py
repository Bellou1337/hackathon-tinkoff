import google.generativeai as genai


genai.configure(api_key='AIzaSyBj4LTjYjlIDXz4cHpg3gg4CiQYoMBS5I4')


model = genai.GenerativeModel(model_name='gemini-1.5-flash')


prompt = ''


response = model.generate_content(prompt)

print(response.text)
