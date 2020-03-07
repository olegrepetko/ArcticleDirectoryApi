**SignupApi**
----
* **URL**

  /api/auth/signup

* **Method:**

  `POST`
  
* **Headers:**

  * **Content-Type**:`application/json`
  
*  **URL Params**

   NONE

* **Data Params**

  `{
    "email": "test@test.com",
    "password": "password"
   }`

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** `{
    "id": "5e62acbdd36fb9d3d7fb7c60"
}`
 
* **Error Response:**

  * **Code:** 400 Bad Request <br />
    **Content:** `{ "message" : "Fields do not exist on the document" }`

  OR

  * **Code:** 400 Bad Request <br />
    **Content:** `{ "message" : "Validation error or missing required fields" }`
    
  OR

  * **Code:** 400 Bad Request <br />
    **Content:** `{ "message" : "Email already exists" }`
