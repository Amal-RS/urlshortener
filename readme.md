URL Shortener API
=================

\================

This API provides a simple URL shortening service. It allows users to shorten URLs and retrieve the original URL from the shortened URL.

Endpoints
---------

### POST /shorten/

Shorten a URL using a third-party URL shortening service (TinyURL).

#### Request Body

*   **original\_url**: The original URL to be shortened.
    

#### Response

*   **short\_url**: The shortened URL.
    

### POST /shorten-custom/

Shorten a URL with a custom name.

#### Request Body

*   **original\_url**: The original URL to be shortened.
    
*   **custom\_name**: The custom name for the shortened URL.
    

#### Response

*   **short\_url**: The shortened URL with the custom name.
    

### GET /{short\_url}

Redirect to the original URL from the shortened URL.

#### Path Parameters

*   **short\_url**: The shortened URL.
    

#### Response

*   Redirect to the original URL if found, otherwise returns a 404 error.
    

Database
--------

The API uses a PostgreSQL database to store the shortened URLs. The database has a single table **urls** with two columns:

*   **original\_url**: The original URL.
    
*   **short\_url**: The shortened URL (primary key).
    

The API uses SQLAlchemy to interact with the database.

Security
--------

The API uses CORS middleware to allow cross-origin requests from specific origins.

Error Handling
--------------

The API returns a 404 error if the shortened URL is not found in the database.

Code Structure
--------------

The code is organized into the following files:

*   **main.py**: The main application file that defines the API endpoints and database interactions.
    
    

Note: This documentation is a summary of the code and may not include all the details.