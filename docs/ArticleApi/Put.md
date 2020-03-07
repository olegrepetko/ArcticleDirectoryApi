**ArticleApi Put**
----
* **URL**

  /api/article/`<id>`

* **Method:**

  `PUT`
  
* **Headers:**

  * **Content-Type**:`application/json`
  * **Authorization**:`Bearer {login_token}`
  
* **URL Params**

   NONE

* **Data Params**

  `{ "name": "name", "description": "description", "link":"http://example.com", "categories":["test1","test2"] }`

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** `
    `
 
* **Error Response:**

  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Invalid Id" }`
    
  OR
  
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
    **Content:** `{ "message" : "Article already exists" }`
