"""Configuration for Who Is Hiring suite"""
from pathlib import Path

def cache_dir() -> Path:
    """Get the location to cache data for Who Is Hiring"""
    return Path().home()
