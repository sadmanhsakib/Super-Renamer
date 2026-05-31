> **⚠️ ARCHIVED PROJECT**  
> This project is archived and now part of my [automation-toolbox](https://github.com/sadmanhsakib/automation-toolbox) repository.

# recursive-renamer

**recursive-renamer** is a robust Python utility designed to automate the process of mass-renaming files across deeply nested directory structures. It streamlines file organization by performing bulk character replacements and enforcing consistent naming conventions (lowercase) in a single pass.

## 🚀 Purpose

Managing file names in large datasets or extensive project directories can be tedious and error-prone. **recursive-renamer** solves this by allowing users to traverse an entire directory tree and standardize filenames instantly. It is particularly useful for developers, data scientists, and system administrators who need to sanitize inputs or organize file systems.

## 🌟 Key Features

- **Recursive Traversal**: Automatically dives into every subfolder within the target directory, ensuring no file is left behind.
- **Bulk Character Replacement**: Swaps specific characters (e.g., replacing spaces with underscores or hyphens) across thousands of files.
- **Automatic Standardization**: Converts all filenames to **lowercase**, eliminating case-sensitivity issues across different operating systems (Windows/Linux/macOS).
- **Execution Metrics**: Provides a summary of the total files scanned and the number of files renamed.

## 💡 Real-World Use Case

### Scenario: Web Asset Sanitization
When deploying a static website or uploading assets to cloud storage (like AWS S3), filenames with spaces or mixed casing can cause broken links or 404 errors.

**Example:**
You have a folder of images for a blog:
- `Images/My Vacation/Beach Photo.JPG`
- `Images/My Vacation/Sunset at the Pier.PNG`

Using **recursive-renamer**, you can replace " " (space) with "-" (hyphen). The script will automatically lowercase the names as well, transforming them into web-safe URLs:
- `Images/My Vacation/beach-photo.jpg`
- `Images/My Vacation/sunset-at-the-pier.png`

This ensures your assets are URL-friendly and consistent across all platforms.

## 🛠️ Prerequisites

- Python 3.x
- `python-dotenv` library

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/recursive-renamer.git
   cd recursive-renamer
   ```

2. **Install Dependencies**
   ```bash
   pip install python-dotenv
   ```

## ⚙️ Configuration

1. Create a `.env` file in the root directory of the project.
2. Add the `FOLDER_PATH` variable pointing to the directory you want to process.

   **Example `.env` file:**
   ```env
   FOLDER_PATH="C:\Users\Name\Documents\MyFiles"
   ```

## 💻 Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Follow the interactive prompts:
   - **Enter the character you want to change**: (e.g., press `Space`)
   - **Enter the character you want to changed to**: (e.g., type `-`)

3. The script will process the files and output the results:
   ```text
   File Count: 150
   Rename Count: 42
   ```

## ⚠️ Note
This script modifies filenames directly on your file system. It is recommended to **backup your data** before running bulk operations on critical directories.

## 🤝 Contributing

This project is solely developed and maintained by **[Sadman Sakib](https://github.com/sadmanhsakib)**.
