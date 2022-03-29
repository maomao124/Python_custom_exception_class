"""
 * Project name(项目名称)：Python自定义异常类
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 11:08
 * Version(版本): 1.0
 * Description(描述)： 
 """


class CustomException(Exception):
    pass


if __name__ == '__main__':
    try:
        raise CustomException("自定义异常")
    except CustomException as e:
        print(str(e))
    raise CustomException("自定义异常")
