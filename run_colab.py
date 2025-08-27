import os
import sys

# Try importing configs from colab_config.py
try:
    import colab_config as cfg
except ImportError:
    cfg = None

def set_env_if_missing(key, value):
    if key not in os.environ and value:
        os.environ[key] = str(value)

if cfg:
    set_env_if_missing("BOT_TOKEN", getattr(cfg, "BOT_TOKEN", None))
    set_env_if_missing("API_ID", getattr(cfg, "API_ID", None))
    set_env_if_missing("API_HASH", getattr(cfg, "API_HASH", None))
    set_env_if_missing("OWNER_ID", getattr(cfg, "OWNER_ID", None))
    set_env_if_missing("DATABASE_URL", getattr(cfg, "DATABASE_URL", None))
    set_env_if_missing("GDRIVE_FOLDER_ID", getattr(cfg, "GDRIVE_FOLDER_ID", None))

# Launch bot
os.execvp(sys.executable, [sys.executable, "-m", "bot"])
