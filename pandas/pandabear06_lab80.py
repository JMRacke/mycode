#!/usr/bin/python3

import pandas as pd


def main():

    mapfile = pd.read_json("~/mycode/rooms.json")

    questions = pd.read_json("~/mycode/iflogic_proj/questions.json")

    mapfile.to_csv("mapfile.csv")

    questions.to_csv("questions.csv")

    print(mapfile)

    print(questions)


if __name__ == "__main__":
    main()

