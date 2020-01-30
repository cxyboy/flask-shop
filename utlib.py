from string import digits, ascii_letters
from random import sample, randint
from app import mail, Message
from flask import session,Response
from PIL import Image, ImageFont, ImageDraw
from datetime import timedelta


def send_email(eml):
    """发送邮件"""
    message = Message('修改密码',recipients=[eml])
    code = ''.join(sample(ascii_letters+digits, 6))
    message.body = '【51商城】验证码：{}\t{}\n{}'.format(code, '此次验证码有效期为5分钟', '如果非本人操作，请忽略！')
    mail.send(message)
    # TODO 应该存入redis 然后设置过期时间为3分钟
    session['code']=code



def modify_pwd(user, data, db):
    """修改密码"""
    from werkzeug.security import generate_password_hash
    user.password = generate_password_hash(data["password"])
    db.session.add(user)
    db.session.commit()


class GetCode:
    """生成登录验证码"""
    @staticmethod
    def random_color():
        """随机颜色"""
        return randint(32, 127), randint(32, 127), randint(32, 127)

    @staticmethod
    def gene_text():
        """生成4位验证码"""
        return ''.join(sample(ascii_letters+digits, 4))

    @staticmethod
    def draw_lines(draw, num, width, height):
        """划干扰线"""
        for num in range(num):
            x1 = randint(0, width / 2)
            y1 = randint(0, height / 2)
            x2 = randint(0, width)
            y2 = randint(height / 2, height)
            draw.line(((x1, y1), (x2, y2)), fill='black', width=1)

    @staticmethod
    def get_verify_code():
        """生成验证码图形"""
        code = GetCode.gene_text()
        # 图片大小120×50
        width, height = 120, 50
        # 新图片对象
        im = Image.new('RGB',(width, height), 'white')
        # 字体
        font = ImageFont.truetype('app/static/fonts/arial.ttf', 40)
        # draw对象
        draw = ImageDraw.Draw(im)
        # 干扰线
        GetCode.draw_lines(draw, 10, 200, 50)
        # 绘制字符串
        for item in range(4):
            draw.text((5+randint(-3,3)+23*item, 5+randint(-3,3)),
                      text=code[item], fill=GetCode.random_color(), font=font)
        return im, code
