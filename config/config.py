class config:
    # Basic configuration: If you are unsure how to obtain the Bot ID, simply start the bot and it will be logged in the console.
    prefix = '!'
    botID = '6e7028c15394ab30991973799bb04f6e4b94227811e929b0cf27365ffb738bf6'
    botName = 'Pagenssmokebot'
    ownerName = '695b3b55d2aef312b814781c'
    roomName = '𝔉𝔦𝔫𝔡 𝔞 𝔰𝔪𝔬𝔨𝔢 𝔅𝔲𝔡𝔡𝔶 🍃'
    coordinates = {
        'x': 18.0,
        'y': 0.25,
        'z': 14.5,
        'facing': 'FrontRight'
    }


class loggers:
    # The following settings are related to events. Each event log can be enabled or disabled. Note that turning these off will not affect their usage in the game.
    SessionMetadata = True
    messages = True
    whispers = True
    joins = True
    leave = True
    tips = True
    emotes = False
    reactions = False
    userMovement = False


class messages:
    # The following are optional and serve as a basic usage example for calling messages and replacing variables.
    invalidPosition = "Your position could not be determined."
    invalidPlayer = "{user} is not in the room."
    invalidUser = "User {user} is not found."
    invalidUsage = "Usage: {prefix}{commandName}{args}"
    invalidUserFormat = "Invalid user format. Please use '@username'."


class permissions:
    # You can add as many IDs as you want, for example: ['id1', 'id2'].
    owners = ['695b3b55d2aef312b814781c']
    moderators = ['695b3b55d2aef312b814781c']


class authorization:
    # To obtain your token, visit https://highrise.game/ and log in. Then, go to the settings and create a new bot. Accept the terms and generate a token.
    # To obtain your room ID, go to the game and navigate to the top right corner where the player list is displayed. Click on "Share this room" and copy the ID.
    room = '696304510df902a35e522aa7'
    token = '6e7028c15394ab30991973799bb04f6e4b94227811e929b0cf27365ffb738bf6'
