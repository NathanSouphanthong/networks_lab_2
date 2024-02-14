import httpx

''' Checkoff Requirements - DELETE'''

# pip3 install httpx

host = "http://127.0.0.1:8000"

def test_delete_resource(id_to_delete: int):
    print('-' * 100)
    print(test_delete_resource.__name__)
    print('-' * 100)
    get_response_initial = httpx.get(f'{host}/students')
    print(f'Database before delete:\n{get_response_initial.text}\n')

    delete_response = httpx.delete(f"{host}/students/{id_to_delete}") # delete student with id:1

    print(f"Response from DELETE request to {host}/students/{id_to_delete} returned {delete_response.status_code}")
    print(delete_response.text)

    get_response_after = httpx.get(f'{host}/students')
    print(f'Updated database:\n{get_response_after.text}')
    print('-' * 100)
    print('\n')

def test_delete_non_existent_resource():
    print('-' * 100)
    print(test_delete_non_existent_resource.__name__)
    print('-' * 100)
    id_to_delete = 1000000000000

    get_response_initial = httpx.get(f'{host}/students')
    print(f'Database before delete:\n{get_response_initial.text}\n')

    delete_response = httpx.delete(f"{host}/students/{id_to_delete}")

    print(f"Response from DELETE request to {host}/students/{id_to_delete} returned {delete_response.status_code}")
    print(delete_response.text)

    get_response_after = httpx.get(f'{host}/students')
    print(f'Updated database:\n{get_response_after.text}')
    print('-' * 100)
    print('\n')

def test_idempotent():
    print(test_idempotent.__name__)
    print('-' * 100)
    print("Calling DELETE request to students with id: 2, two times database should just have that student removed")
    before_response = httpx.get(f'{host}/students')
    print(before_response.text)
    delete_response1 = httpx.delete(f"{host}/students/2")
    delete_response2 = httpx.delete(f"{host}/students/2")
    after_response = httpx.get(f'{host}/students')
    print(after_response.text)
    print('-' * 100)

    
def main():
    print('START OF DELETE TESTS:\n')
    test_delete_resource(1)
    test_delete_non_existent_resource()
    test_idempotent()
    
if __name__ == "__main__":
    main()
