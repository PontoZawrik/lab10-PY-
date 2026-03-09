with open("file02.txt", "w+") as f:
    f.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
            "\nLorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
            "\nwhen an unknown printer took a galley of type and scrambled it to make a type "
            "\nspecimen book. It has survived not only five centuries, but also the leap into "
            "\nelectronic typesetting, remaining essentially unchanged. ")

    f.seek(0)
    lines = f.readlines()
    max_line = lines[0]
    for line in lines:
        if len(line) > len(max_line):
            max_line = line
    print(f"Самая длиная строка: \n{max_line}Длина: {len(max_line)} символов")