import nbformat
from pathlib import Path

def convert_notebooks_to_python(folder_path):
    folder = Path(folder_path)
    
    # Iterate over all files in the specified folder
    for notebook_path in folder.glob("*.ipynb"):
        python_file_path = notebook_path.with_suffix('.py')
        
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
    folder_path = "path/to/your/notebooks"  # Replace with the path to your folder
    convert_notebooks_to_python(folder_path)