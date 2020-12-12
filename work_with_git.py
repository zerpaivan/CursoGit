from sort_lists_function import ordenarlista
file = open("names_list.txt", "r")
text_list = file.readlines()
file.close()

len_list = len(text_list)
for i in range(len_list):
    text_list[i] = text_list[i].rstrip()

print("lista desordenada: ", text_list)
print("lista ordenada: "ordenarlista(text_list))
