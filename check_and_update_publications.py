import os
import re
import glob

def process_publications():
    # Get all publication folders
    publication_folders = glob.glob('content/publication/*/')
    
    # Counter for updated files
    updated_count = 0
    total_count = len(publication_folders)
    
    for folder in publication_folders:
        index_file = os.path.join(folder, 'index.md')
        
        # Check if index.md exists
        if not os.path.isfile(index_file):
            print(f"No index.md found in {folder}, skipping...")
            continue
        
        # Check if any featured image exists (regardless of extension)
        featured_files = glob.glob(os.path.join(folder, 'featured.*'))
        if featured_files:
            print(f"Featured image exists in {folder}, no changes needed.")
            continue
        
        # If we get here, we need to remove the image section
        print(f"No featured image in {folder}, updating index.md...")
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the image section
        image_pattern = r'image:\n  caption: .*?\n  focal_point: .*?\n  preview_only: .*?\n'
        
        # Remove the image section
        updated_content = re.sub(image_pattern, '', content, flags=re.DOTALL)
        
        # Write the updated content back
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        updated_count += 1
        print(f"Updated {index_file}")
    
    print(f"\nSummary: Updated {updated_count} out of {total_count} publication files.")

if __name__ == "__main__":
    process_publications() 