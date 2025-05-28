from fetch_data import import_data

def showMessage(username):
    response = import_data(username)
    for event in response:
        match event["type"]:
            case "PushEvent":
                print(f"- Pushed {len(event["payload"]["commits"])} commits to {event["repo"]["name"]}")
            case "PullRequestEvent":
                print(f"- {event["payload"]["action"]} a pull request in {event["repo"]["name"]}")
            case "WatchEvent":
                print(f"- Starred {event["repo"]["name"]}")
                
if __name__ == "__main__":
    username = input("Please provide a github username.")
    showMessage(username)
    
