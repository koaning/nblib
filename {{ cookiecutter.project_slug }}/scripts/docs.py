import nbformat
from pathlib import Path

def convert_notebook_to_docs(input_folder, output_folder):
    folder = Path(input_folder)
    # Iterate over all files in the specified folder
    for notebook_path in folder.glob("*.nbconvert.ipynb"):
        new_root_folder = Path(output_folder)
        python_file_path = new_root_folder / notebook_path.with_suffix('.md').parts[-1].replace(".nbconvert", "")
        
        # Read the notebook
        with notebook_path.open('r', encoding='utf-8') as nb_file:
            nb_content = nbformat.read(nb_file, as_version=4)
        
        # Write the cells to a Markdown file
        with python_file_path.open('w', encoding='utf-8') as md_file:
            for cell in nb_content['cells']:
                if cell['cell_type'] == 'markdown':
                    md_file.write(cell['source'] + '\n\n')
                elif cell['cell_type'] == 'code':
                    if "## HIDE" not in cell['source'] and "## EXPORT" not in cell['source']:
                        md_file.write('```python\n')
                        md_file.write(cell['source'].strip() + '\n')
                        md_file.write('```\n\n')
                        if 'outputs' in cell and cell['outputs']:
                            md_file.write('**Output:**\n\n')
                            for output in cell['outputs']:
                                if 'text' in output:
                                    md_file.write('```\n' + output['text'] + '\n```\n\n')
                                elif 'data' in output:
                                    if 'text/plain' in output['data']:
                                        if not '<Figure' in output['data']['text/plain']:
                                            md_file.write('```\n' + output['data']['text/plain'] + '\n```\n\n')
                                    if 'image/png' in output['data']:
                                        img_repr = output["data"]["image/png"]
                                        md_file.write(f'\n<img src="data:image/png;base64, {img_repr}"/>\n')

if __name__ == "__main__":
    convert_notebook_to_docs(".tmpdir", "docs")
    Path("docs/__init__.md").rename("docs/index.md")
    Path("README.md").write_text(Path("docs/index.md").read_text())
