# Strings, Bytes, and Character Encodings

import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    #如果读取的line非空，则进行操作，return使得可以读取下一个line
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()#删除字符串两侧的空白符，如' ', '\n', '\t', ...
    raw_bytes = next_lang.encode(encoding, errors=errors)#以指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
    cooked_string = raw_bytes.decode(encoding, errors=errors)#解码

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
