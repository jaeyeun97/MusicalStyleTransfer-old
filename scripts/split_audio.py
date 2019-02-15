import os
import sys
import glob
import librosa
import soundfile as sf


sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from util import split_audio as sa

def main():
    if len(sys.argv) < 2:
        print('Path not provided.')
        return
    paths = glob.glob('{}/*.wav'.format(sys.argv[1]))
    for p in paths:
        y, sr = sf.read(p)
        sa(p, y, sr)
        del y

if __name__ == '__main__':
    main()
