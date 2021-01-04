import csv
import os.path


class Detector:
    def output_in_file(self):
        """Выводит в файл CSV-данные.

        :param self:Detector
        """
        with open(self.path + "/data2.csv", 'w') as file:
            writer = csv.DictWriter(file, delimiter=';', lineterminator='\n', fieldnames=self.data[0].keys())

            writer.writeheader()
            writer.writerows(self.data)

    def list_from_file(self):
        """
        Получение данных CSV-файла по заданному пути и создание словаря по данным.

        :param self:Detector
        """
        with open(self.path + '/data.csv') as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                self.data.append(row)

    def __repr__(self):
        """Возвращает путь и данные словаря при попытке отобразить экземпляр класса путём, отличным от превращения в
        строку.

        :return: string
        """
        return "FileCsvData(\"" + self.path + "\", data)"

    def __str__(self):
        """Возвращает данные словаря при попытке использования str(), а также print(), на экземпляре класса.

        :return: {}
        """
        return self.data

    def __init__(self, path_out):
        """Инициализирует экземпляр данного класса с заданным путём файла и полученными данными из файла как параметры.

        :param path_out:
        """
        self.path = path_out
        self.data = []
        self.list_from_file()

    def __iter__(self):
        """Возвращает итератор для данных объекта при вызове iter для объекта.

        :return:
        """
        return iter(self.data)

    def __len__(self):
        """Возвращает количество элементов в списке data при вызове len для объекта.

        :return: int
        """
        return len(self.data)


class DataProcess(Detector):
    def print_data(self):
        """Форматированный вывод данных.

        :param self:object
        """
        printer = ""
        for i in self.data[0].keys():
            printer += ("{:11s}".format(i) + " ")
        printer += "\n"
        for row in self.data:
            for x in row.values():
                printer += ("{:11s}".format(x) + " ")
            printer += "\n"
        return printer

    def count_files(self):
        """
        Вывод количества файлов в папке по заданному пути.

        :param self:object
        """
        num_files = len([f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))])
        print("Кол-во файлов:", num_files)

    def sorting(self, name):
        """
        Сортировка данных по заданному ключу.

        :param name:string
        """
        if name == "date and time":
            self.data.sort(key=lambda f: f[name])
        else:
            self.data.sort(key=lambda f: int(f[name]))
        self.print_data()

    def __repr__(self):
        """Возвращает __repr__ от класса Detector.

        :return: string
        """
        return super().__repr__()

    def __init__(self, path_out):
        super().__init__(path_out)

    def __setattr__(self, attr, value):
        """Проверяет присваивание значений к параметрам экземпляра класса.

        :param attr:type
        :param value:str/list/int
        :return:
        """
        if attr == "path" and isinstance(value, str):
            self.__dict__[attr] = value
        elif attr == "data" and isinstance(value, list):
            self.__dict__[attr] = value
        elif attr == "i" and isinstance(value, int):
            self.__dict__[attr] = value
        else:
            raise AttributeError("'CsvChecker' object has no attribute '" + attr + "'")

    def __str__(self):
        """Вывызается при str() (а также при print()), выводя метод print_data()

        :return: string
        """
        return self.print_data()

    def longitude_30(self):
        """Выборка при longitude < 30.

        """
        for j in self.data[0].keys():
            print("{:11s}".format(j), end=" ")
        print()
        for i in self.data:
            if int(i['longitude']) < 30:
                for x in i.values():
                    print("{:11s}".format(x), end=" ")
                print()


path = "c://Users/Андрей/Desktop/Hello"

a = DataProcess(path)

a.count_files()

print("Исходные данные:")
print(a.print_data())

print("Сортировка данных по ключу. Введите ключ:")
a.sorting(input())
print(a.print_data())

print("Вывод всех данные, где longitude < 30:")
a.longitude_30()

a.output_in_file()

average = 0
for i in a:
    average += int(i["temperature"])
average /= len(a)
print(average)

print("Программа завершена.")
