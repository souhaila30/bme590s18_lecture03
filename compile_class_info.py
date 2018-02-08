def main():
    csv_files = collect_all_csv_filenames()
    jsonfile = write_data(csv_files)
    combined = combine_all_csv_files(csv_files)
    space = is_space(combined)
    camel_case = is_camel_case(combined)



def collect_all_csv_filenames():
    import glob
    csv_files = glob.glob('*.csv')
    print(csv_files)
    return csv_files


def combine_all_csv_files(csv_files):
    filtered_files = csv_files
    filtered_files.remove('mlp6.csv')
    filtered_files.remove('combined.csv')

    import pandas as pd
    merged = []

    for filtered_file in filtered_files:
        df = pd.read_csv(filtered_file, delimiter=',', header=None)
        merged.append(df)
        print(filtered_files)

    combined = pd.concat(merged, ignore_index=True)
    print(combined)
    print(' ')
    print(csv_files)
    print(filtered_files)
    combined.to_csv('combined.csv', index=False)
    return combined


def is_space(combined):
    import csv
    file = open('combined.csv', 'r')
    data = csv.reader(file)

    for row in data:
        if " " in row[4].strip(' '):
            print(str(row[4]) + ' has whitespace')
        else:
            print(str(row[4]) + ' has no whitespace')

    return print

def is_camel_case(combined):
    import csv
    file = open('combined.csv', 'r')
    data = csv.reader(file)
    for row in data:
        if row[4].islower() or row[4].isupper():
            print(str(row[4]) + " is not CamelCase")
        else:
            print(str(row[4]) + " is CamelCase")

    return print


def write_data(csv_files):
    import pandas as pd
    import json
    from os.path import splitext

    for csv_file in csv_files:
        stem, _ = splitext(csv_file)
        jsonfile = stem + '.json'
        print(jsonfile)
        csv = pd.read_csv(csv_file)
        csv.to_json(jsonfile)

    #     reader = csv.DictReader(filtered_file)
    #     for row in reader:
    #         json.dump([row for row in reader])
    #         jsonfile.write('\n')
        # with open(filtered_file, 'r') as csv, open(jsonfile, 'w') as json:
        #    dump(list(DictReader(csv)),json)
    return jsonfile


if __name__ == "__main__":
    main()

