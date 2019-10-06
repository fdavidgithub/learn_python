class verbs(object):
    def __init__(self, csvfile):
        import csv
        print('Opening ' + csvfile)

        try:
            f = open(csvfile, 'r')
        except FileNotFoundError:
            print('CSV file not exist')
        else:
            self.reader = csv.reader(f, delimiter=';')
    
    def aslist(self):
        return list(self.reader)

    def asdict(self):
        return dict(list(self.reader))

def main():
    simple_past = verbs('simple_past.csv').asdict()
    past_participle = verbs('past_participle.csv').asdict()
 
    print('Common Irregular verbs')
    common_verbs = dict(simple_past.items() & past_participle.items())   
    print(common_verbs)

    print('\nClean List of Verbs in Past Participle')
    outer = [k for k in simple_past if past_participle[k] != simple_past[k]]
    for k in outer:
        print(k + ';' + past_participle[k])

    
if __name__ == "__main__":
    main()

