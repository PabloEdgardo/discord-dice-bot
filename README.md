# Dice Bot 🎲

A versatile Discord bot for rolling dice with support for both simple and complex RPG dice rolls.

## ⚠️ Setup Instructions

To run this bot on your machine:

1. Create a `.env` file in the same directory as `main.py`
2. Add your Discord bot token to the file:
3. Install required dependencies (if any)
4. Run the bot using `python main.py`

## 🎯 Features

- Simple and intuitive commands
- Support for basic single dice rolls
- Advanced multi-dice rolls with modifiers
- Perfect for tabletop RPG sessions

## 🎲 Commands

### Simple Dice Roll
`.dice [number_of_sides]`
- Rolls a single die with the specified number of sides
- **Example:** `.dice 20` - Rolls one 20-sided die

### Advanced RPG Dice Roll
`.cdice [number_of_dices]d[number_of_sides] (+|-)[modifier]`
- Rolls multiple dice with modifiers, perfect for tabletop RPGs
- **Examples:**
- `.cdice 2d6` - Rolls two 6-sided dice
- `.cdice 1d20+5` - Rolls one 20-sided die and adds 5
- `.cdice 4d8-2` - Rolls four 8-sided dice and subtracts 2
- `.cdice 3d10+10` - Rolls three 10-sided dice and adds 10

## 🔧 Requirements

- Python 3.13.7
- discord.py library
- python-dotenv library

## 📦 Installation

```bash
# Install required packages
pip install discord.py python-dotenv

# Clone or download the bot files
# Configure your .env file
# Run the bot
python main.py
