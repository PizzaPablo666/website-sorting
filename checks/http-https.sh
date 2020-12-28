while read line;
do
	http_url="http://"
	http_url+="${line}"
	echo "${http_url}";
	out_curl=$(curl --max-time 15 ${http_url})
	
	https_url="https://"
	https_url+="${line}"

	if [[ $out_curl == *$https_url* ]]; then
		echo ${line} >> https.txt
	fi
		


done < modif.txt
