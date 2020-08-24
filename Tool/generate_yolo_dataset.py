import cv2          # opencv
import copy         # copy.copy(): 얕은 복사, copy.deepcopy(): 깊은 복사
import os           # 디렉토리에서 파일 가져오기
import sys          # exit() 함수

# 마우스 콜백 함수
# 마우스 콜백 함수로 넘어오는 param은 변경해도
# 실제 param으로 넘겨준 값에는 영향을 주지 않는다.
# ex) param으로 넘겨준 src를 param[0] = 0을 해도 
#     실제 src는 변하지 않는다. onMouse()함수 안에서만 변함
def onMouse(event, x, y, flags, param):
    global x1, y1, x2, y2, box_count, list_count, drawing

    location = (x, y)

    # box 그리기 전에는 원본 이미지 표시
    if box_count == 0:
        param[0] = copy.copy(src)
    # box 그리고 난 후에는 원본에 box 그려진 이미지 표시
    else:
        param[0] = copy.copy(param[1])

    # Box 그리기 시작할 때
    if event == cv2.EVENT_LBUTTONDOWN:
        print('LBUTTONDOWN 실행')
        x1, y1 = x, y
        print(x1, '-', y1)
        drawing = True
        cv2.circle(param[0], (x1, y1), 5, (0, 0, 255), 3)

    # 마우스 이동할 때
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:  # 마우스를 누른 상태 일경우
            location = (x1, y1)
            cv2.rectangle(param[0], (x1, y1), (x, y), (255, 0, 0))
        else:
            cv2.line(param[0], (0, y), (1024, y), (0, 255, 0), 1)
            cv2.line(param[0], (x, 0), (x, 768), (0, 255, 0), 1)

    # 드래그해서 box 다 만들었을 때
    elif event == cv2.EVENT_LBUTTONUP:
        print('LBUTTONUP 실행')
        x2, y2 = x, y
        print(x2, '-', y2)
        drawing = False
        cv2.putText(param[0], class_name, (x1, y1), font, fontScale, color, thickness)
        cv2.rectangle(param[0], (x1, y1), (x2, y2), (255, 0, 0))
        param[1] = copy.deepcopy(param[0])
        data_list.append([class_count, x1, y1, x2, y2])
        print('data_list: ', data_list)
        box_count = 1

    # 오른쪽 마우스 클릭
    # 현재 이미지의 box 데이터 저장
    elif event == cv2.EVENT_RBUTTONDOWN:
        print('RBUTTONDOWN 실행')
        if len(data_list) == 0:
            print('저장할 데이터가 없습니다.')
        save_img_txt(data_list)

    cv2.putText(param[0], class_name, location, font, fontScale, color, thickness)
    cv2.imshow("src", param[0])

# box 표시한 이미지를 회전한 후 저장 & box 좌표 txt 파일 생성 함수
def generate_rotate_img(center_of_box, angle, ori_src):

    scale = 1

    # 회전 배열 생성
    matrix = cv2.getRotationMatrix2D(center_of_box, angle, scale)

    # 회전 결과 적용
    src = cv2.warpAffine(ori_src, matrix, (width, height))

# img txt 파일 저장 또는 삭제하는 함수
def save_img_txt(data_list):
    # 현재 이미지의 이름을 -> .txt 파일로 변경
    txt_file_name = img_file_list_jpg[img_count][:-4] + '.txt'  # ex) pepero1.jpg -> pepero1.txt

    f_txt = open(img_path + txt_file_name, 'w')
    if not len(data_list):  # txt 파일 데이터 삭제할 때
        f_txt.write('')
    else:
        print('txt 파일이 저장되었습니다.')
        for data in data_list:
            class_num = data[0]
            box_center_x = ((data[3] + data[1]) / 2) / width
            box_center_y = ((data[4] + data[2]) / 2) / height
            box_width = (data[3] - data[1]) / width
            box_height = (data[4] - data[2]) / height
            data = str(class_num) + ' ' + str(round(box_center_x, 6)) + ' ' + str(round(box_center_y, 6)) + \
                   ' ' + str(round(box_width, 6)) + ' ' + str(round(box_height, 6)) + '\n'
            f_txt.write(data)
    f_txt.close()

