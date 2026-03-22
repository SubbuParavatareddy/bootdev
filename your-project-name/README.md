# your-project-name

Minimal instructions to run the example that loads an API key from `.env`.

Prerequisites
- Python 3.12

Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install python-dotenv==1.1.0 google-genai==1.12.1
```

Create a `.env` file in the project root with:

```
GEMINI_API_KEY=your_api_key_here
```

Run
```bash
python your-project-name/main.py
```

You should see the value of `GEMINI_API_KEY` printed.
