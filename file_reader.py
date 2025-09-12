def opener(file_path):
    ooah = None
    try:
        ooah = open(file_path, 'r')
        content = ooah.read()
        print(content)
    except FileNotFoundError:
        print ("Error: File not found.")
    finally:
        if ooah:
            ooah.close()
        print("File closed.")

