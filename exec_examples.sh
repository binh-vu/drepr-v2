set -ex

export EX=resource_categories
python -m drepr examples/$EX/model.yml default=examples/$EX/categories.csv --progfile examples/$EX/program/write_to_str.py
python -m drepr examples/$EX/model.yml default=examples/$EX/categories.csv --progfile examples/$EX/program/write_to_file.py --outfile examples/$EX/output.ttl

export EX=pseudo_people
python -m drepr examples/$EX/model.yml default=examples/$EX/default.csv --progfile examples/$EX/program/write_to_str.py
python -m drepr examples/$EX/model.yml default=examples/$EX/default.csv --progfile examples/$EX/program/write_to_file.py --outfile examples/$EX/output.ttl

export EX=mineral_site/missing_values
python -m drepr examples/$EX/model.yml default=examples/$EX/default.json --progfile examples/$EX/program/write_to_str.py
python -m drepr examples/$EX/model.yml default=examples/$EX/default.json --progfile examples/$EX/program/write_to_file.py --outfile examples/$EX/output.ttl

export EX=mineral_system/misspath_autoalign
python -m drepr examples/$EX/model.yml default=examples/$EX/default.json --progfile examples/$EX/program/write_to_str.py
python -m drepr examples/$EX/model.yml default=examples/$EX/default.json --progfile examples/$EX/program/write_to_file.py --outfile examples/$EX/output.ttl