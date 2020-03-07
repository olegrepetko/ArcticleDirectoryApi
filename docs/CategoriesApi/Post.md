**CategoriesApi Post**
----
* **URL**

  /api/categories

* **Method:**

  `POST`
  
* **Headers:**

  * **Content-Type**:`application/json`
  * **Authorization**:`Bearer {login_token}`
  
* **URL Params**

   NONE

* **Data Params**

  `{
            "name": "category1"
        }`

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** `
    {
        "id": "5e62acefd36fb9d3d7fb7c63"
    }`
 
* **Error Response:**

  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Fields do not exist on the document" }`
    
  OR
  
  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Validation error or missing required fields" }`
  
  OR
  
  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Category already exists" }`
