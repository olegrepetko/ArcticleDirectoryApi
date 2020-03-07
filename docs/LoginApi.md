**LoginApi**
----
* **URL**

  /api/auth/login

* **Method:**

  `POST`
  
* **Headers:**

  * **Content-Type**:`application/json`
  
*  **URL Params**

   NONE

* **Data Params**

  `{
            "email": "test@mail.com",
            "password": "password"
        }`

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** `{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODM1MjUwNTcsIm5iZiI6MTU4MzUyNTA1NywianRpIjoiMzZhNmEwNmItZDE2ZC00ZWYzLWIyMDYtNWViMDk0NDRhOTgyIiwiZXhwIjoxNTgzNTI1OTU3LCJpZGVudGl0eSI6IjVlNjJhY2JkZDM2ZmI5ZDNkN2ZiN2M2MCIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.3U89G-TFRaay2Sy3QulauZEM290nINp9ov1ucZzgsqw"
}`
 
* **Error Response:**

  * **Code:** 401 Unauthorized  <br />
    **Content:** `{ "message" : "Fields do not exist on the document" }`

