@echo off
echo Abrindo Streamlit...
start "" streamlit run "C:\Users\Gabriel\Downloads\Workana-automatizador-propostas\workana_proposal_generator.py"
timeout /t 5
echo Abrindo túnel para Streamlit na porta 8501...
ssh -i %USERPROFILE%\.ssh\id_rsa -R 80:localhost:8501 gabriel@localhost.run
pause
