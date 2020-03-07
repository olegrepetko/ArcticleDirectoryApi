**ArticleApi Get**
----
* **URL**

  /api/article/`<id>`

* **Method:**

  `GET`
  
* **Headers:**

   NONE
  
* **URL Params**

   NONE

* **Data Params**

   NONE

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** `{ "name": "name", "description": "description", "link":"http://example.com", "categories":["test1","test2"] }`
 
* **Error Response:**

  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Invalid Id" }`
    
  OR
  
  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Article not exists" }`
  