# config.txt 파일 읽는 함수
def read_config_txt():
    # 현재 폴더 경로 가져오기
    current_path = os.getcwd()
    # current_path = os.path.dirname(os.path.realpath(__file__))
    print('current_path: ', current_path)

    # 현재 폴더 경로에 config.txt 파일 있는지 확인
    if not os.path.isfile(current_path + '/config.txt'):
        print('config.txt 파일이 존재하지 않습니다.')
        sys.exit()
    else:
        # 파일에 있는 정보 불러와 저장
        print('config.txt 파일이 있습니다.')
        config_path = current_path + '/config.txt'
        config_f = open(config_path, 'r')
        config_lines = config_f.readlines()  # 파일에서 한줄씩 읽어서 리스트로 저장
        print('config_lines: ', config_lines)
        classes = (int)(config_lines[0][10:(len(config_lines[0]) - 1)])  # \n 전까지 classes 문자열 추출
        print('classes: ', classes)
        name = config_lines[1][7:(len(config_lines[1]) - 1)]  # \n 전까지 name 문자열 추출
        name_list = name.split(' ')  # 공백으로 문자열 나눠서 리스트로 추출
        print('name_list: ', name_list)
        print('name: ', name)
        img_path = config_lines[2][11:(len(config_lines[2]) - 1)]  # img_path 문자열 추출
        print('img_path: ', img_path)
        train_txt_path = config_lines[3][17:]  # train_txt_path 문자열 추출
        print('train_txt_path: ', train_txt_path)
        config_f.close()
        return classes, name_list, img_path, train_txt_path

# img_file_list_jpt, txt 리스트 return 함수
def img_file_list(img_path):
    # img_path가 있는 지 확인
    if not os.path.isdir(img_path):
        print('img_path의 폴더가 존재하지 않습니다.')
        sys.exit()
    file_list = os.listdir(img_path)

    # img_path에서 .jpg 파일만 골라서 리스트에 저장
    img_file_list_jpg = [file for file in file_list if file.endswith(".jpg")]
    print("img_file_list_jpg: {}".format(img_file_list_jpg))
    print("img_file_list_jpg 개수: {}".format(len(img_file_list_jpg)))
    if not len(img_file_list_jpg):
        print('.jpg 이미지가 없습니다.')
        sys.exit()

    # img_path에서 .txt 파일만 골라서 리스트에 저장
    img_file_list_txt = [file for file in file_list if file.endswith(".txt")]
    print("img_file_list_txt: {}".format(img_file_list_txt))
    print("img_file_list_txt 개수: {}".format(len(img_file_list_txt)))
    if not len(img_file_list_txt):
        print('.txt 파일이 없습니다.')

    return img_file_list_jpg, img_file_list_txt

# 현재 사진의 txt 파일이 존재하면 그 값을 읽어 list로 return하는 함수
def read_img_txt(img_file_name):
    global data_list
    data_list = []
    txt_file_name = img_file_name[:-4] + '.txt'  # pepero1.jpg -> pepero1.txt
    if txt_file_name in img_file_list_txt:
        img_file_list_txt.index(txt_file_name)
        txt_f = open(img_path + txt_file_name, 'r')
        for txt_lines in txt_f.readlines():
            if txt_lines == '\n':
                break
            class_num = (int)(txt_lines.split(' ')[0])
            box_center_x = (float)(txt_lines.split(' ')[1])
            box_center_y = (float)(txt_lines.split(' ')[2])
            box_width = (float)(txt_lines.split(' ')[3])
            box_height = (float)(txt_lines.split(' ')[4])
            x1 = (int)((width * (2.0 * box_center_x - box_width)) / 2.0)
            x2 = (int)((width * (2 * box_center_x + box_width)) / 2)
            y1 = (int)((height * (2 * box_center_y - box_height)) / 2)
            y2 = (int)((height * (2 * box_center_y + box_height)) / 2)
            data_list.append([class_num, x1, y1, x2, y2])
        draw_rectangle(data_list)
    else:
        print('해당 이미지의 txt 파일이 없습니다.')

# data_list가 존재하면 src에 box를 그려주는 함수
def draw_rectangle(data_list):
    for data in data_list:
        class_name = ('{}' + '-' + name_list[data[0]]).format(data[0])
        cv2.rectangle(src, (data[1], data[2]), (data[3], data[4]), (255, 0, 0))
        cv2.putText(src, class_name, (data[1], data[2]), font, fontScale, color, thickness)

#
def save_train_txt(img_file_list_jpg):
    f_txt = open(train_txt_path, 'w')
    for jpg_name in img_file_list_jpg:
        f_txt.write(img_path + jpg_name + '\n')


def main():
    print('main() 실행')

