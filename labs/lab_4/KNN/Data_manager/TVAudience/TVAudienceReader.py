#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 14/09/17

@author: Maurizio Ferrari Dacrema
"""


import zipfile, os

from Data_manager.DataReader import DataReader


class TVAudienceReader(DataReader):

    DATASET_URL = "https://polimi365-my.sharepoint.com/:u:/g/personal/10322330_polimi_it/EZ1JPTmU6kRGnRezu3Ex-zQBxZK3-Y_aeP0Tb_3NbsQzHA?e=8YraeO"

    DATASET_SUBFOLDER = "TVAudience/"
    AVAILABLE_ICM = []


    def _get_dataset_name_root(self):
        return self.DATASET_SUBFOLDER



    def _load_from_original_file(self):
        # Load data from original

        print("TVAudienceReader: Loading original data")

        compressed_zip_file_folder = self.DATASET_OFFLINE_ROOT_FOLDER + self.DATASET_SUBFOLDER
        decompressed_zip_file_folder = self.DATASET_SPLIT_ROOT_FOLDER + self.DATASET_SUBFOLDER

        zipFile_name = "tv-audience-dataset.zip"

        try:

            dataFile = zipfile.ZipFile(compressed_zip_file_folder + zipFile_name)

            interactions_path = dataFile.extract("tv-audience-dataset/tv-audience-dataset.csv", path=decompressed_zip_file_folder + "decompressed/")

        except (FileNotFoundError, zipfile.BadZipFile):

            print("TVAudienceReader: Unable to find or extract data zip file.")
            print("TVAudienceReader: Automatic download not available, please ensure the ZIP data file is in folder {}.".format(compressed_zip_file_folder))
            print("TVAudienceReader: Data zip file not found or damaged. You may download the data from: {}".format(self.DATASET_URL))

            # If directory does not exist, create
            if not os.path.exists(compressed_zip_file_folder):
                os.makedirs(compressed_zip_file_folder)

            raise FileNotFoundError("Automatic download not available.")


        #
        # print("TVAudienceReader: Loading item content")
        # self.ICM_all, self.tokenToFeatureMapper_ICM_all, self.item_original_ID_to_index = self._load_ICM(interactions_path, if_new_item = "add")

        print("TVAudienceReader: Loading Interactions")
        self.URM_all, self.item_original_ID_to_index, self.user_original_ID_to_index = self._load_interactions(interactions_path, if_new_user = "add", if_new_item = "add")



        print("TVAudienceReader: cleaning temporary files")

        import shutil

        shutil.rmtree(decompressed_zip_file_folder + "decompressed/", ignore_errors=True)

        print("TVAudienceReader: loading complete")





    def _load_interactions(self, impressions_path, if_new_user ="add", if_new_item ="ignore"):


        from Data_manager.IncrementalSparseMatrix import IncrementalSparseMatrix_FilterIDs

        URM_builder = IncrementalSparseMatrix_FilterIDs(preinitialized_col_mapper = self.item_original_ID_to_index, on_new_col = if_new_item,
                                                        preinitialized_row_mapper = None, on_new_row = if_new_user)




        fileHandle = open(impressions_path, "r")

        numCells = 0

        # Remove header
        fileHandle.readline()


        for line in fileHandle:


            if numCells % 1000000 == 0 and numCells!=0:
                print("Processed {} cells".format(numCells))


            line = line.split(",")
            line[-1] = line[-1].replace("\n", "")
            """
            Columns are:
            channel ID: channel id from 1 to 217.
            slot: hour inside the week relative to the start of the view, from 1 to 24*7 = 168.
            week: week from 1 to 19. Weeks 14 and 19 should not be used because they contain errors.
            genre ID: it is the id of the genre, form 1 to 8. Genre/subgenre mapping is attached below.
            subGenre ID: it is the id of the subgenre, from 1 to 114. Genre/subgenre mapping is attached below.
            user ID: it is the id of the user.
            program ID: it is the id of the program. The same program can occur multiple times (e.g. a tv show).
            event ID: it is the id of the particular instance of a program. It is unique, but it can span multiple slots.
            duration: duration of the view.
            """
            numCells += 1

            channel_id = line[0]
            slot = line[1]
            week = line[2]
            genre_id = line[3]
            subGenre_id = line[4]
            user_id = line[5]
            program_id = line[6]
            event_id = line[7]
            duration = float(line[8])

            if week!="14" and week!="19":
                URM_builder.add_data_lists([user_id], [program_id], [duration])




        fileHandle.close()

        return URM_builder.get_SparseMatrix(), URM_builder.get_column_token_to_id_mapper(), URM_builder.get_row_token_to_id_mapper()


