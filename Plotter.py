import matplotlib.pyplot as plt

from DataExporter import Exporter
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages('AverageCups.pdf')
a = Exporter()
plt.isinteractive()
# User Input here
choice = input("Please enter which data you wish to use")
subj = ["001", "002", "003", "004", "005", "006", "007", "008", "009"]
cup = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
trj = ["curve", "short", "straight", "straightdown", "claw"]
speed = ["5", "10", "15"]
# Print everything
u = 0
if choice == 'raw':
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

                line = float(cup[c]) * 0.1
                plt.axhline(line, label='Target', color='k', dashes=[3, 3])
                lgd = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))
                axes = plt.gca()
                axes.set_ylim([0, 1.5])
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

                line = float(cup[c]) * 0.1
                plt.axhline(line, label='Target', color='k', dashes=[3, 3])
                lgd = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))
                ax.set_xlabel('Normalized Time')
                ax.set_ylabel('Distance')
                axes = plt.gca()
                axes.set_ylim([0, 1.5])
                ax.set_title("Raw Data for Subj{0}_Cup{1}_Speed{2}".format(subj[s], cup[c], speed[sp]))
                ax.grid('on')
                pp.savefig(bbox_extra_artists=(lgd,), bbox_inches='tight')
    pp.close()


if choice == 'cov':
    for s in range(len(subj)):
        for c in range(len(cup)):
            print(cup[c])
            fig = plt.figure(u)
            i = 0
            colors = ["b", "r", "c", "m", "g"]
            width = .15
            names = ['5', '10', '15']
            lgd_name = []
            ax = fig.add_subplot(111)
            ind = [0, 1, 2]
            skipped = False
            for t in range(len(trj)):
                cov = a.get_spdconvergence(subj[s], cup[c], trj[t], .1)
                print(cov)
                if cov == -1:
                    skipped = True
                    break

                nind = ind[0:len(cov)]
                lgd_name.append(trj[t])
                ax.bar(nind, cov, width, color=colors[i])
                i += 1
                ind = [x+width for x in ind]

            if not skipped:
                u += 1
                ind = [x-(3*width) for x in ind]
                plt.xticks(ind, names)
                plt.legend(lgd_name)
                plt.xlabel("Speeds")
                plt.ylabel("Time")
                ax.set_title("Convergence Data for Subj{0}_Cup{1}".format(subj[s], cup[c]))
                axes = plt.gca()
                axes.set_ylim([0, 20])

                #pp.savefig(fig)
    pp.close()

if choice == 'blah':
    averages = [0,0,0]
    for s in range(len(subj)):
        fig = plt.figure(u)
        i = 0
        colors = ["b", "r", "c", "m", "g"]
        width = .15
        names = ['5', '10', '15']
        lgd_name = []
        ax = fig.add_subplot(111)
        ind = [0, 1, 2]

        for t in range(len(trj)):
            cov_aggregate = [0, 0, 0]
            five_elements = 0
            ten_elements = 0
            fif_elements = 0

            for c in range(len(cup)):
                cov = a.get_spdconvergence(subj[s], cup[c], trj[t], .1)
                if cov != -1:
                    cov_aggregate = [x+y for x, y in zip(cov, cov_aggregate)]
                    if 0 in cov:
                        index = cov.index(0)
                        if index == 0:
                            five_elements -= 1
                        if index == 1:
                            ten_elements -= 1
                        if index == 2:
                            fif_elements -= 1
                    five_elements += 1
                    ten_elements += 1
                    fif_elements += 1
            lgd_name.append(trj[t])
            averages[0] = cov_aggregate[0]/five_elements
            averages[1] = cov_aggregate[1]/ten_elements
            averages[2] = cov_aggregate[2]/fif_elements
            ax.bar(ind, averages, width, color=colors[i])
            i += 1
            ind = [m+width for m in ind]

        u += 1
        ind = [n-(3*width) for n in ind]
        plt.xticks(ind, names)
        plt.legend(lgd_name)
        plt.xlabel("Speeds")
        plt.ylabel("Time")
        ax.set_title("Average Convergence Data for Subj{0}".format(subj[s]))
        axes = plt.gca()
        axes.set_ylim([0, 20])
        pp.savefig(fig)
    pp.close()


if choice == 'hi':
    averages = [0,0,0]
    for c in range(len(cup)):
        fig = plt.figure(u)
        i = 0
        colors = ["b", "r", "c", "m", "g"]
        width = .15
        names = ['5', '10', '15']
        lgd_name = []
        ax = fig.add_subplot(111)
        ind = [0, 1, 2]
        skipped = False
        for t in range(len(trj)):
            cov_aggregate = [0, 0, 0]
            five_elements = 0
            ten_elements = 0
            fif_elements = 0

            for s in range(len(subj)):
                cov = a.get_spdconvergence(subj[s], cup[c], trj[t], .1)
                if cov != -1:
                    cov_aggregate = [x+y for x, y in zip(cov, cov_aggregate)]
                    if 0 in cov:
                        index = cov.index(0)
                        if index == 0:
                            five_elements -= 1
                        if index == 1:
                            ten_elements -= 1
                        if index == 2:
                            fif_elements -= 1
                    five_elements += 1
                    ten_elements += 1
                    fif_elements += 1
            if five_elements == 0 and ten_elements == 0 and fif_elements == 0:
                skipped = True
                break
            lgd_name.append(trj[t])
            averages[0] = cov_aggregate[0]/five_elements
            averages[1] = cov_aggregate[1]/ten_elements
            averages[2] = cov_aggregate[2]/fif_elements
            ax.bar(ind, averages, width, color=colors[i])
            i += 1
            ind = [m+width for m in ind]
        if not skipped:
            u += 1
            ind = [n-(3*width) for n in ind]
            plt.xticks(ind, names)
            plt.legend(lgd_name,loc =2)
            plt.xlabel("Speeds")
            plt.ylabel("Time")
            ax.set_title("Average Convergence Data for Cup{0}".format(cup[c]))
            axes = plt.gca()
            axes.set_ylim([0, 20])
            pp.savefig(fig)
    pp.close()













