file = open('result_gamma.txt', 'r')
lines = file.readlines()
percents = []

for line in lines:
    if line[:3] == 'Ear':
        percent = float(line.split('\t')[0].split(' ')[1][:2])
        percents.append(percent)

avg_iou = sum(percents) / len(percents)
print('Average IoU: ' + str(avg_iou))