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
sampletweetsjsonfile = "./data/africa_twitter_data.json"   #put here the path to where you placed the file e.g. ./sampletweets.json.
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
        text = ["#Pelosi airplane landed safely in #Taiwan",
        "Watch the video of the beginning of the Chinese bombing of Taiwan during Pelosi visit from here",
        "#Pelosi \n#Taipei \n#taiwan\n#XiJinping \n#China \nOn a verge of another war https://t.co/DuqDiSnWcd",
        "#HOBIPALOOZA #LaAcademiaExpulsion #WEURO2022 #jhopeAtLollapalooza #SuzukiPakistan #Fantastico #Taiwan #breastfeeding #Kosovo #BORNPINK  strong :writing_hand::purple_heart: https://t.co/GtZeNL24rm",
        "#Pelosi\n#china\nChina Time :v: https://t.co/tEDjzTlszu"]
        self.assertEqual(self.df.find_full_text(), text)
    def test_find_sentiments(self):
        self.assertEqual(
            self.df.find_sentiments(self.df.find_full_text()),
            (
                [0.5, 0.0, 0.0, 0.4333333333333333, 0.0], [0.5, 0.0, 0.0, 0.7333333333333333, 0.0]
            )
        )
    def test_find_created_time(self):
        """Test find created time module."""
        created_at = ["Wed Aug 03 20:19:13 +0000 2022", 
                      "Tue Aug 02 15:24:42 +0000 2022",
                      "Tue Aug 02 15:02:35 +0000 2022",
                       "Mon Aug 01 13:51:42 +0000 2022",
                      "Sun Jul 31 20:02:20 +0000 2022"]
        self.assertEqual(self.df.find_created_time(), created_at)
    def test_find_screen_name(self) -> list:
        name = ['DzCritical', 'toopsat', 'NassimaLilEmy', 'd_dhayae', 'Mohamme65404115']
        self.assertEqual(self.df.find_screen_name(), name)
    def test_find_followers_count(self) -> list:
        f_count = [318, 764, 64, 60, 39]
        self.assertEqual(self.df.find_followers_count(), f_count)
    def test_find_friends_count(self) -> list:
        friends_count = [373, 144, 47, 463, 206]
        self.assertEqual(self.df.find_friends_count(), friends_count)
    def test_find_is_sensitive(self) -> list:
        self.assertEqual(self.df.is_sensitive(), ['', False, False, False, False])
    def test_find_location(self):
        """Test find location module."""
        self.assertEqual(self.df.find_location(), ['Algerie', '', 'Algerie', 'Chlef', 'Algerie'])
    def test_find_retweet_count(self):
        """Test find retweet count module."""
        self.assertEqual(self.df.find_retweet_count(), [0, 0, 0, 0, 0])
    def test_find_source(self):
        """Test find source module."""
        source = ["<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                  "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
                  "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                  "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
                  "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>"]
        self.assertEqual(self.df.find_source(), source)
    # def test_find_hashtags(self):
    #     self.assertEqual(self.df.find_hashtags(), )
    # def test_find_mentions(self):
    #     self.assertEqual(self.df.find_mentions(), )
if __name__ == "__main__":
    unittest.main()