# This file allows you to test to see if you terminal supports all of the ANSI escape codes.
import ModuShell

# END Variable
END = ModuShell.End

# Italic
italic1 = ModuShell.Italic()

# Weight
bold1 = ModuShell.Weight.BOLD()
light1 = ModuShell.Weight.LIGHT()

# Cross
cross1 = ModuShell.Cross()

# Over and Underline
line1 = ModuShell.Line.UNDER(1)
line2 = ModuShell.Line.UNDER(2)
oline1 = ModuShell.Line.OVER()
removeline1 = ModuShell.Line.RM()

# Draw
frame1 = ModuShell.Frame()
circle1 =  ModuShell.Circle()

# Blink
blink1 = ModuShell.Blink.SLOW()
blink2 = ModuShell.Blink.FAST()
blinkoff = ModuShell.Blink.OFF()

# Combos
combo1 = ModuShell.Big2(1)
combo2 = ModuShell.Big2(2)

combo3 = ModuShell.Big3(1)
combo4 = ModuShell.Big3(2)

redcolor_rgb = (255,0,0)
bluecolor_rgb = (49,168,247)
whitecolor_rgb = (255,255,255)
blackcolor_rgb = (0,0,0)

redcolor_hsl = (204,0.93,0.58)
bluecolor_hsl = (0,0.99,0.5)
whitecolor_hsl = (0,0.01,0.99)
blackcolor_hsl = (0,0.01,0.01)

redcolor_hex = "#ff0000"
bluecolor_hex = "#31a8f7"
whitecolor_hex = "#ffffff"
blackcolor_hex = "#000000"

# Color

# RGB
color1 = ModuShell.Colorize.FONT(bluecolor_rgb)
color2 = ModuShell.Colorize.HIGH(redcolor_rgb)

# HSL
color3 = ModuShell.Colorize.FONT(bluecolor_hsl)
color4 = ModuShell.Colorize.HIGH(redcolor_hsl)

# Hex
color5 = ModuShell.Colorize.FONT(bluecolor_hex)
color6 = ModuShell.Colorize.HIGH(redcolor_hex)

# B & W
# RGB
mono1 = ModuShell.Colorize.HIGH(whitecolor_rgb)
mono2 = ModuShell.Colorize.FONT(whitecolor_rgb)
mono3 = ModuShell.Colorize.FONT(blackcolor_rgb)

# HSL
mono4 = ModuShell.Colorize.HIGH(whitecolor_hsl)
mono5 = ModuShell.Colorize.FONT(whitecolor_hsl)
mono6 = ModuShell.Colorize.FONT(blackcolor_hsl)

# Hex
mono7 = ModuShell.Colorize.HIGH(whitecolor_hex)
mono8 = ModuShell.Colorize.FONT(whitecolor_hex)
mono9 = ModuShell.Colorize.FONT(blackcolor_hex)


# Colloquial Color

# Main
bitcolor1 = ModuShell.Colorize.FONT8("red")
bitcolor2 = ModuShell.Colorize.HIGH8("red")

# Pastel
bitcolor3 = ModuShell.Colorize.FONT8("red", set_type="pastel_colors")
bitcolor4 = ModuShell.Colorize.HIGH8("red", set_type="pastel_colors")

# B & W
# Main
monobit1 = ModuShell.Colorize.FONT8("white")
monobit2 = ModuShell.Colorize.HIGH8("white")

monobit3 = ModuShell.Colorize.FONT8("black")
monobit4 = ModuShell.Colorize.HIGH8("black")

# Pastel
monobit5 = ModuShell.Colorize.FONT8("white", set_type="pastel_colors")
monobit6 = ModuShell.Colorize.HIGH8("white", set_type="pastel_colors")

monobit7 = ModuShell.Colorize.FONT8("black", set_type="pastel_colors")
monobit8 = ModuShell.Colorize.HIGH8("black", set_type="pastel_colors")

