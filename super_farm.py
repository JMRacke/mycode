#!/usr/bin/python3

farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


animals = ["sheep","cows","pigs","chickens","llama","cats"]

def main():
    farmvalues = []
    for farm in farms:
        farmvalues.append(farm["name"])

    farminput = input(f"Which farm would you like to know about? {farmvalues} ").lower()

    for farm in farms:
        if farm["name"].lower() == farminput:
            print(f"The following plants/animals are raised on the {farm['name']}:")
            farmlist = farm["agriculture"]
            for a in farmlist:
                print(a,end=", ")
            print("\n")
if __name__ == "__main__":
    main()

