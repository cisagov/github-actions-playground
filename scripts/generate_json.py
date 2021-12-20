"""Generate a JSON from a YAML file's contents.

generate_json.py YAML JSON

Options:
  -h, --help  Show this help message.

"""

# Standard Python Libraries
import argparse
import json
import logging
from pathlib import Path
import sys

# Third-Party Libraries
import yaml


def main():
    """Read in a given YAML file and generate a JSON file from its contents."""
    # Set up logging
    logging.basicConfig(
        format="%(asctime)-15s %(levelname)s %(message)s", level=logging.INFO
    )

    parser = argparse.ArgumentParser(
        description="Generate a JSON from a YAML file's contents."
    )
    parser.add_argument(
        "yaml_file_path",
        metavar="YAML",
        type=Path,
        nargs="?",
        help="The YAML file to read.",
    )
    parser.add_argument(
        "json_file_path",
        metavar="JSON",
        type=Path,
        nargs="?",
        help="The JSON file to output.",
    )
    args = parser.parse_args()

    if not args.yaml_file_path.exists():
        logging.error('The given YAML file "%s" does not exist.', args.yaml_file_path)
        sys.exit(1)

    with open(args.yaml_file_path) as in_file, open(
        args.json_file_path, "w"
    ) as out_file:
        data = yaml.safe_load(in_file)
        out_file.write(json.dumps(data, indent=2, sort_keys=True))
        out_file.write("\n")


if __name__ == "__main__":
    main()
