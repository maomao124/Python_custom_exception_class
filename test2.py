"""
 * Project name(项目名称)：Python自定义异常类
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 11:11
 * Version(版本): 1.0
 * Description(描述)： 
 """
import traceback


class InputError(Exception):
    """当输出有误时，抛出此异常"""

    # 自定义异常类型的初始化
    def __init__(self, value):
        self.value = value

    # 返回异常类对象的说明信息
    def __str__(self):
        return "{} is invalid input".format(repr(self.value))


if __name__ == '__main__':
    try:
        raise InputError(1)  # 抛出 MyInputError 这个异常
    except InputError as err:
        print('error: {}'.format(err))
        traceback.print_exc(file=open("error.log", "a", encoding="UTF-8"))
