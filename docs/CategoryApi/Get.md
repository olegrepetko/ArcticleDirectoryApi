**CategoryApi Get**
----
* **URL**

  /api/category/`<id>`

* **Method:**

  `GET`
  
* **Headers:**

  * **Content-Type**:`application/json`
  
* **URL Params**

   NONE

* **Data Params**

  NONE

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** `
    {
        "name": "test3",
        "id": "5e62ace3d36fb9d3d7fb7c61"
    }`
 
* **Error Response:**

  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Invalid Id" }`
    
  OR
  
  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Category not exists" }`
