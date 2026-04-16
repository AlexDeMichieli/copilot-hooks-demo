"""A messy app for the agent to refactor."""

import json, os, sys

def process(data):
    results = []
    for item in data:
        if item["type"] == "user":
            if item["active"] == True:
                name = item["first_name"] + " " + item["last_name"]
                email = item["email"]
                if email != None and email != "":
                    results.append({"name": name, "email": email, "status": "active"})
                else:
                    results.append({"name": name, "email": "N/A", "status": "active"})
            else:
                pass
        elif item["type"] == "admin":
            name = item["first_name"] + " " + item["last_name"]
            results.append({"name": name, "email": item.get("email", "N/A"), "status": "admin"})
    return results

def load_data(path):
    f = open(path, "r")
    data = json.load(f)
    f.close()
    return data

def save_results(results, path):
    f = open(path, "w")
    json.dump(results, f)
    f.close()

if __name__ == "__main__":
    data = load_data(sys.argv[1])
    results = process(data)
    save_results(results, sys.argv[2])
    print("Done. Processed " + str(len(results)) + " records.")
