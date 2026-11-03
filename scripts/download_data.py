"""Download DAIR.AI Emotion and produce the text/emotion CSV expected by the notebook."""
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('emotion.csv'))
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Output already exists; use another --output path to preserve it.')
    from datasets import load_dataset
    corpus = load_dataset('dair-ai/emotion', 'unsplit', split='train')
    labels = corpus.features['label'].names
    frame = corpus.to_pandas()
    frame['emotion'] = frame['label'].map(dict(enumerate(labels)))
    frame[['text', 'emotion']].to_csv(args.output, index=False, encoding='utf-8')
    print(f'Saved {len(frame)} rows to {args.output}')

if __name__ == '__main__':
    main()
