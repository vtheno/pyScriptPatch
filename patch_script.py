#!python

def main(filename):
    with open(filename, "rb") as file:
        data = file.read()
    pattern_start = b"\x00" * 10 + b"#!"
    pattern_end = b"python.exe"
    start = data.find(pattern_start)
    end = data.find(pattern_end)
    template = data[start:end + len(pattern_end)]
    target = pattern_start + b"python.exe"
    print(template)
    offset = len(template) - len(target)
    print(target)
    result = target + b" " * offset
    resourse = list(data)
    resourse[start:end + len(pattern_end)] = list(result)
    ret = bytes(resourse)
    with open("patch-" + filename, "wb") as file:
        file.write(ret)

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    if argv:
        main(argv[0])
    else:
        print("patch_script.py [absult path filename]")
