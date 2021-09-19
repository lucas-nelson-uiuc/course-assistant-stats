import webbrowser
import json
import datetime
import os
import pandas as pd


class JupyterNotebook:
    '''
    Gather and strip student's Jupyter Notebook

    | def clean_notebook_json |
        > Loads JSON data from student's JSON file
        > Returns list of cells that contain student's declared function
    
    | def write_to_script |
        > Writes student's functions to Python script for testing
    '''

    def __init__(self, net_id):
        self.net_id = net_id
        self.raw_url = 'https://github-dev.cs.illinois.edu/' + f'/stat430-fa21/{self.net_id}/raw/master/lab02/lab02.ipynb'

    def clean_notebook_json(self):
        # strip raw json data from json file
        with open(f'{self.net_id}.json', 'r') as javascript:
            data = json.load(javascript)
        
        cells = data['cells']
        self.cells_code = [cell for cell in cells if cell['cell_type'] == 'code']
        
        outputs = [cell['outputs'] for cell in self.cells_code]
        self.sources = [cell['source'] for cell in self.cells_code]

    def write_to_script(self):
        with open('student_notebook.py', 'w') as st_nb:
            for script in self.sources:
                strip_script = []
                if len(script) > 0 and script[0].strip().startswith('def'):
                    for line in script:
                        st_nb.write(line)
                st_nb.write('\n')

class ScoringClass:
    '''
    Scores student's submission against test cases in `test_class.py`
    and writes score for student in `lab_report.txt` and `lab_report.csv`

    | def call_master_test |
        > Calls pytest conditional on test_class.py
        > Reports scores in student's log file
    
    | def collect_test_scores |
        > Gathers test scores from student's log file
    
    | def report_information |
        > Creates outline for descriptive information of test
        > Performs similar function for csv file
    
    | def student_rows |
        > Writes student data in per test
        > Performs similar function for csv file
    '''
    
    def __init__(self, net_id):
        self.net_id = net_id

    def call_master_test(self):
        cmd = f'pytest -v test_class.py | tee {self.net_id}.log'
        os.system(cmd)
    
    def collect_test_scores(self):
        
        self.test_collection = {}
        
        with open(f'{self.net_id}.log', 'r') as results:
            lines = results.readlines()
            for line in lines:
                if line.startswith('test_class.py::TestClass::'):
                    test_case_start = len('test_class.py::TestClass::') + 5
                    test_case_end = line[test_case_start:].find(' ') + test_case_start
                    test_case = line[test_case_start:test_case_end].strip()
                    if 'PASSED' in line:
                        self.test_collection[test_case] = '1'
                    if 'FAILED' in line:
                        self.test_collection[test_case] = '0'

    def report_information(self):
        with open('lab_report.txt', 'w') as report:
            # header of lab report
            report.write('DATE      : {}\n'.format(datetime.datetime.now().date()))
            report.write('TIME      : {}\n'.format(datetime.datetime.now().time()))
            report.write('-------------------------------------\n')
            # lab report for individual students
            report.write('Table of Student Results\n')
            ## top of table skeleton
            table_outline = ['-' * (len(test) + 2) for test in self.test_collection]
            table_outline = '+'.join(table_outline)
            report.write('+----------------+' + table_outline + '+\n')
            ## row of for net_id and test_cases
            header = [test for test in self.test_collection]
            header_row = ' | '.join(header)
            report.write('|     {}     | '.format('net_id') + header_row + ' |' + '\n')
            report.write('+----------------+' + table_outline + '+\n')

        with open('lab_report.csv', 'w') as csv_report:
            # header of lab report
            headers = ['net_id'] + list(self.test_collection.keys())
            csv_report.write(','.join(headers))
            csv_report.write('\n')
    
    def student_rows(self):
        with open('lab_report.txt', 'a+') as report:
            ## individual student reports
            student_row = [str(' ' * (len(test) - 1)) + str(self.test_collection[test])  for test in self.test_collection]
            student_row = ' | '.join(student_row)
            report.write('|{:^16}| '.format(self.net_id) + student_row + ' |')
            report.write('\n')
        
        with open('lab_report.csv', 'a+') as csv_report:
            csv_report.write(self.net_id + ',' + ','.join(self.test_collection.values()))
            csv_report.write('\n')

class CleanLocalComputer:
    '''
    Cleans local folder of .json and .log files
    '''
    
    def __init__(self, net_id):
        self.net_id = net_id
    
    def clean_local_folder(self):
        #for path in [f'{self.net_id}.json', f'{self.net_id}.log']:
        for path in [f'{self.net_id}.log']:
            if os.path.exists(path):
                os.remove(path)
            else:
                print('File path not found in directory')

                

def main():
    with open('student_net_ids.txt', 'r') as net_ids:
        
        lines = net_ids.readlines()
        
        paths_exist = 0
        
        for i, net_id in enumerate(lines):
            if os.path.exists(f'{net_id.strip()}.json'):
                student = JupyterNotebook(net_id.strip())
                student.clean_notebook_json()
                student.write_to_script()
                report = ScoringClass(student.net_id)
                report.call_master_test()
                report.collect_test_scores()
                if paths_exist == 0:
                    report.report_information()
                    paths_exist += 1
                report.student_rows()
                garbage = CleanLocalComputer(student.net_id)
                garbage.clean_local_folder()
            
            else:
                print('> File does not exist for {}'.format(net_id.strip()))

        print('------------------------------------')
        print(f'GRADING COMPLETE: {paths_exist} repos graded')
        print('------------------------------------')


if __name__ == '__main__':
    main()