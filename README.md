# Python Practice Projects

My Python practice programs and beginner projects.

## Repository structure

```text
.
├── practice/
│   └── basics/             # Small command-line practice programs
└── projects/
    └── unit-converter/     # Streamlit web app
```

## Projects

### Unit Converter

A Streamlit app for converting distance, weight, and temperature units.

Run it locally from the repository root:

```powershell
.\.venv\Scripts\python.exe -m streamlit run projects/unit-converter/main.py
```

To deploy it on Streamlit Community Cloud, select this entrypoint file:

```text
projects/unit-converter/main.py
```

The required Streamlit dependency is listed in
`projects/unit-converter/requirements.txt`.

## Practice programs

- Mom's Pocket Money
- Number Reverser
- Number Comparator
- Voting Eligibility Checker
