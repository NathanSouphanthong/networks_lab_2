import httpx

''' Checkoff Requirements - GET'''

# pip3 install httpx

host = "http://127.0.0.1:8000"

def test_no_query_params():
    print(test_no_query_params.__name__)
    print('-' * 100)
    print("Should return in initial database state: Bob, Alice, Charlie")
    response = httpx.get(f'{host}/students')
    print(response.text)
    print('-' * 100)

def test_sortBy_id():
    print(test_sortBy_id.__name__)
    print('-' * 100)
    print("Should return in entries sorted by id: Charlie, Alice, Bob")
    params = {
        'sortBy' : 'id'
    }
    response = httpx.get(f'{host}/students', params=params)
    print(response.text)
    print('-' * 100)

def test_sortBy_name():
    print(test_sortBy_name.__name__)
    print('-' * 100)
    print("Should return in entries sorted by name: Alice, Bob, Charlie")
    params = {
        'sortBy' : 'name'
    }
    response = httpx.get(f'{host}/students', params=params)
    print(response.text)
    print('-' * 100)

def test_sortBy_gpa():
    print(test_sortBy_gpa.__name__)
    print('-' * 100)
    print("Should return in entries sorted by gpa: Alice, Charlie, Bob")
    params = {
        'sortBy' : 'gpa'
    }
    response = httpx.get(f'{host}/students', params=params)
    print(response.text)
    print('-' * 100)

def test_count_under():
    print(test_count_under.__name__)
    print('-' * 100)
    print("Should return only two entries")
    
    params = { 
        "count" : '2'
    }
    response = httpx.get(f'{host}/students', params=params)
    print(response.text)
    print('-' * 100)

def test_count_exact():
    print(test_count_exact.__name__)
    print('-' * 100)
    print("Should return three entries")
    params = { 
        "count" : '3'
    }
    response = httpx.get(f'{host}/students', params=params)
    print(response.text)
    print('-' * 100)

def test_count_over():
    print(test_count_over.__name__)
    print('-' * 100)
    print("Should return three entries")
    params = { 
        "count" : '1000'
    }
    response = httpx.get(f'{host}/students', params=params)
    print(response.text)
    print('-' * 100)

def test_sort_and_count():
    print(test_sort_and_count.__name__)
    print('-' * 100)
    print("Should return 2 entries sorted by id: Charlie, Alice")
    params = { 
        "count" : '2',
        "sortBy" : "id"
    }

    response = httpx.get(f'{host}/students', params=params)
    print(response.text)
    print('-' * 100)

def test_idempotent():
    print(test_idempotent.__name__)
    print('-' * 100)
    print("Calling GET request to students two times, should be the same both times")
    response = httpx.get(f'{host}/students')
    print(response.text)
    response = httpx.get(f'{host}/students')
    print(response.text)
    print('-' * 100)

    
def main():
    print("START OF GET TESTS\n")
    test_no_query_params()
    print(" ")
    test_sortBy_id()
    print(" ")
    test_sortBy_name()
    print(" ")
    test_sortBy_gpa()
    print(" ")
    test_count_under()
    print(" ")
    test_count_exact()
    print(" ")
    test_count_over()
    print(" ")
    test_sort_and_count()
    print(" ")
    test_idempotent()


if __name__ == "__main__":
    main()
