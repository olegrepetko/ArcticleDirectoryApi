**ArticleApi Delete**
----
* **URL**

  /api/article/`<id>`

* **Method:**

  `DELETE`
  
* **Headers:**

  * **Content-Type**:`application/json`
  * **Authorization**:`Bearer {login_token}`
  
* **URL Params**

   NONE

* **Data Params**

   NONE

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Invalid Id" }`
    
  OR
  
  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Article not exists" }`
  
