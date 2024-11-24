import time
import os
from email.message import EmailMessage

from celery import Celery
import redis
import google.generativeai as genai
import smtplib

# celery -A mycelery worker -P solo -l info
# celery -A mycelery flower

if __name__ == "mycelery":
    from config import config
    from details import *
    redis_db = redis.Redis(host=config["Redis"]["host"], port=config.get("Redis", "port"))

    proxy = 'http://206.189.135.6:3128'

    os.environ['http_proxy'] = proxy
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy
else:
    from .config import config
    from .database import redis_db

genai.configure(api_key=config["Gemini"]["API_KEY"])

model = genai.GenerativeModel(model_name='gemini-1.5-flash')


broker = f'{config["Redis"]["host"]}:{config.get("Redis", "port")}'
app = Celery('mycelery', broker=f'redis://{broker}/0')
app.conf.broker_connection_retry_on_startup = True

@app.task(name='mycelery.prompt_sender')
def prompt_sender(prompt: str, key):
        MAX_ITER_COUNT = 50
        MAX_DELAY = 10

        for _ in range(MAX_ITER_COUNT):
            try:
                response = model.generate_content(prompt)
                
                if response and hasattr(response, 'text'):
                        result = response.text
                        redis_db.set(key, result, 172_800)
                        return
                
                redis_data = redis_db.get(key).decode('utf-8')
                        
                if redis_data == "-1":
                    redis_db.set(key,None)
                    raise Exception()
            
            except Exception as e:
                print(e)
                time.sleep(MAX_DELAY)
    
    
    
@app.task(name='mycelery.send_text_mail_task')
def send_text_mail_task(server, port, email, password, to_email, subject, text_message):
    with smtplib.SMTP(server, port) as mail_server:
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.ehlo()
        mail_server.login(email, password)

        mail_server.sendmail(email, to_email, f"Subject: {subject}\n\n{text_message}".encode('utf-8'))

@app.task(name='mycelery.send_HTML_mail_task')
def send_HTML_mail_task(server, port, email, password, to_email, subject, html):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = to_email
    msg.add_header('Content-Type','text/html')
    msg.set_payload(html)

    with smtplib.SMTP(server, port) as mail_server:
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.ehlo()
        mail_server.login(email, password)

        mail_server.sendmail(email, to_email, msg.as_string().encode('utf-8'))
        
        
