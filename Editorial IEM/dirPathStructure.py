#pip install pandas openpyxl
import os
import pandas as pd

def traversal_path(directory, current_path=None, rows=None):

    if current_path is None:
        current_path = []
    if rows is None:
        rows = []

    items = sorted(os.listdir(directory))
    rows.append(current_path.copy())

    for item in items:
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            traversal_path(path, current_path + [item], rows)
        else:
            rows.append(current_path + [item])

    return rows

if __name__ == "__main__":
    try:
        folder = input("Ingrese la ruta de la carpeta: ").strip()
        if os.path.exists(folder) and os.path.isdir(folder):
            rows = traversal_path(folder, [os.path.basename(folder)])
            max_levels = max(len(row) for row in rows)
            rows = [row + [""] * (max_levels - len(row)) for row in rows]
            columns = [f"Nivel {i+1}" for i in range(max_levels)]
            df = pd.DataFrame(rows, columns=columns)
            excel_name = "Tree.xlsx"
            df.to_excel(excel_name, index=False)

            print(f"Estructura guardada en '{excel_name}'")
        else:
            print("La ruta ingresada no es válida.")
    except Exception as e:
        print(f"Error: {e}")
