#!/usr/bin/python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def main():

    farminput = input("Which farm would you like to know about? (NE Farm, W Farm, or SE Farm) ").lower()

    for farm in farms:
        if farm["name"].lower() == farminput:
            print(f"The following plants/animals are raised on the {farm['name']}:")
            farmlist = farm["agriculture"]
            for a in farmlist:
                print(a,end=", ")

if __name__ == "__main__":
    main()

