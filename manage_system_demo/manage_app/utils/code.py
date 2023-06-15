# 验证码
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def check_code(width=120, height=30, char_length=5, font_file="/static/font/Monaco.ttf", font_size=28):
    code = []
    img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')

    def rndChar():
        """生成随机字母"""
        return chr(random.randint(65, 90))

    def rndColor():
        """生成随机颜色"""
        return (random.randint(0, 255), random.randint(0, 255), random.randint(64, 255))

    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = random.randint(0, 4)
        draw.text((i * width / char_length, h), char, font=font, fill=rndColor())

    # 写干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())

    # 写干扰圆

    # 画干扰线

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    # # 生成验证图片
    # with open('manage_app/static/img/code.png', 'wb') as f:
    #     img.save(f, format='png')

    return img, ''.join(code)

if __name__ == '__main__':
    img, code_str = check_code()
    with open('../../media/code.png', 'wb') as f:
        img.save(f, format='png')
    print(code_str)