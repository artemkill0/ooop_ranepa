class Graph:
    def __init__(self, data):
        self.data = data
        self.is_show = True

    def show_table(self):
        if not self.is_show:
            print("Отображение данных закрыто")
            return
        print(" ".join(map(str, self.data)))

    def set_show(self, fl_show):
        self.is_show = fl_show

g = Graph([1, 2, 3, 4])
g.show_table()
g.set_show(False)
g.show_table()