import requests

ENDPOINT = "https://todo.pixegami.io/"

# We want to test each use, but do so in isolation
# This means repeating steps

def test_api_call():
    response = requests.get(ENDPOINT)
    status = response.status_code
    assert status == 200

def create_payload():
    return {
        "content": "Test_one",
        "user_id": "list_test",
        "task_id": "test_id",
        "is_done": False
    }

def create_tasks_payload():
    return [
       {
        "content": "Testing_once",
        "user_id": "list_test",
        "task_id": "test_1",
        "is_done": False
    },
    {
        "content": "Testing_twice",
        "user_id": "list_test",
        "task_id": "test_2",
        "is_done": False
    },
    {
        "content": "Testing_thrice",
        "user_id": "list_test",
        "task_id": "test_3",
        "is_done": False
    }

    ]

def create_api_call(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def get_api_call(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def update_api_call(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def list_api_call(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

# Named with test_
def test_create():
    payload = create_payload()
    create_response = create_api_call(payload)
    data = create_response.json()
    print(data)
    task_id = data["task"]["task_id"]
    create_status = create_response.status_code
    assert create_status == 200

    test_create = get_api_call(task_id)
    test_create_status = test_create.status_code
    assert test_create_status == 200
    test_create_data = test_create.json()
    assert test_create_data["content"] == payload["content"]

def test_update():
    payload = create_payload()
    create_response = create_api_call(payload)
    data = create_response.json()
    task_id = data["task"]["task_id"]
    create_status = create_response.status_code
    assert create_status == 200

    # Above are repeat tests to make sure everything works in isolation
    # Below are new tests
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "updated info",
        "is_done": True,
    }
    update_response = update_api_call(new_payload)
    assert update_response.status_code == 200
    get_response = get_api_call(task_id)
    get_content = get_response.json()
    assert get_content["content"] == new_payload["content"]
    assert get_content["is_done"] == new_payload["is_done"]

# We will want to create tasks for a user to list
def test_list():
    payload = create_tasks_payload()
    payload1 = payload[0]
    create_api_call(payload1)
    payload2 = payload[1]
    create_api_call(payload2)
    payload3 = payload[2]
    create_api_call(payload3)

    user = payload1["user_id"]
    list_response = list_api_call(user)
    data = list_response.json()
    print(data)
    task_list = data["tasks"]
    assert task_list[0]["content"] == payload1["content"]
    assert task_list[1]["content"] == payload2["content"]
    assert task_list[2]["content"] == payload3["content"]
    print(task_list)

def test_delete():
    payload = create_payload()
    create_response = create_api_call(payload)
    data = create_response.json()
    print(data)
    task_id = data["task"]["task_id"]
    create_status = create_response.status_code
    assert create_status == 200

    test_create = get_api_call(task_id)
    test_create_status = test_create.status_code
    assert test_create_status == 200
    test_create_data = test_create.json()
    assert test_create_data["content"] == payload["content"]