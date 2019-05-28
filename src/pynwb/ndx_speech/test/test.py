from pynwb import NWBHDF5IO, NWBFile
from datetime import datetime
from pynwb.epoch import TimeIntervals
from ndx_speech import Transcription

import pandas as pd

words = TimeIntervals.from_dataframe(pd.DataFrame(
    {'start_time': [.1, 2.], 'stop_time': [.8, 2.3], 'label': ['hello', 'there']}), name='words')

nwbfile = NWBFile('aa','aa', datetime.now().astimezone())
nwbfile.add_acquisition(Transcription(words=words))

with NWBHDF5IO('test_transcription.nwb', 'w') as io:
    io.write(nwbfile, cache_spec=True)

with NWBHDF5IO('test_transcription.nwb', 'r', load_namespaces=True) as io:
    nwbfile2 = io.read()

    assert(nwbfile.acquisition['transcription'].words.to_dataframe().equals(
        nwbfile2.acquisition['transcription'].words.to_dataframe()
    ))

