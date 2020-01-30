#!/usr/bin/env python3
#
# This script is run by a cron job as the DAEMON_USER
#
# Runs lichen plagiarism detector for saved configuration
#

import os
import sys
import pwd
import time
import subprocess
import json
import pickle
from sqlalchemy import create_engine, Table, MetaData, select

def main():
    username = pwd.getpwuid(os.getuid()).pw_name
    if username != "submitty_daemon":
        raise SystemError("ERROR!  This script must be run by submitty_daemon")

    if len(sys.argv) != 4:
        raise SystemError("ERROR!  This script must be given 3 argument which should be path of lichen config")

    semester = sys.argv[1];
    course = sys.argv[2];
    gradeable = sys.argv[3];

    # right outer join -> ( {} x)
    # select r.id, r.gradeable, r.user_id from electronic_gradeable eg RIGHT JOIN
    # lichen_tok_subs l ON r.gradeable = "current" and l.id = r.id WHERE l.id IS NULL
    # js = json.dump([(dict(row.items())) for row in rs], )

    config_path = "/var/local/submitty/courses/"+ semester + "/" +course+ "/lichen/config/lichen_"+ semester+"_"+ course+ "_" +gradeable+".json"
    data_path = "/var/local/submitty/courses/"+ semester + "/" +course+ "/lichen/config/lichen_"+ semester+"_"+ course+ "_" +gradeable+"_data.p"

    subprocess.call(['/usr/local/submitty/Lichen/bin/concatenate_all.py', config_path ])
    ret_code_tok = os.system(f'/usr/local/submitty/Lichen/bin/tokenize_all.py {config_path} {data_path}')
    ret_code_hash = os.system(f'/usr/local/submitty/Lichen/bin/hash_all.py {config_path}')
    subprocess.call(['/usr/local/submitty/Lichen/bin/compare_hashes.out', config_path ])

    if ret_code == 0:
        #insert into tokens
        #rows_returned = len(query)
        #
        print("successfully tokenized them")

    os.remove(data_path)

    print("finished running lichen plagiarism for " + config_path)

if __name__ == "__main__":
    main()
