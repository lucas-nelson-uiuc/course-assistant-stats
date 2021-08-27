import subprocess
import sys
import os
import statistics
import pandas as pd
import uniplot

def call_master_test(num_attempts=15):
    '''
    Call master_test.py a specified count of times

    Parameters:
        || num_attempts ||
            estimated number of attempts the average
            student will try for problem; variable

    Returns:
        || log.txt ||
            text file detailing tests conducted
            and outcome of tests; needed for
            analysis in report_statistics()
    '''

    cmd = f'pytest -v --count={num_attempts} | tee log.txt'
    os.system(cmd)


def longest_test_name(test_dict):
    '''Find longest test name for pprint'''

    longest_key = 0
    for key in test_dict:
        if len(key) > longest_key:
            longest_key = len(key)
    return longest_key


def simulate_students(num_students=5, num_attempts=15):
    '''
    Generate report for provided solution file and test suite

    Parameters:
        || none ||

    Returns:
        || report_table ||
            CLI table detailing score per test and overall score
    '''

    test_collection = {}
    
    i = 0
    while i < num_students:
        i+= 1
        
        call_master_test(num_attempts)
    
        with open('log.txt', 'r') as log:
            lines = [line.strip() for line in log.readlines() if line.startswith('master_test.py::TestClass::')]
            passed = [line[:line.find('[')] for line in lines if 'PASSED' in line]
            failed = [line[:line.find('[')] for line in lines if 'FAILED' in line]
            tests = set(line[line.rfind('::') + 2:line.find('[')] for line in lines)

            for test in tests:
                if test in test_collection.keys():
                    break
                else:
                    test_collection[test] = []
            
            # dict for test : pass, fail, points
            test_info = {test:[0,0] for test in tests}
            for test in test_info:
                for p in passed:
                    if p.endswith(test):
                        test_info[test][0] += 1
            for test in test_info:
                for f in failed:
                    if f.endswith(test):
                        test_info[test][1] += 1

        for test in tests:
            test_collection[test].append((test_info[test][0] / (test_info[test][0] + test_info[test][1])) * 100)

    test_weights = {test : float(input('Points available for {}: '.format(test))) for test in tests}
    
    print('====================EXPECTED SCORE PER TEST====================')
    for test in test_collection:
        print('{:<{}} :: {}'.format(test,
                                    longest_test_name(test_info),
                                    statistics.mean(test_collection[test])))
    
    print('====================PROJ. SUBMISSION SCORE=====================')
    score_per_test = {test : statistics.mean(test_collection[test]) * test_weights[test] for test in test_collection}
    total_score = round((sum(score_per_test.values()) / sum(test_weights.values())), 4)
    print('{:<{}} :: {}'.format('total',
                                longest_test_name(test_info),
                                total_score))

    return test_collection

def hist_results(test_dict):
    df = pd.DataFrame(test_dict)
    option = input('Select test: {}\n> '.format([col for col in df.columns]))
    uniplot.histogram(df[option], title=option, color='green',
                    x_min=0, x_max=100, bins=5)
    print('=====RECAP=====================================')
    print('  # of students = {}'.format(df[option].shape[0]))
    print('  mean score    = {}'.format(df[option].mean()))
    print('  sample var    = {}'.format(df[option].var()))
    print('  sample std    = {}'.format(df[option].std()))
    print('===============================================')
    

if __name__ == '__main__':
    
    num_students = int(input('Enter number of students: '))
    num_attempts = int(input('Enter number of attempts: '))
    hist_results(simulate_students(num_students=num_students, num_attempts=num_attempts))
