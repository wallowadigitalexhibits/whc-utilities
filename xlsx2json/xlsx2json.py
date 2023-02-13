#!/usr/bin/python

import sys, json, pandas, argparse, pathlib

def main():
    print('xlsx2json')

    # set global vars and flags
    dryRunFlag = False
    referenceDb = []
    referenceDbLabels = []

    # check and handle the force flag

    ##############################
    ### read the database file ###
    ##############################
    # - get the list of available node labels

    pDb = pathlib.Path(args.existing_db_file)
    try:
        with pDb.open() as fDb:
            referenceDb = json.load(fDb)
            print('loading the database file')
            if referenceDb:
                for node in referenceDb:
                    referenceDbLabels.append(node['core_props']['label'])
                referenceDbLabels = set(referenceDbLabels)
                print(referenceDbLabels)
            else:
                print('ERROR: database file is empty')

    except OSError:
        print('ERROR: database file does not exist')

    ####################################
    ### read in the spreadsheet file ###
    ####################################
    # - identify all the sheets
    #       must have node labels or error & exit
    # - does each sheet have a header row?
    #       must have a header row or error & exit
    # - is the first column 'id'?
    #       must have first column as 'id' or error & exit
    # - do all the column header names match the schema?
    #       must match or is force arg present?
    #           if not, enter dry-run mode with error message
    #           if force=override or force=skip, ignore these columns

    pInput = pathlib.Path(args.input_file)
    try:
        with pInput.open() as fInput:
            print('input file exists')

            # identify all the sheets


    except OSError:
        print('ERROR: input file does not exist')

    ##############################
    ### build the new database ###
    ##############################
    #


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input',
                        dest='input_file',
                        type=str,
                        help='Name of an input file',
                        required=True)
    parser.add_argument('-o', '--output',
                        dest='output_file',
                        type=str,
                        help='Name of an output file',
                        required=True)
    parser.add_argument('-dry', '--dry-run',
                        dest='force',
                        type=str,
                        help='Force an overwrite or skip conflicts')
    parser.add_argument('-f', '--force',
                        dest='force',
                        type=str,
                        help='Force an overwrite or skip conflicts')
    parser.add_argument('-db', '--existing-db',
                        dest='existing_db_file',
                        type=str,
                        help='Existing db with (at minimum) label nodes defining each sheet to import',
                        required=True)
    args = parser.parse_args()

    print(args)
    main()
