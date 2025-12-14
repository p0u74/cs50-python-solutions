file_name = ((((input("File name : ")).strip()).lower()).split("."))[-1]

# Short way
print(f"image/{file_name}" if file_name in {"gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"} else "application/octet-stream")

# alt way
# match file_name:
#     case "gif" | "jpg" | "jpeg" | "png" | "pdf" | "txt" | "zip":
#         print(f"image/{file_name}")
#     case _:
#         print("application/octet-stream")