import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)# This is a tiny yet powerful piece of magic here. Calling main function again inside the main function. When the function is called, the code will jump to the top of the defination. Then if we call the same function at the end of itself, the code would jump back to the top and run it again! It's a loop, and the if statement on line#8 will prevent looping forever.


def print_line(line, encoding, errors):
    next_lang = line.strip()# This is a simple stripping of the trailing \n on the line string.
    raw_bytes = next_lang.encode(encoding, errors=errors)# Take the line received from the file and encode it into the raw bytes.
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

# This is the start of the code which will be executed.
languages = open("ex23_languages.txt", encoding="utf-8")
# Call the main function with parameters, this will jumps to the defination on line#5, and on line#10 where the main function is called again, causing a loop. And the if line on line#8 will prevent the loop from going forever.
main(languages, input_encoding, error)