import pandas as pd

df = pd.read_csv('lab_report.csv').fillna(0)

with open('lab_report.txt', 'a+') as report:
    
    table_outline = ['-' * (len(col) + 2) for col in df.columns[1:]]
    table_outline = '+'.join(table_outline)
    report.write('+----------------+' + table_outline + '+\n')
    
    report.write('|{:^16}| '.format('num students'))
    for col in df.columns[1:]:
        report.write(' ' * (len(col) - 3) + str(df[col].shape[0]) + ' | ')
    report.write('\n')
    report.write('|{:^16}| '.format('num correct'))
    for col in df.columns[1:]:
        report.write(' ' * (len(col) - 2) + str(int(df[col].sum())) + ' | ')
    report.write('\n')
    report.write('|{:^16}| '.format('mean score'))
    for col in df.columns[1:]:
        report.write(' ' * (len(col) - 5) + '{:.2f}'.format(round(df[col].mean() * 100, 2)) + ' | ')
    report.write('\n')
    report.write('|{:^16}| '.format('std dev'))
    for col in df.columns[1:]:
        report.write(' ' * (len(col) - 5) + '{:.2f}'.format(round(df[col].std() * 100, 2)) + ' | ')
    report.write('\n')

    report.write('+----------------+' + table_outline + '+\n')