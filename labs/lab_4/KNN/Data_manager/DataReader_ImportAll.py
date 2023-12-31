#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20/03/19

@author: Maurizio Ferrari Dacrema
"""


from Data_manager.Movielens100K.Movielens100KReader import Movielens100KReader
from Data_manager.Movielens1M.Movielens1MReader import Movielens1MReader
from Data_manager.Movielens10M.Movielens10MReader import Movielens10MReader
from Data_manager.Movielens20M.Movielens20MReader import Movielens20MReader
from Data_manager.TheMoviesDataset.TheMoviesDatasetReader import TheMoviesDatasetReader
from Data_manager.MultifacetedMovieTrailerFeature.MultifacetedMovieTrailerFeatureReader import MultifacetedMovieTrailerFeatureReader

from Data_manager.Brightkite.BrightkiteReader import BrightkiteReader
from Data_manager.Epinions.EpinionsReader import EpinionsReader
from Data_manager.NetflixPrize.NetflixPrizeReader import NetflixPrizeReader
from Data_manager.ThirtyMusic.ThirtyMusicReader import ThirtyMusicReader
from Data_manager.Yelp.YelpReader import YelpReader
from Data_manager.BookCrossing.BookCrossingReader import BookCrossingReader
from Data_manager.NetflixEnhanced.NetflixEnhancedReader import NetflixEnhancedReader

from Data_manager.AmazonReviewData.AmazonElectronics.AmazonElectronicsReader import AmazonElectronicsReader
from Data_manager.AmazonReviewData.AmazonBooks.AmazonBooksReader import AmazonBooksReader
from Data_manager.AmazonReviewData.AmazonAutomotive.AmazonAutomotiveReader import AmazonAutomotiveReader
from Data_manager.AmazonReviewData.AmazonMoviesTV.AmazonMoviesTVReader import AmazonMoviesTVReader

from Data_manager.SpotifyChallenge2018.SpotifyChallenge2018Reader import SpotifyChallenge2018Reader
from Data_manager.XingChallenge2016.XingChallenge2016Reader import XingChallenge2016Reader
from Data_manager.XingChallenge2017.XingChallenge2017Reader import XingChallenge2017Reader

from Data_manager.TVAudience.TVAudienceReader import TVAudienceReader
from Data_manager.LastFMHetrec2011.LastFMHetrec2011Reader import LastFMHetrec2011Reader
from Data_manager.DeliciousHetrec2011.DeliciousHetrec2011Reader import DeliciousHetrec2011Reader
from Data_manager.CiteULike.CiteULikeReader import CiteULike_aReader, CiteULike_tReader
from Data_manager.SpotifySkipPrediction.SpotifySkipPredictionReader import SpotifySkipPredictionReader
