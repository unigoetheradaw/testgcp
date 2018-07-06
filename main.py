import numpy as np
import os
from google.appengine.api import app_identity

def main():
    print("Hallo World")
    print(os.environ.get('BUCKET_NAME',
                         app_identity.get_default_gcs_bucket_name()))
    with open("sumfile.txt", "w") as f:
        f.write("Das ist ein Test")
    print(np.abs(-3.5))


if __name__ == "__main__":
    main()
