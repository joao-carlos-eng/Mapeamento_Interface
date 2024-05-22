python -m venv .venv
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install --upgrade poetry
pip install -r requirements.txt
echo.
echo Tudo foi instalado com sucesso
pause