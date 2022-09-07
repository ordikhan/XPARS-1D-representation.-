import pandas as pd
import numpy as np


class LoadData(object):
    def __init__(self, file_name):
        self.df = pd.read_excel(file_name)

    def split_data_by_feature(self, feature_list):
        datas = [self.df[self.df[feature_list[0]] == 0], self.df[self.df[feature_list[0]] == 1]]
        for feature in feature_list[1:]:
            temp = []
            for data in datas:
                temp.append(data[data[feature] == 0])
                temp.append(data[data[feature] == 1])
            datas = temp
        return datas

    def split_data_by_feature_and_continue_feature(self, datas, continue_feature_name, continue_feature_list):
        datas = [data.sort_values(by=continue_feature_name) for data in datas]
        out = []
        for data in datas:
            for i in range(len(continue_feature_list)):
                out.append(data[data[continue_feature_name] < continue_feature_list[i]])
                data[data[continue_feature_name] < continue_feature_list[i]] = None
            out.append(data[data[continue_feature_name] >= continue_feature_list[-1]])
        return out

    def split_data_by_list_feature_age_pre(self, feature_list, age, pre):
        datas = self.split_data_by_feature(feature_list)
        datas = self.split_data_by_feature_and_continue_feature(datas, "age", age)
        datas = self.split_data_by_feature_and_continue_feature(datas, "blood_pressure", pre)
        return datas

