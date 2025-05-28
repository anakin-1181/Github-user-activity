import requests
import json

def import_data(username="kamranahmedse"):
    import_string = f"https://api.github.com/users/{username}/events"
    response = requests.get(import_string)
    if response.status_code != 200:
        raise ValueError(f"GitHub API error: {response.status_code} - {response.reason}")
    data = response.json()
    return data

def print_data():
    response = import_data()
    print(json.dumps(response))
    
def type_check(username="kamranahmedse"):
    response = import_data()
    count = dict()
    num_count = 0
    for item in response:
        num_count += 1
        if item["type"] not in count.keys():
            count[item["type"]] = 1
        else:
            count[item["type"]] += 1
            
    print(num_count, count)
    
if __name__ == "__main__":
    print_data()
    
