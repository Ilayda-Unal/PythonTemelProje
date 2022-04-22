# Veri Analizi Patikası Python Bölüm Sonu Projesi
# Task1

new_list = []


def flatten(l):
    for i in l:
        if type(i) == list:
            flatten(i)
        else:
            new_list.append(i)


flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5])
print(new_list)

# Task2

bos_list = []


def tersi(x):

    x.reverse()
    for i in x:
        if isinstance(i, list):
            i.reverse()
            bos_list.append(i)


tersi([[1, 2], [3, 4], [5, 6, 7]])
print(bos_list)
