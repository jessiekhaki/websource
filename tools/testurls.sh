#!/bin/sh

OUT=`tempfile`
OUTSTAT=`tempfile`

grep -o -i "http[s]*://[^\"<]*" content/projects/*.html | sort | uniq >>$OUT
grep -o -i "http[s]*://[^\"<]*" content/people/*.html | sort | uniq >>$OUT
grep -o -i "http[s]*://[^\"<]*" content/news/*.html | sort | uniq >>$OUT

# cat $OUT 

while read LINE; do
    PAGE=`echo $LINE | awk -F: '{print $1}'`
    URL=`echo $LINE | sed 's/[^:]*://'`
    echo $URL
    curl -o /dev/null --silent --write-out "%{http_code} $URL\n" "$URL" >>$OUTSTAT
done < $OUT 
