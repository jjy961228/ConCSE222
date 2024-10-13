import pandas as pd
import ipdb

class LoadNLI:
    @staticmethod
    def en_train():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_NLI/en_train.csv' 
        train_data = pd.read_csv(train_path, sep=',')
        return train_data 
    @staticmethod
    def cross_train():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_NLI/cs_train.csv' 
        train_data = pd.read_csv(train_path, sep=',')
        return train_data
    
class LoadSTSB:
    @staticmethod
    def en_valid():
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_STS/STS_B/en_valid.csv' 
        valid_data = pd.read_csv(valid_path, sep=',')
        return valid_data
    def en_test():
        test_path = '../../preprocessing/Koglish_dataset/Koglish_STS/STS_B/cs_test.csv' 
        test_data = pd.read_csv(test_path, sep=',')
        return test_data
    
    @staticmethod
    def cross_valid():
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_STS/STS_B/cs_valid.csv'  
        valid_data = pd.read_csv(valid_path, sep=',')
        return valid_data
    def cross_test():
        test_path = '../../preprocessing/Koglish_dataset/Koglish_STS/STS_B/cs_test.csv'  
        test_data = pd.read_csv(test_path, sep=',')
        return test_data
    
class TestLoadSTS_12:
    def __init__(self, args):
        self.eval_type = args.eval_type
    def en_test(self):
        if self.eval_type == 'transfer':
            test_path = '../../preprocessing/Koglish_dataset/Koglish_STS/STS_12/en_test.csv' 
        test_data = pd.read_csv(test_path, sep=',')
        return test_data
    
    def cross_test(self):
        if self.eval_type == 'transfer':
            test_path = '../../preprocessing/Koglish_dataset/Koglish_STS/STS_12/cs_test.csv' 
        test_data = pd.read_csv(test_path, sep=',')
        return test_data

class TestLoadSTS_13:
    def __init__(self, args):
        self.eval_type = args.eval_type
    def en_test(self):
        if self.eval_type == 'transfer':
            test_path = '../../preprocessing/Koglish_dataset/Koglish_STS/STS_13/en_test.csv' 
            test_data = pd.read_csv(test_path, sep=',')
        return test_data
    
    def cross_test(self):
        if self.eval_type == 'transfer' :
            test_path = '../../preprocessing/Koglish_dataset/Koglish_STS/STS_13/cs_test.csv'  
            test_data = pd.read_csv(test_path, sep=',')
        return test_data

class TestLoadSTS_14:
    def __init__(self, args):
        self.eval_type = args.eval_type
    def en_test(self):
        if self.eval_type == 'transfer':
            test_path = '../../preprocessing/Koglish_dataset/Koglish_STS/STS_14/en_test.csv'  
            test_data = pd.read_csv(test_path, sep=',')
        return test_data
    def cross_test(self):
        if self.eval_type == 'transfer' :
            test_path = '../../preprocessing/Koglish_dataset/Koglish_STS/STS_14/cs_test.csv'  
            test_data = pd.read_csv(test_path, sep=',')
        return test_data

class TestLoadSTS_15:
    def __init__(self, args):
        self.eval_type = args.eval_type
    def en_test(self):
        if self.eval_type == 'transfer':
            test_path = '../../preprocessing/Koglish_dataset/Koglish_STS/STS_15/en_test.csv' 
            test_data = pd.read_csv(test_path, sep=',')
        return test_data
    
    def cross_test(self):
        if self.eval_type == 'transfer' :
            test_path = '../../preprocessing/Koglish_dataset/Koglish_STS/STS_15/cs_test.csv'
            test_data = pd.read_csv(test_path, sep=',')
        return test_data

class TestLoadSTS_16:
    def __init__(self, args):
        self.eval_type = args.eval_type
    def en_test(self):
        if self.eval_type == 'transfer':
            test_path = '../../preprocessing/Koglish_dataset/Koglish_STS/STS_16/en_test.csv'  
            test_data = pd.read_csv(test_path, sep=',')
        return test_data
    
    def cross_test(self):
        if self.eval_type == 'transfer' :
            test_path = '../../preprocessing/Koglish_dataset/Koglish_STS/STS_16/cs_test.csv' 
            test_data = pd.read_csv(test_path, sep=',')
        return test_data

class TestLoadSICK:
    def __init__(self, args):
        self.eval_type = args.eval_type
    def en_test(self):
        if self.eval_type == 'transfer':
            test_path = '../../preprocessing/Koglish_dataset/Koglish_STS/SICK/en_test.csv' 
        test_data = pd.read_csv(test_path, sep=',')
        return test_data
    
    def cross_test(self):
        if self.eval_type == 'transfer' :
            test_path = '../../preprocessing/Koglish_dataset/Koglish_STS/SICK/cs_test.csv'
        test_data = pd.read_csv(test_path, sep=',')
        return test_data

    