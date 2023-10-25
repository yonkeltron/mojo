import json
import logging

from prep.parse_blank_line_separated import collection_from_raw

import typer

app = typer.Typer()


@app.command()
def prep_input(input_txt: str, output_path: str, url: str = typer.Option(...)) -> None:
    with open(input_txt, 'r') as input_file:
        body = input_file.read()
    logging.info(f"Read {len(body)} bytes from {input_file}.")

    collection = collection_from_raw(input_txt, url, body)
    logging.info(f"Extracted {len(collection['haiku'])} haiku.")

    with open(output_path, 'w') as output_file:
        json.dump(collection, output_file, indent=2)
    logging.info(f"Wrote collection to {output_path}")


@app.command()
def stats(collection_path: str) -> None:
    with open(collection_path, 'r') as collection_file:
        collection = json.load(collection_file)

    print(json.dumps(collection, indent=2))


if __name__ == '__main__':
    app()
