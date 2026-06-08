# Brain Tumor Detection

Project scaffold for brain tumor classification with preprocessing, training, evaluation, and Flask inference app.

## Structure
- `dataset/` raw, processed, and sample images
- `notebooks/` data prep, EDA, and model training notebooks
- `src/` reusable Python modules
- `model/` trained model artifacts
- `static/` CSS, uploads, and images
- `templates/` Flask HTML templates
- `screenshots/` app and training screenshots

## Setup
1. Create a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your trained model at `model/brain_tumor_model.pth`.
4. Run the app:
   ```bash
   python app.py
   ```
