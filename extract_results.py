import cv2, sys, os
import glob


def get_file_names(images_txt_path):
    paths_file = open(images_txt_path, 'r')
    filenames = []
    lines = paths_file.readlines()
    for line in lines:
        filenames.append(line)

    return filenames


file = open('results/result_gamma.txt', 'r')
lines = file.readlines()
percents = []
filenames = sorted(glob.glob('data/ears/test_gamma' + '/*.png', recursive=True))

img_number = -1
det_lists = []
for line in lines:
    if line[:len('/content')] == '/content':
        img_number += 1
        det_lists.append([])
    if line[:3] == 'Ear':
        segment = line.split('\t')[1].split('  ')
        vals = segment[1::2]
        try:
            for v in range(0, len(vals)):
                vals[v] = int(vals[v].replace(')\n', ''))
            det_lists[img_number].append(vals)
        except ValueError:
            print('Skipping this line')
        
i = 0
for dlist in det_lists:
    img = cv2.imread(filenames[i])
    thename = filenames[i].split('\\')[-1]
    print(thename)
    for arr in dlist:
        x = arr[0]
        y = arr[1]
        w = arr[2]
        h = arr[3]
        # for x, y, w, h in arr:
        cv2.rectangle(img, (x,y), (x + w, y + h), (128, 255, 0), 4)
    cv2.imwrite('C:\\biometrics\\assignment2\data\ears\\test_gamma_results\\' + thename.replace('.png', '') + '-detected.png', img)
    # if not cv2.imwrite(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'ears', 'test_results', thename.replace('.png', '-') + '-detected.png'), img):
    #     print(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'ears', 'test_results', thename))
    #     raise Exception("Could not write image")
    i += 1



    

