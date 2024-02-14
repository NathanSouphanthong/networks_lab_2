import httpx
import os

''' Checkoff Requirements - Challenges

Challenges Implemented 

1. File upload in POST request, using multipart/form-data

2. Having a route in your application that returns a binary content type (photo, video, audio)

'''

# pip3 install httpx

host = "http://127.0.0.1:8000"

def test_upload_file():
    print('-' * 100)
    print(test_upload_file.__name__)
    print('-' * 100)
    # ensure that the cwd is the root of the project!
    with open('app/__tests__/test_image.jpeg', 'rb') as f:
        file = {'file' : f}
        response = httpx.post(f"{host}/file", files=file)
        print(f"Response from POST request to {host}/file returned {response.status_code}")
        print(f"check route app/assets to see if file 'test_image.jpeg' exists")
    print('-' * 100)
    print('\n')

def test_get_photo():
    print('-' * 100)
    print(test_get_photo.__name__)
    print('-' * 100)
    response = httpx.get(f"{host}/photo")
    print(f"Response from GET request to {host}/photo returned:\n {response.text}")
    print('-' * 100)
    
def main():
    print("START OF CHALLENGE TESTS\n")
    test_upload_file()
    test_get_photo()

if __name__ == "__main__":
    main()
