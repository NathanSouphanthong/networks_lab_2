# Networks Lab 2 - REST API

How to run the server:

1. run `docker compose up` to start the container
2. make requests to the host `http://127.0.0.1:8000`

## GET Requests 
`/students`\
returns all students in the database

`/students?sortBy={property}`\
returns the students sorted by a property, you can sort by the below properties
- id
- name
- gpa

`/students?count={items}`\
returns the number of items specified in the count query param, if the number is over the number of items in the database the API will return all the items in the database

## POST Requests
`/students`\
Specify a student object in the body of request in JSON, example below. The request will return a 422 - unprocessible identity if the properties specified in the body do not match the required fields. If successful, a 200 will be returned and the body of the request will be returned in the response
``` 
{ 
    "name": "Bane",
    "id": 5,
    "ga": 20.0
}
```

## DELETE Requests
`/students/{id_of_student_to_delete}`\
Specify the id of the student you wish to delete as a path parameter. If the id is not found a 404 will be returned with a message of "Student ID to delete not found", if the delete request goes through a 204 will be returned with the message "{id_of_student_to_delete} deleted successfully!"

## Challenges
POST @ `/file`\
Upload a file to the REST API server. Using form-data for body, specify a key value pair with the key = file and value = file. If successful, a 200 will be returned and the file will be saved in `app/assets`

GET @ `/photo`\
Grab the SUTD logo image! Will return 200 response if successful.

## Running the tests
It is important to ensure that `httpx` module is installed. For Python 3 this should be the default, but if it is not installed run `pip install httpx`, this is needed for the tests as we use the client to make requests to the server. Of course make sure the server is running before running these tests.

Tests are placed in the path `app/__tests__`, there are tests for GET, POST, DELETE and challenge. Run each of the python test files indivdually using `python {path_to_file}`. Ensure that before running the test file the server is reset to its default state. Based on the configuration, saving any file in the project will refresh the server and bring it to its default state. 

Test results will be outputted to the console. In `get_test.py`, the values that the server should return are specified right before the values returned from the server. For `post_test.py` and `delete_test.py` the state of the database before and after the operation in focus will be printed. The tests in challenge are setup the same way.