

def get_font_str(font_char):
    font_div = f"""
                <div class="study-card ">
                    <div class="study-base">
                        <img class="books" src="images/{font_char}.webp" alt="image1">
                    </div>
                    <h3><a target="_blank" class="view" href="https://github.com/Lina-Liuna/Lina-Liuna.github.io/blob/main/chinese_grade1/{font_char}.pdf">View</a>
                    </h3>
                </div>
    """
    return font_div

def get_all_strs(fonts_list):
    str_div_list = ''
    for cf in fonts_list:
        str_div_list += get_font_str(cf)

    return str_div_list



def all_strs2file(strs, file_path):
    with open(file_path, 'w') as file:
        file.write(strs)




chinese_text = '天地日月人你我她它他一二三四五六七八九十金木水火土上下左右中大小多少哥姐爸妈爷奶儿女男头目耳口手足牙吃站坐走山石田狗猫兔鸡鸭牛马鸟羊虫风花雪雨树白红绿黄了子又和里'

filepath = "/Users/linaliu/code/Lina-Liuna.github.io/data_process/grade1_font.html"
font_str = get_all_strs(chinese_text)
all_strs2file(font_str, filepath)



