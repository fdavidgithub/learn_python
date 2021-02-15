import math
from pandas_ods_reader import read_ods

def load(path="./docs/data.ods",  sheet=1):
    return read_ods(path, sheet)

def prepare(ods):
    table = ods.to_dict(orient='records')

    data = {}
    for rec in table: 
        detail = {}

        for col in list(rec.keys()):
            if col == 'Cliente':
                key = rec[col]
            else:
                detail.setdefault(col, rec[col])
        
        data.setdefault(key, detail)

    return data
    
