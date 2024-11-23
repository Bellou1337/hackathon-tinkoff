import httpx

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMyIsImF1ZCI6WyJmYXN0YXBpLXVzZXJzOmF1dGgiXSwiZXhwIjoxNzM0OTc0NTI2fQ.g80PbQI4shpF_zs7sFfnczVUCVvGqWqqHoaNaW8oPL8'

r = httpx.get(
    url="http://git-ts2.ru:8000/auth/users/me",
    headers={"Authorization": f"Bearer {token}"}
)

print(r.json())