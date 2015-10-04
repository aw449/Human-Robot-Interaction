import pickle


class Exporter:

    def __init__(self):
        self.tree = pickle.load(open('test.cpickle', "rb"))
        self.list = []

    def get_plot(self, sub_name, cup_no, speed):
        for key in self.tree[sub_name].keys:
            for hand in self.tree[sub_name][key].keys:
                sub_list = []
                sub_list.append(key)
                sub_list.append(self.tree[sub_name][key][hand][speed])
                self.list.append(sub_list)

        return self.list

    def get_speed(self, sub_name, cup_no, trj):
        for hand in self.tree[sub_name][trj].keys:
            for speed in self.tree[sub_name][trj][hand][cup_no].keys:
                sub_list = []
                sub_list.append(speed)
                sub_list.append(self.tree[sub_name][trj][hand][cup_no][speed])
                self.list.append(sub_list)
        return self.list


