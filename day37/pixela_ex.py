import os
import requests as rq
import datetime as dt

URL = "https://pixe.la/v1/users"
USER_NAME = "manoj7shekhawat"

API_TOKEN = os.environ.get("API_TOKEN")

# STEP 1: Create user account
# body = {
#     "token": API_TOKEN,
#     "username": USER_NAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = rq.post(url=URL, json=body)
# response.raise_for_status()
# print(f"{response.text}")


# STEP 2: Create a graph definition

# URL = f"https://pixe.la/v1/users/{USER_NAME}/graphs"
#
# headers = {
#     "X-USER-TOKEN": API_TOKEN
# }
#
# body = {
#     "id": "my-habit-graph",
#     "name": "habit-graph",
#     "unit": "commit",
#     "type": "int",
#     "color": "shibafu",
#     "timezone": "Europe/Warsaw"
# }
#
# response = rq.post(url=URL, json=body, headers=headers)
# response.raise_for_status()
# print(f"{response.text}")


# STEP 3: Get the graph!
# URL = f"https://pixe.la/v1/users/{USER_NAME}/graphs/my-habit-graph"
#
# headers = {
#     "X-USER-TOKEN": API_TOKEN
# }
#
# response = rq.get(url=URL, headers=headers)
# response.raise_for_status()
# print(f"{response.text}")
#
# STEP 4: Post value to the graph
# URL = f"https://pixe.la/v1/users/{USER_NAME}/graphs/my-habit-graph"
# headers = {
#     "X-USER-TOKEN": API_TOKEN
# }
#
# now = dt.datetime.now().strftime('%Y%m%d')
#
# body = {
#     "date": str(now),
#     "quantity": "5"
# }
#
# response = rq.post(url=URL, json=body, headers=headers)
# response.raise_for_status()
# print(f"{response.text}")

# STEP 5: Update the quantity already registered as a "Pixel"
# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
# now = dt.datetime.now().strftime('%Y%m%d')
# URL = f"https://pixe.la/v1/users/{USER_NAME}/graphs/my-habit-graph/{now}"
#
# headers = {
#     "X-USER-TOKEN": API_TOKEN
# }
#
# body = {
#     "quantity": "35"
# }
#
# response = rq.put(url=URL, json=body, headers=headers)
# response.raise_for_status()
# print(f"{response.text}")

# STEP 6: Delete a Pixel
# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
now = dt.datetime.now().strftime('%Y%m%d')
URL = f"https://pixe.la/v1/users/{USER_NAME}/graphs/my-habit-graph/{now}"

headers = {
    "X-USER-TOKEN": API_TOKEN
}

response = rq.delete(url=URL, headers=headers)
response.raise_for_status()
print(f"{response.text}")