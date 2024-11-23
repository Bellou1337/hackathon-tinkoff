import time

from celery import Celery
from fastapi import HTTPException, status

import google.generativeai as genai
from .config import config as api_config
from .details import *


from .database import redis_db

import smtplib
from email.message import EmailMessage


# celery -A mycelery worker -P solo -l info
# celery -A mycelery flower

if __name__ == "mycelery":
    from config import config
else:
    from .config import config

genai.configure(api_key=api_config["Gemini"]["API_KEY"])

model = genai.GenerativeModel(model_name='gemini-1.5-flash')


broker = f'{config["Redis"]["host"]}:{config.get("Redis", "port")}'
app = Celery('mycelery', broker=f'redis://{broker}/0')
app.conf.broker_connection_retry_on_startup = True

@app.task(name='mycelery.prompt_sender')
def prompt_sender(prompt: str, key):

    try:
        MAX_ITER_COUNT = 50
        MAX_DELAY = 1

        for attempt in range(MAX_ITER_COUNT):
            response = model.generate_content(prompt)
            
            if response and hasattr(response, 'text'):
                    result = response.text
                    redis_db.set(key, result)
                    return {"detail " : result}

            time.sleep(MAX_DELAY)
        
        raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = API_ERROR_SOMETHING_WITH_THE_DATA
            )
        
    except HTTPException:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = API_ERROR_SOMETHING_WITH_THE_DATA
        )
    except Exception:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = API_ERROR_SOMETHING_WITH_THE_DATA
        )
    
    
    
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
        
        
