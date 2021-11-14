# coding=utf-8
from urllib.request import urlopen, Request
from urllib import parse
import string
import json


def get_border_pionts(adcode: str, output: str, out_model: str, key: str):
    """
    获取adcode本级的行政区划范围坐标并以文件形式输出
    @adcode:str 该行政单位的adcode。实际高德API也可以用汉字指定地名，但是为了避免重名，
    这里需要adcode
    @output:str 输出结果的文件
    @output_model:str 输出文件的打开方式，如是输出时是替换模式还是追加模式
    @key:str 申请的高德API key
   """

    url = f'https://restapi.amap.com/v3/config/district?keywords={adcode}'\
          f'&extensions=all&subdistrict=0&key={key}'
    print(f"Requesting: {url}")
    url = parse.quote(url, safe=string.printable)
    fh = urlopen(Request(url))
    return_json = json.loads(fh.read().decode('utf-8'))
    henan_range_str = return_json['districts'][0]['polyline']
    henan_range_str = '>\n'+henan_range_str+'\n>'
    outputfile = open(file=output, mode=out_model)
    outputfile.writelines(henan_range_str.replace(
        ';', '\n').replace(',', ' ').replace('|', "\n>\n"))
    outputfile.close()


def get_sub_border_points(adcode: str, output: str, key: str):
    """
    获取adcode所有下一级的行政区划范围坐标并以文件形式输出，如提取河南省的所有市
    @adcode:str 欲提取行政单位的adcode。如想提取河南省所有地级市的行政区划，adcode输入
    河南省的adcode。实际高德API也可以用汉字指定地名，但是为了避免重名，这里需要adcode
    @output:str 输出结果的文件
    @key:str 申请的高德API key
    """
    url = f'https://restapi.amap.com/v3/config/district?keywords={adcode}'\
          f'&subdistrict=1&key={key}'
    print(f"Requesting: {url}")
    url = parse.quote(url, safe=string.printable)
    fh  = urlopen(Request(url))
    return_json = json.loads(fh.read().decode('utf-8'))
    city_list = [x['adcode'] for x in return_json['districts'][0]['districts']]
    
    for city in city_list:
        get_border_pionts(city, output, 'a', key)


if __name__ == '__main__':
    key = '3aa79e9eded0a57fac28e034ba73245d'
    # 获取河南省的边界，河南省的adcode是410000
    # get_border_pionts('410000', 'Henan-border-L1.dat', out_model='w', key=key)
    # 获取许昌市的边界，许昌市的adcode是411000
    # get_border_pionts('411000','Xuchang-border-L1.dat', out_model='w', key=key)
    # 获取鄢陵县的边界，鄢陵县的adcode是411024
    # get_border_pionts('411024','Yanling-border-L1.dat', out_model='w', key=key)
    # 获取河南所有市的边界
    # get_sub_border_points('410000', 'Henan-border-La.dat', key=key)
    # 获取许昌所有县的边界
    get_sub_border_points('411000', 'Xuchang-border-La.dat', key=key)
