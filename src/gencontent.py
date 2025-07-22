import os
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    # replace any instances of 'href="/' with 'href="{basepath}' and 'src="/' with 'src="{basepath}'
    template = template.replace('href="/', f'href="{os.path.dirname(dest_path)}/')
    template = template.replace('src="/', f'src="{os.path.dirname(dest_path)}/')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    '''
      crawl every entry in content directory
      for each markdown file, generate new .html using same template.html
      and save it to docs directory with same structure
      e.g. content/index.md -> docs/index.html
        e.g. content/about/team.md -> docs/about/team.html
    '''
    for filename in os.listdir(dir_path_content):
        if filename.endswith(".md"):
            from_path = os.path.join(dir_path_content, filename)
            dest_path = os.path.join(dest_dir_path, filename.replace(".md", ".html"))
            generate_page(from_path, template_path, dest_path)
        elif os.path.isdir(os.path.join(dir_path_content, filename)):
            subdir_content = os.path.join(dir_path_content, filename)
            subdir_docs = os.path.join(dest_dir_path, filename)
            generate_pages_recursive(subdir_content, template_path, subdir_docs)
            # Recursively handle subdirectories
        else:
            print(f"Skipping non-markdown file: {filename}")
    print(f"Generated pages in {dest_dir_path}")