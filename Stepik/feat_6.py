class Graph:

    def __init__(self, data, is_show=True):
        self.data = data
        self.is_show = is_show
        self.data_st = ' '.join(self.data)

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print(*self.data)

    def show_graph(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print(f"Графическое отображение данных: {self.data_st}")

    def show_bar(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print(f"Столбчатая диаграмма: {self.data_st}")

    def set_show(self, fl_show):
        self.is_show = fl_show


x = ['8', '11', '10', '-32', '0', '7', '18']
gr = Graph(x)
gr.show_bar()
gr.set_show(False)
gr.show_table()
