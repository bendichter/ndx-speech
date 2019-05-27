from pynwb.epoch import TimeIntervals
from ndx_speech import Transcription

import pandas as pd

words = TimeIntervals.from_dataframe(pd.DataFrame(
    {'start_time': [.1, 2.], 'stop_time': [.8, 2.3], 'label': ['hello', 'there']}), name='words')

tt = Transcription(words=words)

