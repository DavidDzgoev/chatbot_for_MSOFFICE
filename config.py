import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 1234

    APP_ID = os.environ.get("MicrosoftAppId", "1c64626d-b922-4e81-908c-196a8051365d")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "AtLeastSixteenCharacters_0")

    # APP_ID = os.environ.get("MicrosoftAppId", "")
    # APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
