## Description

The goal of the program is to analyze pairs of stocks for basic correlation over the course of the trading day. Additionally there may be some analysis done. I will produce more detailed instructions but for now this is heavily a work in progress. This is a project I am using to learn more about python.

## Version Details

I am using python (and pip) 3.8 but lower 3 versions may work as well.

## Run requirements

#### Pip
First install dependencies using `pip3.8 install -r requirements.txt` (with your pip version of choice).

#### IEX
Next you will need to supply an [IEX](https://iexcloud.io/docs/api/) api key in the collect_config.yaml of collect. This api key will go under token.

#### Sheets

This program utilizes gspread therefore these [instructions](https://gspread.readthedocs.io/en/latest/oauth2.html#for-end-users-using-oauth-client-id) will need to be followed to use it.

Next a sheets file will need to be created and the [sheet id](https://developers.google.com/sheets/api/guides/concepts#spreadsheet_id) will need to be inserted into the config.yaml files under sheet_key.

Finally a sheet with the name api-test will need to be made. This will be changed to be more dynamic in the future.

## Running
Before running the program the first time you should run the init.sh script `bash init.sh` which will create the data folder and secrets folder. The data folder holds previously collected iex data, the secrets folder isn't used yet but is something I am looking to utilize later.

To collect data run the collect_data.py file under collect. A basic analysis will be done and the results of which will be sent to sheets

To perform any kind of analysis (still in the works) you can run examine_pairs.py under analyze.
