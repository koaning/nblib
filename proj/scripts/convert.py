import nbformat
from pathlib import Path


def convert_notebooks_to_python(input_folder, output_folder):
    folder = Path(input_folder)
    
    # Iterate over all files in the specified folder
    for notebook_path in folder.glob("*.ipynb"):
        new_root_folder = Path(output_folder)
        python_file_path = new_root_folder / notebook_path.with_suffix('.py').parts[-1]
        
        # Read the notebook
        with notebook_path.open('r', encoding='utf-8') as nb_file:
            nb_content = nbformat.read(nb_file, as_version=4)
        
        # Extract code cells
        code_cells = [cell['source'] for cell in nb_content['cells'] if cell['cell_type'] == 'code']
        
        # Write the code cells to a Python file
        with python_file_path.open('w', encoding='utf-8') as py_file:
            for cell in code_cells:
                py_file.write(cell + '\n\n')


def convert_notebook_to_docs(input_folder, output_folder):
    print("hello")
    folder = Path(input_folder)
    # Iterate over all files in the specified folder
    for notebook_path in folder.glob("*.ipynb"):
        new_root_folder = Path(output_folder)
        python_file_path = new_root_folder / notebook_path.with_suffix('.md').parts[-1]
        
        # Read the notebook
        with notebook_path.open('r', encoding='utf-8') as nb_file:
            nb_content = nbformat.read(nb_file, as_version=4)
        
        # Write the cells to a Markdown file
        with python_file_path.open('w', encoding='utf-8') as md_file:
            print(python_file_path)
            for cell in nb_content['cells']:
                if cell['cell_type'] == 'markdown':
                    md_file.write(cell['source'] + '\n\n')
                elif cell['cell_type'] == 'code':
                    if cell['source'].strip().startswith('## KEEP'):
                        md_file.write('```python\n')
                        md_file.write(cell['source'].replace("## KEEP", "").strip() + '\n')
                        md_file.write('```\n\n')
                        if 'outputs' in cell and cell['outputs']:
                            md_file.write('Output:\n\n')
                            for output in cell['outputs']:
                                if 'text' in output:
                                    md_file.write('```\n' + output['text'] + '\n```\n\n')
                                elif 'data' in output:
                                    if 'text/plain' in output['data']:
                                        md_file.write('```\n' + output['data']['text/plain'] + '\n```\n\n')



if __name__ == "__main__":
    print("hello")
    convert_notebooks_to_python("src", "proj")
    convert_notebook_to_docs("src", "docs")
