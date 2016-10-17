#!/bin/sh 
#

# make a web site into a staging version.

# add <div class="staging">STAGING</div> after body tag
# apply some CSS

FOLDER=$1

if [ -z $FOLDER ]; then 
    echo "Missing parameter to stagify"
    exit 1 
fi

if [ ! -d $FOLDER ]; then
    echo $FOLDER is not a folder
    exit 2
fi

if [ ! -f ${FOLDER}/index.html ]; then
    echo No ${FOLDER}/index.html found
    exit 3
fi

find $FOLDER -name '*.html' -exec sed -i s'/<\/body>/<div class="staging">STAGING<\/div><\/body>/' {} \;


cat >> $FOLDER/media/css/custom.css <<EOF
div.staging{
z-index: 10;
top: 0px;
left: 0px;
position: fixed;
opacity: 0.5;
pointer-events: none;
transform: translate(100px, 50px) rotate(-17deg);
font-size: 100px;
}

EOF
