# ksalol-chan alpha

![Ksalol-sama](ksalol-sama.png)  
*don't worry, she will comfort you ~~ just let her...*  

Setup:

1. **Requirements:**
   - **Windows Powershell:**  
     `python.exe -m pip install --upgrade pip ; pip install -r requirements.txt`  
   - **Linux:**  
     `source .venv/bin/activate && python -m pip install --upgrade pip && pip install -r requirements.txt`  

2. **Initiate token.txt:**
   - **Windows Powershell:**  
     `New-Item -ItemType File -Name token.txt ; Set-Content -Path token.txt -Value "your_token_here"`  
   - **Linux:**  
     `echo "your_token_here" > token.txt`

3. **Running:**
   - **Windows Powershell:**  
     `python.exe .\ksalol-chan-dev.py`  
   - **Linux:**  
     `python ./ksalol-chan-dev.py`
