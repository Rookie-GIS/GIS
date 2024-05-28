import arcpy
import os

def export_province_shapefile(input_shapefile, output_folder, province_name_field, target_province_name):
    query = "{} = '{}'".format(province_name_field, target_province_name)
    output_folder_path = os.path.join(output_folder, target_province_name)
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    output_shapefile = os.path.join(output_folder_path, target_province_name + ".shp")
    arcpy.Select_analysis(input_shapefile, output_shapefile, query)

# 使用示例
input_shapefile = r"xxxx.shp" #输入全国范围的省级行政区的shp路径
output_folder = r"xxx"#输入输出的路径
province_name_field = "x"#输入全国范围的省级行政区的shp中“省”的字段名
target_province_name = "xx省"#输入需要输出的省的名称

export_province_shapefile(input_shapefile, output_folder, province_name_field, target_province_name)
