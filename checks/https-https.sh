while read line;
do
https_url="https://"
https_url+="${line}"
echo "${https_url}";

#set -xe

#verbose_out_curl=`curl -v --max-time 15 $https_url 2>&1`
#out_curl=`curl --max-time 15 $https_url`

header=`curl -s -o /dev/null --max-time 15 -D - ${https_url}`

output=`echo $?`

#echo $out_curl >>  out.curl
#echo $verbose_out_curl >> vb.out.curl


if [[ ($header == *"200 OK"* ) || ( $header == "") ]]; then 
	if [[ ($output != 28 ) && ( $output != 7) && ( $output != 6) ]]; then
		echo ${line} >> https.txt
	fi
fi

done < modif.txt
