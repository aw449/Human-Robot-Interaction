import pickle


class Exporter:

    def __init__(self):
        self.tree = pickle.load(open('test.cpickle', "rb"))
        self.list = []
        self.convergence_list = []

    def get_plot(self, sub_name, cup_no, speed):
        self.list = []
        for trj in self.tree[sub_name].keys():
            if int(cup_no) < 8:
                hand = "right"
            else:
                hand = "left"

            sub_list = []
            try:
                self.tree[sub_name][trj][hand][cup_no].keys()
            except KeyError:
                return -1
            try:
                l = self.tree[sub_name][trj][hand][cup_no][speed]
            except KeyError:
                continue
            sub_list.append(trj)
            sub_list.append(l)
            self.list.append(sub_list)
        return self.list

    def get_speed(self, sub_name, cup_no, trj):
        self.list = []
        self.convergence_list = []
        if int(cup_no) < 8:
            hand = "right"
        else:
            hand = "left"
        try:
            self.tree[sub_name][trj][hand][cup_no].keys()
        except KeyError:
            return -1
        for speed in self.tree[sub_name][trj][hand][cup_no].keys():
            sub_list = []
            try:
                l = self.tree[sub_name][trj][hand][cup_no][speed]
            except KeyError:
                continue
            sub_list.append(speed)
            sub_list.append(l)
            self.list.append(sub_list)
        return self.list

    def get_trjconvergence(self, sub_name, cup_no, speed, alpha):
        self.convergence_list = []
        for trj in ["curve", "short", "straight", "straightdown", "claw"]:
            if int(cup_no) < 8:
                hand = "right"
            else:
                hand = "left"

            sub_list = []
            try:
                self.tree[sub_name][trj][hand][cup_no].keys()
            except KeyError:
                return -1
            try:
                l = self.tree[sub_name][trj][hand][cup_no][speed]
            except KeyError:
                continue
            upper = (int(cup_no)) * .1
            lower = (int(cup_no) -1) * .1
            a = self.find_convergence(l, upper, lower)
            a = (a-min(l[0]))/(max(l[0]) - min(l[0]))
            sub_list.append(a)
            self.convergence_list.append(sub_list)
        return self.convergence_list

    def get_spdconvergence(self, sub_name, cup_no, trj, alpha):
        self.convergence_list = []
        if int(cup_no) < 8:
            hand = "right"
        else:
            hand = "left"
        try:
            self.tree[sub_name][trj][hand][cup_no].keys()
        except KeyError:
            return -1

        for speed in ['5', '10', '15']:
            try:
                l = self.tree[sub_name][trj][hand][cup_no][speed]
            except KeyError:
                self.convergence_list.append(0)
                continue
            upper = (int(cup_no)) * .1
            lower = (int(cup_no) -1) * .1
            a = self.find_convergence(l, upper, lower)
            adjustment = self.find_middle(l[0])
            a = (a-adjustment)/(max(l[0]) - adjustment)
            self.convergence_list.append(a)
        return self.convergence_list

    def find_convergence(self, l, k, j):
        for i in range(0, len(l), 2):
            time_array = l[0]
            distance_array = l[1]
            time = self.find_timeindex(distance_array, k, j)
            return time_array[time]

    def find_middle(self, l):
        time = 0
        for i in range(len(l)):
            if l[i] == 0.75:
                    time = i
                    break

        return time

    def find_timeindex(self, l, k, j):
        time = -1
        inside = False
        for i in range(len(l)):
            if j <= l[i] <= k:
                if not inside:
                    time = i
                    inside = True
            else:
                inside = False
        return time

    def get_norm(self, l):
        time = []
        raw_time = l
        max = raw_time[-1]
        for i in range(len(raw_time)):
            time.append(raw_time[i]/max)
        return time






