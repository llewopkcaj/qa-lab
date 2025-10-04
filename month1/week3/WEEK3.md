# Week 3 Summary — Files, CSV, JSON

## 📖 Pages Read
- W3Schools: File Open, Read/Write, Close  
- W3Schools: CSV module basics (`DictReader`, `DictWriter`)  
- W3Schools: JSON module (`dump`, `load`)  
- Python Docs: `with open()`, context managers, exceptions  

---

## 📝 Exercises Completed
- **File Basics** (`file_basics.py`) → wrote/ read text with `with open`.  
- **CSV Contacts** (`csv_contacts.py`) → created & read a contacts CSV using `DictWriter`/`DictReader`.  
- **JSON Profile** (`json_profile.py`) → saved & loaded a profile with lists inside.  
- **File Renamer Project** (`file_renamer.py`) → renamed multiple files in a folder using `os.listdir`, `enumerate`, and `os.rename`.  
- **JSON → CSV Converter Project** (`json_to_csv.py`) → transformed JSON records into CSV rows.  
- **Practice Sets** (`day6.py`) → loop practice & file handling drills.  

---

## 💻 Key Snippets I’m Proud Of

### File I/O with Context Manager
```python
with open("hello.txt", "w") as f:
    f.write("Hello, QA Automation!")
```
**Pattern:** always use `with open(...)` → ensures the file closes automatically.  

---

### Writing Contacts to CSV
```python
with open("contacts.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Email", "Tag"])
    writer.writeheader()
    writer.writerows(data)
```
**Pattern:** `DictWriter` → header first, then `writerows()`.  

---

### Renaming Files in a Loop
```python
for index, filename in enumerate(files, start=1):
    new_filename = f"file{index}.txt"
    os.rename(os.path.join(folder_path, filename),
              os.path.join(folder_path, new_filename))
```
**Pattern:** `enumerate` gives you both counter + value, perfect for file renaming.  

---

## ✅ End of Week 3
- Learned file handling basics (read/write, context managers).  
- Practiced CSV and JSON data formats.  
- Built small but **real automation projects** (renamer, converter).  
- Pushed all work to GitHub (`qa-month1/week3`).  
