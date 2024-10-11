import os
import csv
from collections import defaultdict

# Function to replace underscores with spaces for display purposes, but not for path operations
def clean_folder_name(folder_name):
    return folder_name.replace("_", " ").strip()

# Function to walk through the folder structure and save as a CSV with full path
def export_taxonomy_to_csv(root_folder, output_csv):
    taxonomy_data = []

    for dirpath, dirnames, filenames in os.walk(root_folder):
        if 'task_meta.json' in filenames:
            # This directory contains a task
            rel_path = os.path.relpath(dirpath, root_folder)
            parts = rel_path.split(os.sep)  # Split the relative path by directory separators

            # Use cleaned folder names for display in the CSV
            clean_parts = [clean_folder_name(part) for part in parts]
            taxonomy_data.append(clean_parts)

    # Now write the data to CSV
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Dynamically adjust the number of columns based on the longest path
        max_columns = max(len(parts) for parts in taxonomy_data)
        header = [f"Level {i+1}" for i in range(max_columns)]  # Create dynamic headers based on levels
        writer.writerow(header)  # Write the header row

        for row in taxonomy_data:
            writer.writerow(row + [''] * (max_columns - len(row)))  # Pad rows to ensure consistent column length

    print(f"Taxonomy exported to {output_csv}")

# Specify the folder path and the output CSV file
folder_path = '/Users/eric/code/Vision-BIG-bench/vision-bigbench/taxonomy/taxonomy_structure'
output_csv = './static/data/taxonomy_new.csv'

# Call the function to export the taxonomy
export_taxonomy_to_csv(folder_path, output_csv)
