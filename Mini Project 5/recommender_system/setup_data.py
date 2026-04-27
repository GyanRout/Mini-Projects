import urllib.request
import zipfile
import os
import pandas as pd

def download_movielens():
    os.makedirs('data', exist_ok=True)
    url = "https://files.grouplens.org/datasets/movielens/ml-100k.zip"
    zip_path = "data/ml-100k.zip"
    
    print("Downloading MovieLens 100k dataset...")
    urllib.request.urlretrieve(url, zip_path)
    
    print("Extracting...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("data")
        
    # Convert the weirdly formatted .data file to a clean CSV
    print("Cleaning data...")
    df = pd.read_csv('data/ml-100k/u.data', sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])
    df.to_csv('data/ratings.csv', index=False)
    print("Dataset saved to data/ratings.csv. You can delete the zip and unzipped folders now if you want.")

if __name__ == "__main__":
    download_movielens()