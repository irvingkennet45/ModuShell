'''
# This is the core logic for the ModuShell Package
# Description:
# ModuShell is a package that you can use to customize any outputs to the console using simple calls within format strings. Requires a modern terminal that can handle ANSI escape sequences.

# ModuShell is licensed under the MIT License, and adheres to the clauses stated within.
# Credit/attribution within any distributed or modified works is required.
# For more information, visit https://opensource.org/license/mit, or this repository's version.
# If you received this software and a license was not included within, please contact contact.kenneth.irving@gmail.com with more details.

# See the README.md for more information

# Developed by Kenneth Irving (irvingkennet45)
# Project Repository: https://github.com/irvingkennet45/ModuShell
'''

import json
COMMON_COLORS_FILE = "/common_colors.json"

START_CODE_EXT = "\033[" # This is the start of all ANSI escape codes (at least the ones used in this program). This snippet is added to the wrappers before the wrappers applicable code is printed
SGR_VARIABLE_EXT = "m" # Inserts the standard SGR (Select Graphic Rendition) variable extension. This defines that we are changing the graphical look in the terminal, rather than the functionality.
END_CODE_EXT = "\033[0" # This is the end of all ANSI escape codes and resets the text to normal. This snippet is added to the wrappers as a constant variable.
# ------Standard Wrappers------

# Italic Wrapper: Italicizes outputs printed to the console.
def Italic(italS, italE):
	italic_start = "1"
	italS = italic_start
	italE = END_CODE_EXT

# Weight Wrapper: Emboldens or lightens outputs printed to the console. Weight can be specified using applicable arguments.
def Weight():
	# Bold Wrapper: Emboldens outputs printed to the console. Weight can be specified using applicable arguments.
	def BOLD(boldS, boldE):
		bold_start = ""
		boldE = END_CODE_EXT
	# Light Wrapper: Lightens outputs printed to the console. Weight can be specified using applicable arguments.
	def LIGHT(lightS, lightE):
		light_start = ""
		lightE = END_CODE_EXT

# Underline Wrapper: Underlines outputs printed to the console. Can be either double or single. It can also be used to remove the underline from links output to the console. A color may also be specified.
def Uline(color):
	def SINGLE(uline1S, uline1E):
		uline1_start = ""
		uline1E = END_CODE_EXT
	def DOUBLE(uline2S, uline2E):
		uline2_start = ""
		uline2E = END_CODE_EXT
	def REMOVE(ulinermS, ulinermE):
		ulinerm_start = ""
		ulinermE = END_CODE_EXT

# Cross-out Wrapper: Cross-out strings printed to the console, as if marked for deletion.
def Cross(crossS, crossE):
	cross_start = ""
	crossE = END_CODE_EXT

# BigX Wrappers: Combines two or more wrappers into a singular callable function for ease of use.
# Big2 Wrapper: Underlines and emboldens only.
def Big2(big2S, big2E):
	big2_start = ("" + "")
	big2E = END_CODE_EXT

# Big3 Wrapper: Italicizes, bolds, and underlines selected strings.
def Big3(big3S, big3E):
	big3_start = ("" + "" + "")
	big3E = END_CODE_EXT


# ------Others------

# Colorize Wrapper: Colorizes outputs printed to the console. Can colorize either the highlight (background behind the text) or the text itself.
def Colorize(color):
	def HIGH(highS, highE):
		high_start = ""
		highE = END_CODE_EXT
	def FONT(fontS, fontE):
		font_start = ""
		fontE = END_CODE_EXT