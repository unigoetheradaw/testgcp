
import logging
import os
import cloudstorage as gcs
import webapp2
from google.appengine.api import app_identity
import numpy as np

def main():
    datalist = "asdasd"
    bucket_name = os.environ.get('BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
    filename = os.path.join(bucket_name, 'myfile.txt')
    write_retry_params = gcs.RetryParams(backoff_factor=1.1)
    gcs_file = gcs.open(filename, 'w', content_type='text', retry_params=write_retry_params)
    writer = csv.writer(gcs_file, delimiter='\t')
    writer.writerow(['field1', 'field2'])
    gcs_file.close()

if __name__ == "__main__":
    main()
