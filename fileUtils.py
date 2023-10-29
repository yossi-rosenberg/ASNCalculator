import csv
import pandas as pd
import linecache

def get_asn(address_as_long_number):
    df = pd.read_table('resources/ip2asn-v4-u32.tsv')
    high = len(df)
    low = 0
    middle = 0
    with open('resources/ip2asn-v4-u32.tsv') as fd:
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        while low <= high:
            middle = (high + low) // 2
            row = linecache.getline('resources/ip2asn-v4-u32.tsv', middle)
            lower_value = int(row.rsplit("\t").__getitem__(0))
            upper_value = int(row.rsplit("\t").__getitem__(1))
            if address_as_long_number > lower_value and address_as_long_number < upper_value :
                return row.rsplit("\t").__getitem__(2)
            # Take the upper half
            elif address_as_long_number > upper_value:
                low = middle + 1

            # Take the lower half
            else:
                high = middle - 1

