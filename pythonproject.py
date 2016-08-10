# Name: DefineProjection.py 
# Description: This python script will allow you to create a geodatabase,set your output coordinate system and it can be used to clip features based on user selection!
# Author: Mohamed Mostefaoui

# import modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"F:\Python_Project\TryFile\Sample_Data"
coordinate_system = arcpy.GetParameterAsText(1)
arcpy.env.outputCoordinateSystem = coordinate_system

# Set local variables for geodatabase
out_folder_path = r"F:\Python_Project\TryFile" 
out_name = arcpy.GetParameterAsText(0)
arcpy.CreateFileGDB_management(out_folder_path, out_name)
 
# Set the workspace, outputCoordinateSystem and geographicTransformations environments

fcList = arcpy.ListFeatureClasses()
for features in fcList:
    
    
# set the clip features.
    clip_features = arcpy.GetParameterAsText(2)
    out_feature_class ="F:\\Python_Project\\TryFile\\" + arcpy.GetParameterAsText(0)+"\\" + features.replace(".shp","_np")
    arcpy.Clip_analysis (features, clip_features, out_feature_class)


















        




