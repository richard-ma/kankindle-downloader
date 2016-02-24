 #!/bin/bash
 
for line in `cat update.txt`
do
    grep -F "${line}" books-sorted.csv >> tmp
done

sort tmp | uniq | cut -d, -f1 > update-books-links

for line in `cat update-books-links`
do
    sed -i '#'${line}'#d' download.log
done
