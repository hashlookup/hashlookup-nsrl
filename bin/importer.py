import argparse
import os
import sqlite3
import sys

import hashlookup.hashlookup as hashlookup

parser = argparse.ArgumentParser(description="NSRL RDS importer for hashlookup server")

parser.add_argument("-f", "--file", help="NSRL RDS file (sqlite3 format) to import")
parser.add_argument(
    "-u",
    "--update",
    help="Update hash if it already exists. default is to update existing hashlookup record.",
    action="store_true",
    default=True,
)
parser.add_argument(
    "-s",
    "--skip-exists",
    help="Don't insert existing values. Default is to insert value regarless of their existence.",
    action="store_true",
    default=False,
)
args = parser.parse_args()

if not args.file:
    parser.print_help()
    sys.exit(1)

source = os.path.basename(args.file)
if args.update:
    print(f'{source}')
    h = hashlookup.HashLookupInsert(
        update=True, source=source, skipexists=args.skip_exists, publish=True
    )
else:
    h = hashlookup.HashLookupInsert(
        update=False, source=source, skipexists=args.skip_exists, publish=True
    )


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


rds = sqlite3.connect(args.file)
rds.row_factory = dict_factory
cur = rds.cursor()
print(f"Importing {source}...")
cur.execute('''SELECT * from file''')
for i, row in enumerate(cur):
    if 'sha256' in row:
        h.add_hash(value=row['sha256'], hashtype='SHA-256')
    if 'sha1' in row:
        h.add_hash(value=row['sha1'], hashtype='SHA-1')
    if 'md5' in row:
        h.add_hash(value=row['md5'], hashtype='MD5')
    if 'file_name' in row:
        h.add_meta(key='FileName', value=row['file_name'])
    if 'file_size' in row:
        h.add_meta(key='FileSize', value=row['file_size'])
    if 'package_id' in row:
        h.add_meta(key='RDS:package_id', value=row['package_id'])
    h.insert()
    print(row)
