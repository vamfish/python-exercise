escape_backslash = "\\"
escape_single_quote = "\'"
escape_double_quote = "\""
escape_bell = "\a"
escape_formfeed = "\f"
escape_linefeed = "\n"
escape_return = "\r"
escape_tab = "\t"
escape_vertical_tab = "\v"

# All characters can be presented as unicode, other types of value are just different encoding methods
escape_unicode = "\N{Greek Capital Letter Delta}"
escape_16bit = "\u3f31"
escape_32bit = "\U000231dc"
escape_octal = "\345"
escape_hex = "\x48"


print("Backslash: " + escape_backslash)
print("Single-quote: " + escape_single_quote)
print("Double-quote: " + escape_double_quote)
print("ACSII bell (BELL): " + escape_bell)
print("ACSII formfeed (FF): " + escape_formfeed)
print("ACSII linefeed (LF): " + escape_linefeed)
print("Carriage return (CR): " + escape_return)
print("Horizontal tab: " + escape_tab)
print("Vertical tab: " + escape_vertical_tab)

print("Character named Greek Capital Letter Delta: " + escape_unicode)
print("Character with 16-bit hex value of 3f31: " + escape_16bit)
print("Character with 32-bit hex value of 000231bc: " + escape_32bit)
print("Character with octal value of 345: " + escape_octal)
print("Character with hex value of 48: " + escape_hex)
