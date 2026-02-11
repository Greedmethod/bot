# Highrise PY Bot Template

> **This python template helps you get started with your first Highrise Bot.**

## **⚙️ Installation** 
```
pip install highrise-bot-sdk==23.1.0b10
```

## **✨ Features**

- Easy-to-use interface.
- Beginner-friendly design.
- Advanced command and event handlers.
- Customizable permissions and cooldowns for commands.
- Flexible configuration file for easy modifications.




## **🖥️ Run on Ubuntu 22.04 VPS**

1. Clone this repository on your VPS:
```bash
git clone <your-repo-url> highrise-bot
cd highrise-bot
```

2. Configure your bot credentials in `config/config.py` and permissions in `config/permissions.json`.

3. Run the automated installer as root (creates a dedicated `highrisebot` user, virtualenv, and systemd service):
```bash
sudo bash deploy/install_ubuntu.sh
```

4. Start and inspect the service:
```bash
sudo systemctl start highrise-bot.service
sudo systemctl status highrise-bot.service
```

5. Check logs:
```bash
sudo journalctl -u highrise-bot.service -f
```

### Manual setup (optional)
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## **🎐 Usage**
To start the bot:
```
python main.py
```

PATH: config/config.py:
```py
class config:
    # Basic configuration: If you are unsure how to obtain the Bot ID, simply start the bot and it will be logged in the console.
    prefix = '/'
    botID = 'change-me'
    botName = 'change-me'
    ownerName = 'change-me'
    roomName = 'change-me'
    coordinates = {
        'x': 0,
        'y': 0,
        'z': 0,
        'facing': 'FrontRight'
    }

class authorization:
    # To obtain your token, visit https://highrise.game/ and log in. Then, go to the settings and create a new bot. Accept the terms and generate a token.
    # To obtain your room ID, go to the game and navigate to the top right corner where the player list is displayed. Click on "Share this room" and copy the ID.
    room = 'change-me'
    token = 'change-me'
```
PATH: config/permissions.json
```json
{
    "permissions": [
        {
            "user_id": "change-me",
            "username": "optional-legacy-fallback",
            "permissions": [
                "emote"
            ]
        }
    ]
}
```

`user_id` is the primary key used for permission resolution. `username` is kept only for backward compatibility when `user_id` is missing.

## Note

While you have the freedom to modify this package to suit your needs, please refrain from claiming it as your own. Let's respect the efforts put into creating and sharing this resource.