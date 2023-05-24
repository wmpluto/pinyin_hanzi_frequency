import os

pinyin_hanzi_dict = {}
pinyin_num_dict = {}
def main():
    with open('汉语拼音常用汉字对照表.txt', 'r',encoding='utf8') as fh:
        for line in fh.readlines():
            array = line.strip().split(',')[:-1]
            if(len(array) > 1):
                pinyin = array[0]
                hanzi = array[1:]
                pinyin_hanzi_dict[pinyin] = hanzi
                pinyin_num_dict[pinyin] = len(hanzi)

    sorted_pinyin_num_dict = sorted(pinyin_num_dict.items(), key=lambda x:x[1])

    for item in sorted_pinyin_num_dict:
        print(f"{item[0]:8}, {item[1]:3d}: {pinyin_hanzi_dict[item[0]]}")

if __name__ == "__main__":
    main()