if __name__ == '__main__':

    # 전역 변수
    drawing = False     # box 그리는 중인지 확인하는 변수
    box_count = 0       # box 다 그렸는지 지울건지 확인하는 변수
    img_count = 0       # 다음 그림 가져올지 확인하는 변수
    class_count = 0     # 다음 class 이름 가져올지 확인하는 변수
    data_list = []      # class, x1, y1, x2, y2 값 저장하기 위한 변수

    # 이미지에 문자열 표시와 관련된 전역 변수
    font = cv2.FONT_ITALIC  # italic font
    fontScale = 1
    color = (0, 0, 255)
    thickness = 1
    #angle = 6          # 회전 각도

    # config.txt 파일에서 설정 정보 가져오기
    classes, name_list, img_path, train_txt_path = read_config_txt()

    # img_path에서 jpg 파일, txt 파일 목록 가져오기
    img_file_list_jpg, img_file_list_txt = img_file_list(img_path)

    # img_file_list_jpg에서 첫번째 사진을 읽어온다
    src = cv2.imread(img_path + img_file_list_jpg[img_count])
    height, width, _ = src.shape
    print('height: {}, width: {}'.format(height, width))

    # 해당 사진의 txt 파일이 존재하면 그 값을 읽어 data_list에 저장 및 src에 box를 그려준다
    read_img_txt(img_file_list_jpg[img_count])
    print(data_list)

    # class 이름 전역 변수로 설정(마우스 포인터에 표시할 이름)
    class_name = ('{}' + '-' + name_list[class_count]).format(class_count)

    # 첫번째 사진 띄운다
    cv2.imshow('src', src)

    # 마우스 콜백 설정
    cv2.setMouseCallback('src', onMouse, [src, 0])

    while(1):
        key = cv2.waitKey()
        if key == 27 & 0xFF: # esc key
            save_train_txt(img_file_list_jpg)
            cv2.destroyAllWindows()
            print('\'ESC\' key가 눌렸습니다.')
            break
        # 전 이미지 불러오기
        elif key == ord('a'): # 숫자 1 key (ord() 함수: 특정한 한 문자를 아스키 코드 값으로 변환해 주는 함수)
            print('\'a\' key가 눌렸습니다.')
            img_file_list_jpg, img_file_list_txt = img_file_list(img_path)
            box_count = 0
            if img_count > 0:
                img_count -= 1
                src = cv2.imread(img_path + img_file_list_jpg[img_count])
                height, width, _ = src.shape
                read_img_txt(img_file_list_jpg[img_count])
            else:
                src = cv2.imread(img_path + img_file_list_jpg[img_count])
                height, width, _ = src.shape
                read_img_txt(img_file_list_jpg[img_count])
        # 다음 이미지 불러오기
        elif key == ord('d'): # 숫자 1 key (ord() 함수: 특정한 한 문자를 아스키 코드 값으로 변환해 주는 함수)
            print('\'d\' key가 눌렸습니다.')
            img_file_list_jpg, img_file_list_txt = img_file_list(img_path)
            box_count = 0
            if img_count == (len(img_file_list_jpg) - 1):
                src = cv2.imread(img_path + img_file_list_jpg[img_count])
                height, width, _ = src.shape
                read_img_txt(img_file_list_jpg[img_count])
            else:
                img_count += 1
                src = cv2.imread(img_path + img_file_list_jpg[img_count])
                height, width, _ = src.shape
                read_img_txt(img_file_list_jpg[img_count])
        # 다음 클래스 이름 불러오기
        elif key == ord('w'): # 숫자 1 key (ord() 함수: 특정한 한 문자를 아스키 코드 값으로 변환해 주는 함수)
            print('\'w\' key가 눌렸습니다.')
            if class_count == (classes - 1):
                class_name = ('{}' + '-' + name_list[class_count]).format(class_count)
            else:
                class_count += 1
                class_name = ('{}' + '-' + name_list[class_count]).format(class_count)
        # 전 클래스 이름 불러오기
        elif key == ord('s'): # 숫자 1 key (ord() 함수: 특정한 한 문자를 아스키 코드 값으로 변환해 주는 함수)
            print('\'s\' key가 눌렸습니다.')
            if class_count > 0:
                class_count -= 1
                class_name = ('{}' + '-' + name_list[class_count]).format(class_count)
            else:
                class_name = ('{}' + '-' + name_list[class_count]).format(class_count)
        # 그렸던 box 삭제
        elif key == ord('x'): # 숫자 1 key (ord() 함수: 특정한 한 문자를 아스키 코드 값으로 변환해 주는 함수)
            print('\'x\' key가 눌렸습니다.')
            print('box & txt 데이터가 삭제되었습니다.')
            box_count = 0
            data_list = []
            save_img_txt(data_list)
            src = cv2.imread(img_path + img_file_list_jpg[img_count])
            height, width, _ = src.shape
            read_img_txt(img_file_list_jpg[img_count])
        # window 'x' 버튼으로 종료할 때 & 다른 key
        else:
            save_train_txt(img_file_list_jpg)
            cv2.destroyAllWindows()
            break