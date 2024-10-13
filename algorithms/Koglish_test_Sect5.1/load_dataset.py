import pandas as pd
import ipdb

class LoadSST2:
    @staticmethod
    def en2en():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/SST2/en_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/SST2/en_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/SST2/en_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def en2cross():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/SST2/en_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/SST2/en_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/SST2/cs_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data, valid_data, test_data
    @staticmethod
    def cross2cross():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/SST2/cs_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/SST2/cs_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/SST2/cs_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data, valid_data, test_data
    
class LoadMRPC:
    @staticmethod
    def en2en():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/MRPC/en_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/MRPC/en_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/MRPC/en_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def en2cross():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/MRPC/en_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/MRPC/en_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/MRPC/cs_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def cross2cross():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/MRPC/cs_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/MRPC/cs_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/MRPC/cs_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
class LoadCOLA:
    @staticmethod
    def en2en():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/COLA/en_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/COLA/en_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/COLA/en_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def en2cross():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/COLA/en_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/COLA/en_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/COLA/cs_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def cross2cross():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/COLA/cs_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/COLA/cs_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/COLA/cs_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
class LoadRTE:
    @staticmethod
    def en2en():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/RTE/en_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/RTE/en_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/RTE/en_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def en2cross():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/RTE/en_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/RTE/en_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/RTE/cs_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def cross2cross():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/RTE/cs_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/RTE/cs_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/RTE/cs_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data

class LoadSTSB:
    @staticmethod
    def en2en():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/STS_B/en_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/STS_B/en_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/STS_B/en_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def en2cross():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/STS_B/en_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/STS_B/en_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/STS_B/cs_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def cross2cross():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/STS_B/cs_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/STS_B/cs_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/STS_B/cs_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    
class LoadQNLI:
    @staticmethod
    def en2en():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/QNLI/en_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/QNLI/en_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/QNLI/en_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def en2cross():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/QNLI/en_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/QNLI/en_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/QNLI/cs_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data
    @staticmethod
    def cross2cross():
        train_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/QNLI/cs_train.csv'
        valid_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/QNLI/cs_valid.csv'
        test_path = '../../preprocessing/Koglish_dataset/Koglish_GLUE/QNLI/cs_test.csv'
        train_data = pd.read_csv(train_path, sep=',')
        valid_data = pd.read_csv(valid_path, sep=',')
        test_data = pd.read_csv(test_path, sep=',')
        return train_data , valid_data, test_data


    
