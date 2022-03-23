# Script used to remove PII and opinions from data
# Liam Fruzyna 2022-03-23

import sys, os, json

# check for path argument
if len(sys.argv) < 2:
    print('Requires path as argument')
    exit(1)

dir = sys.argv[1]

# go over every json file in given directory
for filename in os.listdir(dir):
    path = os.path.join(dir, filename)
    if os.path.isfile(path) and filename.endswith('.json'):
        obj = None

        # read json
        with open(path, 'r') as f:
            obj = json.load(f)

            # replace values
            if not isinstance(obj, list):
                if 'meta_scouter_id' in obj.keys():
                    obj['meta_scouter_id'] = 0
                if 'match_post_notes_driver_skill' in obj.keys():
                    obj['match_post_notes_driver_skill'] = 3
                if 'match_post_notes_notes' in obj.keys():
                    obj['match_post_notes_notes'] = 'Removed'

        # rewrite json
        with open(path, 'w') as f:
            if obj is not None:
                f.write(json.dumps(obj))
