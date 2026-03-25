import os
import re

VAULT_DIR = "/opt/home_data/Documents/GitHub/Second Brain/20 - Areas"

def get_template(is_lingo, folder_name, title):
    if is_lingo:
        language = "german" if "German" in folder_name else "spanish"
        level = "A2" if "Intermediate" in folder_name else "B2" if "Expert" in folder_name else "A1"
        return f"""# Language Note: {title}
Language: #lingo/{language} 
Level: #level/{level} 

## 📖 New Vocabulary
| Word/Phrase | Meaning | Example Sentence |
| ----------- | ------- | ---------------- |
|             |         |                  |

## ⚖️ Grammar / Structure
- **Rule**: {title} structure rules go here.
- **Example**: 

## 🗣️ Common Phrases & Idioms
- 

## 🎧 Audio/Visual Resources
- [Link to video/audio]

## 🧠 Questions & Flashcards
- **Q**: Key concept of {title}?
  - **A**: 

## ✍️ Practice / Sentences
- [ ] Practice {title} concepts.

## 📅 Review Schedule
- [ ] Review 1 (Tomorrow)
- [ ] Review 2 (In 1 Week)
"""
    else:
        subject = re.search(r'20 - Areas/([^/]+)', folder_name).group(1).lower().replace(' ', '-')
        return f"""# Study Note: {title}
Subject: #study/{subject} 
Status: #study/learning 

## 📖 Key Concepts & Definitions
- **{title}**: Core definitions and mental models.

## 📝 Detailed Notes
### Introduction to {title}
- Key principles and theoretical background.
- How it integrates into the broader {subject} ecosystem.

### Tools & Techniques
- Common tools used in this domain.
- Best practices and methodologies.

## 🧠 Questions & Flashcards
- **Q**: What is the primary goal of {title}?
  - **A**: To be added during study.

## ✍️ Practice / Application
- [ ] Complete a practical lab or exercise related to {title}.

## 📅 Review Schedule
- [ ] First Review (Today)
- [ ] Second Review (Tomorrow)
- [ ] Final Review (Next Week)
"""

def process_directories():
    roadmaps = {}
    for root, dirs, files in os.walk(VAULT_DIR):
        # Identify roadmap files
        for f in files:
            if "Roadmap" in f and f.endswith(".md"):
                roadmaps[root] = os.path.join(root, f)

    for root, dirs, files in os.walk(VAULT_DIR):
        if not dirs and not files:
            # Empty directory
            folder_name = os.path.basename(root)
            # Remove the number prefix if it exists
            title = re.sub(r'^\d+\s*-\s*', '', folder_name)
            is_lingo = "Lingo" in root
            content = get_template(is_lingo, root, title)
            
            file_path = os.path.join(root, f"{title}.md")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Created: {file_path}")
            
            # Find the closest roadmap to append the link
            closest_roadmap_dir = root
            while closest_roadmap_dir != VAULT_DIR:
                closest_roadmap_dir = os.path.dirname(closest_roadmap_dir)
                if closest_roadmap_dir in roadmaps:
                    roadmap_file = roadmaps[closest_roadmap_dir]
                    relative_path = os.path.relpath(file_path, "/opt/home_data/Documents/GitHub/Second Brain").replace('\\', '/')
                    link_text = f"\n- [[{relative_path}|{title}]]"
                    with open(roadmap_file, 'a', encoding='utf-8') as rf:
                        rf.write(link_text)
                    print(f"Appended to roadmap: {roadmap_file}")
                    break

if __name__ == "__main__":
    process_directories()
