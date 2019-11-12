import csv

def get_data(search_string) -> (list, bool):
    result = []

    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            if len(result) >= 20:
                return (result, True)

            if search_string in row[3]:
                result.append({
                    "address": row[1],
                    "code": row[2],
                    "name": row[3]
                })

        return (result, False)
