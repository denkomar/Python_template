@echo off
setlocal enabledelayedexpansion

set "VIRTUAL_ENV=.\venv"
set "PYTHON_SCRIPT=main.py"

REM Перебираем все папки в текущей директории
for /d %%D in (*) do (
    REM Проверяем наличие Python
    if exist "%%D\Scripts\python.exe" (
        set "VIRTUAL_ENV=.\%%D"
    )
)


if not exist %VIRTUAL_ENV%\Scripts\activate.bat (
    python -m venv venv
	
	call %VIRTUAL_ENV%\Scripts\activate
	
	pip install -r requirements.txt

	python %PYTHON_SCRIPT%

	deactivate
) else (
	%VIRTUAL_ENV%\Scripts\pip.exe install -r requirements.txt
	
	%VIRTUAL_ENV%\Scripts\python.exe %PYTHON_SCRIPT%
)


