#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 06/01/18

@author: Maurizio Ferrari Dacrema
"""


import zipfile, os
import scipy.io
import scipy.sparse as sps
import h5py
import shutil

from Base.Recommender_utils import reshapeSparse
from Data_manager.DataReader import DataReader
from Data_manager.IncrementalSparseMatrix import IncrementalSparseMatrix



class CiteULikeReader(DataReader):

    DATASET_URL = "https://polimi365-my.sharepoint.com/:u:/g/personal/10322330_polimi_it/EcjHpkI8TQdHnFVwVMkNGN4BmNkurMWw79sU8kpt4wk8eA?e=QYhdbz"
    AVAILABLE_ICM = ["ICM_title_abstract"]
    DATASET_SPECIFIC_MAPPER = []

    IS_IMPLICIT = True



    def _get_dataset_name_root(self):
        return self.DATASET_SUBFOLDER



    def _load_from_original_file(self):
        # Load data from original

        self.zip_file_folder = self.DATASET_OFFLINE_ROOT_FOLDER + "CiteULike/"
        self.decompressed_zip_file_folder = self.DATASET_SPLIT_ROOT_FOLDER + self.DATASET_SUBFOLDER

        try:

            self.dataFile = zipfile.ZipFile(self.zip_file_folder + "CiteULike_a_t.zip")

        except (FileNotFoundError, zipfile.BadZipFile):

            print("CiteULikeReader: Unable to find data zip file.")
            print("CiteULikeReader: Automatic download not available, please ensure the ZIP data file is in folder {}.".format(self.zip_file_folder))
            print("CiteULikeReader: Data can be downloaded here: {}".format(self.DATASET_URL))

            # If directory does not exist, create
            if not os.path.exists(self.zip_file_folder):
                os.makedirs(self.zip_file_folder)

            raise FileNotFoundError("Automatic download not available.")


        local_dataset_name = "citeulike-{}".format(self.dataset_variant)
        train_interactions_file_suffix = "1"

        URM_train_path = self.dataFile.extract(local_dataset_name + "/cf-train-{}-users.dat".format(train_interactions_file_suffix),
                                              path=self.decompressed_zip_file_folder + "decompressed/")

        URM_test_path = self.dataFile.extract(local_dataset_name + "/cf-test-{}-users.dat".format(train_interactions_file_suffix),
                                              path=self.decompressed_zip_file_folder + "decompressed/")

        ICM_path = self.dataFile.extract(local_dataset_name + "/mult_nor.mat",
                                              path=self.decompressed_zip_file_folder + "decompressed/")


        URM_all_builder = IncrementalSparseMatrix(auto_create_row_mapper=False, auto_create_col_mapper=False)

        URM_all_builder = self._load_data_file(URM_train_path, URM_all_builder)
        URM_all_builder = self._load_data_file(URM_test_path, URM_all_builder)


        self.URM_all = URM_all_builder.get_SparseMatrix()
        self.item_original_ID_to_index = URM_all_builder.get_column_token_to_id_mapper()
        self.user_original_ID_to_index = URM_all_builder.get_row_token_to_id_mapper()


        if self.dataset_variant == "a":
            self.ICM_title_abstract = scipy.io.loadmat(ICM_path)['X']

        else:
            # Variant "t" uses a different file format and is transposed
            self.ICM_title_abstract = h5py.File(ICM_path).get('X')
            self.ICM_title_abstract = sps.csr_matrix(self.ICM_title_abstract).T

        self.ICM_title_abstract = sps.csr_matrix(self.ICM_title_abstract)

        # n_users = self.URM_all.shape[0]
        # n_items = max(self.URM_all.shape[1], self.ICM_title_abstract.shape[0])
        n_features = self.ICM_title_abstract.shape[1]

        # URM_shape = (n_users, n_items)
        # ICM_shape = (n_items, n_features)

        self.tokenToFeatureMapper_ICM_title_abstract = {feature_index:feature_index for feature_index in range(n_features)}

        # self.URM_all = reshapeSparse(self.URM_all, URM_shape)
        # self.ICM_title_abstract = reshapeSparse(self.ICM_title_abstract, ICM_shape)

        print("CiteULikeReader: cleaning temporary files")

        shutil.rmtree(self.decompressed_zip_file_folder + "decompressed/", ignore_errors=True)

        print("CiteULikeReader: loading complete")





    def _load_data_file(self, filePath, URM_all_builder, separator = " "):

        fileHandle = open(filePath, "r")
        user_index = 0


        for line in fileHandle:

            if (user_index % 1000000 == 0):
                print("Processed {} cells".format(user_index))

            if (len(line)) > 1:

                line = line.replace("\n", "")
                line = line.split(separator)

                if len(line)>0:

                    if line[0]!="0":

                        line = [int(line[i]) for i in range(len(line))]

                        URM_all_builder.add_single_row(user_index, line[1:], data=1.0)

            user_index += 1


        fileHandle.close()

        return  URM_all_builder





class CiteULike_aReader(CiteULikeReader):

    DATASET_SUBFOLDER = "CiteULike_a/"

    def __init__(self, **kwargs):
        super(CiteULike_aReader, self).__init__(**kwargs)

        self.dataset_variant = "a"




class CiteULike_tReader(CiteULikeReader):

    DATASET_SUBFOLDER = "CiteULike_t/"

    def __init__(self, **kwargs):
        super(CiteULike_tReader, self).__init__(**kwargs)

        self.dataset_variant = "t"