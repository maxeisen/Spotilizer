# This is a module that chooses colour for a visualization tool based off of
# it's musical elements.

import tkinter

def define_palettes():
    # Creates a series of palettes, and returns them in a list of dictionaries
    # Each colour will be modified based on the static and dynamic parameters
    # of the track.

    # Palette 1 is the coolest palette.
    palette_1 = []
    palette_1.append("970E6D")
    palette_1.append("612B74")
    palette_1.append("2E4D73")
    palette_1.append("256C67")
    palette_1.append("83B332")

    # Palette 2 is the warmest palette.
    palette_2 = []
    palette_2.append("D23305")
    palette_2.append("95404C")
    palette_2.append("AD7643")
    palette_2.append("D3A50B")

    # Palette 3 is a hybrid of warm and cool colours.
    palette_3 = []
    palette_3.append("3C2E9B")
    palette_3.append("226653")
    palette_3.append("27C480")
    palette_3.append("2C92C3")
    palette_3.append("80BB1C")

    # Palette 4 is a more vibrant palette.
    palette_4 = []
    palette_4.append("D62936")
    palette_4.append("612B74")
    palette_4.append("22A64F")
    palette_4.append("26B0BF")
    palette_4.append("EAEF2E")

    palettes = [palette_1, palette_2, palette_3, palette_4]

    return palettes

def choose_palette(danceability, acousticness):
    # Create palettes
    palettes = define_palettes()
    # Choose a palette based on the track parameters
    if danceability >= 0.8:
        palette = palettes[3]
    elif acousticness >= 0.8:
        palette = palettes[2]
    elif acousticness >= 0.1:
        palette = palettes[1]
    else:
        palette = palettes[0]
    return palette

def energy_mod(palette, energy):
    new_palette = []
    # Modify the color saturation based on the energy levels of the track
    for colour in palette:
        red = int(colour[0:2], 16)
        green = int(colour[2:4], 16)
        blue = int(colour[4:6], 16)
        red_en, green_en, blue_en = red, green, blue
        if red >= green and red >= blue:
            red_en = str(hex(int(min(255, red ** (2 * energy))))[2:])
        else:
            red_en = str(hex(red)[2:])
        if green >= red and green >= blue:
            green_en = str(hex(int(min(255, green ** (2 * energy))))[2:])
        else:
            green_en = str(hex(green)[2:])
        if blue >= red and blue >= green:
            blue_en = str(hex(int(min(255, blue ** (2 * energy))))[2:])
        else:
            blue_en = str(hex(blue)[2:])
        if len(red_en) < 2:
            red_en = '0' + red_en
        if len(green_en) < 2:
            green_en = '0' + green_en
        if len(blue_en) < 2:
            blue_en = '0' + blue_en
        colour = red_en + green_en + blue_en
        new_palette.append(colour)
    return new_palette

def brightness_mod(palette, brightness):
    # Modify the colour brightness based on the energy levels of the track
    for colour in palette:
        red = int(colour[0:2], 16)
        green = int(colour[2:4], 16)
        blue = int(colour[4:6], 16)
        red_br, green_br, blue_br = red, green, blue
        if red >= green and red >= blue:
            red_br = hex(int(min(255, red ** (2 * energy))))[2:]
        else:
            red_br = hex(red)[2:]
        if green >= red and green >= blue:
            green_br = hex(int(min(255, green ** (2 * energy))))[2:]
        else:
            green_br = hex(green)[2:]
        if blue >= red and blue >= green:
            blue_br = hex(int(min(255, blue ** (2 * energy))))[2:]
        else:
            blue_br = hex(blue)[2:]
        colour = red_br + green_br + blue_br
    return palette

if __name__ == "__main__":
    palette = choose_palette(0.5, 0.5)
    palette = energy_mod(palette, 0.8)

    # window = tkinter.Tk()
    # top_frame = tkinter.Frame(window).pack()
    # bottom_frame = tkinter.Frame(window).pack(side = "bottom")
    # btn1 = tkinter.Button(top_frame, bg = '#' + palette[0]).pack(side = "left")
    # btn2 = tkinter.Button(top_frame, bg = '#' + palette[1]).pack(side = "left")
    # btn3 = tkinter.Button(bottom_frame, bg = '#' + palette[2]).pack(side = "left")
    # btn4 = tkinter.Button(bottom_frame, bg = '#' + palette[3]).pack(side = "left")
    # # btn4 = tkinter.Button(bottom_frame, bg = '#' + palette[4]).pack(side = "left")
    # window.mainloop()
