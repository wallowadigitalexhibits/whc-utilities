#!/usr/bin/python

import sys, pandas, argparse

def main():
    print('xlsx2json')

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help='Name of an input file')
    parser.add_argument('-o', '--output', type=str, help='Name of an output file')
    parser.add_argument('-s', '--schema', dest='schema_arg', type=str, help='Specify a reference schema')
    parser.add_argument('-f', '--force', dest='force_arg', type=str, help='Force an overwrite or skip conflicts')
    parser.add_argument('-db', '--existing-db', dest='existing_db_arg', type=str, help='Merge with this existing db.json file')
    args = parser.parse_args()

    print(args)
    main()
