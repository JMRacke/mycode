#!/usr/bin/python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def main():

    animal_list = farms[0].get("agriculture")
    for animal in animal_list:
        print(animal)


if __name__ == "__main__":
    main()

