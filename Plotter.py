import matplotlib.pyplot as plt


from DataExporter import Exporter
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages('HumanRobotPlots.pdf')
a = Exporter()
plt.isinteractive()
# User Input here

subj = ["001", "002", "003", "004", "005", "006", "007", "008", "009"]
cup = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
trj = ["curve", "short", "straight", "straightdown", "claw"]
speed = ["5", "10", "15"]
# Print everything
u = 0
for s in range(len(subj)):
    for c in range(len(cup)):
        for t in range(len(trj)):
            data = a.get_speed(subj[s], cup[c], trj[t])
            if data == -1:
                break
            fig = plt.figure(u)
            ax = fig.add_subplot(111)
            u += 1
            for i in range(len(data)):
                x = data[i][1][0]
                y = data[i][1][1]
                new_x = a.get_norm(x)
                name = data[i][0]
                ax.plot(new_x, y, label=name)

            lgd = ax.legend(loc='upper center', bbox_to_anchor=(0.5,-0.1))
            ax.grid('on')
            ax.set_xlabel('Normalized Time')
            ax.set_ylabel('Distance')
            ax.set_title("Raw Data for Subj{0}_Cup{1}_Trj{2}".format(subj[s], cup[c], trj[t]))
            ax.grid('on')
            pp.savefig(bbox_extra_artists=(lgd,), bbox_inches='tight')

        for sp in range(len(speed)):
            data = a.get_plot(subj[s], cup[c], speed[sp])
            if data == -1:
                break
            fig = plt.figure(u)
            ax = fig.add_subplot(111)
            u += 1
            for i in range(len(data)):
                x = data[i][1][0]
                y = data[i][1][1]
                new_x = a.get_norm(x)
                name = data[i][0]
                ax.plot(new_x, y, label=name)

            lgd = ax.legend(loc='upper center', bbox_to_anchor=(0.5,-0.1))
            ax.set_xlabel('Normalized Time')
            ax.set_ylabel('Distance')
            ax.set_title("Raw Data for Subj{0}_Cup{1}_Speed{2}".format(subj[s], cup[c], speed[sp]))
            ax.grid('on')
            pp.savefig(bbox_extra_artists=(lgd,), bbox_inches='tight')

pp.close()









