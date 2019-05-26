
from pynwb.spec import (
    NWBNamespaceBuilder,
    NWBGroupSpec,
)
from export_spec import export_spec


def main():
    ns_builder = NWBNamespaceBuilder(doc='transcriptions and other speech-related data',
                                     name='speech',
                                     version='0.1.1',
                                     author='Ben Dichter',
                                     contact='ben.dichter@gmail.com')

    Transcription = NWBGroupSpec(neurodata_type_def='Transcription', neurodata_type_inc='NWBDataInterface',
                             name='transcription',
                             doc='holds tiers for different levels of transcription (e.g. sentence, word, phoneme)')
    Transcription.add_attribute(name='help', dtype='text', value='holds tiers for different levels of transcription',
                                doc='doc')
    Transcription.add_attribute(name='settings', dtype='text', required=False,
                                doc='text field for entering any algorithms and settings used for automatic transcription')
    
    for feature_type in ('phoneme_features', 'phonemes', 'syllables', 'words', 'sentences'):
        intervals = Transcription.add_group(name=feature_type, neurodata_type_inc='TimeIntervals', quantity='?',
                                            doc='label, start, and stop times for ' + feature_type)
        intervals.add_attribute(name='help', dtype='text', value='holds ' + feature_type + ' tier times',
                                doc='doc')

    new_data_types = [Transcription]

    ns_builder.include_type('NWBDataInterface', namespace='core')
    ns_builder.include_type('TimeIntervals', namespace='core')

    export_spec(ns_builder, new_data_types)


if __name__ == "__main__":
    main()
