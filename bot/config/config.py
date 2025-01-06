from pydantic_settings import BaseSettings, SettingsConfigDict
from bot.utils import logger
import sys

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int = 1234
    API_HASH: str = 'abcd'
    
    SUPPORT_AUTHOR: bool = True
    
    AUTO_SIGN_IN: bool = True
    
    AUTO_TASK: bool = True
    CHEST_SLEEP: bool = True
    AUTO_JOIN_CHANNELS: bool = True
    AUTO_QUIZ: bool = True
    
    AUTO_UPGRADE: bool = True
    SAVE_FEED: int = 1000
    
    AUTO_FEED: bool = True
    
    SLEEP_TIME: list[int] = [2700, 4200]
    START_DELAY: list[int] = [5, 100]
    
    REF_KEY: str = 'ref1178697351'
    IN_USE_SESSIONS_PATH: str = 'bot/config/used_sessions.txt'
    
    NIGHT_MODE: bool = False
    NIGHT_TIME: list[int] = [0, 7] #TIMEZONE = UTC, FORMAT = HOURS, [start, end]
    NIGHT_CHECKING: list[int] = [3600, 7200]
    
    SAVE_RESPONSE_DATA: bool = True
    MAX_REQUEST_RETRY: int = 3
    TRACK_BOT_UPDATES: bool = False
    FLOOD_WAIT: bool = False

settings = Settings()

if settings.API_ID == 1234 and settings.API_HASH == 'abcd':
    sys.exit(logger.info("<r>Please edit API_ID and API_HASH from .env file to continue.</r>"))

if settings.API_ID == 1234:
    sys.exit(logger.info("Please edit API_ID from .env file to continue."))

if settings.API_HASH == 'abcd':
    sys.exit(logger.info("Please edit API_HASH from .env file to continue."))