echo "Creating virtual environment..."
python -m venv env

echo "Installing requirements..."
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
Pause