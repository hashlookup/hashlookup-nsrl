# hashlookup-nsrl importer

hashlookup-nsrl is a NSRL RDSv3 importer for [hashlookup server](https://github.com/adulau/hashlookup-server).

[NSRL RDSv3](https://s3.amazonaws.com/rds.nsrl.nist.gov/RDS/RDSv3_Docs/RDSv3.pdf) is a new SQLite format for the NIST NSRL RDS database.

## Usage

Download the RDSv3 SQLite file and hashlookup-nsrl importer can be run in the following way:

`python3 importer.py -f ../data/RDS_2021.12.2_curated.db -s`

~~~~
usage: importer.py [-h] [-f FILE] [-u] [-s]

NSRL RDS importer for hashlookup server

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  NSRL RDS file (sqlite3 format) to import
  -u, --update          Update hash if it already exists. default is to update existing hashlookup record.
  -s, --skip-exists     Don't insert existing values. Default is to insert value regarless of their existence.
~~~~

## License

~~~~
The software is open source software released under the "Simplified BSD License".

Copyright 2022 Alexandre Dulaunoy

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
~~~~

