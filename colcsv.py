import csv
with open("sample.csv", newline='') as csvfile:
    d = csv.DictReader(csvfile)
    print("ROLL NO STUDENT NAME")
    print("--------------------")
    for i in d:
        print(i['Series_reference'], i['STATUS'])