**ArticlesApi Get**
----
* **URL**

  /api/articles

* **Method:**

  `Get`
  
* **Headers:**

  NONE
  
* **URL Params**

   **Optional:**
 
   `category=[alphanumeric]`

* **Data Params**

  NONE

* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** `
    {
    "name": "name",
    "description": "description",
    "link":"http://example.com",
    "categories":["test1","test2"]
}`
 
* **Error Response:**

  * **Code:** 400 Bad Request  <br />
    **Content:** `{ "message" : "Category not exists" }`
    
