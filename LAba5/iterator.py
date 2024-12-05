import os


class ImageIterator():

    def __init__(self, folder_path=None):
        '''
        Конструктор, инициализирующий массив строчек в зависимости от передаваемых аргументов
        (файла аннотации или папки картинок)
        :param annotation_file: файл аннотации
        :param folder_path: Папка картинок
        '''
        self.images = []

        if folder_path:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(('jpg', 'jpeg', 'png')):
                        self.images.append(os.path.join(root, file))
        self.index = 0


    def __iter__(self):
        '''
        Метод возвращения самого объекта итератора
        '''
        return self


    def __next__(self):
        '''
        Метод прохода по всем элементам массива класса через индекс и вывода их на экран
        '''
        if self.index >= len(self.images):
            raise StopIteration
        self.index += 1
        print("NEXT: ", self.index)
        return self.images[self.index]


    def previous(self):
        if self.index <= 0:
            raise StopIteration
        self.index -= 1
        print("Prev: ", self.index)
        return self.images[self.index]


    def get_curr_elem(self):
        if 0 <= self.index < len(self.images):
            return self.images[self.index]