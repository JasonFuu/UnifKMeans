"""Test client for KMeans++ and Equal Cluster K-Means"""
from KMeansPlus import K_Means_Plus_Plus
from Equal_Cluster_K_Means import Equal_K_Means
import matplotlib.pyplot as plt
import random

"""Tests K-means++ with 50 randomly generated 2-var data points in various ranges"""
def KMeansPlusPlus_Test():
    points = []
    xs = []
    ys = []

    for a in range(50):
        a = 100*random.random()
        b = 50*random.random()
        xs.append(a)
        ys.append(b)
        points.append([a, b])

    test = K_Means_Plus_Plus(points, 7)

    centroidx = []
    centroidy = []

    for points in test.final_centroids():
        centroidx.append(points[0])
        centroidy.append(points[1])

    plt.scatter(xs, ys, color = 'red')
    plt.scatter(centroidx, centroidy, color = 'black')

    plt.show()
    print(test.final_centroids())

def main():
    points = []
    xs = []
    ys = []

    # for a in range(80):
    #     c = 100 * random.random()
    #     b = 50 * random.random()
    #     xs.append(a)
    #     ys.append(b)
    #     points.append([c, b])
    points = [[2.2334879219135297, 80.26881181303189],
 [38.36144907370196, 5.01064889336279],
 [7.685367120772679, 59.749038352690235],
 [34.52772707594913, 62.38700841906134],
 [26.463016746687096, 30.185814682342617],
 [22.65161658966093, 79.53644434621415],
 [1.5641743635126493, 9.805144246145003],
 [12.922546860335494, 72.18795979926799],
 [17.269059670935267, 29.360823877679763],
 [27.025175041085483, 58.22886384299763],
 [30.291106229011756, 56.36043985337646],
 [39.071578308580364, 47.918057875695816],
 [6.207426396390714, 95.72116465718732],
 [41.10863865176995, 75.8534077649487],
 [40.85200145367374, 41.841259713439584],
 [29.779445095966906, 41.301966827589744],
 [22.47496411881044, 17.205256024821956],
 [34.98395336335275, 38.87482146186421],
 [20.902841218543493, 11.931864603360898],
 [26.18307607476384, 76.31377671849758],
 [34.47972501850906, 20.64187877324517],
 [9.853788752799304, 55.023272604355554],
 [42.47960633492531, 86.74642212696182],
 [22.905340278568225, 4.070787373277152],
 [39.22785539884622, 32.46223167796798],
 [6.402093717784075, 49.844283075739305],
 [21.456377816456516, 12.88758449173063],
 [42.99779615088784, 0.011076545854593611],
 [18.384743668860715, 96.1627772401566],
 [25.005904835759186, 24.104075365455614],
 [32.61950367689858, 71.11306012912829],
 [13.78086039537817, 19.9191956963926],
 [49.615234472784714, 25.231270083577016],
 [34.28808136875212, 3.5100569011424443],
 [26.668879803267924, 5.289379423997021],
 [42.78517483366822, 52.45677352795549],
 [1.3403428454385358, 68.61280312804485],
 [27.252304293283565, 33.585308020580214],
 [2.7710870389937803, 34.63649534839982],
 [29.027391188076418, 54.998604187549205],
 [0.7510022170433228, 94.08634064963876],
 [4.680386032580214, 45.634820981205756],
 [8.184275423354315, 95.25712058682485],
 [21.8071164509995, 68.5972171743426],
 [33.50600168078515, 57.13663103562041],
 [31.203560914741935, 21.55579250252363],
 [39.31178272026516, 28.82279165055569],
 [20.735352906020697, 7.926235633532242],
 [26.812463156015554, 87.95874803422943],
 [2.9251014767206094, 35.62980137554745],
 [0.4486724147564958, 8.201476922110885],
 [34.9270417037214, 52.18755510475596],
 [33.85005764739976, 13.093043759332812],
 [2.0992212110605593, 58.72864249071931],
 [42.99587598148381, 56.49988608148869],
 [3.0623197818321843, 8.658045061920106],
 [18.168086333310256, 23.96926296314682],
 [26.232646512911924, 24.089497808178596],
 [36.0779276503635, 57.0813204399387],
 [32.31651075287015, 24.62615234011278],
 [22.537255182872695, 71.88562577139635],
 [33.88989670462477, 44.99477730784347],
 [23.906701671065477, 73.34400065462593],
 [45.3638852031621, 46.719168568596814],
 [24.25041224877934, 62.93732955274318],
 [48.89481521196453, 60.79394098436103],
 [25.59840730944999, 79.38485170187388],
 [15.716890739730582, 22.933733273963085],
 [25.88690056073907, 51.44063572360549],
 [44.48984202904613, 21.90684009481115],
 [34.07613457978867, 8.769512579587047],
 [34.783626507383765, 42.96781806786987],
 [9.249725555638022, 1.1226716643395696],
 [12.079169624530362, 4.6240028065608785],
 [14.909492244258027, 85.55724600231811],
 [14.466699898140934, 50.683553975745035],
 [28.687865636235582, 8.672040814646643],
 [24.652810633479, 1.4556464853776263],
 [38.66829985645283, 18.30147298438771],
 [35.74690872311168, 2.057323850925352]]

    # test = K_Means_Plus_Plus(points, 4)
    # centroids = test.final_centroids()
    centroids = [[31.203560914741935, 21.55579250252363], [1.3403428454385358, 68.61280312804485], [12.922546860335494, 72.18795979926799], [42.78517483366822, 52.45677352795549]]

    nexttest = Equal_K_Means(points, centroids, 4)
    clusters = nexttest.final_clusters()
    centroids = nexttest.final_centroids()
    print(nexttest.swap_proposals)

    group0x = []
    group0y = []
    group1x = []
    group1y = []
    group2x = []
    group2y = []
    group3x = []
    group3y = []
    centroidsx = []
    centroidsy = []

    for points in clusters[0]:
        group0x.append(points[0])
        group0y.append(points[1])
    for points in clusters[1]:
        group1x.append(points[0])
        group1y.append(points[1])
    for points in clusters[2]:
        group2x.append(points[0])
        group2y.append(points[1])
    for points in clusters[3]:
        group3x.append(points[0])
        group3y.append(points[1])
    for points in centroids:
        centroidsx.append(points[0])
        centroidsy.append(points[1])

    plt.scatter(group0x, group0y, color = 'red')
    plt.scatter(group1x, group1y, color = 'yellow')
    plt.scatter(group2x, group2y, color = 'blue')
    plt.scatter(group3x, group3y, color = 'green')

    plt.scatter(centroidsx, centroidsy, color = 'black')
    plt.show()


main()