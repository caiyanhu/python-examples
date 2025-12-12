def jpeg_res(filename):
    # Non-text files must be open in binary mode
    with open(filename, "rb") as img_file:
        img_file.seek(163)

        a = img_file.read(2)
        height = (a[0] << 8) + a[1]

        a = img_file.read(2)
        width = (a[0] << 8) + a[1]
    print("The resolution of the image is", width, "x", height)


jpeg_res("./jpeg-image-file-12.jpg")
