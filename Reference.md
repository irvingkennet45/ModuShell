# Reference & Documentation
This file can be used as sort of a quick reference for different features related to `ModuShell` and ANSI escape codes in general.

![Last Commit](https://img.shields.io/github/last-commit/irvingkennet45/ModuShell)
&nbsp;

---
# Glossary

**ANSI - American National Standards Institute**
- Regulates the standards for products, processes, and systems offered from the United States of America. Colloquially can reference the 8-bit character encoding standard.

**ASCII - American Standard Code for Information Interchange**
- Created by the ANSI as a 7-bit subset of characters that mainly focuses on the English language and symbols within, such as dashes, parentheses, etcetra.

**ANSI Escape Codes**
- Escape codes that normally start with a pre-defined character (`\`) and sequence, with a bracket and command following 
directly. The terminal interprets this as a command rather than displaying it as-is, and they can be used to control 
color, animation, or other terminal graphics, as well as some terminal features.

&nbsp;

---
# Basics

When you want to use ModuShell, you first call it like such:
    
    END = ModuShell.End 
    my_variable = ModuShell.Italic()
    
    print(f"This word is {my_variable}italic{END}")

`my_variable` is the variable that you use to call the styling.
All styling starts with `ModuShell` followed by it's appropriate function.

Styling that has multiple versions, such as `BOLD`, starts with it's `class` and then it's `styling function`. With `ModuShell.Weight.BOLD`, `Weight` is the class that contains the styling functions.

&nbsp;

---
# Styling Functions

`Italic` - Italicizes text.

    ModuShell.Italic

&nbsp;

`Weight` - Changes the weight of the text. Specified by either `BOLD` or `LIGHT`_*_.

    ModuShell.Weight.[BOLD/LIGHT]

&nbsp;

`Line` - Underlines or overlines text. Specified by either `UNDER`_**_ or `OVER`. Alternatively, call `RM` to remove underline from links or other text.

    ModuShell.Line.[OVER/UNDER/RM]

&nbsp;

`Cross` - Strike-through text, as if it has been marked for deletion.

    ModuShell.Cross

&nbsp;

`Frame` - Frame text in a box.

    ModuShell.Frame

&nbsp;

`Circle` - Encircle text.

    ModuShell.Circle

&nbsp;

`Blink` - Set the terminal's cursor blink rate. `FAST` for 150+ blinks a minute, `SLOW` for less than 150 blinks a minute, and `OFF` to turn cursor blinking off.

    ModuShell.Blink.[FAST | SLOW | OFF]

&nbsp;

`BigX` - Define either `Big2` or `Big3` to set the respective amount of styling.

> `ModuShell.Big2()`_**_ - Underlines and emboldens.

> `ModuShell.Big3()`_**_ - Underlines, emboldens, and italicizes.

&nbsp;

`Colorize` - Sets either font color (`FONT`) or background color (`HIGH` for `HIGHLIGHTER`).

    ModuShell.Colorize.[FONT | HIGH](([RGB | Hex | HSL]))***

Alternatively, add an `8` after the function to define colloquial colors. (`FONT8` and `HIGH8` for `8-bit colors`)

&nbsp;

Example of using colloquial colors:

    END = ModuShell.End 
    my_variable = ModuShell.Colorize.FONT8("red")
    
    print(f"This text is {my_variable}red{END}")

&nbsp;

> _*_ `LIGHT` may not work on all terminals, or have limited change. It can be used to remove bold text, however.
&nbsp;

> _**_ When calling the `UNDERLINE` function, a value of either `1` or `2` MUST be specified. This determines the amount of lines. On most terminals, `2` shows up as a single, thicker
line, rather than individual ones. `2` also removes any bold styling from text, as they cannot be used together.
&nbsp;

> _***_  You can use either `RGB`, `HSL`, or `Hex` codes.

&nbsp;

`Hex` codes can be passed as such:

    ModuShell.Colorize.FONT("#ffffff")

`RGB` can be passed as:

    ModuShell.Colorize.FONT((255, 255, 255)) <- Notice it requires another set of parentheses. This also applies to HSL.

And `HSL` can be passed as:

    ModuShell.Colorize.FONT((15, .5, .5)) <- Degrees, Saturation, Lightness
    
    # Specify a degrees greater than or equal to 0 and less than or equal to 360. 
    # Saturation and Lightness MUST be greater than 0 and less than one. This may be fixed in future updates, but for now keeps the code functional.

&nbsp;

---
# End Variable

You can define a global end variable that resets the styling of text. To do this, call `ModuShell.End`. With ANSII escape codes, the 
styling continues until the text style is reset or the function ends, so you do not technically need a closing tag, but be warned: 
if you have already called a style in the same string, it **WILL** carry over even if you call another style unless you reset the styling.

Example:
    
    my_variable = ModuShell.End

    print(f"The text is {italic1}italic{my_variable}")

&nbsp;

---
# Valid Colloquial Codes

Here is a short list of the valid colloquial codes you can use with `FONT8` or `HIGH8`. Included are their regular (`main`) and pastel (`pastel`) RGB values according to the VGA standard:

### Colors:

| Color       | Main Color Values                                                                                              | Pastel ("Bright") Color Values                                                                                  |
|-------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| `"black"`   | `main`: `0, 0, 0` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(0,0,0)&style=flat)              | `pastel`: `85, 85, 85` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(85,85,85)&style=flat)       |
| `"white"`   | `main`: `170, 170, 170` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(170,170,170)&style=flat)  | `pastel`: `255, 255, 255` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(255,255,255)&style=flat) |
| `"red"`     | `main`: `170, 0, 0` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(170,0,0)&style=flat)          | `pastel`: `255, 85, 85` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(255,85,85)&style=flat)     |
| `"green"`   | `main`: `0, 170, 0` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(0,170,0)&style=flat)          | `pastel`: `85, 255, 85` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(85,255,85)&style=flat)     |
| `"yellow"`  | `main`: `170, 85, 0` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(170,85,0)&style=flat)        | `pastel`: `255, 255, 85` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(255,255,85)&style=flat)   |
| `"blue"`    | `main`: `0, 0, 170` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(0,0,170)&style=flat)          | `pastel`: `85, 85, 255` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(85,85,255)&style=flat)     |
| `"magenta"` | `main`: `170, 0, 170` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(170,0,170)&style=flat)      | `pastel`: `255, 85, 255` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(255,85,255)&style=flat)   |
| `"cyan"`    | `main`: `0, 170, 170` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(0,170,170)&style=flat)      | `pastel`: `85, 255, 255` ![preview](https://img.shields.io/badge/&nbsp;-bar?color=rgb(85,255,255)&style=flat)   |

&nbsp;

---
## The `set_type` Variable

    ModuShell.Colorize.FONT8("red", set_type = "[main_colors | pastel_colors]")

The `set_type` variable is a variable within the `Colorize 8-bit Functions` (`FONT8` and `HIGH8`). It allows you to define whether or not you want the red from the `main_color` or red from the `pastel_colors`. If no value is passed or specified, it automatically defaults to `main_colors`.

&nbsp;

---

## Compatability

Most of the functions in here should work with any modern-day `VT52` terminal, but some may have varying degrees of 
success depending on the platform. From testing so far, `Windows` is stable, but `Linux`, or any other platforms have 
yet to be tested (e.g `PuTTy`, etc.). Forks for improvements to the code or expanding compatability are always appreciated, and 
will be reviewed ASAP.