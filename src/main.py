import os
import shutil
from markdown_blocks import *
from copystatic import copy_files_recursive


dir_path_static = "./static"
dir_path_public = "./public"


def main():
    # delete public directory if it exists
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    # copy all static files from static to public
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

# generate a page from content/index.md using template.html and write it to public/index.html
    print("Generating index page...")
    generate_page(
        from_path="content/index.md",
        template_path="template.html",
        dest_path="public/index.html"
    )


main()
