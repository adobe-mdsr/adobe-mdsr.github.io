#!/usr/bin/env python3
import os
import re
import subprocess
import tempfile
from pathlib import Path
import requests
import json

def extract_year_from_publication(publication):
    """Extract year from publication string like 'WACV-25', 'WACV-2025', or 'AAAI 24'."""
    # Try to find a 4-digit year
    full_year_match = re.search(r'20(\d{2})', publication)
    if full_year_match:
        return f"20{full_year_match.group(1)}"
    
    # Try to find a 2-digit year with hyphen (e.g., WACV-25)
    short_year_match = re.search(r'-(\d{2})', publication)
    if short_year_match:
        return f"20{short_year_match.group(1)}"
    
    # Try to find a 2-digit year after conference name (e.g., AAAI 24)
    conf_year_match = re.search(r'[A-Z]+\s+(\d{2})(?:\s|$)', publication)
    if conf_year_match:
        return f"20{conf_year_match.group(1)}"
    
    # If no year found, return None
    return None

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

def generate_tags_from_abstract(abstract, max_tags=5):
    """Generate relevant tags from the abstract using local NLP techniques."""
    return extract_keywords_fallback(abstract, max_tags)

def extract_keywords_fallback(text, max_keywords=5):
    """Extract keywords from text using simple NLP techniques."""
    # Remove common stop words
    stop_words = {'a', 'an', 'the', 'and', 'or', 'but', 'if', 'because', 'as', 'what',
                 'when', 'where', 'how', 'this', 'that', 'these', 'those', 'then',
                 'to', 'of', 'for', 'with', 'in', 'on', 'at', 'from', 'by', 'about',
                 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
                 'do', 'does', 'did', 'can', 'could', 'will', 'would', 'should', 'may',
                 'might', 'must', 'we', 'our', 'ours', 'us', 'i', 'my', 'mine', 'me',
                 'he', 'his', 'him', 'she', 'her', 'hers', 'it', 'its', 'they', 'them',
                 'their', 'theirs', 'you', 'your', 'yours', 'using', 'used', 'use',
                 'paper', 'propose', 'proposed', 'method', 'methods', 'approach', 'approaches',
                 'result', 'results', 'show', 'shows', 'shown', 'demonstrate', 'demonstrates',
                 'demonstrated', 'present', 'presents', 'presented', 'introduce', 'introduces',
                 'introduced', 'work', 'works', 'study', 'studies', 'research', 'researches'}
    
    # First try to extract multi-word phrases (likely to be more specific)
    # Look for capitalized phrases which often indicate technical terms
    phrases = re.findall(r'\b([A-Z][a-z]+(?:\s+[A-Za-z][a-z]+){1,3})\b', text)
    
    # Also look for phrases with hyphens or technical terms
    technical_phrases = re.findall(r'\b([A-Za-z][a-z]*(?:-[A-Za-z][a-z]*)+)\b', text)
    phrases.extend(technical_phrases)
    
    # Look for phrases with common technical patterns
    tech_patterns = [
        r'\b([A-Za-z][a-z]*\s+[Ll]earning)\b',
        r'\b([A-Za-z][a-z]*\s+[Nn]etworks?)\b',
        r'\b([A-Za-z][a-z]*\s+[Mm]odels?)\b',
        r'\b([A-Za-z][a-z]*\s+[Aa]nalysis)\b',
        r'\b([A-Za-z][a-z]*\s+[Rr]ecognition)\b',
        r'\b([A-Za-z][a-z]*\s+[Pp]rocessing)\b',
        r'\b([A-Za-z][a-z]*\s+[Gg]eneration)\b',
        r'\b([A-Za-z][a-z]*\s+[Dd]etection)\b',
        r'\b([A-Za-z][a-z]*\s+[Ss]egmentation)\b',
        r'\b([A-Za-z][a-z]*\s+[Cc]lassification)\b',
        r'\b([A-Za-z][a-z]*\s+[Pp]rediction)\b',
        r'\b([A-Za-z][a-z]*\s+[Tt]racking)\b',
        r'\b([A-Za-z][a-z]*\s+[Bb]ehavior)\b',
        r'\b([A-Za-z][a-z]*\s+[Uu]nderstanding)\b',
        r'\b([Dd]eep\s+[A-Za-z][a-z]*)\b',
        r'\b([Mm]achine\s+[A-Za-z][a-z]*)\b',
        r'\b([Nn]eural\s+[A-Za-z][a-z]*)\b',
        r'\b([Cc]omputer\s+[A-Za-z][a-z]*)\b',
        r'\b([Aa]rtificial\s+[A-Za-z][a-z]*)\b',
        r'\b([Hh]uman\s+[A-Za-z][a-z]*)\b',
        r'\b([Bb]ehavior\s+[A-Za-z][a-z]*)\b',
        r'\b([Ss]emantic\s+[A-Za-z][a-z]*)\b',
        r'\b([Tt]emporal\s+[A-Za-z][a-z]*)\b',
        r'\b([Ss]patial\s+[A-Za-z][a-z]*)\b',
        r'\b([Mm]ultimodal\s+[A-Za-z][a-z]*)\b',
        r'\b([Rr]eal-[Tt]ime\s+[A-Za-z][a-z]*)\b',
    ]
    
    for pattern in tech_patterns:
        tech_terms = re.findall(pattern, text)
        phrases.extend(tech_terms)
    
    # Count phrase frequencies
    phrase_freq = {}
    for phrase in phrases:
        phrase_lower = phrase.lower()
        if len(phrase) > 5 and not any(word.lower() in stop_words for word in phrase.split()):
            phrase_freq[phrase] = phrase_freq.get(phrase, 0) + 1
    
    # Get single words as backup
    words = re.findall(r'\b[A-Za-z][A-Za-z-]+\b', text)
    word_freq = {}
    
    # Count word frequencies, ignoring stop words and short words
    for word in words:
        word_lower = word.lower()
        if len(word) > 5 and word_lower not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Combine phrases and words, prioritizing phrases
    combined_freq = {**phrase_freq, **word_freq}
    
    # Get top terms by frequency
    top_terms = sorted(combined_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Deduplicate (remove terms that are substrings of others)
    unique_terms = []
    for term, freq in top_terms:
        if len(unique_terms) >= max_keywords:
            break
            
        # Check if this term is a substring of any existing term
        is_substring = False
        for existing_term in unique_terms:
            if term.lower() in existing_term.lower() and term.lower() != existing_term.lower():
                is_substring = True
                break
                
        if not is_substring:
            unique_terms.append(term)
    
    # Format keywords (capitalize first letter of each word)
    keywords = []
    for term in unique_terms:
        words = term.split()
        capitalized = ' '.join(word.capitalize() for word in words)
        keywords.append(capitalized)
    
    # If we still don't have enough keywords, add some common academic fields
    if len(keywords) < 3:
        common_fields = ["Computer Science", "Machine Learning", "Artificial Intelligence", 
                         "Data Science", "Computer Vision", "Natural Language Processing",
                         "Behavior Analysis", "Human-Computer Interaction", "Robotics"]
        
        # Try to guess the field based on keywords in the abstract
        field_keywords = {
            "Computer Vision": ["image", "vision", "object", "detection", "segmentation", "camera", 
                               "visual", "recognition", "scene", "tracking", "video", "face", 
                               "pose", "depth", "3d", "reconstruction", "optical", "flow"],
            
            "Natural Language Processing": ["language", "text", "nlp", "linguistic", "sentiment", 
                                          "translation", "speech", "dialogue", "conversation", 
                                          "chatbot", "word", "sentence", "document", "corpus", 
                                          "token", "parsing", "grammar", "semantic", "syntax"],
            
            "Machine Learning": ["learning", "model", "training", "prediction", "classifier", 
                                "regression", "supervised", "unsupervised", "semi-supervised", 
                                "feature", "parameter", "hyperparameter", "optimization", 
                                "gradient", "backpropagation", "loss", "accuracy", "precision", 
                                "recall", "f1", "cross-validation", "overfitting"],
            
            "Artificial Intelligence": ["ai", "intelligence", "agent", "reasoning", "knowledge", 
                                      "cognitive", "planning", "decision", "expert", "system", 
                                      "logic", "inference", "symbolic", "reasoning", "constraint", 
                                      "satisfaction", "search", "heuristic"],
            
            "Data Science": ["data", "analysis", "statistics", "mining", "visualization", 
                           "analytics", "big data", "dataset", "database", "sql", "nosql", 
                           "warehouse", "etl", "dashboard", "bi", "business intelligence", 
                           "exploratory", "descriptive", "predictive", "prescriptive"],
            
            "Robotics": ["robot", "autonomous", "navigation", "manipulation", "control", 
                        "actuator", "sensor", "kinematics", "dynamics", "path", "planning", 
                        "slam", "localization", "mapping", "gripper", "arm", "drone", "uav", 
                        "ugv", "swarm", "humanoid"],
            
            "Behavior Analysis": ["behavior", "behavioural", "psychology", "cognitive", 
                                "human", "animal", "social", "interaction", "activity", 
                                "action", "gesture", "emotion", "affect", "attention", 
                                "gaze", "movement", "motion", "trajectory", "pattern", 
                                "habit", "routine", "anomaly", "abnormal", "normal"],
            
            "Human-Computer Interaction": ["hci", "interface", "user", "experience", "ux", 
                                         "ui", "usability", "accessibility", "interaction", 
                                         "design", "ergonomic", "human-centered", "touch", 
                                         "gesture", "augmented", "virtual", "reality", "ar", 
                                         "vr", "mixed", "wearable"],
            
            "Deep Learning": ["neural", "network", "deep", "cnn", "rnn", "lstm", "gru", 
                            "transformer", "attention", "self-attention", "bert", "gpt", 
                            "vae", "gan", "autoencoder", "embedding", "fine-tuning", 
                            "transfer", "pretrained", "convolutional", "recurrent"],
            
            "Reinforcement Learning": ["reinforcement", "rl", "reward", "policy", "agent", 
                                     "environment", "state", "action", "q-learning", "dqn", 
                                     "a3c", "ppo", "td", "temporal", "difference", "markov", 
                                     "mdp", "pomdp", "exploration", "exploitation"],
            
            "Computer Graphics": ["graphics", "rendering", "shader", "texture", "mesh", 
                                "animation", "modeling", "simulation", "ray", "tracing", 
                                "rasterization", "illumination", "shadow", "reflection", 
                                "refraction", "global", "local", "particle", "fluid"],
            
            "Bioinformatics": ["bio", "biological", "genomic", "protein", "dna", "rna", 
                             "sequence", "alignment", "phylogenetic", "evolution", 
                             "molecular", "cell", "tissue", "organism", "species", 
                             "taxonomy", "classification", "medical", "clinical", "health"]
        }
        
        for field, indicators in field_keywords.items():
            if any(indicator in text.lower() for indicator in indicators) and field not in keywords:
                keywords.append(field)
                if len(keywords) >= max_keywords:
                    break
    
    return keywords[:max_keywords]

def update_front_matter(front_matter, new_date, new_tags=None):
    """Update front matter with new date values and tags if provided."""
    updated_lines = []
    date_updated = False
    publish_date_updated = False
    tags_updated = False
    
    in_tags_section = False
    
    for line in front_matter.strip().split('\n'):
        if line.startswith('date:'):
            updated_lines.append(f'date: "{new_date}"')
            date_updated = True
        elif line.startswith('publishDate:'):
            updated_lines.append(f'publishDate: "{new_date}"')
            publish_date_updated = True
        elif line.startswith('tags:'):
            if new_tags:
                updated_lines.append('tags:')
                for tag in new_tags:
                    updated_lines.append(f'- {tag}')
                tags_updated = True
                in_tags_section = True
            else:
                updated_lines.append(line)
                in_tags_section = True
        elif in_tags_section and line.startswith('- '):
            if not new_tags:  # Only add existing tags if we're not replacing them
                updated_lines.append(line)
        elif in_tags_section and not line.startswith('- '):
            in_tags_section = False
            updated_lines.append(line)
        else:
            updated_lines.append(line)
    
    # Add date fields if they don't exist
    if not date_updated:
        updated_lines.append(f'date: "{new_date}"')
    if not publish_date_updated:
        updated_lines.append(f'publishDate: "{new_date}"')
    
    # Add tags if they don't exist and we have new ones
    if not tags_updated and new_tags:
        updated_lines.append('tags:')
        for tag in new_tags:
            updated_lines.append(f'- {tag}')
    
    return '\n'.join(updated_lines)

def should_update_tags(front_matter_text):
    """Check if tags should be updated (only if they contain 'Source Themes')."""
    in_tags_section = False
    has_source_themes = False
    
    for line in front_matter_text.strip().split('\n'):
        if line.startswith('tags:'):
            in_tags_section = True
        elif in_tags_section and line.startswith('- '):
            if 'Source Themes' in line:
                has_source_themes = True
        elif in_tags_section and not line.startswith('- '):
            in_tags_section = False
    
    return has_source_themes

def update_publication_dates(file_path, dry_run=False):
    """Update date and publishDate in the front matter based on publication info."""
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
            
            # Extract year from publication
            year = extract_year_from_publication(publication)
            
            # Check if we need to update tags
            update_tags = should_update_tags(front_matter_text)
            new_tags = None
            
            if update_tags:
                abstract = front_matter.get('abstract', '')
                if abstract:
                    new_tags = generate_tags_from_abstract(abstract)
            
            if year:
                # Create new date string (January 1st of the extracted year)
                new_date = f"{year}-01-01T00:00:00Z"
                
                # Check if dates are already correct
                current_date = front_matter.get('date', '')
                current_publish_date = front_matter.get('publishDate', '')
                
                needs_update = not (current_date.startswith(f"{year}-") and 
                                   current_publish_date.startswith(f"{year}-")) or update_tags
                
                if needs_update:
                    # Update the front matter
                    new_front_matter = update_front_matter(front_matter_text, new_date, new_tags)
                    
                    # Reconstruct the file content
                    new_content = f"---\n{new_front_matter}\n---{body}"
                    
                    print(f"File: {file_path}")
                    print(f"  Publication: {publication}")
                    print(f"  Current date: {current_date}")
                    print(f"  Current publishDate: {current_publish_date}")
                    print(f"  Extracted year: {year}")
                    print(f"  New date to be set: {new_date}")
                    
                    if update_tags:
                        print(f"  Updating tags: {new_tags}")
                    
                    if not dry_run:
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(new_content)
                        print("  ✓ File updated")
                    else:
                        print("  ⚠ Dry run - no changes made")
                    
                    return True  # Indicates file needed update
                else:
                    if dry_run:
                        print(f"File: {file_path}")
                        print(f"  Publication: {publication}")
                        print(f"  Current date: {current_date}")
                        print(f"  Current publishDate: {current_publish_date}")
                        print(f"  ✓ Dates already correct (year: {year})")
                    return False  # Indicates file did not need update
            else:
                print(f"File: {file_path}")
                print(f"  Publication: {publication}")
                print(f"  ⚠ Could not extract year from publication")
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
                result = update_publication_dates(index_file, dry_run)
                if result:
                    update_count += 1
                total_count += 1
                print("-" * 80)
    
    print("\nSUMMARY")
    print("=" * 80)
    print(f"Total publication files processed: {total_count}")
    print(f"Files with incorrect dates or tags: {update_count}")
    if dry_run and update_count > 0:
        print(f"\nRun without --dry-run to apply these changes.")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Update publication dates and tags based on content")
    parser.add_argument("--base-dir", default=".", help="Base directory of the website (default: current directory)")
    parser.add_argument("--dry-run", action="store_true", help="Don't actually modify files, just show what would be changed")
    parser.add_argument("--api-key", help="Hugging Face API key for tag generation")
    
    args = parser.parse_args()
    
    # If API key is provided via command line, use it
    if args.api_key:
        # Update the API key in the generate_tags_from_abstract function
        generate_tags_from_abstract.__globals__['headers'] = {"Authorization": f"Bearer {args.api_key}"}
    
    process_all_publications(args.base_dir, args.dry_run)