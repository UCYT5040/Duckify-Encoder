# Duckify Encoder

## Usage

Download `main.py` and run it.

`main.py` has an encoded version in `encoded_main.py.txt`.

### As A Module

Coming soon (real soon)

## How It Works
Space ( ) shows a new character.
Every new character has a value.
Duck (🦆) is worth 1
Corn (🌽) is worth 10
Lettuce (🥬) is worth 100
It checks how many lettuce it can subtract.
Then, how many corn.
Last, how many duck.
### Examples

#### Duckify `'a'`

`ord('a') == 97`

Result: `'🌽🌽🌽🌽🌽🌽🌽🌽🌽🦆🦆🦆🦆🦆🦆🦆'`

9 corn \* 10 per corn = 90 + 7 duck \* 1 per duck = 97

#### Duckify 'abc'

`ord('a') == 97`
`ord('b') == 98`
`ord('c') == 99`
Result: `'🌽🌽🌽🌽🌽🌽🌽🌽🌽🦆🦆🦆🦆🦆🦆🦆 🌽🌽🌽🌽🌽🌽🌽🌽🌽🦆🦆🦆🦆🦆🦆🦆🦆 🌽🌽🌽🌽🌽🌽🌽🌽🌽🦆🦆🦆🦆🦆🦆🦆🦆🦆'`
space ( ) is used to show a new character