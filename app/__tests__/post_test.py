import httpx

''' Checkoff Requirements - POST'''

# pip3 install httpx

host = "http://127.0.0.1:8000"

def test_create_new_resource():
    print('-' * 100)
    print(test_create_new_resource.__name__)
    print('-' * 100)

    data = { 
    "name": "Bane",
    "id": 4,
    "gpa": 4.0
    }

    get_response_initial = httpx.get(f'{host}/students')
    print(f'Database before post:\n{get_response_initial.text}\n')

    post_response = httpx.post(f"{host}/students", json=data)
    print(f"Response from POST request to {host}/students returned {post_response.status_code}\n")

    get_response = httpx.get(f'{host}/students')
    print(f'Updated database:\n{get_response.text}')
    print('-' * 100)
    print('\n')

def test_create_new_resource_invalid():
    print('-' * 100)
    print(test_create_new_resource_invalid.__name__)
    print('-' * 100)

    data = { 
    "id": 4,
    "gpa": 4.0
    }

    get_response_initial = httpx.get(f'{host}/students')
    print(f'Database before post:\n{get_response_initial.text}\n')

    print(f'Sending POST request with malformed body: {data}')
    post_response = httpx.post(f"{host}/students", json=data)
    print(f"Response from POST request to {host}/students returned {post_response.status_code}\n")
    print('-' * 100)
    print('\n')

def main():
    print('START OF POST TESTS:\n')
    test_create_new_resource()
    test_create_new_resource_invalid()

if __name__ == "__main__":
    main()
