import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap

from iterator import ImageIterator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Вызов инициализатора род класса QMainWindow

        self.setWindowTitle("Мощная тема от Никитосика")
        self.setFixedWidth(1280)
        self.setFixedHeight(780)
        self.setStyleSheet("background-color: #bfbfbf;")

        self.image_label = QLabel(self)  # объект QLabel(приложение графический интерфейса GUI)
        self.image_label.move(250, 0)
        self.image_label.setFixedSize(850, 700)

        self.button_next = QPushButton("Следующее изображение", self)
        self.button_next.setFixedSize(640, 80)
        self.button_next.move(640,700)
        self.button_next.setStyleSheet('QPushButton {background-color: #5a90bd}')
        self.button_next.clicked.connect(self.show_next_image)  # Подключение обработчика события clicked к методу show

        self.button_previous = QPushButton("Предыдущее изображение",self)
        self.button_previous.setFixedSize(640, 80)
        self.button_previous.move(0, 700)
        self.button_previous.setStyleSheet('QPushButton {background-color: #5a90bd}')
        self.button_previous.clicked.connect(self.previous_image)

        self.button_dir = QPushButton("Выбрать папку датасета", self)
        self.button_dir.setFixedSize(1280, 70)
        self.button_dir.move(0, 630)
        self.button_dir.setStyleSheet('QPushButton {background-color: #4c51b7}')
        self.button_dir.clicked.connect(self.open_dataset_folder)
        self.iterator = None



    def open_dataset_folder(self) -> None:
        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку с фоточками")
        if folder_path:
            self.iterator = ImageIterator(folder_path=folder_path)
            if len(self.iterator.images) == 0:
                self.image_label.setText("Изображений нет в папке")
                return None
            # Открытие изображения сразу
            next_image_path = self.iterator.get_curr_elem()
            pixmap = QPixmap(next_image_path)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), aspectRatioMode=1))


    def show_next_image(self) -> None:
        if self.iterator and len(self.iterator.images) != 0:
            try:
                next_image_path = next(self.iterator)
                print(next_image_path)
                pixmap = QPixmap(next_image_path)  # QPixmap содержит всю информацию о пикселях изображения (их цвет и позицию)
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), aspectRatioMode=1))
            except StopIteration:
                pass


    def previous_image(self):
        if self.iterator is not None:
            try:
                prev_image_path = self.iterator.previous()
                print(prev_image_path)
                pixmap = QPixmap(prev_image_path)
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))
            except StopIteration:
                pass



def main():
    try:
        app = QApplication(sys.argv)
        window = MainWindow()  # Создаем свой класс
        window.show()  # Вывод окна на экран
        sys.exit(app.exec_())  # Устанавливаем закрытие окна только после события нажатия на крестик

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()