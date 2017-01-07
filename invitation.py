with open("inlay1.svg") as f:
    for line in f:
        if '       sodipodi:linespacing="140%"><tspan\n' in line:
            print line
with open("WeddingPlanner - Ga%08steliste detail.csv") as f:
    for line in f:
        print(line)
