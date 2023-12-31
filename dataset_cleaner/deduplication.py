import hashlib
import gzip
import json
from tqdm import tqdm
import io
import os
import glob

def rename_file(path):
    # Split the path into directory and filename
    directory, filename = os.path.split(path)

    # Extract the base filename and extension
    base_filename, extension = os.path.splitext(filename)
    name, ext = base_filename.split('.')
    # Create the new filename with '_update' appended
    new_filename = f"{directory}/{name}_update.{ext}{extension}"
    #print(new_filename)
    return new_filename

def hash_str(text):
    m = hashlib.sha256()
    m.update(text)
    return m.hexdigest()


def read_json_gz(f):
    with gzip.open(f, 'rb') as fh:
        reader = io.BufferedReader(fh)
        yield from tqdm(reader)

def write_json_gz(f, lines):
    with gzip.open(f, 'ab') as fh:
        fh.write(lines)


def exact_deduplication(path):
    seenHash = set()
    for i in glob.glob(f'{path}/*.json.gz'):
        raw = read_json_gz(i)
        for j in raw:
            hash = hash_str(j)
            if hash not in seenHash:
                wf = rename_file(i)
                write_json_gz(wf, j)
                seenHash.add(hash)
    return "Done"
