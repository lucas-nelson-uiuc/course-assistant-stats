import pprint

def longest_test_name(test_dict):
    longest_key = 0
    for key in test_dict:
        if len(key) > longest_key:
            longest_key = len(key)
    return longest_key

def report_statistics():
    with open('log.txt', 'r') as log:
        lines = [line.strip() for line in log.readlines() if line.startswith('master_test.py::TestClass::')]
        passed = [line[:line.find('[')] for line in lines if 'PASSED' in line]
        failed = [line[:line.find('[')] for line in lines if 'FAILED' in line]
        tests = set(line[line.rfind('::') + 2:line.find('[')] for line in lines)
        
        # dict for test : pass, fail, points
        test_info = {test:[0,0,0] for test in tests}
        for test in test_info:
            for p in passed:
                if p.endswith(test):
                    test_info[test][0] += 1
        for test in test_info:
            for f in failed:
                if f.endswith(test):
                    test_info[test][1] += 1

    for test in test_info:
        test_info[test][2] = float(input('Total points for {}: '.format(test)))
        
    print('====================EXPECTED SCORE PER TEST====================')
    total_score = 0
    for test in test_info:
        exp_score = test_info[test][2] * (test_info[test][0] / (test_info[test][0] + test_info[test][1]))
        total_score += exp_score
        print('{:<{}} :: {}'.format(test,
                                    longest_test_name(test_info),
                                    exp_score))
    print('{:<{}} :: {}'.format('total',
                                longest_test_name(test_info),
                                total_score / sum([test_info[test][2] for test in test_info])))

if __name__ == '__main__':
    report_statistics()
