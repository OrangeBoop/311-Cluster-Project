import json

notebook_path = r"c:\Users\idanp\Downloads\clusProject\311-Cluster-Project\Clustering_Zip\Clustering_zip_KMEANS.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for idx, cell in enumerate(nb.get('cells', [])):
    cell_type = cell.get('cell_type')
    source = cell.get('source', [])
    source_str = "".join(source)
    first_few_lines = "\n".join(source_str.split("\n")[:3])
    print(f"Cell {idx} ({cell_type}):")
    print(first_few_lines)
    print("-" * 40)
