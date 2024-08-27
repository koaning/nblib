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

if __name__ == "__main__":
    convert_notebooks_to_python("src", "{{ cookiecutter.project_slug }}")
