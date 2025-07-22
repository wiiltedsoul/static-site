import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import *
# use sys.argv to get first CLI argument as content directory then save as basepath; if one is not provided, use default "/"
if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "."  # <-- fix here

dir_path_static = os.path.join(basepath, "static")

dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating page...")
    # use generate_pages_recursive to generate a page for each markdown file in content directory and write to docs directory
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs)
    print("Done.")


main()
