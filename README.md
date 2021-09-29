# Discord Bot
A bot to play music *definitely not from YouTube*

## Running the Bot
1. Install Python 3. (Tested on Python 3.9)
2. Create virtual environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a Discord bot and add the token key to file name `TOKEN.py` the inside of the file should look like this
```python
TOKEN="<discord bot token>"
```

5. Run script
```bash
python main.py
```

## TODO
* Parse input
* Join Voice Channels
* Play music
