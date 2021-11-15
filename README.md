# Duckify Encoder

## Usage

Download `main.py` and run it.

`main.py` has an encoded version in `encoded_main.py.txt`.

### As A Module

Download the `duckify` folder (or just download duckify.py from there.)

If you downloaded the folder:
```
|--[main.py]
|--[duckify]
   |--[__main__.py]
   |--[duckify.py (can be deleted)]
main.py:
import duckify
duckify.encode("hi")
duckify.decode("stuff to decode")
```
If you downloaded the file:
```
|--[main.py]
|--[duckify.py]
main.py:
import duckify
duckify.encode("hi")
duckify.decode("stuff to decode")
```
## How It Works
Space ( ) shows a new character.
Every new character has a value.
Duck (🦆) is worth 1
Corn (🌽) is worth 10
Lettuce (🥬) is worth 100
The following are new and have not been added to the examples below yet.
broccoli (🥦) is worth 50
strawberry (🍓) is worth 1000
It checks how many strawberry it can subtract.
Then, how many lettuce.
Then, how many broccoli.
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