from sort_lists_function import ordenarlista

try:
    file = open("namesx_list.txt", "r")
except:
    print("Error en archivo")
    quit()

text_list = file.readlines()
file.close()

len_list = len(text_list)

for i in range(len_list):
    text_list[i] = text_list[i].rstrip()

if __name__ == "__main__":
    print("lista desordenada: ", text_list)
    print("lista ordenada: "ordenarlista(text_list))
