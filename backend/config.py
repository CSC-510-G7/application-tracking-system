"""
This module loads the application configuration from a YAML file.
"""

import yaml
from dotenv import load_dotenv
import os

with open("application.yml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

load_dotenv()

config["OLLAMA_URL"] = os.getenv("OLLAMA_URL", "http://localhost:11434")
config["SELENIUM_URL"] = os.getenv("SELENIUM_URL", "http://localhost:4444")
