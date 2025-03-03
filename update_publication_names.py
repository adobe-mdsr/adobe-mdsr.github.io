#!/usr/bin/env python3
import os
import re
from pathlib import Path

def parse_front_matter(front_matter_text):
    """Parse YAML-like front matter without using the yaml package."""
    front_matter = {}
    for line in front_matter_text.strip().split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            # Remove quotes if present
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            front_matter[key] = value
    return front_matter

def clean_publication_name(publication):
    """Remove all numbers and dashes from publication names like 'WACV-25' or 'AAAI 2020'."""
    # Remove all digits
    cleaned = re.sub(r'\d+', '', publication)
    # Remove any dashes
    cleaned = cleaned.replace('-', '')
    # Clean up any double spaces that might result
    cleaned = re.sub(r'\s+', ' ', cleaned)
    # Trim whitespace
    cleaned = cleaned.strip()
    return cleaned

def update_publication_name(file_path, dry_run=False):
    """Update publication field in the front matter by removing numbers and dashes."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the content into front matter and body
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter_text = parts[1]
            body = parts[2] if len(parts) > 2 else ""
            
            # Parse the front matter
            front_matter = parse_front_matter(front_matter_text)
            
            # Extract publication information
            publication = front_matter.get('publication', '')
            
            if publication:
                # Clean the publication name
                cleaned_publication = clean_publication_name(publication)
                
                # Debug output
                print(f"File: {file_path}")
                print(f"  Original publication: '{publication}'")
                print(f"  Cleaned publication: '{cleaned_publication}'")
                print(f"  Are they different? {cleaned_publication != publication}")
                
                # Check if publication name needs to be updated
                if cleaned_publication != publication:
                    # Update the front matter
                    updated_front_matter_lines = []
                    for line in front_matter_text.strip().split('\n'):
                        if line.startswith('publication:'):
                            # Preserve the original quoting style
                            if '"' in line:
                                updated_front_matter_lines.append(f'publication: "{cleaned_publication}"')
                            elif "'" in line:
                                updated_front_matter_lines.append(f"publication: '{cleaned_publication}'")
                            else:
                                updated_front_matter_lines.append(f'publication: {cleaned_publication}')
                        else:
                            updated_front_matter_lines.append(line)
                    
                    new_front_matter = '\n'.join(updated_front_matter_lines)
                    
                    # Reconstruct the file content
                    new_content = f"---\n{new_front_matter}\n---{body}"
                    
                    print(f"File: {file_path}")
                    print(f"  Original publication: {publication}")
                    print(f"  Cleaned publication: {cleaned_publication}")
                    
                    if not dry_run:
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(new_content)
                        print("  ✓ File updated")
                    else:
                        print("  ⚠ Dry run - no changes made")
                    
                    return True  # Indicates file was updated
                else:
                    if dry_run:
                        print(f"File: {file_path}")
                        print(f"  Publication: {publication}")
                        print(f"  ✓ Publication name already clean")
                    return False  # Indicates file did not need update
            else:
                print(f"File: {file_path}")
                print(f"  ⚠ No publication field found")
                return False
        else:
            print(f"File: {file_path}")
            print(f"  ⚠ Invalid front matter format")
            return False
    else:
        print(f"File: {file_path}")
        print(f"  ⚠ No front matter found")
        return False

def process_all_publications(base_dir, dry_run=False):
    """Process all index.md files in publication subdirectories."""
    base_path = Path(base_dir)
    publication_dir = base_path / "content" / "publication"
    
    if not publication_dir.exists():
        print(f"Publication directory not found: {publication_dir}")
        return
    
    total_count = 0
    update_count = 0
    
    print(f"\n{'DRY RUN - SHOWING POTENTIAL CHANGES' if dry_run else 'UPDATING FILES'}")
    print("=" * 80)
    
    for pub_folder in publication_dir.iterdir():
        if pub_folder.is_dir():
            index_file = pub_folder / "index.md"
            if index_file.exists():
                result = update_publication_name(index_file, dry_run)
                if result:
                    update_count += 1
                total_count += 1
                print("-" * 80)
    
    print("\nSUMMARY")
    print("=" * 80)
    print(f"Total publication files processed: {total_count}")
    print(f"Files with updated publication names: {update_count}")
    if dry_run and update_count > 0:
        print(f"\nRun without --dry-run to apply these changes.")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Clean publication names by removing numbers and dashes")
    parser.add_argument("--base-dir", default=".", help="Base directory of the website (default: current directory)")
    parser.add_argument("--dry-run", action="store_true", help="Don't actually modify files, just show what would be changed")
    
    args = parser.parse_args()
    
    process_all_publications(args.base_dir, args.dry_run)