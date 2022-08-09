import unittest
import pandas as pd
import sys, os
sys.path.append(os.path.abspath(os.path.join("../..")))
from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor
# For unit testing the data reading and processing codes,
# we will need about 5 tweet samples.
# Create a sample not more than 10 tweets and place it in a json file.
# Provide the path to the samples tweets file you created below
sampletweetsjsonfile = "data/africa_twitter_data.json"   #put here the path to where you placed the file e.g. ./sampletweets.json.
_, tweet_list = read_json(sampletweetsjsonfile)
columns = [
    "created_at",
    "source",
    "original_text",
    "clean_text",
    "sentiment",
    "polarity",
    "subjectivity",
    "lang",
    "favorite_count",
    "retweet_count",
    "original_author",
    "screen_count",
    "followers_count",
    "friends_count",
    "possibly_sensitive",
    "hashtags",
    "user_mentions",
    "place",
    "place_coord_boundaries",
]
class TestTweetDfExtractor(unittest.TestCase):
    """
        A class for unit-testing function in the fix_clean_tweets_dataframe.py file
        Args:
        -----
            unittest.TestCase this allows the new class to inherit
            from the unittest module
    """
    def setUp(self) -> pd.DataFrame:
        self.df = TweetDfExtractor(tweet_list[:5])
        # tweet_df = self.df.get_tweet_df()
    def test_find_statuses_count(self):
        self.assertEqual(
            self.df.find_statuses_count(), [888, 1597, 2293, 44, 1313]
        )
    def test_find_full_text(self):
        text = ["#Pelosi airplane landed safely in #Taiwan \ud83c\uddf9\ud83c\uddfc  \n1) - Both \ud83c\udde8\ud83c\uddf3 &amp;  \ud83c\uddfa\ud83c\uddf8 are playing \"win win\" on financial markets. 2) - Taiwan may be the future Asian   Cuba  3) - \ud83c\uddfa\ud83c\uddf8 &amp; \ud83c\udde8\ud83c\uddf3 need an Asian #NATO / #5G\nWhat's your thoughts?",
        "Watch the video of the beginning of the Chinese bombing of Taiwan during Pelosi visit from here : https://t.co/twah6WU4fZ\n\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\u0640\n#Pelosi #\u30de\u30c4\u30b3\u306e\u77e5\u3089\u306a\u3044\u4e16\u754c #Yediiklim #BadDecisionsTrailer1 #LawnBowls #\u795d_CALL119_MV900\u4e07\u56de #\u0e21\u0e32\u0e01\u0e2d\u0e14\u0e01\u0e31\u0e19\u0e19\u0e30\u0e0b\u0e35\u0e1e\u0e24\u0e01\u0e29\u0e4c https://t.co/m4CXfyZRS7",
        "#Pelosi \n#Taipei \n#taiwan\n#XiJinping \n#China \nOn a verge of another war https://t.co/DuqDiSnWcd",
        "#HOBIPALOOZA #LaAcademiaExpulsion #WEURO2022 #jhopeAtLollapalooza #SuzukiPakistan #Fantastico #Taiwan #breastfeeding #Kosovo #BORNPINK  strong \u270d\ufe0f\ud83d\udc9c https://t.co/GtZeNL24rm",
        "#Pelosi\n#china\nChina Time \u270c\ufe0f https://t.co/tEDjzTlszu"]
        self.assertEqual(self.df.find_full_text(), text)
    def test_find_sentiments(self):
        self.assertEqual(
            self.df.find_sentiments(self.df.find_full_text()),
            (
                [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]
            )
        )
    def test_find_screen_name(self):
        name = ['DzCritical', 'toopsat', 'NassimaLilEmy', 'd_dhayae', 'Mohamme65404115']
        self.assertEqual(self.df.find_screen_name(), name)
    def test_find_followers_count(self):
        f_count = [318, 764, 64, 60, 39]
        self.assertEqual(self.df.find_followers_count(), f_count)
    def test_find_friends_count(self):
        friends_count = [373, 144, 47, 463, 206]
        self.assertEqual(self.df.find_friends_count(), friends_count)
    def test_find_is_sensitive(self):
        self.assertEqual(self.df.is_sensitive(), ['','','','',''])
    # def test_find_hashtags(self):
    #     self.assertEqual(self.df.find_hashtags(), )
    # def test_find_mentions(self):
    #     self.assertEqual(self.df.find_mentions(), )
if __name__ == "__main__":
    unittest.main()