print(f"This is styled: {italic1}italic{END}")
print(f"This is styled: {bold1}bold{END}")
print(f"This is styled: {light1}light{END}")
print(f"This is styled: {cross1}cross{END}")
print(f"This is styled: {line1}underline{END}")
print(f"This is styled: {line2}dbl underline{END}")
print(f"This is styled: {oline1}overline{END}")
print(f"This is for comparison: https://github.com/irvingkennet45/ModuShell")
print(f"This is styled: *removes underline from link* {removeline1}https://github.com/irvingkennet45/ModuShell{END}")
print(f"This is styled: {frame1}frame{END}")
print(f"This is styled: {circle1}circle{END}")

print(f"This is styled: {blink1}slow blink{END}")
testinput1 = input("Look at the flashing colors! ")
testinput1

print(f"This is styled: {blink2}fast blink{END}")
testinput2 = input("Look at the flashing colors! ")
testinput2

print(f"This is styled: {blinkoff}blink off{END}")
testinput3 = input("Look at the flashing colors! ")
testinput3

print(f"This is styled: {combo1}big2 1 line{END}")
print(f"This is styled: {combo2}big2 2 line{END}")
print(f"This is styled: {combo3}big3 1 line{END}")
print(f"This is styled: {combo4}big3 2 line{END}")

# ---RGB---
print(f"This is styled: {color1}rgb font{END}")
print(f"This is styled: {color2}rgb highlight{END}")
print(f"This is styled: {color1}{color2}rgb font + highlight{END}")  # Combine

# BW (RGB)
print(f"This is styled: {mono1}rgb white highlight{END}")
print(f"This is styled: {mono2}rgb white font{END}")
print(f"This is styled: {mono3}rgb black font{END}")
print(f"This is styled: {mono1}{mono3}rgb white highlight + black font{END}")  # Combine

# ---HSL---
print(f"This is styled: {color3}hsl font{END}")
print(f"This is styled: {color4}hsl highlight{END}")
print(f"This is styled: {color3}{color4}hsl font + highlight{END}")  # Combine

# BW (HSL)
print(f"This is styled: {mono4}hsl white highlight{END}")
print(f"This is styled: {mono5}hsl white font{END}")
print(f"This is styled: {mono6}hsl black font{END}")
print(f"This is styled: {mono4}{mono6}hsl white highlight + black font{END}")  # Combine

# ---Hex---
print(f"This is styled: {color5}hex font (#31a8f7){END}")
print(f"This is styled: {color6}hex highlight (#ff0000){END}")
print(f"This is styled: {color5}{color6}hex font + highlight{END}")  # Combine

# BW (Hex)
print(f"This is styled: {mono7}hex white highlight{END}")
print(f"This is styled: {mono8}hex white font{END}")
print(f"This is styled: {mono9}hex black font{END}")
print(f"This is styled: {mono7}{mono9}hex white highlight + black font{END}")  # Combine

# ---8BIT---
# MAIN
print(f"This is styled: {bitcolor1}8bit font red{END}")
print(f"This is styled: {bitcolor2}8bit highlight red{END}")
print(f"This is styled: {bitcolor1}{bitcolor2}8bit font + highlight red{END}")  # Combine

# PASTEL
print(f"This is styled: {bitcolor3}8bit pastel font red{END}")
print(f"This is styled: {bitcolor4}8bit pastel highlight red{END}")
print(f"This is styled: {bitcolor3}{bitcolor4}8bit pastel font + highlight red{END}")  # Combine

# ---Main BW---
# Whites
print(f"This is styled: {monobit1}8bit font white{END}")
print(f"This is styled: {monobit2}8bit highlight white{END}")
# Blacks
print(f"This is styled: {monobit3}8bit font black{END}")
print(f"This is styled: {monobit4}8bit highlight black{END}")
print(f"This is styled: {monobit1}{monobit4}8bit white font + black highlight{END}")  # Combine

# ---Pastel BW---
# Whites
print(f"This is styled: {monobit5}8bit pastel font white{END}")
print(f"This is styled: {monobit6}8bit pastel highlight white{END}")
# Blacks
print(f"This is styled: {monobit7}8bit pastel font black{END}")
print(f"This is styled: {monobit8}8bit pastel highlight black{END}")
print(f"This is styled: {monobit5}{monobit8}8bit pastel white font + black highlight{END}")  # Combine