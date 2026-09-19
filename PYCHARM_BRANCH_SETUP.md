# PyCharm + personal Git branch setup

Suggested branch: `feature/mineru-improved-ui`

## 1. Start from your own repository

Open your existing Asepsis repository in PyCharm. Do not create a new Git repository inside it.

In the PyCharm terminal:

```bash
git status
git switch main
git pull
git switch -c feature/mineru-improved-ui
```

The working tree should be clean before copying this version in.

## 2. Copy this source onto the new branch

Extract this package somewhere outside your repository, then copy its contents into the root of your existing repository and allow matching source files to be overwritten. Do not copy any `.git` directory from another repository.

Then inspect the result:

```bash
git status
git diff --stat
```

## 3. Create a Python environment

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

In PyCharm choose `.venv` as the project interpreter.

## 4. Run in PyCharm

Create a Python Run Configuration:

- Script path: `<repo>\run.py`
- Parameters: `--data-dir data`
- Working directory: repository root
- Python interpreter: `.venv`

Run it and open:

```text
http://127.0.0.1:8765
```

For MinerU dataset discovery, place local source files under:

```text
data/<document>/auto/
    <document>_origin.pdf
    <document>_model.json
```

The package intentionally does not include the large document corpus.

## 5. Verify before committing

```bash
python -m pytest -q
node --check annotation_tool/static/app.js
```

## 6. Commit and push only the new branch

```bash
git add -A
git commit -m "Add MinerU workflow with layered OCR UI and autosave"
git push -u origin feature/mineru-improved-ui
```

Your `main` branch is unchanged until you explicitly merge the feature branch.
