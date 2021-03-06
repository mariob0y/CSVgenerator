from __future__ import absolute_import, unicode_literals

from celery import shared_task

import csv
from faker import Faker
from dummy_gen.models import Scheme
import datetime
import os
from os import path
from pathlib import Path
from planeks.settings import *

from celery_progress.backend import ProgressRecorder

from time import sleep
from django.core.files.base import ContentFile
import boto3


@shared_task(bind=True)
def datagenerate(self, records, columns, names, filename, scheme_id):

    scheme = Scheme.objects.get(id=scheme_id)
    scheme.upload = 'In Progress'
    scheme.save()

    # Progress recorder

    sleep(1)

    progress_recorder = ProgressRecorder(self)
    for i in range(records):
        progress_recorder.set_progress(i + 1, records, f'Row {i} out of {records}')

    # Data for CSV
    fake = Faker('en_US')
    fake1 = Faker('en_GB')   # adding phone number

    # testing folder
    # BASE_DIR = Path(__file__).resolve().parent.parent
    filename_ = filename

  

    # writing rows
    with open(filename_, 'w') as csvFile:
        writer = csv.writer(csvFile)
        if names:
            writer.writerow(names)

        writer = csv.DictWriter(csvFile, fieldnames=columns)
        writer.writeheader()

        for i in range(records):
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@testDomain.com"
            userId = Fname + "." + Lname + domain_name

            gen_dict = {
                    "email": userId,
                    "name": fake.name(),
                    "date": fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1, 1)),
                    'job': fake.job(),
                    'company': fake.company(),
                    "phone": fake1.phone_number(),
                    "address": fake.address(),
                    "city": fake.city(),
                    "country": fake.country(),
                    }

            filtered_dict = {}
            for (k, v) in gen_dict.items():
                if k in columns:
                    filtered_dict[k] = v

            writer.writerow(filtered_dict)
            

        # Saving at S3 (comment this section for saving locally)
        scheme.upload = 'media/' + filename_
        scheme.save()
        
        s3 = boto3.client('s3',
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY, )
        
        s3.upload_file(filename_, AWS_STORAGE_BUCKET_NAME, '%s/%s' % ('media', filename_))



    return filename + ' have been generated!'
