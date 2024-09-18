import pandas as pd


def txt_to_excel(txt_file, excel_file):
    data = []

    with open(txt_file, 'r', encoding='utf-8') as file:
        for line in file:
            if 'Classement Général' in line:
                continue

            parts = list(filter(None, line.split('    ')))

            if len(parts) == 4:
                rank = parts[0]
                name = parts[1]
                car = parts[2]
                points = parts[3]
                time = parts[3]
                data.append([rank, name, car, points, time])


    df = pd.DataFrame(data, columns=['Rank', 'Name', 'Car', 'Points', 'Time'])

    df.to_excel(excel_file, index=False)
    print(f"Data successfully written to {excel_file}")

txt_file = 'text.txt'
excel_file = 'classement_general.xlsx'
txt_to_excel(txt_file, excel_file)
