class TextColor:
    def print_format_table(self):
        """ 
        prints table of formatted text format options 
        """
        for style in range(8):
            for fg in range(30, 38):
                s1 = ''
                for bg in range(40, 48):
                    format = ';'.join([str(style), str(fg), str(bg)])
                    s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
                print(s1)
            print('\n')

            from classes.Color import Color

class Color:
    foreground = {
        'Default': "\x1b[39m",
        'Black': "\x1b[30m",
        'Red': "\x1b[31m",
        'Green': "\x1b[32m",
        'Yellow': "\x1b[33m",
        'Blue': "\x1b[34m",
        'Magenta': "\x1b[35m",
        'Cyan': "\x1b[36m",
        'LightGray': "\x1b[37m",
        'DarkGray': "\x1b[90m",
        'LightRed': "\x1b[91m",
        'LightGreen': "\x1b[92m",
        'LightYellow': "\x1b[93m",
        'LightBlue': "\x1b[94m",
        'LightMagenta': "\x1b[95m",
        'LightCyan': "\x1b[96m",
        'White': "\x1b[97m"
    }
    background = {
        'Default': "\x1b[49m",
        'Black': "\x1b[40m",
        'Red': "\x1b[41m",
        'Green': "\x1b[42m",
        'Yellow': "\x1b[43m",
        'Blue': "\x1b[44m",
        'Magenta': "\x1b[45m",
        'Cyan': "\x1b[46m",
        'LightGray': "\x1b[47m",
        'DarkGray': "\x1b[100m",
        'LightRed': "\x1b[101m",
        'LightGreen': "\x1b[102m",
        'LightYellow': "\x1b[103m",
        'LightBlue': "\x1b[104m",
        'LightMagenta': "\x1b[105m",
        'LightCyan': "\x1b[106m",
        'White': "\x1b[107m"
    }
    
    RESET = foreground['Default'] + background['Default']
    BLACK = foreground['Black'] + background['White']
    RED = foreground['Red'] + background['White']
    EMPTY = foreground['White'] + background['Green']
    FACE_DOWN = foreground['White'] + background['LightBlue']