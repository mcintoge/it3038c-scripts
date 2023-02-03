#!/bin/bash
# This script downloads covid data and displays it

POSITIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].positive')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases"




#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
HOSPITAL=$(echo $DATA | jq '.[0].hospitalizedCurrently')
ICU=$(echo $DATA | jq '.[0].inIcuCurrently')
VENT=$(echo $DATA | jq '.[0].onVentilatorCurrently')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases. Currently there are $HOSPITAL hospitalized, with $ICU in the ICU and $VENT on ventilators. "
