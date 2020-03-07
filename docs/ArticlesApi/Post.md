**ArticlesApi Post**
----
* **URL**

  /api/articles

* **Method:**

  `POST`
  
* **Headers:**

  * **Content-Type**:`application/json`
  * **Authorization**:`Bearer {login_token}`
  
* **URL Params**

   NONE

* **Data Params**

  `{ "name": "name", "description": "description", "link":"http://example.com", "categories":["test1","test2"] }`

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** `{
    "id": "5e62acf9d36fb9d3d7fb7c65"
}`
 
* **Error Response:**

  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Fields do not exist on the document" }`
    
    OR
  
  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Validation error or missing required fields" }`
    
    OR
  
  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Category not exists" }`
    
    OR
  
  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Name or link of article already exists" }`
    
    OR
  
  * **Code:** 401 Bad Request  <br />
    **Content:** `{ "message" : "Invalid Authorization" }`
