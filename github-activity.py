import argparse
from fetch_data import import_data

def showMessage(username):
    response = import_data(username)
    count = 0
    print("\n")
    for event in response:
        match event["type"]:
            case "PushEvent":
                print(f"- Pushed {len(event["payload"]["commits"])} commits to {event["repo"]["name"]}")
            case "PullRequestEvent":
                action = event["payload"]["action"]
                print(f"- {action[0].upper()}{action[1::]} a pull request in {event["repo"]["name"]}")
            case "WatchEvent":
                print(f"- Starred {event["repo"]["name"]}")
            case "CreateEvent":
                print(f"- Created a {event["payload"]["ref_type"]} in {event["repo"]["name"]}")
            case "DeleteEvent":
                print(f"- Deleted a {event["payload"]["ref_type"]} in {event["repo"]["name"]}")
            case "ForkEvent":
                print(f"- Forked {event["repo"]["name"]}")
            case "IssueCommentEvent":
                action = event["payload"]["action"]
                print(f"- {action[0].upper()}{action[1::]} a comment in {event["repo"]["name"]}")
            case "IssuesEvent":
                action = event["payload"]["action"]
                print(f"- {action[0].upper()}{action[1::]} an issue in {event["repo"]["name"]}")
            case "PublicEvent":
                print(f"- Turned {event["repo"]["name"]} from private to public")
            case "PullRequestReviewEvent":
                action = event["payload"]["action"]
                print(f"- {action[0].upper()}{action[1::]} a pull request review in {event["repo"]["name"]}")
            case "PullRequestReviewCommentEvent":
                action = event["payload"]["action"]
                print(f"- {action[0].upper()}{action[1::]} a pull request review comment in {event["repo"]["name"]}")
        count += 1  
    print(f"\nResults: {count}/{len(response)} events shown")    
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    args = parser.parse_args()
    showMessage(args.username)
    
if __name__ == "__main__":
    main()
                
                       
