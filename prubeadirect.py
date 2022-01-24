from nubapi import NubApi
import os
aa = NubApi()
paths = os.path.dirname(os.path.abspath(__file__))
aa.UploadFile(paths+"/config.json")
