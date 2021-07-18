quicktype_common_args := "-s schema Collection.schema.json"

default:
  @just --list

quicktype:
  quicktype --python-version 3.7 -l python {{quicktype_common_args}} > prep/mojo/collection.py

