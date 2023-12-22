#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23/10/17

@author: Maurizio Ferrari Dacrema
"""


from Base.Recommender import Recommender
from Base.Recommender_utils import check_matrix
from Base.SimilarityMatrixRecommender import SimilarityMatrixRecommender

from Base.IR_feature_weighting import okapi_BM_25, TF_IDF
import numpy as np

from Base.Similarity.Compute_Similarity import Compute_Similarity


class UserKNNCFRecommender(SimilarityMatrixRecommender, Recommender):
    """ UserKNN recommender"""

    RECOMMENDER_NAME = "UserKNNCFRecommender"

    FEATURE_WEIGHTING_VALUES = ["BM25", "TF-IDF", "none"]


    def __init__(self, URM_train, sparse_weights=True):
        super(UserKNNCFRecommender, self).__init__()

        # Not sure if CSR here is faster
        self.URM_train = check_matrix(URM_train, 'csr')

        self.dataset = None

        self.sparse_weights = sparse_weights

        self._compute_item_score = self._compute_score_user_based



    def fit(self, topK=50, shrink=100, similarity='cosine', normalize=True, feature_weighting = "none", **similarity_args):

        self.topK = topK
        self.shrink = shrink

        if feature_weighting not in self.FEATURE_WEIGHTING_VALUES:
            raise ValueError("Value for 'feature_weighting' not recognized. Acceptable values are {}, provided was '{}'".format(self.FEATURE_WEIGHTING_VALUES, feature_weighting))


        if feature_weighting == "BM25":
            self.URM_train = self.URM_train.astype(np.float32)
            self.URM_train = okapi_BM_25(self.URM_train.T).T
            self.URM_train = check_matrix(self.URM_train, 'csr')

        elif feature_weighting == "TF-IDF":
            self.URM_train = self.URM_train.astype(np.float32)
            self.URM_train = TF_IDF(self.URM_train.T).T
            self.URM_train = check_matrix(self.URM_train, 'csr')

        similarity = Compute_Similarity(self.URM_train.T, shrink=shrink, topK=topK, normalize=normalize, similarity = similarity, **similarity_args)

        if self.sparse_weights:
            self.W_sparse = similarity.compute_similarity()
            self.W_sparse = check_matrix(self.W_sparse, 'csr')
        else:
            self.W = similarity.compute_similarity()
            self.W = self.W.toarray()

