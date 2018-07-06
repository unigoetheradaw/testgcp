
import logging
import os
import cloudstorage as gcs
import webapp2
from google.appengine.api import app_identity
import numpy as np

def main():
    print("Hallo World")
    print(os.environ.get('BUCKET_NAME',
                         app_identity.get_default_gcs_bucket_name()))
    with open("sumfile.txt", "w") as f:
        f.write("Das ist ein Test")
    print(np.abs(-3.5))


if __name__ == "__main__":
    main()
