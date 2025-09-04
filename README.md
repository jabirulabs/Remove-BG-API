Run API uvicorn main:app --reload --host 0.0.0.0 --port 8080

You’ll now have 3 endpoints:

POST /enhance/ → Just enhances image (sharpness, contrast, brightness). POST /remove-bg/ → Just removes background. POST /process/ → Runs full pipeline (enhance + remove background).
