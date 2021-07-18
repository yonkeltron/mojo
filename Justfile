quicktype_common_args := "-s schema Collection.json"

default:
  @just --list

quicktype:
  quicktype --python-version 3.7 -l python {{quicktype_common_args}} -o prep/mojo/collection.py

