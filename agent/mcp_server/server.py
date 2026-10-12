from datetime import datetime
from pathlib import Path
import sys

# tools.py lives at the repository root, two levels above this file.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools import gen_dice_values, gen_password
from fastmcp import FastMCP

mcp = FastMCP("Time Server")

@mcp.tool()
def current_time():
    """Return the current date and time."""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

@mcp.tool()
def generate_password(length=12):
    """Return secure password length according to the length provided or default to 12 character secure password"""
    return gen_password(length)


@mcp.tool()
def roll_dice (start=1,end=6):
    """return dice roll for two dice values"""
    return gen_dice_values(start,end)

if __name__=="__main__":
    mcp.run(transport="stdio")
